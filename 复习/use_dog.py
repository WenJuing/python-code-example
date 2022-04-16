from Dog import Dog, ElecDog  # 从模块中导入类


my_dog = Dog('lili', 4)
my_dog.sit()
my_elecdog = ElecDog('cycber', 1)
my_elecdog.sit()  # 子类既可以使用父类的属性和方法，可可以使用自己的属性和方法
my_elecdog.show_battery()
