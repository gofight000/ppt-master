#!/usr/bin/env python3
"""Analyze PPTX file and extract style information"""
import zipfile
import json
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}

pptx_path = Path('e:/AI/2026/Master/ppt-master/test01/2025年新疆通服云业务能力介绍E(修).pptx')
print(f'File exists: {pptx_path.exists()}')

if not pptx_path.exists():
    print("File not found!")
    exit(1)

with zipfile.ZipFile(pptx_path, 'r') as zf:
    files = zf.namelist()
    print(f'Total files: {len(files)}')
    
    # Get slide size
    presentation_xml = zf.read('ppt/presentation.xml')
    root = ET.fromstring(presentation_xml)
    
    sld_sz = root.find('p:sldSz', NS)
    if sld_sz is not None:
        cx = int(sld_sz.attrib.get('cx', '0'))
        cy = int(sld_sz.attrib.get('cy', '0'))
        print(f'Slide size: {cx} x {cy} EMUs')
        print(f'Slide size px: {cx/914400*10:.0f} x {cy/914400*10:.0f} cm')
    
    # Find theme files
    theme_files = [f for f in files if 'theme' in f and f.endswith('.xml')]
    print(f'\nTheme files: {theme_files}')
    
    # Extract colors from first theme
    if theme_files:
        theme_xml = zf.read(theme_files[0])
        theme_root = ET.fromstring(theme_xml)
        
        clr_scheme = theme_root.find('.//a:clrScheme', NS)
        if clr_scheme is not None:
            print('\nTheme Colors:')
            for child in list(clr_scheme):
                if not isinstance(child.tag, str):
                    continue
                name = child.tag.split('}', 1)[-1]
                srgb = child.find('a:srgbClr', NS)
                sys_clr = child.find('a:sysClr', NS)
                if srgb is not None and 'val' in srgb.attrib:
                    print(f'  {name}: #{srgb.attrib["val"]}')
                elif sys_clr is not None:
                    last = sys_clr.attrib.get('lastClr')
                    if last:
                        print(f'  {name}: #{last}')
    
    # Check for background images
    media_files = [f for f in files if 'media' in f]
    print(f'\nMedia files ({len(media_files)}):')
    for f in media_files[:10]:
        print(f'  {f}')
    
print("\nAnalysis complete!")
