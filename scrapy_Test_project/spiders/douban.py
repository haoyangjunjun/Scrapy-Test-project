import scrapy
from scrapy import Selector
<<<<<<< HEAD
from scrapy.http import HtmlResponse
=======
>>>>>>> c5eecd26edc6c84e6816ee76f4f69638b69f52c0

from scrapy_Test_project.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

<<<<<<< HEAD
    def parse(self, response: HtmlResponse):
=======
    def parse(self, response):
>>>>>>> c5eecd26edc6c84e6816ee76f4f69638b69f52c0
        sel = Selector(response)  # 选择器对象
        list_items = sel.css('#content > div > div.article > ol > li')  # css解析, 列表
        for list_item in list_items:
            movie_item = MovieItem()  # 都组装在movieitem里了
            movie_item['title'] = list_item.css('span.title::text').extract_first()
            movie_item['rank'] = list_item.css('span.rating_num::text').extract_first()
            movie_item['subject'] = list_item.css('span.inq::text').extract_first()
            # extract_first()这个方法用于从选择器返回的结果中提取第一个匹配项的文本内容。如果选择器没有找到任何匹配项，它将返回 None
            yield movie_item  # 告诉 Scrapy 框架：“我找到了一个我感兴趣的数据项，请将其发送到后续的管道（Pipeline）中进行处理。”
<<<<<<< HEAD
        # 用return只能返回一个
        href_list = sel.css('div.paginator > a::attr(href)')  # 翻页选择器列表
        for href in href_list:
            url = response.urljoin(href.extract())  # 拼接url
            print(url)
=======
# 用return只能返回一个
>>>>>>> c5eecd26edc6c84e6816ee76f4f69638b69f52c0
