#!/bin/bash
#
# Video Downloader - Mac/Linux Launcher
# Author: Davey Wong <wgwcko@gmail.com> (https://www.guangweiblog.com)
#
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

echo "========================================"
echo "视频下载工具 - Mac/Linux 启动脚本"
echo "========================================"
echo ""

# Check Python3
if ! command -v python3 &>/dev/null; then
    echo "[错误] 未检测到 Python3"
    echo "请先安装 Python3:"
    echo "  Mac: brew install python3"
    echo "  Ubuntu/Debian: sudo apt install python3 python3-pip"
    exit 1
fi

echo "[信息] Python3: $(python3 --version)"
echo ""

# Install yt-dlp if missing
if ! python3 -c "import yt_dlp" 2>/dev/null; then
    echo "[安装] 正在安装 yt-dlp..."
    pip3 install -U yt-dlp
fi

echo "[启动] 正在启动视频下载工具..."
echo ""
python3 video_downloader.py
