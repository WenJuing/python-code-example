import pandas as pd


# Series创建
t1 = pd.Series([1, 2, 3])  # 传列表，下标默认从0开始
print(t1)
t2 = pd.Series([1, 2, 3, 4, 5], index=list("abcde"))  # 可加上指定下标
print(t2)
user = {"name": "oner", "age": 17, "tel": 18822224444}
t3 = pd.Series(user)  # 也可传字典
print(t3)
# 取值（支持灵活取值）
print(t3['name'])
print(t3[0])
print(t3[['name', 'age']])
print(t3[[0, 2]])
print(t2[t2 > 3])  # 支持布尔索引
# 取索引（取值则是t3.values）
print(list(t3.index))  # 转成列表输出
for i in t3.index:  # 也可遍历
    print(i)
print(len(t3.index))  # 获取索引长度
