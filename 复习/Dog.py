class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kind = 'big dog'  # 可定义默认属性

    def sit(self):
        print(self.name + " is sitting")


class Battery():
    def __init__(self, size):
        self.size = size


class ElecDog(Dog):
    '''电子狗'''
    def __init__(self, name, age):
        super().__init__(name, age)  # 给父类所有属性赋值，注意没有self
        self.battery = Battery(1000)  # 给子类添加属性，且是将实例用作属性

    def show_battery(self):  # 给子类添加方法
        print("电池容量：" + str(self.battery.size) + "A")

    def sit(self):  # 重写父类的方法
        print(self.name + " is sitting, " + "and it's a electronic dog.")
