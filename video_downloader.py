#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台视频下载工具
支持 Mac、Linux、Windows 系统
用于教学研究目的
"""

import os
import sys
import subprocess
import platform


def check_yt_dlp():
    """检查 yt-dlp 是否已安装"""
    try:
        subprocess.run(['yt-dlp', '--version'], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def install_yt_dlp():
    """安装 yt-dlp"""
    print("正在安装 yt-dlp...")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 
                      'install', '-U', 'yt-dlp'], check=True)
        print("✓ yt-dlp 安装成功！")
        return True
    except subprocess.CalledProcessError:
        print("✗ 安装失败，请手动安装：")
        print("  pip install -U yt-dlp")
        print("  或访问：https://github.com/yt-dlp/yt-dlp")
        return False


def show_menu():
    """显示菜单"""
    print("\n" + "="*50)
    print("视频下载工具 - 用于教学研究")
    print("="*50)
    print("1. 下载视频（最高画质）")
    print("2. 下载视频（指定画质）")
    print("3. 仅下载音频")
    print("4. 下载视频+字幕")
    print("5. 批量下载（从文件读取链接）")
    print("6. 查看视频信息（不下载）")
    print("0. 退出")
    print("="*50)


def download_best_quality(url, output_dir="downloads"):
    """下载最高画质视频"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo+bestaudio/best',
        '--merge-output-format', 'mp4',
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✓ 下载完成！")
    except subprocess.CalledProcessError:
        print("\n✗ 下载失败")


def download_custom_quality(url, output_dir="downloads"):
    """下载指定画质"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    print("\n画质选项：")
    print("1. 1080p")
    print("2. 720p")
    print("3. 480p")
    print("4. 360p")
    
    choice = input("\n选择画质 (1-4): ").strip()
    
    quality_map = {
        '1': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '2': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '3': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        '4': 'bestvideo[height<=360]+bestaudio/best[height<=360]'
    }
    
    quality = quality_map.get(choice, quality_map['2'])
    
    cmd = [
        'yt-dlp',
        '-f', quality,
        '--merge-output-format', 'mp4',
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✓ 下载完成！")
    except subprocess.CalledProcessError:
        print("\n✗ 下载失败")


def download_audio(url, output_dir="downloads"):
    """仅下载音频"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cmd = [
        'yt-dlp',
        '-f', 'bestaudio',
        '--extract-audio',
        '--audio-format', 'mp3',
        '--audio-quality', '0',
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✓ 音频下载完成！")
    except subprocess.CalledProcessError:
        print("\n✗ 下载失败")


def download_with_subtitles(url, output_dir="downloads"):
    """下载视频和字幕"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo+bestaudio/best',
        '--merge-output-format', 'mp4',
        '--write-sub',
        '--write-auto-sub',
        '--sub-lang', 'zh-Hans,zh-Hant,en',
        '--convert-subs', 'srt',
        '-o', f'{output_dir}/%(title)s.%(ext)s',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✓ 下载完成（含字幕）！")
    except subprocess.CalledProcessError:
        print("\n✗ 下载失败")


def batch_download(file_path, output_dir="downloads"):
    """批量下载"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if not os.path.exists(file_path):
        print(f"\n✗ 文件不存在: {file_path}")
        return
    
    cmd = [
        'yt-dlp',
        '-f', 'bestvideo+bestaudio/best',
        '--merge-output-format', 'mp4',
        '-a', file_path,
        '-o', f'{output_dir}/%(title)s.%(ext)s'
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✓ 批量下载完成！")
    except subprocess.CalledProcessError:
        print("\n✗ 下载失败")


def show_video_info(url):
    """显示视频信息"""
    cmd = [
        'yt-dlp',
        '--print', '%(title)s\n%(duration_string)s\n%(resolution)s',
        '--no-download',
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print("\n✗ 获取信息失败")


def main():
    """主函数"""
    # 检查 yt-dlp 是否已安装
    if not check_yt_dlp():
        print("未检测到 yt-dlp")
        install = input("是否现在安装？(y/n): ").strip().lower()
        if install == 'y':
            if not install_yt_dlp():
                return
        else:
            print("请先安装 yt-dlp")
            return
    
    while True:
        show_menu()
        choice = input("\n请选择功能 (0-6): ").strip()
        
        if choice == '0':
            print("\n再见！")
            break
        
        elif choice == '1':
            url = input("\n请输入视频链接: ").strip()
            if url:
                download_best_quality(url)
        
        elif choice == '2':
            url = input("\n请输入视频链接: ").strip()
            if url:
                download_custom_quality(url)
        
        elif choice == '3':
            url = input("\n请输入视频链接: ").strip()
            if url:
                download_audio(url)
        
        elif choice == '4':
            url = input("\n请输入视频链接: ").strip()
            if url:
                download_with_subtitles(url)
        
        elif choice == '5':
            file_path = input("\n请输入包含链接的文件路径: ").strip()
            if file_path:
                batch_download(file_path)
        
        elif choice == '6':
            url = input("\n请输入视频链接: ").strip()
            if url:
                show_video_info(url)
        
        else:
            print("\n✗ 无效选择，请重试")
        
        input("\n按回车键继续...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
        sys.exit(0)
