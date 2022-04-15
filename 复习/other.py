# msg = input("请输入你最喜欢的颜色：")
# print("你最喜欢" + msg)

# age = input("请输入你的年龄：")
# if int(age) >= 18:  # 输入数值型时注意类型转换
#     print("你已成年")
# else:
#     print("你未成年")

while True:
    msg = input("随便输入点什么：")
    if msg != 'quit':
        print("你输入的是：" + msg)
    else:
        break
