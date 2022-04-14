# 向函数传递信息

def greet(username):
    '''显示简单的问候语'''
    print('Hello,' + username.title() + '!')


greet('ai lun')
greet('hai ering')

# 实参与形参


def describe_pet(pet_type, pet_name):   # 括号里的是形参
    print('\nI have a', pet_type)
    print('His name is', pet_name.title())


describe_pet('dog', 'wanwan')   # 括号里的是实参
describe_pet('cat', 'maomao')

# 关键字实参

describe_pet(pet_type='chick', pet_name='jiji')

# 默认值


def describe_pet(pet_name, pet_type='dog'):   # 默认值放后面
    print('\nI have a', pet_type)
    print('His name is', pet_name.title())


describe_pet('wangwang')
describe_pet('miaomiao', 'cat')

# 返回值


def get_formatted_name_1(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


print(get_formatted_name_1('wang', 'dalong'))

# 让实参可选


def get_formatted_name_2(first_name, last_name, middle_name=''):
    full_name = first_name.title() + ' ' + middle_name + ' ' + last_name.title()
    return full_name


print(get_formatted_name_2('wang', 'dalong'))
print(get_formatted_name_2('britsh', 'yeleen', '·'))

# 返回字典


def bulid_person(name, age, height=''):
    person = {'name': name, 'age': age}
    if height:
        person['height'] = height
    return person


person = bulid_person('leimu', 16)
print(person)
person = bulid_person('lamu', 16, 160)
print(person)

# 结合使用函数和while循环
'''
while True:
    print("input 'q' in any time to exit")
    print("please tell me your name")
    f_name = input("first name:")
    l_name = input("last name:")
    if f_name == 'q' or l_name == 'q':
        break
    full_name = get_formatted_name(f_name, l_name)
    print("Hello," + full_name + "!")
'''
# 传递列表


def greet_users(names):
    '''向列表中的每个名字发出问候'''
    for name in names:
        mes = 'Hello, ' + name.title() + '!'
        print(mes)


name_list = ['peek', 'duck', 'doog']
greet_users(name_list)

# 在函数中修改列表


def print_models(unprint_design, completed_model):
    while unprint_design:
        current_model = unprint_design.pop()
        print("Printing:" + current_model)
        completed_model.append(current_model)


def show_models(completed_model):
    print("Completed models are following")
    for model in completed_model:
        print(model)


unprint_design = ['shabinaike', 'china lining', 'china anta']
completed_model = []
print_models(unprint_design, completed_model)
show_models(completed_model)

# 传递任意数量的实参


def make_pizza(size, *material):    # 提示：*代表生成一个空元组
    '''打印这个披萨的所有原料'''
    print("\nMaking a " + size + " pizza with the following material:")
    for m in material:
        print("-", m)


make_pizza('big', 'meet')
make_pizza('small', 'meet', 'vegetable', 'tomato jam')

# 传递任意数量的关键字实参


def bulid_profile(first, last, **user_info):    # 提示：**代表生成一个空字典
    user = {}
    user['first'] = first
    user['last'] = last
    for k, v in user_info.items():
        user[k] = v
    return user


people = bulid_profile('albert', 'einstein',
                       location='princeton', field='physics')
print(people)
