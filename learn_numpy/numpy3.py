import numpy as np


# 读取文件
t1 = np.loadtxt("./count.csv", delimiter=",", dtype="int")
print(t1)

# unpack属性用于转置
t2 = np.loadtxt("./count.csv", delimiter=",", dtype="int", unpack=True)
print(t2)

# 转置的其他方法
t3 = np.arange(12).reshape(3, 4)
print(t3)
print(t3.transpose())
print(t3.T)
print(t3.swapaxes(1, 0))  # 交换轴下标

print('*'*100)
print(t1)
# 取行
print('*'*100)
print(t1[1])  # 提取第二行
print('*'*100)
print(t1[1:])  # 提取第一行后的所有行
print('*'*100)
print(t1[[0, 2]])  # 提取第一行和第三行
# 取列  t1[行,列]
print('*'*100)
print(t1[:, 0])  # 提取第一列
print('*'*100)
print(t1[:, 1:])  # 提取第一列后面的所有列
# 取多行多列
print('*'*100)
print(t1[1, 1])  # 提取第二行第二列
print('*'*100)
print(t1[1:3, 1:3])  # 提取第二行到第三行，第二列到第三列区域
# 取多个不相邻的点
print('*'*100)
print(t1[[0, 1, 2], [0, 1, 2]])  # 提取主对角线的点
print(t1[[2, 1, 0], [0, 1, 2]])  # 提取副对角线的点
