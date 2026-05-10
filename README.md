# Video Downloader · 视频下载工具

🎬 Download videos from 1000+ websites (YouTube, Bilibili, Douyin, Twitter, etc.)
🎬 跨平台视频下载工具，支持 YouTube、B站、抖音等 1000+ 视频网站

**Author:** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/weinotes/video-downloader)

---

## Features · 主要特性

| English | 中文 |
|---------|------|
| 🌍 Cross-platform (Windows / macOS / Linux) | 🌍 **跨平台支持** |
| 🎯 1000+ supported sites: YouTube, Bilibili, Douyin, Twitter, etc. | 🎯 **支持 1000+ 网站** |
| 🎨 Interactive menu, easy to use | 🎨 **交互式菜单，操作简单** |
| 📹 Multiple download modes: video, audio, subtitles | 📹 **多种下载模式** |
| ⚙️ Custom quality: 1080p, 720p, 480p, 360p | ⚙️ **自定义画质** |
| 📦 Batch download from URL list file | 📦 **批量下载** |
| 🔑 Premium member login via browser cookies | 🔑 **大会员登录支持** |
| 🔒 For educational and research purposes | 🔒 **教育研究用途** |

---

## Quick Start · 快速开始

### Method 1: One-click · 一键启动

**Windows:** Double-click `start_windows.bat`

**macOS / Linux:**
```bash
chmod +x start_mac_linux.sh
./start_mac_linux.sh
```

### Method 2: Manual · 手动运行

```bash
# Install yt-dlp · 安装依赖
pip install -U yt-dlp

# Run · 运行
python video_downloader.py   # Windows
python3 video_downloader.py  # macOS / Linux
```

---

## Usage · 使用说明

```
==================================================
    Video Downloader · 视频下载工具
==================================================
1. Download video (best quality) · 最高画质
2. Download video (custom quality) · 指定画质
3. Download audio only (MP3) · 仅下载音频
4. Download video + subtitles · 视频+字幕
5. Batch download · 批量下载
6. Show video info · 查看视频信息
7. Login settings (browser cookies) · 登录设置
0. Exit · 退出
==================================================
```

### Login for Premium Content · 大会员登录

Bilibili premium members (大会员) need to enable cookie login to access 4K and 1080P high-bitrate content:

1. Select **option 7** in the menu
2. Choose your browser (Chrome / Firefox / Edge)
3. The tool will extract your login session automatically
4. All formats become available

B站大会员用户请先选 **选项 7** 设置浏览器 Cookie，解锁 4K/1080P高码率画质。

### Batch Download · 批量下载

1. Edit `urls.txt`, one URL per line
2. Select option **5** in the menu
3. Enter the file path: `urls.txt`

```
https://www.youtube.com/watch?v=xxxxx
https://www.bilibili.com/video/BVxxxxx
https://www.douyin.com/video/xxxxxx
```

---

## Supported Sites · 支持的网站

| Chinese Platforms · 国内平台 | International · 国际平台 |
|-----------------------------|------------------------|
| 🎬 Bilibili (B站) | ▶️ YouTube |
| 📱 Douyin (抖音) | 🐦 Twitter/X |
| 🎥 Tencent Video (腾讯视频) | 📘 Facebook |
| 🎬 iQIYI (爱奇艺) | 📸 Instagram |
| 📺 Youku (优酷) | 🎵 TikTok |
| 🎞️ Xigua Video (西瓜视频) | 🎬 Vimeo |

Full list: [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) (1000+)

---

## Project Structure · 项目结构

```
video-downloader/
├── video_downloader.py      # Main program · 主程序
├── start_windows.bat        # Windows launcher
├── start_mac_linux.sh       # macOS/Linux launcher
├── urls.txt                 # Batch URL example
├── QUICK_REFERENCE.md       # Command cheatsheet
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── pyproject.toml
├── LICENSE                  # MIT
├── .gitignore
└── downloads/               # Output directory (auto-created)
```

---

## System Requirements · 系统要求

- **Python**: 3.8+
- **yt-dlp**: auto-installed
- **FFmpeg**: optional (recommended for video merging)

### Install FFmpeg

| OS | Command |
|----|---------|
| Windows | `choco install ffmpeg` |
| macOS | `brew install ffmpeg` |
| Linux | `sudo apt install ffmpeg` |

---

## FAQ · 常见问题

<details>
<summary><b>Slow download speed? / 下载速度慢？</b></summary>

- Use a proxy or VPN · 使用代理或 VPN
- Some sites rate-limit · 某些网站有限速
- Use `-r` to limit speed and avoid being throttled
</details>

<details>
<summary><b>Video unavailable? / 视频不可用？</b></summary>

- Check if the URL is valid · 检查链接是否有效
- Update yt-dlp: `pip install -U yt-dlp`
- Some videos require login (use option 7)
- Check verbose log: `yt-dlp -v "URL"`
</details>

<details>
<summary><b>Download a playlist? / 下载播放列表？</b></summary>

```bash
# Full playlist · 整个播放列表
yt-dlp "playlist URL"

# Partial (videos 1-10) · 部分视频
yt-dlp --playlist-start 1 --playlist-end 10 "URL"
```
</details>

---

## Disclaimer · 免责声明

This tool is for **educational and research purposes only**.
本工具仅供 **教学研究** 使用。

- ✅ Personal learning and research · 个人学习和研究
- ✅ Course materials · 教学课件制作
- ❌ Commercial use · 商业用途
- ❌ Copyright infringement · 侵犯版权
- ❌ Redistributing downloaded content · 传播下载内容

**Please comply with platform terms of service and local copyright laws.**
**请遵守视频平台的使用条款和当地的版权法律。**

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
