class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.kind = 'big dog'  # 可定义默认属性

    def sit(self):
        print(self.name + " is sitting")


my_dog = Dog('lili', 4)
my_dog.sit()
print(my_dog.kind)
