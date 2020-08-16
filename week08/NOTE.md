# 学习笔记
1. 比较下return 与 yield的区别：

  -return：在程序函数中返回某个值，返回之后函数不再继续执行，彻底结束。
  -yield: 带有yield的函数就变成了生成器，函数执行到yield时返回一个值，指针暂时停留在该位置，再次调用该函数时，会从指针停留的位置继续执行，直到结束。一般生成器里会包含一个循环，以便每次调用时都先执行一段程序, 然后返回一个值。

2. yield表达式
   一个生成器刚生成后, 必须先要执行一次 next()才能通过执行send(2)把参数值传递进去, 否则会报错:
    TypeError: can't send non-None value to a just-started generator
   ```python
    def jumping_range(up_to):
        index = 0
        while index < up_to:
            jump = yield index
            print(f'jump is {jump}')
            if jump is None:
                jump = 1
            index += jump
            print(f'index is {index}')

    if __name__ == '__main__':
        iterator = jumping_range(10)
        print(next(iterator))
        print(iterator.send(2))
        print(next(iterator))
        print(iterator.send(-1))
        for x in iterator:
            print(x)
   ```

    测试代码:

   ```python
    >>> iterator = jumping_range(10)
    >>> print(iterator.send(2))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: can't send non-None value to a just-started generator
    >>> print(next(iterator))
    0
    >>> print(iterator.send(2))
    jump is 2
    index is 2
    2
   ```
3. 迭代器和生成器的区别
   迭代器可以遍历很多次, 而生成器只能遍历一次，迭代完成时再调用next()方法会返回
   StopIteration异常。
   正因为如此, 生成器更节省内存, 因为它生成一个值, 然后返回一个值, 不必记住所有的值；
   