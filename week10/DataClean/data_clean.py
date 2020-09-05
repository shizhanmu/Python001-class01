import datetime
import random
import pandas as pd
import numpy as np
import  pymysql
from sqlalchemy import create_engine

import config
from DBOperator import DBOperation


def random_datetime():
    """ 产生指定格式的随机时间 """
    now = datetime.datetime.now()
    days = random.uniform(1, 100)
    delta = datetime.timedelta(days=days)
    ndt = now - delta
    dt = ndt.strftime("%Y-%m-%d %H:%M:%S")
    return ndt

def update_qptime(table):
    """ 用sql给表中所有数据插入随机时间（模拟发布时间） """
    con = DBOperation().conn
    with con.cursor() as cur:
        sql = f"""select id from {table};"""
        cur.execute(sql)
        result = cur.fetchall()
        for line in result:
            id = line[0]
            sql = """update {} set qptime='{}' where id={};""".format(table, random_datetime(), id)
            cur.execute(sql)
    con.commit()
    con.close()
    print('数据库写入成功')


# def update_qptime(source_table, dest_table):
#     """ 利用pandas中的apply批量插入随机时间"""
#     do = DBOperation()
#     df = do.read_table_df(source_table)
#     df['qptime'] = df['qptime'].apply(lambda x: random_datetime())
#     do.write_df_table(df, dest_table)


def clean_data(source_table, dest_table):
    df = DBOperation().read_table_df(source_table)
    df.isnull().sum()                           # 没有发现空值，但是有空格
    df.loc[df['comment'] == ' '] = None         # 将空格替换为空值 也可 =np.NaN
    df.isnull().sum()                           # 或 df.isna().sum()
    df = df.dropna(subset=['comment'])          # 将 comment 为空值的行删除
    df.isna().sum()
    df.drop_duplicates()                        # 删除重复数据
    value_counts = df['pid_id'].value_counts()     # 获取 pid_id 计数
    to_remove = value_counts[value_counts <= 3].index  # 获取评论数<3的行的索引名称
    df =df[~df['pid_id'].isin(to_remove)]          # 删去相应的记录
    df = df.dropna() 
    DBOperation().write_df_table(df, dest_table)  # 存入另一个表，否则报错

def get_mean(table):
    """ 将情感倾向分析的平均值写入数据库表 """
    do = DBOperation()
    df = do.read_table_df(table)
    # 通过分组统计pid_id相同的记录数量
    df2 = df.groupby(['pid_id', 'title']).size().reset_index(name='count') # 分别统计各产品评论数
    df3 = df.groupby('pid_id').mean()          # 求均值
    df3 = df3.reset_index().drop(['id'],  axis=1)  # 删除无用的id列
    df3 = df3.rename(columns = {'pid_id':'pid_id', 'sentiment':'mean'})  # 表头改名
    m = df3.set_index('pid_id')['mean']        # 以pid_id为df3的索引
    df2['mean'] = df2['pid_id'].map(m)         # 这步是关键，将df3中的均值映射到df2中
    # df2 = df2.drop(df2[df2['count'] < 3].index)       # 删除评论数在 3 以下的行 
    df2 = df2.sort_values(by=['mean'],  ascending=False)  # 降序排列
    df2 = df2.reset_index(drop=True)        # 添加新的id索引
    # df2.index = df2.index + 1               # 修改索引从 1 开始
    # df2 = df2.reset_index()                 # 将索引作为表的一列
    # df2 = df2.rename(columns = {'index':'id', 'pid_id':'pid_id', 'title':'title', 'count':'count', 'mean':'mean'}) # 改列名
    df2 = df2.rename(columns = {'pid_id':'id', 'title':'title', 'count':'count', 'mean':'mean'}) # 改列名 pid_id -> id
    do.write_df_table(df2, 'stat_table')
    sql = 'ALTER TABLE stat_table ADD PRIMARY KEY(id);' # 将id字段设置为主键
    do.run(sql)

if __name__ == '__main__':
    # update_qptime('qipaoshui')                    # 插入随机发布时间
    # clean_data('qipaoshui_cleaned2', 'qipaoshui_cleaned')  # 删除空值和重复值
    get_mean('qipaoshui_cleaned')                   # 生成按sentiment排序的新表
