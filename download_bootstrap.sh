#!/bin/bash
echo "正在下载Bootstrap CSS..."
curl -L --connect-timeout 10 --max-time 30 -o bootstrap.min.css https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css

if [ -f bootstrap.min.css ] && [ -s bootstrap.min.css ]; then
    echo "✓ Bootstrap CSS 下载成功"
    ls -lh bootstrap.min.css
else
    echo "✗ 下载失败，请手动下载"
    echo "访问: https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
fi

echo ""
echo "正在下载Bootstrap Icons..."
curl -L --connect-timeout 10 --max-time 30 -o bootstrap-icons.css https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css

if [ -f bootstrap-icons.css ] && [ -s bootstrap-icons.css ]; then
    echo "✓ Bootstrap Icons 下载成功"
    ls -lh bootstrap-icons.css
else
    echo "✗ 下载失败"
fi
