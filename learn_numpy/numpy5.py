import numpy as np


t1 = np.arange(8).reshape(2, 4)
t2 = np.arange(8, 16).reshape(2, 4)

print(t1)
print(t2)

# 竖直拼接
print(np.vstack((t1, t2)))
# 水平拼接
print(np.hstack((t1, t2)))

t1[[0, 1], :] = t1[[1, 0], :]  # 一二行交换
print(t1)
t1[:, [0, 1]] = t1[:, [1, 0]]  # 一二列交换
print(t1)

t3 = np.zeros((3, 4))  # 创建三行四列全为0的数组
t4 = np.ones((3, 4))  # 创建三行四列全为1的数组
print(t3)
print(t4)

t5 = np.eye(3)  # 创建一个单位矩阵
print(t5)

t6 = np.random.rand(2, 3)  # 创建一个两行三列的值在0~1随机生成的小数的数组
print(t6)

np.random.seed(10)  # 添加随机种子后，根据种子值产生固定的数字
t7 = np.random.randint(10, 20, (2, 4))  # 创建一个两行四列的值在10~20随机生成的整数的数组
print(t7)

t8 = np.arange(12).reshape(3, 4).astype(float)
t8[2, 3] = np.nan  # nan为浮点类型
t8[0, 1] = np.nan
print(t8)
print(np.count_nonzero(t8 != t8))  # 统计nan个数
print(np.count_nonzero(np.isnan(t8)))  # 统计nan个数

t9 = np.arange(12).reshape(3, 4)
print(t9)
print(np.sum(t9))  # 计算数组和
print(np.sum(t9, axis=0))  # 计算每一列的和
print(np.sum(t9, axis=1))  # 计算每一行的和
print(np.mean(t9))  # 均值
print(np.median(t9))  # 中值
print(np.max(t9))  # 最大值
print(np.min(t9))  # 最小值
print(np.ptp(t9))  # 级值
print(np.std(t9))  # 标准差
