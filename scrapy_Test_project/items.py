# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):  # 组装为item对象
    title = scrapy.Field()
    rank = scrapy.Field()
    subject = scrapy.Field()


# 这意味着在抓取网页时，我们会期望从每个网页中提取这三个字段的数据。

# class TianqiItem(scrapy.Item):  # 组装为item对象
#     title = scrapy.Field()
#     rank = scrapy.Field()
#     subject = scrapy.Field()
