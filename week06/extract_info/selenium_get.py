# 将短评页保存为 html 文件，以便在后面的步骤中提取信息。
# 由于反爬没有做好，只能取得前面大约10页内容
from selenium import webdriver
from lxml import etree
import time
import random
import re

def generated_url(root, total):
    '''生成短评页的 url ，没用上，因反爬失败'''
    total_page = total//20
    a, b = root.split("?")
    for p in range(total_page + 2):
        if p == 0:
            url = root
        else:
            url = f"{a}?start={p * 20}&limit=20&sort=new_score&{b}"
        yield url

def url_id(url):
    ''' 从 url 地址中提取电影 id 号'''
    try:
        id = re.findall(r"/([\d]+)/", url)[0]
        return id
    except Exception as e:
        print("Can't find an id number in your url.", e)

def save_pages(url, total, folder):
    ''' 根据 url 地址及短评总数保存页面为 html 文件
        文件名以电影 id 号开头
    '''
    id = url_id(url)
    # 进入浏览器设置
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    # 修改 user-agent
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36\
                 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36"')
    browser = webdriver.Chrome(chrome_options=options)
    try:
        browser.get(url)
        # 保存短评的首页为 html文件
        with open(f"{folder}/{id}_000000.html", "w", encoding='utf-8') as f:
            f.write(browser.page_source)
        # 自动点击下一页，然后保存页面为 html文件
        for page in range(1, total+2):        
            btm1 = browser.find_element_by_xpath('//div[@id="paginator"]/a[@class="next"]')
            btm1.click()
            time.sleep(random.uniform(3, 10))
            with open(f"{folder}/{id}_{page:06}.html", "w", encoding='utf-8') as f:
                f.write(browser.page_source)
    except Exception as e:
        print(e)
    finally:
        # browser.close()
        pass


if __name__ == '__main__':
    root = 'https://movie.douban.com/subject/1292052/comments?status=P'
    # root = 'https://movie.douban.com/subject/1292052/comments?start=200&limit=20&sort=new_score&status=P'
    total = 382463  # 短评总数
    folder = 'short_html'
    save_pages(root, total, folder)
