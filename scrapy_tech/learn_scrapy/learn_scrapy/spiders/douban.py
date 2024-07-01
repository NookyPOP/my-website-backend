import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from learn_scrapy.items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    # }

    def start_requests(self):
        for page in range(10):
            url = f"https://movie.douban.com/top250?start={page * 25}&filter="
            # yield Request(url, headers=self.headers)
            yield Request(url)

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        movie_items = sel.css("#content > div > div.article > ol > li")
        for movie_sel in movie_items:
            item = DoubanItem()
            item["title"] = movie_sel.css(".title::text").get()
            item["score"] = movie_sel.css(".rating_num::text").get()
            item["motto"] = movie_sel.css(".inq::text").get()
            yield item

        # hrefs = sel.css(
        #     '#content > div > div.article > div.paginator > a::attr("href")'
        # )

        # for next_page in hrefs:
        #     yield response.follow(
        #         next_page,
        #         self.parse,
        #         headers=self.headers,
        #     )
        # """ 通过运行爬虫获得的 JSON 文件中有275条数据，那是因为首页被重复爬取了。
        # 要解决这个问题，可以对上面的代码稍作调整，
        # 不在parse方法中解析获取新页面的 URL，
        # 而是通过start_requests方法提前准备好待爬取页面的 URL，调整后的代码如下所示。
        #
        # """
