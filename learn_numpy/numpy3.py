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
