# 列表

# 访问和增删改查
color = ['red', 'yellow', 'green', 'pink']
print(color)
print(color[0])  # 访问第一个
print(color[-1])  # 访问最后一个
print(color[-2])  # 访问倒数第二各

color[1] = 'orange'  # 修改第二个元素
print(color)

user = []
user.append('ouo')  # 添加元素
user.append('iVi')
print(user)

user.insert(1, 'new')  # 在第2个位置插入元素
print(user)

del user[0]  # 删除元素
print(user)

last = user.pop()  # 删除最后一个元素，返回值为删除的元素
print(last)
print(user)

user = ['aaa', 'bbb', 'ccc']
print(user)
print(user.pop(1))  # pop()可删除任意位置的元素
print(user)
user.remove('ccc')  # 可根据值删除元素
print(user)

# 排序
car = ['bbb', 'ddd', 'aaa', 'ccc']
print(car)
car.sort()  # 按字母顺序排序
print(car)
car.sort(reverse=True)
print(car)  # 按字母倒序排序
print('\n')
car = ['bbb', 'ddd', 'aaa', 'ccc']
print(car)
print(sorted(car))  # 临时排序
print(car)

user = ['aa', 'bb', 'cc']
print(user)
user.reverse()  # 反转元素顺序
print(user)

print(len(user))  # 获取列表长度

# 遍历

books = ['java', 'python', 'c++']
for book in books:  # 遍历并打印元素
    print(book)

# 使用数值列表

for i in range(1, 6):
    print(i)

# 创建数值列表
nums = list(range(1, 11, 2))
print(nums)

nums = []
for i in range(1, 6):
    nums.append(i**2)
print(nums)

nums = list(range(1, 6))
print(max(nums))  # 最大值
print(min(nums))  # 最小值
print(sum(nums))  # 求和

# 列表解析
nums = [i**2 for i in range(1, 6)]  # 生成格式：[存储元素 循环代码]
print(nums)

# 切片
user = ['aa', 'bb', 'cc', 'dd', 'ee']
print(user)
print(user[0:3])  # 截取前三个
print(user[:2])   # 截取到第二个
print(user[2:])   # 从第3个开始截取
print(user[-3:])  # 截取最后三个

for i in user[:3]:  # 遍历切片
    print(i)

# 复制列表

my_food = ['beef', 'noddle', 'rice']
you_food = my_food[:]  # 通过切片复制列表
my_food.append('jam')
you_food.append('air')
print(my_food)
print(you_food)

my_food = ['beef', 'noddle', 'rice']
you_food = my_food  # 错误的复制方式，两个变量实际指向同一个列表
my_food.append('jam')
you_food.append('air')
print(my_food)
print(you_food)
