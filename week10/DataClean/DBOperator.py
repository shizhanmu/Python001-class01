import os
import sys
import datetime
import pymysql
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import NVARCHAR, Float, Integer
from pymysql import DatabaseError
from pandas.io.sql import DatabaseError as PandasDatabaseError

import config


# 创建数据库表的sql语句
# CREATE TABLE `qipaoshui`  (
#   `id` int(20) NOT NULL AUTO_INCREMENT,
#   `pid_id` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
#   `title` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
#   `comment` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
#   `qptime` datetime(0) NULL DEFAULT NULL,
#   PRIMARY KEY (`id`) USING BTREE
# ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;


class DBOperation(object):
    """ 操作数据库的工具类 """
    # 创建数据库连接/引擎
    conn = pymysql.connect(host=config.HOST,
                            port=config.PORT,
                            user=config.USERNAME,
                            password=config.PASSWORD,
                            db=config.DB,
                            charset=config.CHARSET)
    engine = create_engine(f'mysql+pymysql://{config.USERNAME}:{config.PASSWORD}@{config.HOST}/{config.DB}')

    @classmethod
    def run(cls, sql):
        with cls.conn.cursor() as cur:
            cur.execute(sql)
            cls.conn.commit()
            print("Executed succesfully!")

    @classmethod
    def read_table_df(cls, table):
        """ 从数据库表中读取数据，返回 Dataframe """
        sql = f'SELECT * FROM {table}'
        try:
            dataframe = pd.read_sql(sql, cls.conn)
            # print(dataframe)
            total = dataframe.shape[0]
            print(f'读取成功：共 {total} 条记录 (来自 {table} 表)')
        except PandasDatabaseError as e:
            print('数据库读取失败', e)
        return dataframe


    @classmethod
    def iter_table_df(cls, table, limit=5):
        """ 从数据库表中循环分批读取数据，每次定量吐出 Dataframe """
        try:
            id = 0 
            while True:
                sql = f'SELECT * FROM {table} WHERE id > {id} limit {limit}';
                dataframe = pd.read_sql(sql, cls.conn)
                if dataframe.shape[0] == 0:             # 数据数量为空则退出循环
                    break
                id = dataframe.tail(1).values[0][0]     # 获取最后一条数据的id号
                print(f'读取了 {dataframe.shape[0]} 条记录 (来自 {table} 表)')
                yield dataframe
        except PandasDatabaseError as e:
            print('数据库读取失败', e)

    @classmethod
    def write_df_table(cls, dataframe, table):
        """ 将 DataFrame 数据覆盖保存至数据库表 """
        dtypedict = {
            'id': Integer(),
            'pid_id': Integer(),
            'title': NVARCHAR(length=255),
            'sentiment': Integer(),
            'count': Integer(),
            'mean': Float()
        }
        dataframe.to_sql(name=table, con=cls.engine, if_exists="replace", index=False, dtype=dtypedict)
        print(f'数据库写入成功')
        # print('数据库写入失败', e)

    @classmethod
    def append_df_table(cls, dataframe, table):
        """ 将 DataFrame 数据追加至数据库表 """
        dataframe.to_sql(name=table, con=cls.engine, if_exists="append", index=False)
        print(f'数据库写入成功')
        # print('数据库写入失败', e)


if __name__ == "__main__":
    do = DBOperation()
    df = do.read_table_df('qipaoshui_test')
    do.write_df_table(df, 'qipaoshui_test2')
