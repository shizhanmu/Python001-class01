import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import random
from lxml import etree

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
user_agent = random.choice(user_agents)

with open('D:/VScodeProjects/django_projects/graduate_pro/proxy_list.txt') as f:
    try:
        proxy_list = f.readlines()
    except Exception as e:
        print(e)
PROXY = random.choice(proxy_list) # IP:PORT or HOST:PORT
print(PROXY)

for PROXY in proxy_list:
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f'--proxy-server={PROXY}')
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(5)

    try :
        driver.get("https://xxx.com/ip/")
        print("URL successfully Accessed")
        source = driver.page_source  # 获取html源代码
        with open(filename, 'a+', encoding='utf-8') as f:
            f.write(source)
            print(source, '写入成功', PROXY)
        time.sleep(5)
        driver.close()
    except TimeoutException as e:
        print("Page load Timeout Occured. Quiting !!!")
        driver.close()
