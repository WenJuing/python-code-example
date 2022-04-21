# 绘制多个条形图
# 对比四部电影其中三日票房的售卖情况
from matplotlib import pyplot as plt


x = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
y_1 = [15823, 321, 4492, 312]  # 第一天
y_2 = [12344, 124, 2021, 162]  # 第二天
y_3 = [2114, 388, 2361, 362]  # 第三天
w = 0.2  # 宽度
x_1 = [0.2+i*4*w for i in range(4)]  # 第一天刻度
x_2 = [0.4+i*4*w for i in range(4)]  # 第二天刻度
x_3 = [0.6+i*4*w for i in range(4)]  # 第三天刻度

plt.figure(figsize=(15, 8), dpi=80)

plt.bar(x_1, y_1, width=w, label="第一天")
plt.bar(x_2, y_2, width=w, label="第二天")
plt.bar(x_3, y_3, width=w, label="第三天")
# 调整x轴刻度
plt.xticks(x_2, x)

plt.legend()
plt.xlabel("电影名")
plt.ylabel("票房 单位（万）")
plt.title("四部电影其中三日票房的售卖情况")

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
