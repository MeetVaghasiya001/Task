from url_parser import *
from request_data import *
import json
from db import *
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor

st=time.time()
main_url='https://www.espn.in/cricket/scores/series/8048/season/2026/indian-premier-league'
main_responce=get_page_data(main_url)
all_matches=extract_data(main_responce)

create_db()
conn,cur=connection()

cur.execute("SELECT match_url FROM matches")
existing_urls=set(i[0] for i in cur.fetchall())

new_matches=[m for m in all_matches if m.get('score') not in existing_urls]

def process(a):
    try:
        match_url=a.get('score')
        if not match_url:
            return None
        
        page_d=get_page_data(match_url)
        if not page_d:
            return None
        
        match_responce=json.loads(page_d)
        game=match_responce.get('gamePackage',{})
        all_data=game.get('scorecard',{}).get('innings',{})
        teams=game.get('gameStrip',{}).get('teams',{})
        raw_date=a.get('date')
        match_date=datetime.strptime(raw_date,"%Y-%m-%dT%H:%MZ")
        match_data={
            'match':a.get('match'),
            'date':match_date,
            'winner':game.get('summary'),
            'score':{
                teams.get('home',{}).get('name'):teams.get('home',{}).get('score'),
                teams.get('away',{}).get('name'):teams.get('away',{}).get('score')
            },
            'match_url':match_url,
            'innings':{}
        }
        for k,v in all_data.items():
            match_data['innings'][k]={
                'team':v.get('title'),
                'batsmen':{
                    b.get('displayName'):{s.get('name'):s.get('value') for s in b.get('stats')}
                    for b in v.get('batsmen') if b.get('displayName')
                },
                'bowlers':{
                    b.get('displayName'):{s.get('name'):s.get('value') for s in b.get('stats')}
                    for b in v.get('bowlers') if b.get('displayName')
                }
            }
        return match_data
    except:
        return None

with ThreadPoolExecutor(max_workers=5) as executor:
    results=list(executor.map(process,new_matches))

count=0
for r in results:
    if not r:
        continue
    count+=1
    print(count)
    cur.execute("""INSERT INTO matches(match_name,winner,date,score,match_url,innings) VALUES(%s,%s,%s,%s,%s,%s)""",(
        r['match'],
        r['winner'],
        r['date'],
        json.dumps(r['score']),
        r['match_url'],
        json.dumps(r['innings'])
    ))

conn.commit()
conn.close()

et=time.time()
print(f"time:{(et-st)/60:.2f}")