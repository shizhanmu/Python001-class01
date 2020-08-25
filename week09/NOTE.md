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
  
4. 解决在vscode里 按command键点击path，go to definition 无法出现partial而是type hint(conf.pyi文件)的问题：
  - 删除插件pylance
  - pycharm也会遇到类似的问题，File->Setting->Editor->Code Style->File Types中找到Python Stub
    然后将Registered Patterns里面的内容清空就好了
    pycharm默认认为你"不需要"看源代码，就转到pyi上面了，pyi实际是type hint ，类型提示，所以看不到源码 
    关于type hint 参考 pep-0484
  
5. 导入路径问题。如果本地文件名celery与第三方包的文件名相同，而需要从第三方包的路径导入时必须在__init__.py*最上方*加入 from __future__ import absolute_import 。这样， from celery import Celery, platforms则是从第三方包的路径导入。
如果要引入本地的celery.py文件，则要用 from .celery import app as celery_app 。