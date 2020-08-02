# 学习笔记

反爬还是搞不定，request和selenium自动登录都没有成功，只爬了前面10页左右。有时间要学习一下Pyautogui的用法。
Django前端只能修修补补，欠的知识比较多。

## 学到的知识点

  1. xpath中的contains的用法：

    n_star = tag.xpath('.//span[contains(@class,"allstar")]/@title')

  2. 处理数据时，用 item['n_star'] = n_star 更新字典时，发现循环添加的字典都是一样的，后来改成下面这样就好了：
   
    items.append({'title': title, 'n_star': n_star, 'short': short, 'sentiment': sentiment})

  3. lxml.etree 的xpath语法与scrapy中的xpath选择器还是有一些区别的。scrapy里面需要用到get()、getall()，而lxml.etree不用，经常取出数组来，需要多在shell里测试。
   
   scapy shell 测试本地文件的方法：
   先把spider文件中的start_urls等位置的路径改为: file:///C:/xxxx 的形式，然后运行：

    scrapy shell ./maoyan_hot.html

   注意：如果要解析的文件在当前文件夹下，文件名前面一定要有 ./ 否则出不来东西！
