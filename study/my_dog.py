# 从一个模块导入多个类
from dog import Dog, SmartDog


my_god = Dog('pitty', 3)
my_god.describe_dog()
my_smart_dog = SmartDog('greed', 14, 'very smart')
my_smart_dog.describe_dog()
