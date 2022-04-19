# 绘制你和同学从11岁到30岁每年旅游的数量
# 你的每年旅游数量：[1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
# 同学的每年旅游数量：[1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
from matplotlib import pyplot as plt


plt.figure(figsize=(15, 8), dpi=80)

x = ["{}岁".format(i) for i in range(11, 31)]
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# lable图例  color颜色  linestyle线条类型  linewidth线条粗细
plt.plot(x, y_1, label="自己", color='red', linestyle=':')
plt.plot(x, y_2, label="同学", color='green', linestyle='-.')  # 绘制第二条线

plt.xticks(x)
plt.yticks(range(0, 8))
plt.xlabel("年龄")
plt.ylabel("旅游次数")
plt.title("11岁到30岁每年旅游的数量情况")
# 绘制网格
plt.grid(alpha=0.5)  # 参数为透明的
# 添加图例
plt.legend(loc="upper left")  # 参数为图例位置

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
