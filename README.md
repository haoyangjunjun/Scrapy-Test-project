# Scrapy-Test-project

测试、学习 Scrapy

对 https://movie.douban.com/top250  进行爬取解析

跟随教程：

https://www.bilibili.com/video/BV1a14y1b7dw?vd_source=7f2e8da90ee6d1aad530032f3137a78c&spm_id_from=333.788.videopod.episodes&p=3

---

简单爬虫启动命令:

``scrapy crawl douban ``

保存为csv

``scrapy crawl douban -o douban.csv``

安装本项目三方库：

``pip install -r requirements.txt``

## 制作 Scrapy 爬虫 一共需要4步：

1. 新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
2. 明确目标 （编写items.py）：明确你想要抓取的目标
3. 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
4. 存储内容 （pipelines.py）：设计管道存储爬取内容

## 爬虫2号  -----  保定天气爬虫

目标：在

```
http://www.tianqihoubao.com/lishi/baoding/month/202010.html
```

爬取保定2021-2024的天气，并存入表中，供其他程序分析。

启动：``scrapy crawl weather ``  

添加一个数据整理程序，整理爬取到的表格

在项目内写了一个数据分析程序，可以生成一些图表，还有简单的统计数据
