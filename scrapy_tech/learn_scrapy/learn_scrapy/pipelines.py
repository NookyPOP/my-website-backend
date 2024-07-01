# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
from learn_scrapy.items import DoubanItem


class LearnScrapyPipeline:
    def process_item(self, item, spider):
        return item


class DoubanPipeline:
    def __init__(self) -> None:
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = "Top250 Movies"
        self.sheet.append(("电影名", "评分", "名言"))

    def process_item(self, item: DoubanItem, spider):
        self.sheet.append((item["title"], item["score"], item["motto"]))
        return item

    def close_spider(self, spider):
        self.wb.save("豆瓣电影数据.xlsx")
