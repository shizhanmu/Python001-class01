# -*- coding: utf-8 -*-
# 第二周 作业一：
# 为 Scrapy 增加代理 IP 功能。
# 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。

import pymysql
from scrapy.exporters import CsvItemExporter


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '12345678',
    'charset' : 'utf8mb4',
    'db' : 'hotmovie'
}


class MaoyanProPipeline:

    def __init__(self):
        # Connect to the database
        conn = pymysql.connect(
            host=dbInfo['host'],
            port=dbInfo['port'],
            user=dbInfo['user'],
            password=dbInfo['password'],
            db=dbInfo['db'],
            charset=dbInfo['charset'],
            cursorclass=pymysql.cursors.DictCursor
        )
        self.conn = conn

    def open_spider(self, spider):
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        play_date = item['play_date']

        try:
            # Create a new record
            sql = "INSERT INTO `movie_info` (`movie_name`, `movie_type`, `play_date`) VALUES (%s, %s, %s)"
            values = (movie_name, movie_type, play_date)
            self.cur.execute(sql, values)
        except:
            self.cur.rollback()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.commit()
        self.conn.close()