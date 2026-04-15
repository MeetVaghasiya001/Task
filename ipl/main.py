from url_parser import *
from request_data import *
import json
main_url = 'https://www.espn.in/cricket/scores/series/8048/season/2025/indian-premier-league'

main_responce = get_page_data(main_url)

all_matches = extract_data(main_responce)

full_details = []

for a in all_matches:
    match_url = a.get('score')

    if match_url is not None:
        page_d = get_page_data(match_url)
        if not page_d:
            print(f'skipp{match_url}')
            continue

        match_responce = json.loads(page_d)

        all_data = match_responce.get('gamePackage').get('scorecard').get('innings')
        teams = match_responce.get('gamePackage').get('gameStrip').get('teams')
        match_data ={
            'match':a.get('match'),
            'date':a.get('date'),
            'winner':match_responce.get('gamePackage').get('summary'),
            teams.get('home').get('name'):teams.get('home').get('score'),
            teams.get('away').get('name'):teams.get('away').get('score'),
            'innings':{}
        }

        for k,v in all_data.items():
            match_data['innings'][k] = {
                'team':v.get('title'),
                'batsmen':[{
                    'batsman_name':b.get('displayName'),
                    'all_stats':{s.get('name'):s.get('value') for s in b.get('stats')}
                } for b in v.get('batsmen')],
                'bowlers':[{
                    'bowlers_name':b.get('displayName'),
                    'all_stats':{s.get('name'):s.get('value') for s in b.get('stats')}
                } for b in v.get('bowlers')]
            }

        full_details.append(match_data)
        

with open('all_match.json','w',encoding='utf-8') as f:
    json.dump(full_details,f,indent=4,default=str)
    

