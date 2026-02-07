#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成技能词云图片
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def generate_wordcloud():
    """生成技能词云图片"""

    # 技能词汇及权重（出现频率/重要程度）
    # 基于技术分站内容和简历技能整理
    skills = {
        # 编程语言
        'Golang': 15,
        'Python': 15,
        'JavaScript': 12,
        'HTML': 10,
        'CSS': 10,
        'C语言': 6,
        'VC++': 5,
        'Delphi': 4,
        '单片机': 4,

        # 框架与库
        'Vue': 10,
        'Flutter': 12,
        'Beego': 5,
        'Echo': 5,
        'Flask': 6,
        'ET框架': 5,

        # 数据库
        'MySQL': 12,
        'Redis': 12,
        'MongoDB': 10,
        'Neo4j': 10,
        'SQL Server': 5,

        # 协议与通讯
        'Protobuf': 8,
        'TCP': 8,
        'HTTP': 8,
        'gRPC': 7,

        # 工具与服务
        'Git': 10,
        'Docker': 12,
        'Kubernetes': 10,
        'K8s': 8,
        'Jenkins': 7,
        'Nginx': 10,
        'Consul': 5,

        # AI与搜索
        'iflow': 8,
        'CodeBuddy': 7,
        'Qwen': 7,
        'opencode': 7,
        '豆包': 6,
        'FastGPT': 6,
        'Elasticsearch': 7,
        'TypeSense': 6,
        'PaddleOCR': 7,

        # 其他工具
        'VsCode': 6,
        'Trae': 6,
        'Sublime': 4,
        'Warp': 4,
        'Zed': 4,
        'WireShark': 5,

        # 技术分站相关
        'Docx': 8,
        'Excel': 8,
        'PDF': 8,
        '支付': 8,
        '算法': 8,
        '医学': 6,
        '经济': 6,
        '统计学': 6,
        '产品经理': 6,
        '商业模式': 6,
        '视频处理': 6,

        # 游戏开发
        'Unity3D': 5,
    }

    # 创建词云对象
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        colormap='viridis',
        max_words=100,
        relative_scaling=0.5,
        min_font_size=12,
        font_path='NotoSansSC-700.ttf',  # 使用中文字体
        margin=10,
        random_state=42,
    ).generate_from_frequencies(skills)

    # 保存图片
    wordcloud.to_file('wordcloud.png')
    print("词云图片已生成: wordcloud.png")

    # 优化版本（渐变色）
    wordcloud_color = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        colormap='plasma',
        max_words=100,
        relative_scaling=0.5,
        min_font_size=12,
        font_path='NotoSansSC-700.ttf',
        margin=10,
        random_state=42,
    ).generate_from_frequencies(skills)

    wordcloud_color.to_file('wordcloud_color.png')
    print("彩色词云图片已生成: wordcloud_color.png")


if __name__ == '__main__':
    generate_wordcloud()