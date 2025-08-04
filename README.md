# PDF to Image Converter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyMuPDF](https://img.shields.io/badge/PyMuPDF-1.23.0+-green.svg)](https://pymupdf.readthedocs.io/)
[![Pillow](https://img.shields.io/badge/Pillow-10.0.0+-orange.svg)](https://pillow.readthedocs.io/)
[![English Docs](https://img.shields.io/badge/docs-English-blue.svg)](README_en.md)

[English](README.md) | [中英对照](README_zh_en.md) | [中文](README_zh.md) 

This tool can batch convert all PDF files in the figures folder to high-quality PNG images and copy existing PNG files to the assets folder.

## Features

- 🔄 Batch convert PDFs to high-quality PNG images
- 📁 Recursively search all subfolders
- 📋 Copy existing PNG files
- 🗂️ Preserve original folder structure
- ⚙️ Customizable DPI resolution
- 🌐 Bilingual output messages
- ✅ Detailed processing status reports

## Install Dependencies

```bash
cd pdf2img_tool
pip install -r requirements.txt
```

Or install manually:
```bash
pip install PyMuPDF Pillow
```

## Usage

### Basic Usage

```bash
cd pdf2img_tool
python pdf2img.py
```

This will use default settings:
- Source directory: `../figures`
- Output directory: `../assets`
- DPI resolution: 300

### Custom Parameters

```bash
cd pdf2img_tool
python pdf2img.py --figures-dir "path/to/figures" --output-dir "path/to/output" --dpi 600
```

### Parameter Description

- `--figures-dir`: Source figures directory path
- `--output-dir`: Output directory path
- `--dpi`: DPI resolution for PDF conversion (default 300)

### View Help

```bash
cd pdf2img_tool
python pdf2img.py --help
```

## Output Example

```
PDF to Image Converter
==================================================
Source directory: arXiv-2504.20073v1/figures
Output directory: ./assets
DPI resolution: 300
==================================================
✓ Dependencies check passed
Starting file processing...
==================================================
Output directory created: /path/to/assets
Found 35 files to process
------------------------------
✓ Converted: example.pdf -> example.png
✓ Copied: frozenlake_env_example.png -> frozenlake_env_example.png
...
------------------------------
Processing complete! Success: 35, Failed: 0
All images saved to: /path/to/assets
```

## Supported File Formats

- **Input**: PDF, PNG
- **Output**: PNG (High Quality)

## Notes

1. Ensure sufficient disk space for converted images
2. Higher DPI settings will produce larger files
3. The program will automatically create the output directory
4. Existing output files will be overwritten

## Troubleshooting

### Dependency Installation Issues

If you encounter PyMuPDF installation issues:

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

### Out of Memory

If running out of memory with large files, reduce DPI setting:

```bash
cd pdf2img_tool
python pdf2img.py --dpi 150
```

## License

MIT License 