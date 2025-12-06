# 视频下载快速参考

## 🚀 快速开始

### Windows
双击运行：`start_windows.bat`

### Mac/Linux
```bash
chmod +x start_mac_linux.sh
./start_mac_linux.sh
```

---

## 💡 常用命令速查

### 基本下载
```bash
# 下载单个视频（最佳画质）
yt-dlp "视频链接"

# 下载并转换为 MP4
yt-dlp -f "bestvideo+bestaudio" --merge-output-format mp4 "链接"

# 下载 720p 视频
yt-dlp -f "bestvideo[height<=720]+bestaudio" "链接"

# 下载 1080p 视频
yt-dlp -f "bestvideo[height<=1080]+bestaudio" "链接"
```

### 音频下载
```bash
# 提取音频为 MP3
yt-dlp -x --audio-format mp3 --audio-quality 0 "链接"

# 提取音频为 M4A
yt-dlp -x --audio-format m4a "链接"
```

### 字幕下载
```bash
# 下载视频和自动生成的字幕
yt-dlp --write-auto-sub --sub-lang zh-Hans,en "链接"

# 只下载字幕（不下载视频）
yt-dlp --write-sub --skip-download "链接"

# 嵌入字幕到视频
yt-dlp --embed-subs "链接"
```

### 播放列表
```bash
# 下载整个播放列表
yt-dlp "播放列表链接"

# 下载播放列表中的第 1-5 个视频
yt-dlp --playlist-start 1 --playlist-end 5 "播放列表链接"

# 只下载播放列表中的特定视频
yt-dlp --playlist-items 1,3,5 "播放列表链接"
```

### 批量下载
```bash
# 从文件读取链接批量下载
yt-dlp -a urls.txt

# 指定输出目录
yt-dlp -a urls.txt -o "下载/%(title)s.%(ext)s"
```

### 限速和代理
```bash
# 限制下载速度为 1MB/s
yt-dlp -r 1M "链接"

# 使用代理
yt-dlp --proxy socks5://127.0.0.1:1080 "链接"
```

### 查看信息
```bash
# 列出所有可用格式（不下载）
yt-dlp -F "链接"

# 查看视频信息
yt-dlp --print "%(title)s - %(duration)s - %(resolution)s" --no-download "链接"

# 获取直链
yt-dlp -g "链接"
```

---

## 📱 特定网站技巧

### B站（Bilibili）
```bash
# 下载B站视频
yt-dlp "https://www.bilibili.com/video/BVxxxxx"

# 下载B站视频（指定画质）
yt-dlp -f "bestvideo[height<=1080]+bestaudio" "B站链接"
```

### YouTube
```bash
# 下载年龄限制视频（需要登录）
yt-dlp --cookies-from-browser chrome "YouTube链接"

# 下载 YouTube 频道所有视频
yt-dlp "https://www.youtube.com/@频道名/videos"
```

### 抖音
```bash
# 下载抖音视频
yt-dlp "抖音视频链接"
```

---

## 🔧 高级选项

### 文件命名
```bash
# 自定义文件名格式
yt-dlp -o "%(uploader)s - %(title)s.%(ext)s" "链接"

# 按日期命名
yt-dlp -o "%(upload_date)s - %(title)s.%(ext)s" "链接"

# 包含视频ID
yt-dlp -o "%(title)s [%(id)s].%(ext)s" "链接"
```

### 使用 cookies（需要登录的网站）
```bash
yt-dlp --cookies-from-browser chrome "链接"
```

### 继续未完成的下载
```bash
yt-dlp -c "链接"
```

---

## 🌟 实用组合

### 下载教学视频的推荐设置
```bash
yt-dlp \
  -f "bestvideo[height<=1080]+bestaudio" \
  --merge-output-format mp4 \
  --write-sub \
  --sub-lang zh-Hans,en \
  --convert-subs srt \
  --embed-subs \
  -o "教学资料/%(title)s.%(ext)s" \
  "链接"
```

### 批量下载课程
```bash
yt-dlp \
  -f "bestvideo[height<=720]+bestaudio" \
  --merge-output-format mp4 \
  -o "课程/%(playlist_index)s - %(title)s.%(ext)s" \
  "播放列表链接"
```

---

## 📋 输出格式变量

常用的文件名模板变量：

- `%(title)s` - 视频标题
- `%(id)s` - 视频ID
- `%(ext)s` - 文件扩展名
- `%(uploader)s` - 上传者
- `%(upload_date)s` - 上传日期（YYYYMMDD）
- `%(duration)s` - 视频时长（秒）
- `%(resolution)s` - 分辨率
- `%(playlist_index)s` - 播放列表序号

---

## 🔄 更新 yt-dlp

定期更新以支持最新的网站变化：

```bash
pip install -U yt-dlp
# 或
pip3 install -U yt-dlp
```

---

## ⚠️ 注意事项

1. **版权**：仅用于教学研究，遵守版权法
2. **网络**：某些网站在中国大陆可能需要代理
3. **更新**：定期更新 yt-dlp 以支持网站变化
4. **登录**：某些内容需要账号，使用 `--cookies-from-browser`
5. **速度**：使用 `-r` 参数避免被限速

---

## 📚 更多资源

- 官方文档：https://github.com/yt-dlp/yt-dlp
- 支持的网站列表：https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md
