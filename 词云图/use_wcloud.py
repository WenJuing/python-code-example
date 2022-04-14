import jieba    # 分词
from wordcloud import WordCloud  # 制作词云图
import matplotlib.pyplot as plt  # 展示图像
import re   # 使用正则表达式
from PIL import Image   # 使用图片
import numpy as np      # 处理图片


with open("../douBan/douban_top250.txt", "r", encoding="utf8") as o:
    text = o.read()     # 导入文本
    text = re.sub('[/：:\n.|-]', '', text)  # 去除不必要的字符

# 分词
words_list = jieba.lcut(text)
words_str = ' '.join(words_list)
# 添加停词列表（除去不必要的词汇）
stop_words = open("./cn_stopwords.txt", "r", encoding="utf8").read().split("\n")
# 扩展停词列表
stop_words.extend(('No', '国家', '年份', '演员', '片名', '评分', '导演', '类型', '评价', '人数'))

# 导入背景图
background = Image.open('./1344340629730.jpg')
graph = np.array(background)

# 使用WordCloud生成词云
word_cloud = WordCloud(
    font_path='simsun.ttc',  # 设置字体
    max_font_size=80,
    min_font_size=3,
    background_color='white',
    stopwords=stop_words,
    mask=graph,     # 设置背景图
)
word_cloud.generate(words_str)

# 使用matplotlib展现结果
plt.subplots(figsize=(12, 8))
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
