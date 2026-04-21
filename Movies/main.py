from parsers import * 
from concurrent.futures import ThreadPoolExecutor
from db import connection,create_db
from request_data import request

all_urls = main('https://www.rottentomatoes.com/browse/movies_in_theaters/sort:newest')

create_db()

def process(url):
    try:
        main_url ='https://www.rottentomatoes.com/'
        data = extract_page_data(url)

        
        cast_url = urljoin(main_url,data.xpath("string(//section[@aria-labelledby='cast-and-crew-label']//rt-button/@href)").strip())
        
        cast_page = request(cast_url)
        cast_tree = html.fromstring(cast_page)
        all_cast = {}

        for c in cast_tree.xpath("//cast-and-crew-card"):
            all_cast[c.xpath("string(.//rt-text[@slot='title']/text())").strip()] = c.xpath("string(.//rt-text[@slot='credits']/text())").strip()
        reviews_count = data.xpath("string(//rt-link[@slot='critics-reviews'])").strip()
        reviews_href = data.xpath("string(//section[@aria-labelledby='critics-reviews-label']//rt-button/@href)").strip()
        all_reviews = []
        if reviews_href:
            reviews = request(urljoin(main_url,reviews_href))
            review_tree = html.fromstring(reviews)
            json_obj =review_tree.xpath("//script[@data-json='props']/text()")
            if not json_obj:
                print('No data')
                return
            json_obj_2 = json.loads(json_obj[0])

            page_id = json_obj_2.get('media').get('emsId')
            
            review_url= f'https://www.rottentomatoes.com/napi/rtcf/v1/movies/{page_id}/reviews?after=&before=&pageCount=20&topOnly=false&type=critic&verified=false'

            review_data = find_url(review_url)
            for i in (review_data.get('reviews')) or [] :
                all_reviews.append(
                    {
                        'name': (i.get('critic') or {}).get('displayName'),
                        'review': i.get('reviewQuote'),
                        'count': i.get('originalScore'),
                        'review_type': i.get('scoreSentiment')
                    }
                    )
                

        video_href = data.xpath("string(//rt-button[@data-qa='videos-view-all-link']/@href)")
        video_main_href=urljoin(main_url,video_href)
        request_video=extract_page_data(video_main_href)
        videos = []

        videos_xpath = request_video.xpath("//div[@data-qa='video-item']")

        for v in videos_xpath:
            title = v.xpath(".//a[@data-qa='video-item-title']/text()")
            link = v.xpath(".//a[@data-qa='video-item-title']/@href")
            duration = v.xpath(".//span[@data-qa='video-item-duration']/text()")
            thumbnail = v.xpath(".//img[@data-qa='video-img']/@srcset")

            videos.append({
                "title": title[0].strip() if title else None,
                "url": urljoin(main_url, link[0]) if link else None,
                "duration": duration[0].strip() if duration else None,
                "thumbnail": thumbnail[0] if thumbnail else None
            })
            
        data = {
            'movie_name':data.xpath("string(//rt-text[@size='1.25,1.75']/text())"),
            'score':data.xpath("string(//rt-text[@slot='critics-score'])") or "0%",
            'desc':data.xpath("string(//div[@slot='description']//rt-text)").strip() or None,
            'img':data.xpath("string(//img[@slot='poster']/@src)"),
            'reviews_count':reviews_count,
            'videos':videos or None,
            'want_to_know':data.xpath("string(//div[@id='critics-consensus']//p)").strip() or None,
            'cast':all_cast,
            'all_reviews':all_reviews,
        }

        print(f'{data.get('movie_name')} was added!!')
            
        return data
    except Exception as e:
        return f'Error-{e}'

with ThreadPoolExecutor(max_workers=5) as exceute:
    result = exceute.map(process,all_urls)

    conn,cur = connection()

    for r in result:
        if not r:
            continue
        cur.execute("""
            INSERT INTO movie(movie_name,score,description,img,reviews_count,videos,want_to_know,cast,reviews) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,(
            r.get('movie_name'),
            r.get('score'),
            r.get('desc'),
            r.get('img'),
            r.get('reviews_count'),
            json.dumps(r.get('videos')),
            r.get('want_to_know'),
            json.dumps(r.get('cast')),
            json.dumps(r.get('all_reviews'))
        ))

        conn.commit()

print('all done!!')
conn.close()
