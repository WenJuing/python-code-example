# 元组
cube = (100, 100, 100)
print(cube[1])
for i in cube:
    print(i)

# 虽然无法修改元组的元素，但可以给元组重新赋值
cube = (10, 10, 10)
for i in cube:
    print(i)

# 判断
age = 3
if age > 5 and age <= 10:
    print("you are young student.")
elif age <= 5:
    print("you are young.")
else:  # else有时可不写
    print("you are old")

color = ['red', 'green', 'blue']
if 'red' in color:
    print("red is exist.")
else:
    print("red is not exist")
if 'blue' not in color:
    print("blue is not exist.")
else:
    print("blue is exist")

color = []
if color:   # 此时color为空，为false
    print("color表不为空")
else:
    print("color表为空")
print(color)
