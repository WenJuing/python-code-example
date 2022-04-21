import numpy as np
import random

# 构建数组的三种方法
t1 = np.array([1, 2, 'hello'])
print(t1)
t2 = np.array(range(10))
print(t2)
# array()和arange()的结合
t3 = np.arange(1, 10, 2)
print(t3)
print(t3.dtype)  # 输出数据类型

# 定义时设置数据类型
t4 = np.array([1, 0, 1, 1, 0], dtype=bool)
print(t4)
print(t4.dtype)

# 改变数据类型
t5 = t4.astype("int8")
print(t5)
print(t5.dtype)

# 保留2位小数
t6 = np.array([random.random() for i in range(5)])  # random.random()表示0~1之间的小数
print(t6)
t7 = np.round(t6, 2)
print(t7)
