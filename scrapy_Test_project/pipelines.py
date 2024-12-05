# Define your item pipelines here
# 管道
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter
import openpyxl


class ScrapyTestProjectPipeline:
    pass
    '''这里暂时注释掉了，因为爬虫douban和weather可能有冲突'''
    # def __init__(self):  # 初始化方法，创建工作簿
    #     self.wb = openpyxl.Workbook()
    #     self.ws = self.wb.active
    #     self.ws.title = 'Top 250'
    #     self.ws.append(('标题', '评分', '主题'))  # self管道对象
    #
    # def open_spider(self):
    #     pass
    #
    # def close_spider(self, spider):
    #     self.wb.save('电影数据.xlsx')
    #
    # def process_item(self, item, spider):  # 钩子/回调函数（方法）callback
    #     title = item.get('title', '')
    #     rank = item.get('rank', '')
    #     subject = item.get('subject', '')
    #     self.ws.append((title, rank, subject))
    #     return item


class WeatherPipeline:
    def __init__(self):
        # 初始化工作簿和工作表
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'Weather Data'
        # 添加表头
        self.ws.append(['Date', 'Weather', 'Temp Range', 'Wind'])

    def open_spider(self, spider):
        # 这个方法在爬虫开始时被调用
        pass

    def close_spider(self, spider):
        # 在爬虫结束时保存工作簿
        self.wb.save('weather_data.xlsx')

    def process_item(self, item, spider):
        item = self.clean_data(item)
        date = item.get('date', '')
        weather = item.get('weather', '')
        temp_range = item.get('temp_range', '')
        wind = item.get('wind', '')
        # 将数据追加到工作表中
        self.ws.append([date, weather, temp_range, wind])
        # 返回item以便后续的pipeline（如果有的话）可以进一步处理
        return item

    def clean_data(self, data):
        cleaned_data = {}
        for key, value in data.items():
            # 去除前后空白字符，并替换所有的换行符和多余的空格为空字符串
            cleaned_value = value.strip().replace('\r\n', '').replace('\n', '').replace(' +', ' ')
            # 对于日期，去除多余的空格，但保留一个空格作为分隔符
            if key == 'date':
                cleaned_value = re.sub(r'\s+', ' ', cleaned_value).strip()
                # 可能还需要根据具体的日期格式进行进一步处理
            # 对于天气，去除多余的空格和换行符，并保留 '/' 分隔符
            elif key == 'weather':
                cleaned_value = '/'.join(part.strip() for part in cleaned_value.split('/') if part.strip())
            # 对于温度范围，尝试拆分并重新格式化，如果无法拆分则保留原始值
            elif key == 'temp_range':
                cleaned_value = '/'.join(part.strip() for part in cleaned_value.split('/') if part.strip())
            # 对于风，同样处理多余的空格和换行符
            elif key == 'wind':
                cleaned_value = '/'.join(part.strip() for part in cleaned_value.split('/') if part.strip())
            cleaned_data[key] = cleaned_value
        return cleaned_data
