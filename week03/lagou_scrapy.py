import requests
from lxml import etree
from queue import Queue
import threading
import json


class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''
    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue

    def run(self):
        '''
        重写run方法
        '''
        print(f'启动线程：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        while True:
            if self.queue.empty():  # 队列为空不处理
                break
            else:
                page = self.queue.get()
                print('下载线程为：', self.thread_id, ' 下载页面：', page)
                url = f'https://book.douban.com/top250?start={page*25}'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
                }
                try:
                    # downloader 下载器
                    response = requests.get(url, headers=headers)
                    dataQueue.put(response.text)
                except Exception as e:
                    print('下载出现异常', e)
    

class ParserThread(threading.Thread):
    '''
    页面内容分析d
    '''
    def __init__(self, thread_id, queue, file):
        super().__init__(self)
        self.thread_id = threading
        self.queue = queue
        self.file = file

    def run(self):
        print(f'启动线程：{self.thread_id}')
        while not flag:
            try:
                item = self.queue.get(False)  # 参数为false时队列为空，抛出异常
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done()  # get之后检测是否阻塞
            except Exception as e:
                pass
