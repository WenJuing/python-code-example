# 字典
leimu = {'name': '雷姆', 'age': 16, 'color': 'blue'}
print(leimu)
print(leimu['name'], leimu['age'], leimu['color'])  # 访问键值

leimu['height'] = 162.5  # 添加键值
print(leimu)

del leimu['color']  # 删除键值
print(leimu)

# 遍历字典
for key, value in leimu.items():  # items()返回键值对列表
    print(key, ":", value)

for key in leimu.keys():  # keys()返回所有键
    print(key)

for key in sorted(leimu.keys()):  # 已特定顺序遍历所有键
    print(key)

for value in leimu.values():  # values()返回所有值
    print(value)

leimu['weight'] = 162.5
print(leimu)
print(set(leimu.values()))  # set()剔除重复项

# 在列表中存储字典
user = [{'name': 'aaa', 'age': 18}, {'name': 'bbb', 'age': 21}]
print(user[0]['name'])

# 在字典中存储列表
leimu = {'name': '雷姆', 'hobby': ['singing', 'painting', 'running']}
print(leimu['hobby'][1])
for i in leimu['hobby']:
    print(i)
