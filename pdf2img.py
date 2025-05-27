#!/usr/bin/env python3
"""
PDF to Image Converter
将figures文件夹下的所有PDF文件转换为高清PNG图片，并复制现有PNG文件到assets文件夹
Converts all PDF files in the figures folder to high-quality PNG images and copies existing PNG files to assets folder


使用方法 / Usage:

# 查看帮助信息 / Show help information
python pdf2img.py --help

# 基本使用 / Basic usage
python pdf2img.py

# 自定义参数 / Custom parameters  
python pdf2img.py --figures-dir "path/to/figures" --output-dir "path/to/output" --dpi 600
"""

import os
import shutil
from pathlib import Path
from typing import List, Tuple
import fitz  # PyMuPDF
from PIL import Image
import argparse


def setup_output_directory(output_dir: str) -> Path:
    """
    创建输出目录 / Create output directory
    """
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    print(f"输出目录已创建: {output_path.absolute()}")
    print(f"Output directory created: {output_path.absolute()}")
    return output_path


def find_all_files(figures_dir: str, extensions: List[str]) -> List[Tuple[Path, str]]:
    """
    递归查找所有指定扩展名的文件 / Recursively find all files with specified extensions
    Returns list of (file_path, extension) tuples
    """
    files = []
    figures_path = Path(figures_dir)
    
    if not figures_path.exists():
        print(f"错误: 图片目录不存在: {figures_path}")
        print(f"Error: Figures directory does not exist: {figures_path}")
        return files
    
    for ext in extensions:
        # 使用glob递归搜索所有子目录 / Use glob to recursively search all subdirectories
        pattern = f"**/*{ext}"
        found_files = list(figures_path.glob(pattern))
        files.extend([(f, ext) for f in found_files])
    
    return files


def pdf_to_png(pdf_path: Path, output_path: Path, dpi: int = 300) -> bool:
    """
    将PDF转换为高清PNG / Convert PDF to high-quality PNG
    """
    try:
        # 打开PDF文件 / Open PDF file
        pdf_document = fitz.open(str(pdf_path))
        
        # 获取第一页（大多数图片PDF只有一页）/ Get first page (most figure PDFs have only one page)
        page = pdf_document[0]
        
        # 设置缩放矩阵以获得高分辨率 / Set zoom matrix for high resolution
        zoom = dpi / 72.0  # 72 DPI is default
        mat = fitz.Matrix(zoom, zoom)
        
        # 渲染页面为像素图 / Render page as pixmap
        pix = page.get_pixmap(matrix=mat)
        
        # 保存为PNG / Save as PNG
        pix.save(str(output_path))
        
        pdf_document.close()
        
        print(f"✓ 已转换: {pdf_path.name} -> {output_path.name}")
        print(f"✓ Converted: {pdf_path.name} -> {output_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ 转换失败: {pdf_path.name} - {str(e)}")
        print(f"✗ Conversion failed: {pdf_path.name} - {str(e)}")
        return False


def copy_png(src_path: Path, dst_path: Path) -> bool:
    """
    复制PNG文件 / Copy PNG file
    """
    try:
        shutil.copy2(src_path, dst_path)
        print(f"✓ 已复制: {src_path.name} -> {dst_path.name}")
        print(f"✓ Copied: {src_path.name} -> {dst_path.name}")
        return True
    except Exception as e:
        print(f"✗ 复制失败: {src_path.name} - {str(e)}")
        print(f"✗ Copy failed: {src_path.name} - {str(e)}")
        return False


def process_files(figures_dir: str, output_dir: str, dpi: int = 300):
    """
    处理所有文件 / Process all files
    """
    print("开始处理文件...")
    print("Starting file processing...")
    print("=" * 50)
    
    # 设置输出目录 / Setup output directory
    output_path = setup_output_directory(output_dir)
    figures_path = Path(figures_dir)
    
    # 查找所有PDF和PNG文件 / Find all PDF and PNG files
    all_files = find_all_files(figures_dir, ['.pdf', '.png'])
    
    if not all_files:
        print("未找到任何PDF或PNG文件")
        print("No PDF or PNG files found")
        return
    
    print(f"找到 {len(all_files)} 个文件需要处理")
    print(f"Found {len(all_files)} files to process")
    print("-" * 30)
    
    success_count = 0
    fail_count = 0
    
    for file_path, extension in all_files:
        # 计算相对于figures目录的路径 / Calculate relative path from figures directory
        relative_path = file_path.relative_to(figures_path)
        
        if extension == '.pdf':
            # 转换PDF为PNG，保持文件夹结构 / Convert PDF to PNG, preserve folder structure
            output_file = output_path / relative_path.parent / f"{relative_path.stem}.png"
            # 确保输出目录存在 / Ensure output directory exists
            output_file.parent.mkdir(parents=True, exist_ok=True)
            if pdf_to_png(file_path, output_file, dpi):
                success_count += 1
            else:
                fail_count += 1
                
        elif extension == '.png':
            # 复制PNG文件，保持文件夹结构 / Copy PNG file, preserve folder structure
            output_file = output_path / relative_path
            # 确保输出目录存在 / Ensure output directory exists
            output_file.parent.mkdir(parents=True, exist_ok=True)
            if copy_png(file_path, output_file):
                success_count += 1
            else:
                fail_count += 1
    
    print("-" * 30)
    print(f"处理完成! 成功: {success_count}, 失败: {fail_count}")
    print(f"Processing complete! Success: {success_count}, Failed: {fail_count}")
    print(f"所有图片已保存到: {output_path.absolute()}")
    print(f"All images saved to: {output_path.absolute()}")


def main():
    """
    主函数 / Main function
    """
    parser = argparse.ArgumentParser(
        description="将PDF图片转换为PNG格式并复制现有PNG文件 / Convert PDF figures to PNG format and copy existing PNG files"
    )
    parser.add_argument(
        "--figures-dir", 
        default="../figures",
        help="图片源目录路径 / Source figures directory path (default: ../figures)"
    )
    parser.add_argument(
        "--output-dir",
        default="../assets",
        help="输出目录路径 / Output directory path (default: ../assets)"
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="PDF转换的DPI分辨率 / DPI resolution for PDF conversion (default: 300)"
    )
    
    args = parser.parse_args()
    
    print("PDF转图片工具 / PDF to Image Converter")
    print("=" * 50)
    print(f"源目录 / Source directory: {args.figures_dir}")
    print(f"输出目录 / Output directory: {args.output_dir}")
    print(f"DPI分辨率 / DPI resolution: {args.dpi}")
    print("=" * 50)
    
    # 检查依赖 / Check dependencies
    try:
        import fitz
        import PIL
        print("✓ 依赖检查通过")
        print("✓ Dependencies check passed")
    except ImportError as e:
        print(f"✗ 缺少依赖: {e}")
        print(f"✗ Missing dependency: {e}")
        print("请安装依赖: pip install PyMuPDF Pillow")
        print("Please install dependencies: pip install PyMuPDF Pillow")
        return
    
    # 开始处理 / Start processing
    process_files(args.figures_dir, args.output_dir, args.dpi)


if __name__ == "__main__":
    main()

