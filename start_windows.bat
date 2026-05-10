@echo off
chcp 65001 >nul
REM Video Downloader - Windows Launcher
REM Author: Davey Wong <wgwcko@gmail.com> (https://www.guangweiblog.com)

cd /d "%~dp0"

echo ========================================
echo 视频下载工具 - Windows 启动脚本
echo ========================================
echo.

REM Check Python
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

echo [启动] 正在启动视频下载工具...
echo.
python video_downloader.py

pause
