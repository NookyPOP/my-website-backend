import re
import requests
import random
import time


for page in range(1, 2):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page-1)*25}",
        # 使用浏览器的User-Agent来骗过服务器，不是爬虫
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
    )
    title_pattern = re.compile(r'<span class="title">([^&nbsp;/&nbsp;].*?)</span>')
    titles = title_pattern.findall(resp.text)
    title_eng_pattern = re.compile(r'<span class="title">([&nbsp;/&nbsp;].*?)</span>')
    tilte_engs = title_eng_pattern.findall(resp.text)

    rank_pattern = re.compile(r'<span class="rating_num".*?>(.*?)</span>')
    ranks = rank_pattern.findall(resp.text)

    print(titles, tilte_engs, ranks)

    time.sleep(random.random() * 4 + 1)
