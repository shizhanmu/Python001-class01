# 学习笔记

1. 关于Django+Nginx+Gunicorn三兄弟这篇说得太清楚了：
https://www.jianshu.com/p/c85a7604ae61
如果用餐馆来做比喻的话，Nginx 就是迎宾小姐，客人如果点了酒水，迎宾小姐自己就帮忙拿了；而 Gunicorn 是传菜员，Django 是厨师，他两一起满足客人对现炒美食的需求。

2. 专门测试网站负载的：https://loader.io/ 
   
3. dj-static 管理django 静态文件 static
    https://pypi.org/project/dj-static/


    Usage
    Configure your static assets in settings.py:
    STATIC_ROOT = 'staticfiles'

    STATIC_URL = '/static/'
    Then, update your wsgi.py file to use dj-static:
    from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())


    安装gunicorn
    $ pip install gunicorn


    运行gunicorn
    $ gunicorn -b 0.0.0.0:8000 tree_project.wsgi
    其中 tree_project为django项目文件夹名称，gunicorn会自动搜索到相应的文件。