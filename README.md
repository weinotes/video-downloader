# 🎬 视频下载工具 | Video Downloader

**Author:** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/weinotes/video-downloader)

一个功能强大的跨平台视频下载工具，支持 YouTube、B站、抖音等 1000+ 视频网站。专为教学研究设计，界面友好，操作简单。

**A powerful cross-platform video downloader supporting 1000+ websites. Designed for educational purposes.**

---

## ✨ 主要特性

- 🌍 **跨平台支持** - Windows、macOS、Linux 全平台支持
- 🎯 **支持 1000+ 网站** - YouTube、B站、抖音、Twitter 等主流平台
- 🎨 **中文友好界面** - 交互式菜单，操作简单直观
- 📹 **多种下载模式** - 视频、音频、字幕独立下载
- ⚙️ **自定义画质** - 支持 1080p、720p、480p、360p 等多种画质
- 📦 **批量下载** - 从文件读取链接，一键批量下载
- 🔒 **教育用途** - 专为教学研究设计，合法合规

---

## 🚀 快速开始

### 方法一：一键启动（推荐）

#### Windows 系统
双击运行 `start_windows.bat`

#### Mac/Linux 系统
```bash
chmod +x start_mac_linux.sh
./start_mac_linux.sh
```

### 方法二：手动运行

#### 1. 安装依赖
```bash
pip install -U yt-dlp
# 或者 Mac/Linux 使用
pip3 install -U yt-dlp
```

#### 2. 运行程序
```bash
# Windows
python video_downloader.py

# Mac/Linux
python3 video_downloader.py
```

---

## 📖 使用说明

### 基本使用

1. **运行程序**：执行启动脚本或直接运行 `video_downloader.py`
2. **选择功能**：根据菜单提示输入数字（0-6）
3. **输入链接**：粘贴要下载的视频链接
4. **等待完成**：视频会自动下载到 `downloads` 文件夹

### 功能菜单

```
==================================================
视频下载工具 - 用于教学研究
==================================================
1. 下载视频（最高画质）
2. 下载视频（指定画质）
3. 仅下载音频
4. 下载视频+字幕
5. 批量下载（从文件读取链接）
6. 查看视频信息（不下载）
0. 退出
==================================================
```

### 批量下载

1. 编辑 `urls.txt` 文件
2. 每行填入一个视频链接
3. 选择菜单选项 `5`
4. 输入文件路径：`urls.txt`

**urls.txt 示例：**
```
https://www.youtube.com/watch?v=xxxxx
https://www.bilibili.com/video/BVxxxxx
https://www.douyin.com/video/xxxxxx
```

---

## 🌐 支持的网站

### 国内平台
- 🎬 **Bilibili** (B站)
- 📱 **Douyin** (抖音)
- 🎥 **Tencent Video** (腾讯视频)
- 🎬 **iQIYI** (爱奇艺)
- 📺 **Youku** (优酷)
- 🎞️ **Xigua Video** (西瓜视频)

### 国际平台
- ▶️ **YouTube**
- 🐦 **Twitter/X**
- 📘 **Facebook**
- 📸 **Instagram**
- 🎵 **TikTok**
- 🎬 **Vimeo**

**更多网站**：查看 [完整支持列表](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)（1000+）

---

## 💡 高级用法

### 命令行直接使用

```bash
# 下载视频（最佳画质）
yt-dlp "视频链接"

# 下载指定画质（720p）
yt-dlp -f "bestvideo[height<=720]+bestaudio" "视频链接"

# 仅下载音频（MP3）
yt-dlp -x --audio-format mp3 "视频链接"

# 下载视频+字幕
yt-dlp --write-sub --sub-lang zh-Hans,en "视频链接"

# 列出所有可用格式
yt-dlp -F "视频链接"

# 批量下载
yt-dlp -a urls.txt
```

### 使用代理

```bash
# 使用 SOCKS5 代理
yt-dlp --proxy socks5://127.0.0.1:1080 "视频链接"

# 使用 HTTP 代理
yt-dlp --proxy http://127.0.0.1:8080 "视频链接"
```

---

## 📋 项目结构

```
video-downloader/
├── video_downloader.py      # 主程序
├── start_windows.bat         # Windows 启动脚本
├── start_mac_linux.sh        # Mac/Linux 启动脚本
├── urls.txt                  # 批量下载链接示例
├── README.md                 # 项目说明
├── QUICK_REFERENCE.md        # 快速参考手册
├── LICENSE                   # MIT 许可证
├── .gitignore               # Git 忽略文件
└── downloads/               # 下载目录（自动创建）
```

---

## 🔧 常见问题

<details>
<summary><b>Q: 下载速度很慢怎么办？</b></summary>

**A:** 
- 使用代理或 VPN
- 某些网站可能有限速
- 可以使用 `-r` 参数限制速度避免被封
</details>

<details>
<summary><b>Q: 提示视频不可用或下载失败？</b></summary>

**A:**
- 检查链接是否有效
- 更新 yt-dlp：`pip install -U yt-dlp`
- 某些视频可能需要登录
- 查看详细错误：`yt-dlp -v "链接"`
</details>

<details>
<summary><b>Q: 如何下载播放列表？</b></summary>

**A:**
```bash
# 下载整个播放列表
yt-dlp "播放列表链接"

# 下载播放列表的部分视频（1-10）
yt-dlp --playlist-start 1 --playlist-end 10 "播放列表链接"
```
</details>

---

## 🛠️ 系统要求

- **Python**: 3.8 或更高版本
- **yt-dlp**: 自动安装
- **FFmpeg**: 可选（用于合并视频音频）

### 安装 FFmpeg（可选）

**Windows:**
```cmd
# 使用 Chocolatey
choco install ffmpeg
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install ffmpeg
```

---

## 📚 文档

- 📘 [快速参考手册](QUICK_REFERENCE.md) - 常用命令速查
- 📕 [yt-dlp 官方文档](https://github.com/yt-dlp/yt-dlp) - 更多高级功能

---

## ⚠️ 免责声明

本工具仅供**教学研究**使用，请遵守以下原则：

- ✅ 用于个人学习和研究
- ✅ 用于制作教学课件
- ✅ 用于学术研究资料收集
- ❌ 不得用于商业用途
- ❌ 不得侵犯版权
- ❌ 不得传播下载的内容

**请遵守视频平台的使用条款和当地的版权法律。**

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📝 License

MIT License — see [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

---

## 📮 联系方式

- 📧 Email: wgwcko@gmail.com
- 🌐 Blog: [www.guangweiblog.com](https://www.guangweiblog.com)

---

## 🙏 致谢

- 感谢 [yt-dlp](https://github.com/yt-dlp/yt-dlp) 项目提供强大的下载引擎
- 感谢所有贡献者和使用者

---

<div align="center">

**如果觉得有用，请给个 ⭐️ 支持一下！**

Made with ❤️ for Education

</div>
