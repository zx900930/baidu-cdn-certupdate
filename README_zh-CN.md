# baidu-cdn-certupdate

[ENGLISH](README.md) | 中文版

百度智能云 CDN 证书自动更新脚本

## 描述

这是一个 Python 脚本，可以自动将 SSL 证书推送到百度智能云 CDN。

## 安装

- 安装 Python 3：[https://wiki.python.org/moin/BeginnersGuide/Download](https://wiki.python.org/moin/BeginnersGuide/Download)
- 克隆项目：`git clone https://github.com/zx900930/baidu-cdn-certupdate.git`
- 进入项目文件夹：`cd baidu-cdn-certupdate`
- 安装依赖：`pip install -r requirements.txt`
- 编辑环境变量：`mv example.env .env`

## 使用方法

### 使用默认的 .env 文件

`python3 baiducertificates.py`

### 若要使用其它的 .env 文件运行脚本，请在终端中运行以下命令：

`python3 baiducertificates.py path/to/alternative.env`

## 支持

请使用Github issue。

## 路线图

- Docker 镜像
- Corn 定时任务

## 贡献

欢迎为该项目做出贡献。

## 许可证

GNU General Public License v3.0
