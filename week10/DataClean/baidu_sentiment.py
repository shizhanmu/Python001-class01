import time
import pandas as pd
import pymysql
import json
from aip import AipNlp

import config
from DBOperator import DBOperation


class SentimentAnalyzer(object):
    """ 百度AI情感倾向分析器 """

    def __init__(self):
        self.client = AipNlp(config.APP_ID, config.API_KEY, config.SECRET_KEY)

    def get_sentiment(self, text):
        """
        调用百度AI对一个字符串进行情感倾向分析
        分析成功返回sentiment整数，分析失败返回 -1
        """
        # 将 text从 UTF8编码转为GBK编码
        text = text.encode('gb18030', 'ignore').decode('gbk', 'ignore')
        try:
            result = self.client.sentimentClassify(text)
            # print(result)
            if 'items' in result:
                sentiment = result['items'][0]['sentiment']
                print('情感倾向值：', sentiment)
            else:
                print('分析失败')
                sentiment = -1
            time.sleep(1)
            return sentiment
        except Exception as e:
            print(e)
            return -1

    def batch_sentiment(self, source_table, dest_table):
        """
        利用pandas循环读取数据库记录，批量进行情感倾向分析
        :param source_table: 原始数据库表名
        :param dest_table: 目标数据库表名
        """
        dfs = DBOperation().iter_table_df(source_table)
        for df in dfs:
            df['sentiment'] = df['comment'].map(
                lambda a: self.get_sentiment(a))
            DBOperation().append_df_table(df, dest_table)


if __name__ == '__main__':
    sa = SentimentAnalyzer()
    sa.batch_sentiment('qipaoshui_cleaned', 'qipaoshui_cleaned2')
