# 文件
import json


with open('book.txt', encoding='utf-8') as f:
    content = f.read()  # 全部读取
    print(content)

with open('book.txt', encoding='utf-8') as f:
    for line in f:  # 逐行读取
        print(line.rstrip())  # rstrip()消除每句后面的换行符

with open('book.txt', encoding='utf-8') as f:
    lines = f.readlines()  # 将各行存在列表中
print(lines)

with open('book2.txt', 'w', encoding='utf-8') as f:
    f.write("人生苦短，我学Python")  # 写入文件


def count(filename):
    '''计算文本单词个数'''
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(filename + "不存在！")
    else:
        words = content.split()
        print("一共有" + str(len(words)) + "个单词")


# filename = input("请输入文件名（带后缀）：")
# count(filename)

# 存储数据
data = ['aaa', 'bbb', 'ccc']
with open("data.json", 'w') as f:
    json.dump(data, f)  # 存储数据，使用write()存储会报错

with open("data.json") as f:
    d = json.load(f)  # 读取数据
print(d)
