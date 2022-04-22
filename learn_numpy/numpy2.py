import numpy as np


# 数组的形状：几行几列，使用shape查看
t1 = np.arange(12)
print(t1.shape)  # 当一维时，（数组长度）
print(t1)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2.shape)  # 当二维时，（行，列）
print(t2)

t = np.arange(12).reshape(2, 2, 3)
print(t.shape)  # 当三维时，（块（层），行，列）
print(t)

# 改变数组的形状
t3 = np.arange(12).reshape((3, 4))  # 将一维数组转变成3行4列的二维数组
print(t3.shape)
print(t3)

# 二维转变成一维
t4 = t2.reshape(6)
print(t4)

t5 = t2.flatten()  # 直接转一维
print(t5)

# 数组的计算
# 数组和数字的计算
print('*'*100)
t6 = np.arange(24).reshape(4, 6)  # reshape()参数可省略括号
print(t6)
print(t6+2)  # 二维时，可以当作矩阵进行运算
print(t6*2)
print(t6/0)  # 警告但可以运行，nan代表not a number，inf代表无穷大

# 数组和数组的计算（相同形状）
t7 = np.arange(100, 124).reshape(4, 6)
print(t7+t6)  # 对应位置进行一一计算
print(t7-t6)
print(t7*t6)  # 注意不是矩阵乘法

# 数组和数组的计算（不同形状）
t8 = np.arange(6)
print(t8)
print(t7)
print(t7+t8)  # 广播机制，t8与t7的每行进行计算
print(t7*t8)  # 某一维相同才能计算，都不同则无法计算
