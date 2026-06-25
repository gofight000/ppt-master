import shutil
import os

src_dir = r'e:/AI/2026/Master/ppt-master/skills/ppt-master/templates/layouts/government_blue'
dst_dir = r'e:/AI/2026/Master/ppt-master/projects/projects/师大校园安防升级改造_ppt169_20260404/templates'

files = ['01_cover.svg', '02_chapter.svg', '02_toc.svg', '03_content.svg', '04_ending.svg', 'design_spec.md']

for f in files:
    src = os.path.join(src_dir, f)
    dst = os.path.join(dst_dir, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f'Copied: {f}')
    else:
        print(f'Not found: {f}')

print('Done')
