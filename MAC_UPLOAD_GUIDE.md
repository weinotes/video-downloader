# Mac 系统 GitHub 上传指南

## 🍎 准备工作

### 1. 安装 Git（如果还没有）

打开终端（Command + Space，输入 Terminal），执行：

```bash
# 检查是否已安装
git --version

# 如果未安装，执行以下命令安装
xcode-select --install
```

### 2. 配置 Git

```bash
# 设置你的名字
git config --global user.name "你的名字"

# 设置你的邮箱（GitHub注册邮箱）
git config --global user.email "你的邮箱@example.com"
```

---

## 📝 修改个人信息

打开 `README.md` 文件，替换以下内容：

1. `yourusername` → 你的 GitHub 用户名
2. `your-email@example.com` → 你的邮箱

保存文件。

---

## 🚀 上传到 GitHub

### 步骤 1: 在 GitHub 创建仓库

1. 访问 https://github.com 并登录
2. 点击右上角 `+` → `New repository`
3. 填写：
   - Repository name: `video-downloader`
   - Description: `跨平台视频下载工具`
   - 选择 Public
   - **不要勾选**任何初始化选项
4. 点击 `Create repository`
5. **记下仓库地址**（类似：`https://github.com/你的用户名/video-downloader.git`）

### 步骤 2: 上传代码

在终端中，进入项目文件夹，然后执行：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交到本地仓库
git commit -m "Initial commit: 添加视频下载工具"

# 关联远程仓库（替换为你的仓库地址）
git remote add origin https://github.com/你的用户名/video-downloader.git

# 推送到 GitHub
git push -u origin main
```

如果提示 `master` 分支错误，执行：
```bash
git branch -M main
git push -u origin main
```

### 步骤 3: 首次推送需要登录

系统会提示输入用户名和密码。

**重要：密码不是你的 GitHub 登录密码，而是 Personal Access Token！**

#### 创建 Token：

1. 在 GitHub 点击头像 → `Settings`
2. 左侧菜单最底部 → `Developer settings`
3. `Personal access tokens` → `Tokens (classic)`
4. `Generate new token` → `Generate new token (classic)`
5. 填写：
   - Note: `video-downloader`
   - Expiration: `90 days`
   - 勾选：✅ `repo`（所有子选项）
6. 点击 `Generate token`
7. **复制 Token**（以 `ghp_` 开头，只显示一次！）

#### 在终端输入：
```
Username: 你的GitHub用户名
Password: 粘贴刚才复制的Token
```

#### 保存凭据（避免重复输入）：
```bash
git config --global credential.helper osxkeychain
```

---

## ✅ 验证上传成功

访问：`https://github.com/你的用户名/video-downloader`

应该能看到所有文件！

---

## 📤 分享给学生

把这个链接发给学生：
```
https://github.com/你的用户名/video-downloader
```

学生可以：
- 直接下载 ZIP 文件
- 或使用 `git clone` 克隆项目

---

## 🔄 后续更新

修改代码后，只需执行：

```bash
git add .
git commit -m "更新说明"
git push
```

---

## 💡 完整命令速查

```bash
# 进入项目目录
cd /path/to/video-downloader-project

# 初始化并上传
git init
git add .
git commit -m "Initial commit: 添加视频下载工具"
git remote add origin https://github.com/你的用户名/video-downloader.git
git push -u origin main

# 如果提示分支错误
git branch -M main
git push -u origin main
```

---

**需要帮助？在 GitHub 上创建 Issue！**
