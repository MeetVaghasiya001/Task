from request_data import request
from lxml import html
import re
import json
from urllib.parse import urljoin


def get_page_data(url):
    data = request(url)

    if not data:
        return
    try:
        tree = html.fromstring(data)
        script = tree.xpath('//script[contains(text(),"__INITIAL_STATE__")]')

        if not script:
            return 

        script_text = script[0].text
        match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', script_text, re.DOTALL)

        if not match:
            return
        return match.group(1)
    except Exception as e:
        print(f'Error-{e}')

def extract_data(page_data):

    base_url = 'https://www.espn.in/'
    ipl_data = json.loads(page_data)

    all_matches = []

    for a in ipl_data.get('scoreboard').get('leagues'):
        for j in a.get('events'):
            all_matches.append({
                'date':j.get('date'),
                'match':j.get('teams').get('gameInfo'),
                'score':"".join(urljoin(base_url,i.get('href')) for i in j.get('links') if i.get('text')=='Scorecard')
            })

    return all_matches 





