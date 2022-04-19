# 函数
def hello(name):
    print("hello!" + name.title())


def pat(kind, name='null'):  # 可给后面的形参加上默认值
    print("my", kind, "is", name)


def username(first, last, middle=''):  # 参数可选
    print("your name is " + first, middle, last)


def greet(names):  # 传递列表
    for name in names:
        print("hello, " + name)

    names.append('fff')


def show_names(*names):  # 接受任意个数的参数，以元组形式保存
    print(names)


def create_user(name, **other):  # 接受任意个数的键值参数，以字典形式保存
    user = {}
    user['name'] = name
    for key, value in other.items():
        user[key] = value
    return user


hello('leimu')
pat('dog', 'lusi')  # 位置实参
pat(name='mmm', kind='cat')  # 关键字实参
pat('tiger')
username('lee', 'oo', 'mid')
username('lee', 'oo')
users = ['aaa', 'bbb', 'ccc']
print(users)
# greet(users)  # 可改动列表
greet(users[:])  # 传副本，无法改动列表
print(users)

show_names('jam')
show_names('jam', 'koo', 'yxx')

data = {'age': 16, 'color': 'blue'}
user = create_user('leimu', **data)
# user = create_user('leimu', age=16, color='blue')
print(user)
