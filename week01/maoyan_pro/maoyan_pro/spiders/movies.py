# -*- coding: utf-8 -*-
# 第一周 作业二：
# 使用 Scrapy 框架和 XPath 抓取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
# 要求：必须使用 Scrapy 框架及其自带的 item pipeline、选择器功能，不允许使用 bs4 进行页面内容的筛选。
# 难点： 1.在settings中设置headers才能使用　scrapy shell （COOKIES_ENABLED = False， DEFAULT_REQUEST_HEADERS）
#       2.理解yield一行中的callback，循环调用parse方法解析网页内容, 可多层调用parse

import scrapy
from bs4 import BeautifulSoup
from maoyan_pro.items import MaoyanProItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
            yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        for i in range(10):
            url = response.css('div.channel-detail.movie-item-title a::attr(href)')[i].get()
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_movie)

    def parse_movie(self, response):
        items = []
        movie_name = response.css('div.movie-brief-container h1.name::text').get()
        type_list = response.css('div.movie-brief-container a::text').getall()
        type_list = [s.strip() for s in type_list]
        movie_type = ' '.join(type_list)
        raw_date = response.css('div.movie-brief-container li.ellipsis::text')[-1]
        play_date = raw_date.re_first(r'\d{4}-\d{2}-\d{2}')
        item = MaoyanProItem()
        item['movie_name'] = movie_name
        item['movie_type'] = movie_type
        item['play_date'] = play_date
        items.append(item)
        return items