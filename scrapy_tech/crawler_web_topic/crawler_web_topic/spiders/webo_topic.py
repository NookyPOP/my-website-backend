from typing import Iterable
import scrapy
from scrapy.http import HtmlResponse, Request
from scrapy import Selector, Request
from crawler_web_topic.items import CrawlerWebTopicItem


class WeboTopicSpider(scrapy.Spider):
    name = "weibo_topic"
    allowed_domains = ["weibo.com"]

    def start_requests(self) -> Iterable[Request]:
        yield Request("https://weibo.com/newlogin?tabtype=search&gid=&openLoginLayer=0&url=")

    def parse(self, response: HtmlResponse):
        sel = Selector(response)

        topic_list = sel.css("#scroller > div.vue-recycle-scroller__item-wrapper > div")
        print(topic_list)
        for topic in topic_list:
            item = CrawlerWebTopicItem()
            item["title"] = topic.css("a::text").get()
            item["url"] = topic.css("a::attr(href)").get()
            item["status"] = topic.css(
                " div.woo-box-flex.woo-box-alignCenter > span::text"
            ).get()
            item["heat"] = topic.css("div.HotTopic_num_1H-j8 > span::text").get()
            yield item
