# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，
# 注意需要考虑函数可能会接收不定长参数。
import time
from functools import wraps
def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        period = stop - start
        print(f'函数 {func.__name__} 的运行时间为：{period}秒')
        return ret
    return inner

@timer
def foo(a, b, c):
    time.sleep(2)
    return (a + b + c)

print(foo(1, 3, 5))
