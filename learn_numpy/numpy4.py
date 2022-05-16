import numpy as np


t1 = np.loadtxt("./count.csv", delimiter=",", dtype="int")
print(t1)

# 修改值
print('*'*100)
t1[1, 1] = 100
print(t1)
# 条件修改
print('*'*100)
t1[t1 < 50] = 1  # 小于50的全部赋值1
print(t1)
print('*'*100)
t1 = np.where(t1 < 50, 0, 100)  # 三元运算：小于50的全部赋值1，否则赋值100
print(t1)
print('*'*100)
t1 = t1.clip(1, 50)  # 小于1的全部赋值1，大于50的全部赋值50
print(t1)
