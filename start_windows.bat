@echo off
chcp 65001 >nul
echo ========================================
echo 视频下载工具 - Windows 启动脚本
echo ========================================
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo [错误] 未检测到 Python
    echo 请先安装 Python: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [信息] Python 已安装
echo.

REM 启动程序
echo [启动] 正在启动视频下载工具...
echo.
python video_downloader.py

pause
