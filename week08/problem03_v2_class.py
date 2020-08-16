from functools import wraps
import time

class Timer(object):
    """
    计数器，类装饰器
    :param self._n: int, 重复运行次数
    """
    def __init__(self, n=1, *args, **kwargs):
        self._n = n  # 
        super(Timer, self).__init__(*args, **kwargs)
    def __call__(self, func):
        # 类的函数装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__
            total_period = 0
            for i in range(1, self._n + 1):
                start = time.time()
                ret = func(*args, **kwargs)
                stop = time.time()
                period = stop - start
                total_period += period
                print(f"第 {i} 次运行 {func_name} 耗时秒数：{period}")
            print(f"一共运行 {i} 次 {func_name} , 总耗时秒数：{total_period}")
            return ret
        return wrapped_function

# 第一种调用装饰器的方法
@Timer(3)
def myfunc(a, b, c):
    time.sleep(1.1)
    return a**2 + b**2 + c**2
myfunc(1, 3, 5)

# 第二种调用装饰器的方法
MyClass(3)(myfunc)(1, 3, 5)
