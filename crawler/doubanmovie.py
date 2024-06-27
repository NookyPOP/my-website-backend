import re
import requests
import random
import time

top_250 = []
for page in range(1, 11):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page - 1) * 5}",
        # 使用浏览器的User-Agent来骗过服务器，不是爬虫
        headers={"User-Agent": "BaiduSpider"},
    )
    title_pattern = re.compile(r'<span class="title">([^&nbsp;/&nbsp;].*?)</span>')
    titles = title_pattern.findall(resp.text)
    title_eng_pattern = re.compile(r'<span class="title">([&nbsp;/&nbsp;].*?)</span>')
    tilte_engs = [
        title_eng.replace("&nbsp;/&nbsp;", "")
        for title_eng in title_eng_pattern.findall(resp.text)
    ]

    rank_pattern = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    ranks = rank_pattern.findall(resp.text)

    print(titles, tilte_engs, ranks)

    for title, title_eng, rank in zip(titles, tilte_engs, ranks):
        movie = {"title": title, "title_eng": title_eng, "rank": rank}
        top_250.append(movie)

    time.sleep(random.random() * 4 + 1)

print(top_250)
