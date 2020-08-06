# 背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求
# 定义动物园、动物、猫三个类。
# 这个类可以使用如下形式为动物园增加一只猫：
# if __name__ == '__main__':
#     # 实例化动物园
#     z = Zoo('时间动物园')
#     # 实例化一只猫，属性包括名字、类型、体型、性格
#     cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
#     # 增加一只猫到动物园
#     z.add_animal(cat1)
#     # 动物园是否有猫这种动物
#     have_cat = getattr(z, 'Cat')
# 具体要求：
# 定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
# 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物
# 的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
# 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类
# 继承自动物类。
# 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个
# 动物实例）不能被重复添加的功能。

# 第一版
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animal_list = []

    def add_animal(self, animal):
        self.animal_list.append(animal)

class Animal:
    def __init__(self, food_type, shape, temper):
        self.food_type = food_type
        self.shape = shape
        self.temper = temper

class Cat(Animal):
    def __init__(self, name, food_type, shape, temper):
        super().__init__(food_type, shape, temper)
        self.name = name


def getattr(zoo, animal):
    for animal in zoo.animal_list:
        try:
            return isinstance(animal, Cat)
        except NameError as e:
            pass
    return False

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')