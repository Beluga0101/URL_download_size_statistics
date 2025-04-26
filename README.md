# URL大小检测器

一个用于检查列表中指定URL文件大小的Python脚本。它首先尝试使用HEAD请求获取大小，如果失败，则下载文件以确定其大小。
PS：这是一个实验性的解决方案，本项目仅供参考

## 特点

- 使用HEAD请求检查文件大小，无需下载整个文件。
- 如果HEAD请求没有提供Content-Length，则回退到GET请求。
- 遵守Retry-After头部信息以应对速率限制。
- 请求之间有随机延迟，以避免触发速率限制。

## 安装

要使用这个脚本，你需要在系统上安装Python。你可以下载脚本并在本地运行。

1. 克隆仓库:
   ```bash
   git clone https://github.com/Beluga0101/URL_download_size_statistics.git
   cd URL_download_size_statistics

2. 确保你安装了requests库:
   ```bash
   pip install requests

## 使用方法

在同一目录下创建一个名为urls.txt的文件，每行一个URL（示例文件在example_urls.txt）。然后运行脚本：
   ```bash
   python URL_download_size_statistics.py
脚本将输出每个URL的大小，并在最后输出所有URL的总大小。
