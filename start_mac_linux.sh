#!/bin/bash

echo "========================================"
echo "视频下载工具 - Mac/Linux 启动脚本"
echo "========================================"
echo ""

# 检查 Python3 是否安装
if ! command -v python3 &> /dev/null; then
    echo "[错误] 未检测到 Python3"
    echo "请先安装 Python3:"
    echo "  Mac: brew install python3"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    exit 1
fi

echo "[信息] Python3 已安装: $(python3 --version)"
echo ""

# 确保脚本有执行权限
chmod +x video_downloader.py

echo "[启动] 正在启动视频下载工具..."
echo ""

# 运行主脚本
python3 video_downloader.py
