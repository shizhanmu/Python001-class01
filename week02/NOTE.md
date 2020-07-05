# 学习笔记
### 作业一
1. 搜索免费ip代理比较困难，最后在github上找到一段简单的代码。
2. 虽然照着老师的程序写上了更换IP地址的部分，也运行成功了，但还是无法确定运行爬虫的时候是否真的更换了IP地址。
3. 使用系统代理及下载中间件更换ip
   - export http_proxy='http://ip地址:端口号'
   - 在settings文件中增的 DOWNLOADER_MIDDLEWARES 中增加 增加scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
   - middlewares.py 导入 from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
   - 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理
4. 异常处理还是不太会用，只能照葫芦画瓢。

### 作业二
1. 很简单就实现了。
