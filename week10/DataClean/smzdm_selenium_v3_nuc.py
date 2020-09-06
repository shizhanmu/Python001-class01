# coding: utf-8
import time
import json
import os
import sys
import re
import random
import logging
from functools import partial
from itertools import count

from selenium import webdriver
import pyautogui
from lxml import etree

from DBOperator import DBOperation


class cached_class_property(object):
    """ 类属性缓存装饰器 """
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(cls, self.func.__name__, value)
        return value


class DriverWrapper():
    """
    基于selenium的二次封装
    参考：https://www.cnblogs.com/ydf0509/p/9221969.html
    """

    def __init__(self, driver_name):
        """
        :param driver_name: 浏览器名字数字或者字母
        """
        self.driver_name = driver_name


    @cached_class_property
    def driver(self):
        browser = None
        if self.driver_name in ['chrome', 1]:
            browser = webdriver.Chrome()
            options = webdriver.ChromeOptions()
            options.add_argument('lang=zh_CN.UTF-8')
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_argument(f'--proxy-server={self.random_proxy()}')
            options.add_argument(f'user-agent={self.random_user_agent()}')
            browser = webdriver.Chrome(options=options)
            browser.maximize_window()
            browser.implicitly_wait(30)
            time.sleep(3)
        if self.driver_name in ['firefox', 2]:
            browser = webdriver.firefox()
        
        return browser


    @cached_class_property
    def logger(self):
        logger_var = logging.getLogger(self.__class__.__name__)
        logger_var.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S"))
        logger_var.addHandler(stream_handler)
        return logger_var

    @staticmethod
    def random_user_agent():
        # 获取随机user_agent
        user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        ]
        return random.choice(user_agents)

    @staticmethod
    def random_proxy():
        """ 获取随机proxy地址 """
        with open('proxy_list.txt') as f:
            try:
                proxy_list = f.readlines()
            except Exception as e:
                print(e)
            return random.choice(proxy_list).strip()

    def open(self, url):
        self.driver.get(url)

    def find_element_by_xpath(self, xpath_str):  # 使用自定义的方法覆盖了原方法，比如先打印出一段话
        self.logger.debug('要查找的元素的xpath选择器是 --> ' + xpath_str)
        self.driver.find_element_by_xpath(xpath_str)

    def __getattr__(self, item):  # 想把其他的webdriver的操作方法直接添加进来，不一个一个的再写一个方法然后调用driver属性的方法，不想一直搞冗余的代码，可以这么做。python先使用__getattribute__，查不到才会调用__getsttr__方法，利用这个特性，来实现这个添加driver的属性到自己类里面
        return getattr(self.driver, item)


class Smzdm():
    """ 用 selenim和 pyautogui获取产品评论 """
    def __init__(self):
        self.items = []
        self.counter = partial(next, count())
        self.err_counter = partial(next, count())
        self.driver = DriverWrapper('chrome')
        # self.read_cookies()


    @staticmethod
    def get_html(url):
        """ 获取页面 html元素 """
        self.driver.get(url)
        self.driver.implicitly_wait(30)
        time.sleep(random.randint(1, 5))
        html = etree.HTML(self.driver.page_source)  # 获取html元素
        print(html)
        return html


    def save_cookies(self, start_url):
        # 模拟登录，获取cookie
        try:
            try:
                self.driver.get(start_url)
                self.driver.implicitly_wait(30)
            except Exception as e:
                print('Failed to connect', e)
            time.sleep(2)
            pyautogui.click(x=2700, y=190)
            self.driver.implicitly_wait(30)
            time.sleep(2)
            pyautogui.click(x=2180, y=840)
            self.driver.implicitly_wait(30)
            time.sleep(3)
            pyautogui.doubleClick(x=1835, y=976)
            time.sleep(1)
            pyautogui.write('13121661863', interval=0.25)
            pyautogui.press('esc')
            pyautogui.doubleClick(x=1800, y=1070)
            time.sleep(1)
            pyautogui.write('tert1234', interval=0.25)
            pyautogui.press('esc')
            time.sleep(5)
            pyautogui.click(x=1900, y=1238)
            self.driver.implicitly_wait(30)
            time.sleep(2)
            cookies = self.driver.get_cookies()   # 获取cookies
            with open("D:\VScodeProjects\django_projects\cookies.json", "w") as fp:  # 将cookies保存到json文件
                json.dump(cookies, fp)
        
        except Exception as e:
            print(e)


    def read_cookies(self):
        """ 从json文件中读取cookie信息 """
        with open("D:\VScodeProjects\django_projects\cookies.json", "r") as fp:
            cookies = json.load(fp)
            for cookie in cookies:
                self.driver.add_cookie(cookie)


    @staticmethod
    def generate_url(start_url):
        """ 生成产品列表的分页url """
        n = 0
        while True:
            n += 1
            url = os.path.join(start_url, f'p{n}/#feed-main')
            yield url


    @staticmethod
    def generate_comment_url(comment_tuple):
        """
        生成评论列表页的 URL list
        comment_tuple 是元祖类型，包含评论首页URL和评论总数
        """
        total = int(comment_tuple[1])
        page_count = total // 30 + (total % 30 > 0)  # 计算评论总页数
        url_list = []
        for n in range(1, page_count + 1):
            left_url = comment_tuple[0].rstrip('#comments')
            url = os.path.join(left_url, f'p{n}/#comments')
            url_list.append(url)
        return url_list


    def fetch_comment_url(self, start_url):
        """提取评论页 URL（评论数量 > 2）"""
        try:
            # self.read_cookies()
            gu = self.generate_url(start_url)       # 产品列表页 URL生成器初始化
            self.driver.get(next(gu))               # 获取一个产品列表页
            self.driver.implicitly_wait(30)
            time.sleep(random.randint(1, 5))
            
            # 以下4行注释为本地调试代码
            # pagefile = 'D:/VScodeProjects/django_projects/graduate_pro/graduate_pro/smzdm/smzdm/spiders/html_pages/最新全部精选气泡水优惠信息大全_什么值得买.html'
            # with open(pagefile, 'r', encoding='utf-8') as f:
            #     content = f.read()
            # html = etree.HTML(content)
            
            # 解析列表页HTML内容
            html = etree.HTML(self.driver.page_source)  # 获取html元素
            tags = html.xpath('//li[@class="feed-row-wide"]')
            for tag in tags:
                comment_number = tag.xpath('div//i[@class="icon-comment-o-thin"]/following-sibling::span/text()')[0]
                if int(comment_number) > 2:              # 至少3条评论
                    url = tag.xpath('div//h5/a/@href')[0]
                    comment_url = os.path.join(url, '#comments')
                    yield (comment_url, comment_number)

        except Exception as e:
            err_cnt = self.err_counter()
            print('Failed to fetch comments', err_cnt, 'times.\n', e )
            if err_cnt > 3:                    #如果出错超3次，自动退出程序
                print('The end.')
                sys.exit()

        finally:
            self.fetch_comment_url(start_url)           # 递归解析下一个列表页


    def fetch_all_comment_url(self, start_url):
        """ 生成所有评论列表页的 url """
        all_comment_url_list = []
        for url_tuple in self.fetch_comment_url(start_url):
            one_comment_url_list = self.generate_comment_url(url_tuple)
            all_comment_url_list.extend(one_comment_url_list)
        print(all_comment_url_list)
        return all_comment_url_list


    def fetch_comments(self, url):
        """ 获取单个页面的所有评论。返回在当前页不重复的评论 list """
        try:
            # self.read_cookies()
            self.driver.get(url)
            self.driver.implicitly_wait(30)
            time.sleep(random.randint(1, 5))

            # 设置文件名，保存网页为 html文件
            filename = url.lstrip('https://www.smzdm.com/p/').replace('/', '_') + '.html'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.driver.page_source)
                print(filename, '写入成功')
            
            # 以下3行注释为本地调试代码
            # with open(url, 'r', encoding='utf-8') as f:
            #     content = f.read()
            # html = etree.HTML(content)

            # 解析网页内容
            html = etree.HTML(self.driver.page_source)
            print("Fetching comments：", url)
            comments = set()                            # 初始化评论集合
            title = html.xpath('//h1[@class="title J_title"]/text()')[0]
            title = ' '.join(title.split())             # 去除标题中多余空格
            pid = re.findall(r"/([\d]+)/", url)[0]
            tags = html.xpath('//li[@class="comment_list"]')
            for tag in tags:
                comment = tag.xpath('div[2]//span[@itemprop="description"]/text()')[0]
                cnt = self.counter()                    # 计数器 + 1
                comments.add(comment)                   # 向集合中添加评论
            for comment in comments:                    # 向items列表添加记录
                self.items.append({'pid': pid, 'title': title, 'comment': comment})
                print('产品ID：', pid, ' | ', '产品标题：', title, ' | ', '评论总数：', cnt)

        except Exception as e:
            print(e)

    def save_to_db(self):
        """  
        将items字典列表保存至数据库
        列表格式：self.items = [
        {'pid': '1231213', 'title': 'title1', 'comment': 'comment1'},
        {'pid': '6757677', 'title': 'title2', 'comment': 'comment2'},
        {'pid': '455642', 'title': 'title3', 'comment': 'comment3'}]
        """
        for item in self.items:
            sql = f"""INSERT INTO qipaoshui (pid, title, comment) VALUES ('{item['pid']}', '{item['title']}', '{item['comment']}');"""
            DBOperation().run(sql)


if __name__ == "__main__":
    start_url = 'https://www.smzdm.com/fenlei/qipaoshui/'
    smzdm = Smzdm()
    smzdm.save_cookies(start_url)
    all_comment_url_list = smzdm.fetch_all_comment_url(start_url)
    for url in all_comment_url_list:
        smzdm.fetch_comments(url)
    smzdm.save_to_db()