#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import qrcode
import os

# 网站列表
websites = [
    ("Python", "https://python.yijunjun.icu"),
    ("Golang", "https://golang.yijunjun.icu"),
    ("Flutter", "https://flutter.yijunjun.icu"),
    ("JavaScript", "https://javascript.yijunjun.icu"),
    ("Docker", "https://docker.yijunjun.icu"),
    ("Git", "https://git.yijunjun.icu"),
    ("Redis", "https://redis.yijunjun.icu"),
    ("技术文档", "https://doc.yijunjun.icu"),
    ("Excel", "https://excel.yijunjun.icu"),
    ("PDF", "https://pdf.yijunjun.icu"),
    ("Neo4j", "https://neo4j.yijunjun.icu"),
    ("Nginx", "https://nginx.yijunjun.icu"),
    ("MySQL", "https://mysql.yijunjun.icu"),
    ("Kubernetes", "https://k8s.yijunjun.icu"),
    ("支付", "https://pay.yijunjun.icu"),
    ("医学", "https://doctor.yijunjun.icu"),
    ("经济", "https://money.yijunjun.icu"),
]

# 生成二维码
for name, url in websites:
    # 创建QR码实例
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 添加数据
    qr.add_data(url)
    qr.make(fit=True)

    # 创建图像
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存文件
    filename = f"qr_{name}.png"
    img.save(filename)
    print(f"已生成: {filename} - {url}")

print("\n所有二维码生成完成！")