# 时间动物园第二版
from abc import ABC, abstractmethod


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animal_list = []
        self.animal_class_list = []

    def add_animal(self, animal):
        animal_class = animal.__class__.__name__
        if animal_class not in self.animal_class_list:
            self.animal_list.append(animal)
            self.animal_class_list.append(animal_class)
            print(f"{animal.name} 来到了 {self.name}.")
            print(self.__str__())
        else:
            print(f"本动物园已经有{animal_class}了, 拒绝接收.")

    def __str__(self):
        return f'{self.name}(animals: {self.animal_class_list})'


class Animal(ABC):
    def __init__(self, food_type, shape, temper):
        self.food_type = food_type
        self.shape = shape
        self.temper = temper
        self.is_killer = False

    @classmethod
    def judge_killer(cls):
        shape_list = ["小", "中", "大"]
        def shape_mid_up(shape):
            if shape.index >= 1 and cls.food_type == "食肉" \
                        and cls.temper == "凶猛":
                cls.is_killer = True
            else:
                cls.is_killer = False
        if cls.shape in shape_list:
            return shape_mid_up(cls.shape)

    def __str__(self):
        return f'{self.__class__.__name__}({self.name}, {self.food_type}, {self.shape}, {self.temper}, 是否可当宠物: {self.pet_fit}, 是否凶猛动物: {self.is_killer})'
    
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    pet_fit = True
    voice = "Miaow~"
    
    def __init__(self, name, food_type, shape, temper):
        super().__init__(food_type, shape, temper)
        self.name = name
    
    @classmethod
    def make_sound(cls):
        print(cls.voice)


def getattr(zoo, animal_type):
    if animal_type in zoo.animal_class_list:
        print(f"本动物园已经有{animal_type}这种动物了.")
        return True
    print(f"本动物园还没有{animal_type}这种动物.")
    return False


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z)
    ani = Animal('食肉', '小', '温顺')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    print(cat1)
    cat1.make_sound()

    # 添加一只猫到动物园
    z.add_animal(cat2)

    # 再次实例化并增加一只猫到动物园
    cat2 = Cat('小黑猫 1', '食肉', '小', '凶猛')
    print(cat2)
    z.add_animal(cat2)

    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')

