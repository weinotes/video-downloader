# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Author:** Davey Wong <wgwcko@gmail.com> | [www.guangweiblog.com](https://www.guangweiblog.com)

## [2.0.0] - 2025-05-10

### Fixed
- `show_video_info` — replaced single `--print` with `\n` (literal `\n` printed) with multiple `--print` calls
- `--convert-subs` deprecation — corrected flag usage for newer yt-dlp versions
- All download functions now capture and display yt-dlp stderr on failure instead of silent "下载失败"
- Added FFmpeg detection — warns user before merge-dependent operations
- Startup scripts now chdir to script directory, preventing "file not found" when launched from elsewhere

### Added
- Type hints throughout the codebase (PEP 484)
- `--no-playlist` flag on all single-video operations to prevent accidental playlist download
- `--embed-thumbnail` and `--embed-metadata` for richer output files
- Pre-flight check (`preflight()`) runs before menu — checks yt-dlp + FFmpeg
- `CHANGELOG.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` — standard open-source files
- Author attribution in all source files per project convention

### Changed
- Refactored repeated `os.makedirs` / output-path logic into `ensure_dir()` and `fmt_output()` helpers
- `subprocess.run` — switched from `check=True` + bare `except` to capturing stderr for actionable error messages
- `LICENSE` — updated copyright to Davey Wong <wgwcko@gmail.com>
- README visual alignment, English-primary docstrings
- Startup scripts — auto-install yt-dlp if missing (macOS/Linux)

### Removed
- Redundant `os.path` usage — replaced with `pathlib.Path`

## [1.0.0] - 2024

- Initial release: menu-driven video downloader with 6 functions
