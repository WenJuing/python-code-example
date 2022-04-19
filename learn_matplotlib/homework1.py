# 绘制10点到12点每一分钟的气温
from matplotlib import pyplot as plt
import random


y = [random.randint(20, 35) for i in range(120)]
x = range(0, 120)

plt.figure(figsize=(15, 8), dpi=80)
plt.plot(x, y)

# 在x轴加字符串
_x = list(x)
_x_laber = ["10点{}分".format(i) for i in range(60)]
_x_laber += ["11点{}分".format(i) for i in range(60)]
# 去步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::3], _x_laber[::3], rotation=45)  # 旋转45度
plt.yticks(range(min(y), max(y)+5, 1))

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位（℃）")
plt.title("10点到12点每分钟的气温变化情况")

# 添加这行代码后可以显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.show()
