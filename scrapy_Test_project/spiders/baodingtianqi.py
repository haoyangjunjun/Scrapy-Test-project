import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from scrapy_Test_project.items import MovieItem


class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ["tianqihoubao.com"]
    # start_urls = ["http://www.tianqihoubao.com/lishi/baoding/month/202301.html"]
    def start_requests(self):
        for month in range(1, 13):  # 月份从 1 到 12
            # 格式化月份为两位数，例如 '01', '02', ..., '12'
            formatted_month = f'{month:02d}'
            # 构造完整的 URL
            url = f'http://www.tianqihoubao.com/lishi/baoding/month/2023{formatted_month}.html'
            # 生成并返回 Request 对象
            yield Request(url=url)  # 假设您有一个名为 parse 的回调方法

    def parse(self, response: HtmlResponse, **kwargs):
        # 定位表格
        table = response.css('table:first-of-type')
        # 遍历表格的每一行
        for row in table.css('tr'):
            # 提取每一列的数据
            date = row.css('td:nth-child(1)::text').get()
            weather = row.css('td:nth-child(2)::text').get()
            temp_range = row.css('td:nth-child(3)::text').get()
            wind = row.css('td:nth-child(4)::text').get()

            # 创建一个字典来存储数据
            yield {
                'date': date,
                'weather': weather,
                'temp_range': temp_range,
                'wind': wind,
            }