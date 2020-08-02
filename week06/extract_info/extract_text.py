import lxml.etree
import conn
import glob
from snownlp import SnowNLP


def get_sentiment(text):
    '''获取情感倾向数值'''
    s = SnowNLP(text)
    s = s.han  # 繁体转简体
    s = SnowNLP(s)
    sentiment = s.sentiments
    return sentiment

def read_html(file):
    '''读取 html 文件，返回全部文本'''
    print(file)
    with open(file, 'rt', encoding='utf-8') as f:
        html = f.read()
    return html

def file_list(folder):
    '''获取文件夹下所有文件地址'''
    files = glob.glob(f'{folder}/*.html', recursive=True)
    return files

def parse_short(html):
    '''解析 html 文本内容，返回由字典组成的列表
       注意 items.append 有坑，当item指向同一字典时会生成相同的记录
    '''
    sel = lxml.etree.HTML(html)
    star_dict = {'力荐': 5, '推荐': 4, '还行': 3, '较差': 2, '很差': 1}
    items = []
    title = sel.xpath('//div[@id="content"]/h1/text()')[0].split(" ")[0]
    tags = sel.xpath('//div[@class="comment"]')
    for tag in tags:
        try:
            n_star = tag.xpath('.//span[contains(@class,"allstar")]/@title')[0]
            n_star = star_dict[n_star]
            short = tag.xpath('./p/span[@class="short"]/text()')[0].strip()
            sentiment = get_sentiment(short)
            items.append({'title': title, 'n_star': n_star, 'short': short, 'sentiment': sentiment})
        except Exception as e:
            print(e)
    return items

def gen_sqls(items):
    '''生成插入记录的 sql 语句
       注意插入sentiment这个数值类型时，{}两边的引号要去掉
    '''
    sqls = []
    for item in items:
        title = item['title']
        n_star = item['n_star']
        short = item['short']
        sentiment = item['sentiment']
        sql = f"insert into t1 (title, n_star, short, sentiment) values('{title}', '{n_star}', '{short}', {sentiment})"
        sqls.append(sql)
    return sqls

def save_to_database(sqls):
    try:
        db = conn.ConnDB()
        db.execute(sqls)
        print('Saved one page.')
    except Exception as e:
        print(e)
    finally:
        db.close()

def main():
    folder = 'short_html'  # 存放 html 的文件夹
    files = file_list(folder)
    for file in files:
        html = read_html(file)
        items = parse_short(html)
        sqls = gen_sqls(items)
        save_to_database(sqls)

if __name__ == '__main__':
    main()

