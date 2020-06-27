# 第一周  作业一：
# 安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间
# 并以 UTF-8 字符集保存到 csv 格式的文件中。
# 难点：1. header里必须添加cookie信息。
#      2. 对bs4中的标签利用 [索引号] 提取相同标签中的内容

import requests
from bs4 import BeautifulSoup as bs
import re
from time import sleep
import pandas as pd


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
cookie = '''__mta=19176199.1593004055145.1593005658093.1593007927878.4; uuid_n_v=v1; uuid=AA238C10B61B11EA8A833903D31672836012E0D50DBA44E5BBE3ADECCD9B2E29; _csrf=790960f76c9f00ffa83475be376f8b23232ad50463f6dbb0ccb8063da85255d2; _lxsdk_cuid=172e670d396c8-03b1072a6b489f-6701b35-384000-172e670d396c8; _lxsdk=AA238C10B61B11EA8A833903D31672836012E0D50DBA44E5BBE3ADECCD9B2E29; mojo-uuid=977abed41d34bc696c901fc0c80766f2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593004053,1593008805; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593008814; __mta=19176199.1593004055145.1593007927878.1593008814624.5; _lxsdk_s=172e9387a50-975-7f6-2b0%7C%7C3'''
header = {'user-agent': user_agent, 'cookie': cookie}


def get_ten_urls(myurl):
    """ 提取前10个电影的详情页URL, 返回一个list """
    response = requests.get(myurl, headers=header)
    response.encoding = 'utf-8'
    bs_info = bs(response.text, 'html.parser')

    url_list = []
    cnt = 0
    for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
        for atag in tags.find_all('a',):
            url = 'https://maoyan.com' + atag.get('href')
            url_list.append(url)
            cnt += 1
        if cnt > 9:
            break
    return url_list


def get_movie_info(url):
    """ 从单个电影详情页中提取电影名称、电影类型和上映时间 """
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    bs_info = bs(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        name = tags.find('h1',).text
        print(name)
        movie_type = ''
        for atag in tags.find_all('a', ):
            movie_type += ' ' + atag.text.strip()
        movie_type = movie_type.strip()
        print(movie_type)
        li_tags = tags.find_all('li', attrs={'class': 'ellipsis'})
        raw_date = li_tags[2].text    # 提取第 3 个li标签中的文字
        play_date = re.match(r'\d{4}-\d{2}-\d{2}', raw_date).group()
        print(play_date)
    return [name, movie_type, play_date]


if __name__ == '__main__':
    myurl = 'https://maoyan.com/films?showType=3'
    ten_urls = get_ten_urls(myurl)  # 获取10个详情页地址
    movie_infos = []                # 电影信息汇总列表
    sleep(10)

    for page in ten_urls:   # 从10个页面中逐个提取电影信息，加入汇总列表
        movie_infos.append(get_movie_info(page))
        sleep(5)
    
    movies = pd.DataFrame(data=movie_infos)
    movies.to_csv('movies.csv', encoding='utf-8', index=False, header=False)
