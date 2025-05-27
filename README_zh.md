# PDF转图片工具

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.23.0+-green.svg)](https://pymupdf.readthedocs.io/)
[![Pillow](https://img.shields.io/badge/Pillow-10.0.0+-orange.svg)](https://pillow.readthedocs.io/)
[![中文文档](https://img.shields.io/badge/文档-中文-red.svg)](README_zh.md)

这个工具可以将figures文件夹下的所有PDF文件批量转换为高清PNG图片，并将现有的PNG文件复制到assets文件夹中。

## 功能特性

- 🔄 批量转换PDF为高清PNG图片
- 📁 递归搜索所有子文件夹
- 📋 复制现有PNG文件
- 🗂️ 保留原有文件夹结构
- ⚙️ 可自定义DPI分辨率
- 🌐 双语输出信息
- ✅ 详细的处理状态报告

## 安装依赖

```bash
cd pdf2img_tool
pip install -r requirements.txt
```

或者手动安装：
```bash
pip install PyMuPDF Pillow
```

## 使用方法

### 基本用法

```bash
cd pdf2img_tool
python pdf2img.py
```

这将使用默认设置：
- 源目录：`../figures`
- 输出目录：`../assets`  
- DPI分辨率：300

### 自定义参数

```bash
cd pdf2img_tool
python pdf2img.py --figures-dir "path/to/figures" --output-dir "path/to/output" --dpi 600
```

### 参数说明

- `--figures-dir`: 图片源目录路径
- `--output-dir`: 输出目录路径  
- `--dpi`: PDF转换的DPI分辨率（默认300）

### 查看帮助

```bash
cd pdf2img_tool
python pdf2img.py --help
```

## 输出示例

```
PDF转图片工具
==================================================
源目录: arXiv-2504.20073v1/figures
输出目录: ./assets
DPI分辨率: 300
==================================================
✓ 依赖检查通过
开始处理文件...
==================================================
输出目录已创建: /path/to/assets
找到 35 个文件需要处理
------------------------------
✓ 已转换: example.pdf -> example.png
✓ 已复制: frozenlake_env_example.png -> frozenlake_env_example.png
...
------------------------------
处理完成! 成功: 35, 失败: 0
所有图片已保存到: /path/to/assets
```

## 支持的文件格式

- **输入**: PDF, PNG
- **输出**: PNG (高清)

## 注意事项

1. 确保有足够的磁盘空间存储转换后的图片
2. 高DPI设置会产生更大的文件
3. 程序会自动创建输出目录
4. 如果输出文件已存在，会被覆盖

## 故障排除

### 依赖安装问题

如果遇到PyMuPDF安装问题：

```bash
# macOS
brew install mupdf-tools
pip install PyMuPDF

# Ubuntu/Debian  
sudo apt-get install libmupdf-dev
pip install PyMuPDF

# Windows
pip install --upgrade pip
pip install PyMuPDF
```

### 内存不足

如果处理大文件时内存不足，可以降低DPI设置：

```bash
cd pdf2img_tool
python pdf2img.py --dpi 150
```

## 许可证

MIT License 