# 绘制横向条形图
# 展示电影前10名的票房
from matplotlib import pyplot as plt


y = [
    '长津湖', '战狼2', '你好，李焕英', '哪吒之魔童降世', '流浪地球', '唐人街探案3', '复仇者联盟4：终局之战',
    '长津湖之水门桥', '红海行动', '唐人街探案2']
x = [57.75, 56.95, 54.14, 50.36, 46.88, 45.24, 42.5, 40.57, 36.51, 33.98]

plt.figure(figsize=(15, 8), dpi=80)
plt.barh(y, x, height=0.3)

plt.ylabel("电影名")
plt.xlabel("票房 单位（亿）")
plt.title("中国累计票房前10名的电影票房情况")
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.show()
