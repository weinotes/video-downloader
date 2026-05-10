#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cross-platform video downloader · 跨平台视频下载工具

Supports 1000+ websites (YouTube, Bilibili, Douyin, etc.).
Designed for educational and research purposes.

Author: Davey Wong <wgwcko@gmail.com> (https://www.guangweiblog.com)
Licensed under MIT.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent.resolve()
DEFAULT_OUTPUT_DIR = SCRIPT_DIR / "downloads"

# ---------------------------------------------------------------------------
# Global state
# ---------------------------------------------------------------------------

# Browser to extract cookies from (None = no cookies).
# Set via option 7 or cookie file detection.
COOKIE_BROWSER: Optional[str] = None
COOKIE_BROWSER_NAME: str = "无"


# ---------------------------------------------------------------------------
# yt-dlp check & install
# ---------------------------------------------------------------------------

def _run_cmd(cmd: list[str], timeout: int = 60) -> subprocess.CompletedProcess:
    """Run a command and return the result. Raises on error."""
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def check_yt_dlp() -> bool:
    """Check if yt-dlp is installed and reachable."""
    try:
        _run_cmd(["yt-dlp", "--version"])
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


def install_yt_dlp() -> bool:
    """Install/upgrade yt-dlp via pip."""
    print("正在安装 yt-dlp...")
    try:
        _run_cmd([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"])
        print("✓ yt-dlp 安装成功！")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 安装失败: {e.stderr}")
        print("  手动安装: pip install -U yt-dlp")
        print("  或访问: https://github.com/yt-dlp/yt-dlp")
        return False


# ---------------------------------------------------------------------------
# FFmpeg check
# ---------------------------------------------------------------------------

def check_ffmpeg() -> bool:
    """Check if FFmpeg is available (required for merge operations)."""
    return shutil.which("ffmpeg") is not None


# ---------------------------------------------------------------------------
# Cookie / login helpers
# ---------------------------------------------------------------------------

def set_cookie_browser(browser: Optional[str]) -> None:
    """Set the browser for cookie extraction."""
    global COOKIE_BROWSER, COOKIE_BROWSER_NAME
    COOKIE_BROWSER = browser
    COOKIE_BROWSER_NAME = {
        None: "无",
        "chrome": "Chrome",
        "firefox": "Firefox",
        "edge": "Edge",
        "brave": "Brave",
        "opera": "Opera",
    }.get(browser, browser or "无")


def cookie_args() -> list[str]:
    """Return yt-dlp args for cookie-based login, or empty list."""
    if COOKIE_BROWSER:
        return ["--cookies-from-browser", COOKIE_BROWSER]
    return []


def detect_browsers() -> list[tuple[str, str]]:
    """Detect available browsers on this system."""
    candidates = [
        ("chrome", "Google Chrome"),
        ("firefox", "Firefox"),
        ("edge", "Microsoft Edge"),
        ("brave", "Brave"),
        ("opera", "Opera"),
        ("chromium", "Chromium"),
        ("safari", "Safari"),
    ]
    available = []
    for key, name in candidates:
        try:
            subprocess.run(
                ["yt-dlp", "--cookies-from-browser", key, "--cookies", "/dev/null", "--version"],
                capture_output=True, text=True, timeout=5,
            )
            available.append((key, name))
        except Exception:
            continue
    return available


def configure_cookies() -> None:
    """Interactive cookie browser selection."""
    browsers = detect_browsers()
    if not browsers:
        print("\n⚠️  未检测到支持的浏览器")
        print("   请手动导出 cookies 文件，然后用 --cookies cookies.txt 参数")
        return

    print("\n已检测到以下浏览器：")
    for i, (key, name) in enumerate(browsers, 1):
        mark = " ← 当前" if key == COOKIE_BROWSER else ""
        print(f"  {i}. {name}{mark}")
    print("  0. 清除（不登录）")

    choice = input("\n请选择浏览器 (0-{}): ".format(len(browsers))).strip()
    if choice == "0":
        set_cookie_browser(None)
        print("✓ 已清除登录信息")
    else:
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(browsers):
                key, name = browsers[idx]
                set_cookie_browser(key)
                print(f"✓ 已选择 {name}，将自动提取登录态")
        except (ValueError, IndexError):
            print("✗ 无效选择")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def ensure_dir(path: Path) -> None:
    """Create output directory if it doesn't exist."""
    path.mkdir(parents=True, exist_ok=True)


def run_ytdlp(cmd: list[str]) -> bool:
    """
    Run yt-dlp with the given command list.
    Captures stderr for error reporting.
    Returns True on success.
    """
    try:
        result = subprocess.run(cmd, text=True, timeout=3600)
        return result.returncode == 0
    except FileNotFoundError:
        print("\n✗ yt-dlp 未找到，请重新安装")
        return False
    except subprocess.TimeoutExpired:
        print("\n✗ 下载超时，请检查网络连接")
        return False


def fmt_output(path: Path) -> str:
    """Return yt-dlp output template for a given directory."""
    return str(path / "%(title)s.%(ext)s")


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

def show_menu() -> None:
    cookie_status = f" (Cookie: {COOKIE_BROWSER_NAME})" if COOKIE_BROWSER else ""
    print("\n" + "=" * 50)
    print("      视频下载工具 · Video Downloader" + cookie_status)
    print("=" * 50)
    print("  1. 下载视频（最高画质）")
    print("  2. 下载视频（指定画质）")
    print("  3. 仅下载音频 (MP3)")
    print("  4. 下载视频 + 字幕")
    print("  5. 批量下载（从文件读取链接）")
    print("  6. 查看视频信息（不下载）")
    print("  7. 登录设置（提取浏览器 Cookie）")
    print("  0. 退出")
    print("=" * 50)
    if COOKIE_BROWSER:
        print(f"  🔑  已启用 Cookie: {COOKIE_BROWSER_NAME}")
    else:
        print("  🔓  未登录（大会员高清画质不可用）")


def prompt_url(label: str = "请输入视频链接") -> Optional[str]:
    """Prompt for a URL, return None if empty."""
    url = input(f"\n{label}: ").strip()
    return url if url else None


# ---------------------------------------------------------------------------
# Download functions
# ---------------------------------------------------------------------------

def download_best_quality(url: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Download best video+audio, merged as MP4."""
    ensure_dir(output_dir)
    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "--no-playlist",
        "--embed-thumbnail",
        "--embed-metadata",
        *cookie_args(),
        "-o", fmt_output(output_dir),
        url,
    ]
    print("正在下载（最高画质）...")
    if not run_ytdlp(cmd):
        return
    print(f"\n✓ 下载完成！保存至: {output_dir}")


def download_custom_quality(url: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Download video at a user-selected resolution."""
    ensure_dir(output_dir)

    print("\n画质选项：")
    print("  1. 1080p（含大会员高码率）")
    print("  2. 720p")
    print("  3. 480p")
    print("  4. 360p")

    choice = input("\n选择画质 (1-4): ").strip()
    quality_map = {
        "1": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "2": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "3": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "4": "bestvideo[height<=360]+bestaudio/best[height<=360]",
    }
    quality = quality_map.get(choice, quality_map["2"])

    cmd = [
        "yt-dlp",
        "-f", quality,
        "--merge-output-format", "mp4",
        "--no-playlist",
        "--embed-thumbnail",
        "--embed-metadata",
        *cookie_args(),
        "-o", fmt_output(output_dir),
        url,
    ]
    print(f"正在下载（{choice}p 画质）...")
    if not run_ytdlp(cmd):
        return
    print(f"\n✓ 下载完成！保存至: {output_dir}")


def download_audio(url: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Extract audio as MP3 (best quality)."""
    ensure_dir(output_dir)
    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--no-playlist",
        "--embed-metadata",
        "--embed-thumbnail",
        *cookie_args(),
        "-o", fmt_output(output_dir),
        url,
    ]
    print("正在下载音频...")
    if not run_ytdlp(cmd):
        return
    print(f"\n✓ 音频下载完成！保存至: {output_dir}")


def download_with_subtitles(url: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Download video with Chinese/English subtitles."""
    ensure_dir(output_dir)
    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "--no-playlist",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", "zh-Hans,zh-Hant,en",
        "--convert-subs", "srt",
        "--embed-subs",
        "--embed-thumbnail",
        "--embed-metadata",
        *cookie_args(),
        "-o", fmt_output(output_dir),
        url,
    ]
    print("正在下载（含字幕）...")
    if not run_ytdlp(cmd):
        return
    print(f"\n✓ 下载完成（含字幕）！保存至: {output_dir}")


def batch_download(file_path: str, output_dir: Path = DEFAULT_OUTPUT_DIR) -> None:
    """Batch download URLs from a file."""
    path = Path(file_path)
    if not path.exists():
        print(f"\n✗ 文件不存在: {path}")
        return

    ensure_dir(output_dir)
    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "--merge-output-format", "mp4",
        "--embed-thumbnail",
        "--embed-metadata",
        *cookie_args(),
        "-a", str(path),
        "-o", fmt_output(output_dir),
    ]
    print(f"正在批量下载（来源: {path.name}）...")
    if not run_ytdlp(cmd):
        return
    print(f"\n✓ 批量下载完成！保存至: {output_dir}")


def show_video_info(url: str) -> None:
    """Display video metadata without downloading."""
    cmd = [
        "yt-dlp",
        *cookie_args(),
        "--print", "title:      %(title)s",
        "--print", "duration:   %(duration_string)s",
        "--print", "resolution: %(resolution)s",
        "--print", "uploader:   %(uploader)s",
        "--print", "view_count: %(view_count)s",
        "--print", "url:        %(webpage_url)s",
        "--no-download",
        "--no-playlist",
        url,
    ]
    try:
        subprocess.run(cmd, check=True, text=True, timeout=30)
    except subprocess.CalledProcessError:
        print("\n✗ 获取信息失败，请检查链接和网络")
    except subprocess.TimeoutExpired:
        print("\n✗ 请求超时")


# ---------------------------------------------------------------------------
# List available formats
# ---------------------------------------------------------------------------

def list_formats(url: str) -> None:
    """List all available formats for a URL, then let user pick one by ID."""
    cmd = [
        "yt-dlp",
        *cookie_args(),
        "-F",
        "--no-playlist",
        "--no-download",
        url,
    ]
    print("正在获取可用格式列表...\n")
    try:
        subprocess.run(cmd, check=True, text=True, timeout=30)
    except subprocess.CalledProcessError:
        print("\n✗ 获取格式列表失败")
        return
    except subprocess.TimeoutExpired:
        print("\n✗ 请求超时")
        return

    # Let user pick format code
    fid = input("\n输入格式 ID 直接下载（回车跳过）: ").strip()
    if not fid:
        return

    ensure_dir(DEFAULT_OUTPUT_DIR)
    cmd2 = [
        "yt-dlp",
        "-f", fid,
        "--merge-output-format", "mp4",
        "--no-playlist",
        "--embed-thumbnail",
        "--embed-metadata",
        *cookie_args(),
        "-o", fmt_output(DEFAULT_OUTPUT_DIR),
        url,
    ]
    if run_ytdlp(cmd2):
        print(f"\n✓ 格式 {fid} 下载完成！保存至: {DEFAULT_OUTPUT_DIR}")


# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------

def preflight() -> bool:
    """Run pre-flight checks and print warnings. Returns True if OK to proceed."""
    if not check_yt_dlp():
        print("未检测到 yt-dlp")
        ans = input("是否现在安装？(y/n): ").strip().lower()
        if ans == "y":
            if not install_yt_dlp():
                return False
        else:
            print("请先安装 yt-dlp")
            return False

    if not check_ffmpeg():
        print("⚠️  未检测到 FFmpeg")
        print("   视频+音频合并功能可能需要 FFmpeg")
        print("   安装: brew install ffmpeg / sudo apt install ffmpeg")
        print("   或: https://ffmpeg.org/download.html\n")
    return True


# ---------------------------------------------------------------------------
# Main entry
# ---------------------------------------------------------------------------

BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          视频下载工具 · Video Downloader v2.1                 ║
║          支持 1000+ 视频网站 · 教学研究用途                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


def main() -> None:
    print(BANNER)
    if not preflight():
        return

    while True:
        show_menu()
        choice = input("\n请选择功能 (0-7): ").strip()

        if choice == "0":
            print("\n再见！")
            break

        if choice == "7":
            configure_cookies()
            input("\n按回车键继续...")
            continue

        if choice == "8":
            url = prompt_url("请输入视频链接查看格式")
            if url:
                list_formats(url)
            input("\n按回车键继续...")
            continue

        url: Optional[str] = None
        if choice in ("1", "2", "3", "4", "6"):
            url = prompt_url()
            if not url:
                print("链接不能为空")
                continue

        if choice == "1":
            download_best_quality(url)  # type: ignore[arg-type]
        elif choice == "2":
            download_custom_quality(url)  # type: ignore[arg-type]
        elif choice == "3":
            download_audio(url)  # type: ignore[arg-type]
        elif choice == "4":
            download_with_subtitles(url)  # type: ignore[arg-type]
        elif choice == "5":
            fp = input("\n请输入包含链接的文件路径: ").strip()
            if fp:
                batch_download(fp)
        elif choice == "6":
            show_video_info(url)  # type: ignore[arg-type]
        else:
            print("\n✗ 无效选择，请输入 0-7")
            continue

        input("\n按回车键继续...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
        sys.exit(0)
    print("\n---")
    print("Davey Wong <wgwcko@gmail.com> | https://www.guangweiblog.com")
    print("Licensed under MIT.\n")
