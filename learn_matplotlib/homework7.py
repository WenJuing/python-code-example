# 绘制直方图
# 组数计算公式：(maxnum-minnum) / 组距
from matplotlib import pyplot as plt
import random


data = [random.randint(0, 100) for i in range(50)]
# 组距：视情况而定
d = 5
# 计算组数
num_bin = (max(data)-min(data)) // d

plt.figure(figsize=(15, 8), dpi=80)
plt.hist(data, num_bin)

# 调整x轴刻度
plt.xticks(range(min(data), max(data)+d, d))
plt.grid()

plt.show()
