import requests
import lxml.etree
import conn
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
                 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36',
}


def get_page(url):
    try:
        with requests.session() as s:
            s.headers.update(headers)
            r = s.get(url)
            return r.text
    except Exception as err:
        print(err)


def parse_page(html):
    pos_list = []
    sel = lxml.etree.HTML(html)
    city = sel.xpath('//a[@class="current_city current"]/text()')[0]
    lis = sel.xpath('//li[@class="con_list_item default_list"]')
    for li in lis:
        title = li.xpath('./@data-positionname')[0].lower()
        salary = li.xpath('./@data-salary')[0]
        pos_list.append({'city': city, 'title': title, 'salary': salary})
    return pos_list


def gen_sqls(pos_list):
    sqls = []
    for d in pos_list:
        city = d['city']
        title = d['title']
        salary = d['salary']
        sql = f"insert ignore into position values(null, \'{city}\',\'{title}\',\'{salary}\')"
        sqls.append(sql)
    return sqls


def gen_urls():
    urls = {'https://www.lagou.com/beijing-zhaopin/Python/', 'https://www.lagou.com/shanghai-zhaopin/Python/',
            'https://www.lagou.com/guangzhou-zhaopin/Python/', 'https://www.lagou.com/shenzhen-zhaopin/Python/'}
    for url in urls:
        page_total = 5  # 应通过xpath解析页面获取页面总数，时间来不及了，略
        for page in range(1, page_total+1):
            q.put(url+str(page))


def main():
    gen_urls()
    with ThreadPoolExecutor(max_workers=4) as executor:
        task_list = [executor.submit(get_page, q.get())\
                     for i in range(q.qsize())]

    try:
        db = conn.ConnDB()
        for f in concurrent.futures.as_completed(task_list):
            html = f.result()
            pos_list = parse_page(html)
            sqls = gen_sqls(pos_list)
            db.execute(sqls)
            print('Parsed one page.')
    except Exception as e:
        print(e)
    finally:
        db.close()


if __name__ == '__main__':
    q = Queue()
    main()
