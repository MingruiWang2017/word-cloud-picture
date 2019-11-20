# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2019/11/19 19:36
@ desc: 创建云词
"""

import re
import collections
import numpy as np
import jieba
import wordcloud
from PIL import Image
import matplotlib.pyplot as plt

# 读取文件
artical = None
with open('artical.txt', 'r', encoding='utf-8') as f:
    artical = f.read()

# 文本预处理
pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
artical = re.sub(pattern, '', artical)  # 将符合上面正则的字符去除

# 分词
seg_list_exact = jieba.cut(artical, cut_all=False)  # 精确分词模式
object_list = []
remove_words = ['你', '我', '他', '她', '的', '，', '和', '是', '随着', '对于', '对', '等', '能', '都', '。', ' ', '、', '中', '在', '了',
                '通常', '如果', '我们', '需要', '月', '日', '以', '又', '不', '说', '里', '也', '什么', '有', '这', '那', '但是',
                '想']  # 自定义去除词库

for word in seg_list_exact:
    if word not in remove_words:
        object_list.append(word)

# 统计词频
word_counts = collections.Counter(object_list)  # 对分词统计词频
word_counts_top10 = word_counts.most_common(10)  # 获取前10的高频词

# 词频展示
mask = np.array(Image.open('wordcloud.jpg'))
wc = wordcloud.WordCloud(
    background_color='white',
    font_path='C:/Windows/Fonts/simhei.ttf',
    mask=mask,
    max_words=200,
    max_font_size=100
)

wc.generate_from_frequencies(word_counts)
# image_colors = wordcloud.ImageColorGenerator(mask)
# wc.recolor(color_func=image_colors)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()
wc.to_file('out_fig.jpg')
