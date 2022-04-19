from matplotlib import pyplot as plt


x = range(30, 180, 30)
y = [33, 50, 110.5, 80, 140]

plt.figure(figsize=(10, 5), dpi=80)  # 设置图片大小，像素（可选）

plt.plot(x, y)  # 绘图

# 设置x轴刻度（可选）
plt.xticks(x)
# 设置y轴刻度（可选）
plt.yticks(range(min(y), max(y)+1, 10))

# 绘制完后保存（可选）
plt.savefig("./1.png")

plt.show()  # 展示图形
