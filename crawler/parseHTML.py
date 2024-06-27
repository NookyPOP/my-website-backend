from lxml import etree
import requests
import bs4

# for page in range(1, 2):
#     resp = requests.get(
#         url=f"https://movie.douban.com/top250?start={(page - 1) * 25}",
#         headers={"User-Agent": "BaiduSpider"},
#     )
#     tree = etree.HTML(resp.text)
#     # print(tree, resp.text)
#     # 通过xPath语法冲页面中提取电影标题
#     title_spans = tree.xpath(
#         '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]'
#     )
#     title_span_engs = tree.xpath(
#         '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[2]'
#     )

#     movie_ranks = tree.xpath(
#         '//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]'
#     )
#     sts = "/html/body/div[3]/div[1]/div/div[1]/ol/li[1]/div/div[2]/div[1]/a/span[1]"
#     print(title_spans, title_span_engs, movie_ranks, list(title_spans))

#     for title_span, title_span_eng, movie_rank in zip(
#         title_spans, title_span_engs, movie_ranks
#     ):
#         print(title_span.text, title_span_eng.text, movie_rank.text)

for page in range(1, 2):
    resp = requests.get(
        url=f"https://movie.douban.com/top250?start={(page - 1) * 25}",
        headers={"User-Agent": "BaiduSpider"},
    )
    # 创建一个 BeautifulSoup 对象
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    # 通过css选择器从页面中提取电影标题
    titles = soup.select("div.info > div.hd> a > span:nth-child(1)")
    ranks = soup.select(" div.info > div.bd > div > span.rating_num")
    print(titles[0].text, ranks[0].text)
