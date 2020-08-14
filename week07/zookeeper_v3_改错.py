# 时间动物园第3版  (根据伟翼的代码修改)
# 注意property类属性装饰器的用法 
# 注意字典的get与setdefault方法的区别
from abc import ABC, abstractmethod


class Zoo:
    """ 动物园类 """
    def __init__(self, name):
        """
        :param name: str, 名字
        """
        self.name = name
        self.animals = {}  # 存放动物, {类名: set()}

    def add_animal(self, animal):
        animal_class = animal.__class__.__name__
        self.animals.setdefault(animal_class, set()).add(animal)

    def __str__(self):
        return f'{self.name}(animals: {self.animal_class_list})'

    def __getattr__(self, item):
        return bool(self.animals.get(item)) or False

class Animal(ABC):
    @abstractmethod
    def __init__(self, food_type, shape, temper):
        """
        :param food_type: str, 食物类型, 如'食肉', '食草', '杂食'
        :param shape: str, 体型, 如'小', '中', '大'
        :param temper: str, 性情, 如'温顺', '凶猛'
        """
        self.food_type = food_type
        self.shape = shape
        self.temper = temper

    @property
    def is_killer(self):
        """
        是否属于凶猛动物
        :return: bool
        """
        shape_list = ["小", "中", "大"]
        if self.food_type == "食肉" and shape_list.index(self.shape) >= 1 and self.temper == "凶猛":
            return True
        return False

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.food_type}, {self.shape}, {self.temper}, 是否可当宠物: {self.is_pet}, 是否凶猛动物: {self.is_killer})'
    

class Cat(Animal):
    voice = "Miaow~"
    
    def __init__(self, name, food_type, shape, temper):
        super().__init__(food_type, shape, temper)
        self.name = name
        self.is_pet = True  # 是否适合做宠物, 除了凶猛的都适合
        if self.is_killer:
            self.is_pet = False
    

if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z)
    # ani = Animal('食肉', '小', '温顺')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(cat1)

    # 添加一只猫到动物园
    z.add_animal(cat1)

    # 再次实例化并增加一只猫到动物园
    cat2 = Cat('小黑猫 1', '食肉', '小', '凶猛')
    print(cat2)
    z.add_animal(cat2)

    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')

