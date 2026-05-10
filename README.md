# Video Downloader

[简体中文](README.zh-CN.md) | English

🎬 Download videos from 1000+ websites (YouTube, Bilibili, Douyin, Twitter, etc.)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/weinotes/video-downloader)

---

## Features

- 🌍 **Cross-platform** — Windows, macOS, Linux
- 🎯 **1000+ sites supported** — YouTube, Bilibili, Douyin, Twitter, Facebook, Instagram, TikTok, Vimeo and more
- 🎨 **Interactive menu** — easy to use, no command memorization
- 📹 **Multiple modes** — video, audio, subtitles
- ⚙️ **Custom quality** — 1080p, 720p, 480p, 360p
- 📦 **Batch download** — from a URL list file
- 🔑 **Premium login** — browser cookie extraction for member-only content
- 🔒 **Educational use** — for learning and research purposes

---

## Quick Start

### One-Click Launcher

**Windows:** Double-click `start_windows.bat`

**macOS / Linux:**
```bash
chmod +x start_mac_linux.sh
./start_mac_linux.sh
```

### Manual

```bash
pip install -U yt-dlp
python video_downloader.py   # Windows
python3 video_downloader.py  # macOS / Linux
```

---

## Usage

```
==================================================
       Video Downloader
==================================================
1. Download video (best quality)
2. Download video (custom quality)
3. Download audio only (MP3)
4. Download video + subtitles
5. Batch download
6. Show video info
7. Login settings (browser cookies)
0. Exit
==================================================
```

### Premium Member Login

For Bilibili premium members (大会员) to access 4K and 1080P high-bitrate content:

1. Select **option 7** from the menu
2. Choose your browser (Chrome / Firefox / Edge)
3. The tool extracts your login session automatically
4. All premium formats become available

### Batch Download

1. Edit `urls.txt`, one URL per line
2. Select option **5**
3. Enter: `urls.txt`

---

## Supported Sites

| Chinese Platforms | International |
|------------------|---------------|
| Bilibili | YouTube |
| Douyin (TikTok CN) | Twitter/X |
| Tencent Video | Facebook |
| iQIYI | Instagram |
| Youku | TikTok |
| Xigua Video | Vimeo |

Full list: [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) (1000+)

---

## Project Structure

```
video-downloader/
├── video_downloader.py      # Main program
├── start_windows.bat        # Windows launcher
├── start_mac_linux.sh       # macOS/Linux launcher
├── urls.txt                 # Batch URL example
├── QUICK_REFERENCE.md       # Command cheatsheet
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── pyproject.toml
└── ...
```

---

## System Requirements

- **Python**: 3.8+
- **yt-dlp**: auto-installed
- **FFmpeg**: optional (recommended for video/audio merging)

### Install FFmpeg

| OS | Command |
|----|---------|
| Windows | `choco install ffmpeg` |
| macOS | `brew install ffmpeg` |
| Linux | `sudo apt install ffmpeg` |

---

## FAQ

<details>
<summary><b>Slow download speed?</b></summary>

- Use a proxy or VPN
- Some sites rate-limit
- Use `-r 1M` to limit speed and avoid throttling
</details>

<details>
<summary><b>Video unavailable or download fails?</b></summary>

- Check if the URL is valid
- Update yt-dlp: `pip install -U yt-dlp`
- Some videos require login (use option 7)
- Verbose log: `yt-dlp -v "URL"`
</details>

<details>
<summary><b>Download a playlist?</b></summary>

```bash
# Full playlist
yt-dlp "playlist URL"

# Videos 1-10
yt-dlp --playlist-start 1 --playlist-end 10 "URL"
```
</details>

---

## Disclaimer

This tool is for **educational and research purposes only**.

- ✅ Personal learning and research
- ✅ Course material creation
- ❌ Commercial use
- ❌ Copyright infringement
- ❌ Redistributing downloaded content

**Please comply with platform terms of service and local copyright laws.**

---

## License

MIT License — see [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
