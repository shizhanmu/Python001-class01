# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

def mymap(func, seq):
    for s in seq:
        yield func(s)

if __name__ == '__main__':
    lst = [1,4,5]
    g = map(lambda x: x**2, lst)
    list(g)
