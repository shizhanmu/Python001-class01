# -*- coding: utf-8 -*-
import random

BOT_NAME = 'maoyan_pro'

SPIDER_MODULES = ['maoyan_pro.spiders']
NEWSPIDER_MODULE = 'maoyan_pro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'maoyan_pro (+http://www.yourdomain.com)'


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Encoding': 'gzip, deflate, br',
 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
 'Cache-Control': 'max-age=0',
 'Connection': 'keep-alive',
 'Cookie': '''uuid_n_v=v1; uuid=1BC1AA00BD3311EA983E3B3CFFA467A9C6E5BF54244544DF887AFA7990BB5B74; _csrf=c3727939d1dda9790c1cef260ddecbecfcf4a39d1e26fdb024a07afbb9dbcf32; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593783780; _lxsdk_cuid=17314ea82cac8-0e59eafb4cee41-5d4e2a12-384000-17314ea82cac8; _lxsdk=1BC1AA00BD3311EA983E3B3CFFA467A9C6E5BF54244544DF887AFA7990BB5B74; mojo-uuid=b4d7ac684f6f60f9b0bbc4a9fb310825; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593783808; __mta=244152250.1593783781351.1593783781351.1593783807893.2; _lxsdk_s=17314ea82cc-2bf-c63-26f%7C%7C6''',
 'DNT': '1',
 'Host': 'maoyan.com',
 'Sec-Fetch-Dest': 'document',
 'Sec-Fetch-Mode': 'navigate',
 'Sec-Fetch-Site': 'none',
 'Sec-Fetch-User': '?1',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.14 Safari/537.36'
 }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maoyan_pro.middlewares.MaoyanProSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maoyan_pro.middlewares.MaoyanProDownloaderMiddleware': 543,
#}


DOWNLOADER_MIDDLEWARES = {
    'maoyan_pro.middlewares.MaoyanProDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'maoyan_pro.middlewares.RandomHttpProxyMiddleware': 400,
}

HTTP_PROXY_LIST = [
  'http://69.162.82.154:5836',
  'http://182.23.107.210:3128',
  'http://212.129.34.183:5836',
  'http://167.71.91.204:8080',
  'http://154.79.246.178:34577',
  'http://212.129.3.196:5836',
  'http://177.85.102.132:80',
  'http://5.101.195.166:18182',
  'http://45.188.184.70:8080',
  'http://181.209.82.154:23500',
  'http://182.160.119.154:8080',
  'http://46.37.30.30:80',
  'http://165.22.213.55:3128',
  'http://212.129.39.165:5836',
  'http://190.103.178.14:8080',
  'http://181.129.103.210:37647',
  'http://69.162.82.155:5836',
  'http://103.61.101.74:38871',
]


# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyan_pro.pipelines.MaoyanProPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
