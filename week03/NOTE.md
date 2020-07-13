# 学习笔记

### 作业一的参考文档：
  1. 执行系统命令的工具 subprocess: https://docs.python.org/zh-cn/3/library/subprocess.html
  2. 命令行解析工具 fire: https://zhuanlan.zhihu.com/p/31274256
   
### 作业二
  1. 实在做不出来了，修改了韩昌杰同学的代码： https://github.com/hanchangjie429/Python001-class01/tree/master/week03 ，他的代码比较简洁，从中学到了concurrent.futures.as_completed的用法。
  2. 改进了一下，加入了queue；把原代码参数中的元祖简化成了单个字符串（url）。
  3. 去重的功能采用在用sql语句插入的时候，添加insert ignore，同时在获取到职位信息时，将所有字母变成小写，如Python变为python。
  4. 开始用的selenium自动点击的方式来下载网页，遇到点坑，只实现了部分功能。