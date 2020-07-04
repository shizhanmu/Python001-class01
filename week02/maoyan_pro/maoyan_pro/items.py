# -*- coding: utf-8 -*-

import scrapy


class MaoyanProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_type = scrapy.Field()
    play_date = scrapy.Field()
