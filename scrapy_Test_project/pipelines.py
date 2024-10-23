# Define your item pipelines here
# 管道
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl


class ScrapyTestProjectPipeline:

    def __init__(self):  # 初始化方法，创建工作簿
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'Top 250'
        self.ws.append(('标题', '评分', '主题'))  # self管道对象

    def close_spider(self, spider):
        self.wb.save('电影数据.xlsx')

    def process_item(self, item, spider):
        return item
