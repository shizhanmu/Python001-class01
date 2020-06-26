# 学习笔记
### 作业1难点：
1. header里必须添加cookie信息。卡了大半天，从发现班里有高手，以后要多问才行。
2. 对bs4中的标签利用 [索引号] 提取相同标签中的内容

### 作业2难点：
1. 在settings中设置headers才能使用　scrapy shell （COOKIES_ENABLED = False， DEFAULT_REQUEST_HEADERS）
2. start_requests定义需要抓取的起始页面，不能放入解析的语句，因为没有传入response。解析的语句需要放在parse里面
3. 理解yield一行中的callback，循环调用parse方法解析网页内容, 可多层调用parse
4. 不明白的时候，要先看官方文档