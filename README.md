# PDF转图片工具 / PDF to Image Converter

这个工具可以将figures文件夹下的所有PDF文件批量转换为高清PNG图片，并将现有的PNG文件复制到assets文件夹中。

This tool can batch convert all PDF files in the figures folder to high-quality PNG images and copy existing PNG files to the assets folder.

## 功能特性 / Features

- 🔄 批量转换PDF为高清PNG图片 / Batch convert PDFs to high-quality PNG images
- 📁 递归搜索所有子文件夹 / Recursively search all subfolders  
- 📋 复制现有PNG文件 / Copy existing PNG files
- ⚙️ 可自定义DPI分辨率 / Customizable DPI resolution
- 🌐 双语输出信息 / Bilingual output messages
- ✅ 详细的处理状态报告 / Detailed processing status reports

## 安装依赖 / Install Dependencies

```bash
cd pdf2img_tool
pip install -r requirements.txt
```

或者手动安装 / Or install manually:
```bash
pip install PyMuPDF Pillow
```

## 使用方法 / Usage

### 基本用法 / Basic Usage

```bash
cd pdf2img_tool
python pdf2img.py
```

这将使用默认设置：
- 源目录：`../figures`
- 输出目录：`../assets`  
- DPI分辨率：300

This will use default settings:
- Source directory: `../figures`
- Output directory: `../assets`
- DPI resolution: 300

### 自定义参数 / Custom Parameters

```bash
cd pdf2img_tool
python pdf2img.py --figures-dir "path/to/figures" --output-dir "path/to/output" --dpi 600
```

### 参数说明 / Parameter Description

- `--figures-dir`: 图片源目录路径 / Source figures directory path
- `--output-dir`: 输出目录路径 / Output directory path  
- `--dpi`: PDF转换的DPI分辨率（默认300）/ DPI resolution for PDF conversion (default 300)

### 查看帮助 / View Help

```bash
cd pdf2img_tool
python pdf2img.py --help
```

## 输出示例 / Output Example

```
PDF转图片工具 / PDF to Image Converter
==================================================
源目录 / Source directory: arXiv-2504.20073v1/figures
输出目录 / Output directory: ./assets
DPI分辨率 / DPI resolution: 300
==================================================
✓ 依赖检查通过
✓ Dependencies check passed
开始处理文件...
Starting file processing...
==================================================
输出目录已创建: /path/to/assets
Output directory created: /path/to/assets
找到 35 个文件需要处理
Found 35 files to process
------------------------------
✓ 已转换: example.pdf -> example.png
✓ Converted: example.pdf -> example.png
✓ 已复制: frozenlake_env_example.png -> frozenlake_env_example.png
✓ Copied: frozenlake_env_example.png -> frozenlake_env_example.png
...
------------------------------
处理完成! 成功: 35, 失败: 0
Processing complete! Success: 35, Failed: 0
所有图片已保存到: /path/to/assets
All images saved to: /path/to/assets
```

## 支持的文件格式 / Supported File Formats

- **输入 / Input**: PDF, PNG
- **输出 / Output**: PNG (高清/High Quality)

## 注意事项 / Notes

1. 确保有足够的磁盘空间存储转换后的图片 / Ensure sufficient disk space for converted images
2. 高DPI设置会产生更大的文件 / Higher DPI settings will produce larger files
3. 程序会自动创建输出目录 / The program will automatically create the output directory
4. 如果输出文件已存在，会被覆盖 / Existing output files will be overwritten

## 故障排除 / Troubleshooting

### 依赖安装问题 / Dependency Installation Issues

如果遇到PyMuPDF安装问题 / If you encounter PyMuPDF installation issues:

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

### 内存不足 / Out of Memory

如果处理大文件时内存不足，可以降低DPI设置 / If running out of memory with large files, reduce DPI setting:

```bash
cd pdf2img_tool
python pdf2img.py --dpi 150
``` 