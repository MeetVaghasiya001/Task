from request_data import request
from lxml import html
import re
import json
from urllib.parse import urljoin
import time


def get_page_data(url, retries=3):
    for _ in range(retries):
        data = request(url)

        if not data:
            time.sleep(2)
            continue

        try:
            tree = html.fromstring(data)
            script = tree.xpath('//script[contains(text(),"__INITIAL_STATE__")]')

            if not script:
                time.sleep(2)
                continue

            script_text = script[0].text
            match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', script_text, re.DOTALL)

            if not match:
                time.sleep(2)
                continue

            return match.group(1)

        except:
            time.sleep(2)

    return None

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





