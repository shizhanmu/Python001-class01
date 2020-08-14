# 学习笔记

## 本次收获:

1. 最大收获学会了使用抽象类. 如果想不允许父类实例化, 有两个条件:
   - 让父类继承ABC
   - 在父类某个方法上加 @abstractmethod装饰器
2. 获取实例所属类名称的两种方法:

    cat.\_\_class\_\_.\_\_name\_\_
    
    type(cat).\_\_name\_\_

3. 在Python shell中粘贴类定义的时候, 注意不要有空行, 否则会报错.
4. 注意property类属性装饰器的用法, 是否凶猛动物的判断非常适合用类属性
5. 注意字典的get与setdefault方法的区别:
   - setdefault: 当字典的key不存在时, 将会给字典添加一个 key=default 的元素; 
   - get: 当字典的key不存在时, 只会返回default值,而不会给字典添加缺省的元素

```python
>> animals = {}
>>> animal_class = "Cat"
>>> animal = "cat1"  
>>> a = animals.get(animal_class, set())
>>> a
set()
>>> animals
{}
>>> a.add(animal)
>>> a
{'cat1'}
>>> animals
{}
>>> b = animals.setdefault(animal_class, set())
>>> b
set()
>>> b.add(animal)
>>> b
{'cat1'}
>>> animals
{'Cat': {'cat1'}}
```
