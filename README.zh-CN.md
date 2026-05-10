# 视频下载工具

中文 | [English](README.md)

🎬 跨平台视频下载工具，支持 YouTube、B站、抖音等 1000+ 视频网站

**作者：** Davey Wong <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/weinotes/video-downloader)

---

## 主要特性

- 🌍 **跨平台支持** — Windows、macOS、Linux
- 🎯 **支持 1000+ 网站** — YouTube、B站、抖音、Twitter 等
- 🎨 **交互式菜单** — 操作简单，无需记忆命令
- 📹 **多种下载模式** — 视频、音频、字幕独立下载
- ⚙️ **自定义画质** — 1080p、720p、480p、360p
- 📦 **批量下载** — 从文件读取链接，一键下载
- 🔑 **大会员登录** — 提取浏览器 Cookie，解锁高清画质
- 🔒 **教育研究用途** — 仅供学习和研究

---

## 快速开始

### 一键启动

**Windows：** 双击运行 `start_windows.bat`

**macOS / Linux：**
```bash
chmod +x start_mac_linux.sh
./start_mac_linux.sh
```

### 手动运行

```bash
pip install -U yt-dlp
python video_downloader.py   # Windows
python3 video_downloader.py  # macOS / Linux
```

---

## 使用说明

```
==================================================
       视频下载工具
==================================================
1. 下载视频（最高画质）
2. 下载视频（指定画质）
3. 仅下载音频 (MP3)
4. 下载视频 + 字幕
5. 批量下载
6. 查看视频信息
7. 登录设置（提取浏览器 Cookie）
0. 退出
==================================================
```

### 大会员登录

B站大会员用户如需下载 4K 或 1080P 高码率画质：

1. 在菜单中选择 **选项 7**
2. 选择你的浏览器（Chrome / Firefox / Edge）
3. 工具会自动提取登录态
4. 之后下载即享大会员画质

### 批量下载

1. 编辑 `urls.txt` 文件，每行一个链接
2. 选择选项 **5**
3. 输入文件路径：`urls.txt`

---

## 支持的网站

| 国内平台 | 国际平台 |
|---------|---------|
| Bilibili (B站) | YouTube |
| 抖音 | Twitter/X |
| 腾讯视频 | Facebook |
| 爱奇艺 | Instagram |
| 优酷 | TikTok |
| 西瓜视频 | Vimeo |

完整列表：[yt-dlp 支持网站](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)（1000+）

---

## 项目结构

```
video-downloader/
├── video_downloader.py      # 主程序
├── start_windows.bat        # Windows 启动脚本
├── start_mac_linux.sh       # Mac/Linux 启动脚本
├── urls.txt                 # 批量下载链接示例
├── QUICK_REFERENCE.md       # 快速参考
├── CHANGELOG.md             # 变更日志
├── CODE_OF_CONDUCT.md       # 行为准则
├── CONTRIBUTING.md          # 贡献指南
├── SECURITY.md              # 安全策略
├── pyproject.toml           # 项目元数据
└── ...
```

---

## 系统要求

- **Python**：3.8+
- **yt-dlp**：自动安装
- **FFmpeg**：可选（推荐用于视频音频合并）

### 安装 FFmpeg

| 系统 | 命令 |
|------|------|
| Windows | `choco install ffmpeg` |
| macOS | `brew install ffmpeg` |
| Linux | `sudo apt install ffmpeg` |

---

## 常见问题

<details>
<summary><b>下载速度慢怎么办？</b></summary>

- 使用代理或 VPN
- 某些网站有限速
- 用 `-r 1M` 限制速度避免被封
</details>

<details>
<summary><b>视频不可用或下载失败？</b></summary>

- 检查链接是否有效
- 更新 yt-dlp：`pip install -U yt-dlp`
- 部分视频需要登录（使用选项 7）
- 查看详细错误：`yt-dlp -v "链接"`
</details>

<details>
<summary><b>如何下载播放列表？</b></summary>

```bash
# 下载整个列表
yt-dlp "播放列表链接"

# 仅下载第 1-10 个视频
yt-dlp --playlist-start 1 --playlist-end 10 "链接"
```
</details>

---

## 免责声明

本工具仅供 **教学研究** 使用。

- ✅ 个人学习和研究
- ✅ 教学课件制作
- ❌ 商业用途
- ❌ 侵犯版权
- ❌ 传播下载内容

**请遵守视频平台的使用条款和当地的版权法律。**

---

## 许可证

MIT License — 详见 [LICENSE](LICENSE)

---

**Davey Wong** <wgwcko@gmail.com> · [www.guangweiblog.com](https://www.guangweiblog.com)
