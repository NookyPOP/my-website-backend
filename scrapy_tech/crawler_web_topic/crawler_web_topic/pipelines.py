# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
from crawler_web_topic.items import CrawlerWebTopicItem
import datetime


class CrawlerWebTopicPipeline:
    def __init__(self) -> None:
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = "微博话题"
        self.sheet.append(("话题", "状态", "热度", "链接"))

    def process_item(self, item: CrawlerWebTopicItem, spider):
        self.sheet.append((item["title"], item["status"], item["heat"], item["url"]))
        return item

    def close_spider(self, spider):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.wb.save(f"微博话题列表-{date}.xlsx")
