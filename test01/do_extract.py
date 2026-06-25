import fitz
import os

os.chdir(r'e:/AI/2026/Master/ppt-master/test01')

pdf_path = r'【提纲】-师大校园安防升级改造-V3.0.pdf'
doc = fitz.open(pdf_path)

with open('pdf_content.md', 'w', encoding='utf-8') as f:
    f.write('# 师大校园安防升级改造项目\n\n')
    for i, page in enumerate(doc):
        text = page.get_text()
        f.write(f'\n## 第{i+1}页\n\n')
        f.write(text)
        f.write('\n')

doc.close()
print('Done')
