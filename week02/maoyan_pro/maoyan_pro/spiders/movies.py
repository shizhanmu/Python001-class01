# -*- coding: utf-8 -*-
# 第二周 作业一：
# 为 Scrapy 增加代理 IP 功能。
# 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。

import scrapy
from maoyan_pro.items import MaoyanProItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')[:10].getall()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_movie)

    def parse_movie(self, response):
        items = []
        movie_name = response.xpath('//div[@class="movie-brief-container"]/h1/text()').get()
        type_list = response.xpath('//li[@class="ellipsis"]/a/text()').getall()
        type_list = [s.strip() for s in type_list]
        movie_type = ' '.join(type_list).strip()
        raw_date = response.xpath('//li[@class="ellipsis"]')[-1]
        play_date = raw_date.re_first(r'\d{4}-\d{2}-\d{2}')
        item = MaoyanProItem()
        item['movie_name'] = movie_name
        item['movie_type'] = movie_type
        item['play_date'] = play_date
        items.append(item)
        return items