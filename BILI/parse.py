from lxml import html
import json
import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS song(
            s_id INT AUTO_INCREMENT PRIMARY KEY,
            song_name VARCHAR(255),
            artist VARCHAR(255),
            image VARCHAR(255),
            lw VARCHAR(255),
            peak INT,
            weeks INT,
            debut_position VARCHAR(255),
            debut_chart_date VARCHAR(255),
            peak_position VARCHAR(255),
            peak_chart_date VARCHAR(255),
            share JSON,
            awards VARCHAR(255)
            )

""")

with open("new_billboard.html", "r", encoding="utf-8") as f:
    data = f.read()

tree = html.fromstring(data)

all_data = tree.xpath(
    "//div[@id='post-1479786']//div[@class='o-chart-results-list-row-container']"
)

song = []
for s in all_data:

    song_data = s.xpath(
        ".//ul//li[contains(@class,'a-chart-result-item-container')]//ul//li"
    )

    for l in song_data:
        song_name = s.xpath("string(.//h3[@id='title-of-a-story']/text())").strip()
        a_artist = s.xpath(
            "string(.//span[contains(@class,'a-no-trucate')]/a/text())"
        ).strip()
        artist = s.xpath(
            "string(.//span[contains(@class,'a-no-trucate')]/text())"
        ).strip()
        other = {
            i.xpath("string(.//span[contains(@class,'u-color-grey-141')]//text())")
            .strip(): i.xpath("string(.//li/span//text())")
            .strip()
            for i in s.xpath(".//div")
            if i.xpath("string(.//span[contains(@class,'u-color-grey-141')]//text())")
        }
    count = s.xpath(
        "string(.//ul//li[contains(@class,'lrv-u-color-black')]//span/text())"
    ).strip()
    debute_path = s.xpath(
        ".//div//div[@class='charts-results-item-detail-inner //']//div"
    )
    debute_data = {}
    for d in debute_path:
        if d.xpath("./@class")[0] == "o-chart-position-stats__debut":
            debute_data[d.xpath("string(.//h3/text())").strip()] = d.xpath(
                "string(.//span/text())"
            ).strip()
            debute_data[d.xpath("string(.//h4/text())").strip()] = d.xpath(
                "string(.//span/a/text())"
            ).strip()

        if d.xpath("./@class")[0] == "o-chart-position-stats__peak":
            debute_data[d.xpath("string(.//h3/text())").strip()] = d.xpath(
                "string(.//span/text())"
            ).strip()
            debute_data[d.xpath("string(.//h4/text())").strip()] = d.xpath(
                "string(.//span/a/text())"
            ).strip()

        if d.xpath("./@class")[0] == "o-chart-share //":
            debute_data[d.xpath("string(.//h3/text())").strip()] = {
                i.xpath("string(.//span/text())")
                .strip(): i.xpath("string(./@href)")
                .strip()
                for i in d.xpath(".//a")
            }

        if d.xpath("./@class")[0] == "o-chart-awards-list":
            debute_data["Awards"] = ",".join([i.xpath("string(.//p/text())").strip() for i in d.xpath(".//div")])
    
    
    song.append(
        {
            "count": count,
            "song_name": song_name,
            "artist": a_artist if a_artist else artist,
            "image": s.xpath(
                "string(.//img[contains(@class,'c-lazy-image__img')]/@src)"
            ),
            "other": other,
            "meta_data": debute_data,
        }
    )
    cur.execute("""
        INSERT INTO song(song_name,artist,image,lw,peak,weeks,debut_position,debut_chart_date,peak_position,peak_chart_date,share,awards) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,(
        song[-1].get('song_name'),
        song[-1].get('artist'),
        song[-1].get('image'),
        song[-1].get('other').get('LW'),
        song[-1].get('other').get('PEAK'),
        song[-1].get('other').get('WEEKS'),
        song[-1].get('meta_data').get('Debut Position'),
        song[-1].get('meta_data').get('Debut Chart Date'),
        song[-1].get('meta_data').get('Peak Position'),
        song[-1].get('meta_data').get('Peak Chart Date'),
        json.dumps(song[-1].get('meta_data').get('Share')),
        song[-1].get('meta_data').get('Awards') if song[-1].get('meta_data').get('Awards') else None,
    ))

    conn.commit()
conn.close()

with open("clean.json", "w", encoding="utf-8") as f:
    json.dump(song, f, indent=4, default=str)
