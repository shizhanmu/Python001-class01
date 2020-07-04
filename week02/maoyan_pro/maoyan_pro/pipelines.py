# -*- coding: utf-8 -*-
# 第二周 作业一：
# 为 Scrapy 增加代理 IP 功能。
# 将保存至 csv 文件的功能修改为保持到 MySQL，并在下载部分增加异常捕获和处理机制。
# 备注：代理 IP 可以使用 GitHub 提供的免费 IP 库。

import csv
import pymysql.cursors
from scrapy.exporters import CsvItemExporter


dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : '12345678',
    'charset' : 'utf8mb4',
    'db' : 'hotmovie'
}


# Connect to the database
connection = pymysql.connect(host=dbInfo['host'],
                             port=dbInfo['port'],
                             user=dbInfo['user'],
                             password=dbInfo['password'],
                             db=dbInfo['db'],
                             charset=dbInfo['charset'],
                             cursorclass=pymysql.cursors.DictCursor)

cursor = None

class MaoyanProPipeline:

    def open_spider(self, spider):
        global cursor
        cursor = connection.cursor()


    def process_item(self, item, spider):
        global cursor
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        play_date = item['play_date']

        try:
            # Create a new record
            sql = "INSERT INTO `movie_info` (`movie_name`, `movie_type`, `play_date`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (movie_name, movie_type, play_date))
        except:
            cursor.rollback()
            # with connection.cursor() as cursor:
            #     # Read a single record
            #     sql = "SELECT `movie_name`, `movie_type`, `play_date` FROM `movie_info`"
            #     cursor.execute(sql)
            #     result = cursor.fetchone()
            #     print(result)

        return item

    def close_spider(self, spider):
        cursor.close()
        connection.commit()
        connection.close()