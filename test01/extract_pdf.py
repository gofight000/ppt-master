#!/usr/bin/env python3
import fitz
import sys

pdf_path = "【提纲】-师大校园安防升级改造-V3.0.pdf"

doc = fitz.open(pdf_path)
print(f"PDF has {len(doc)} pages")

content = []
for page_num, page in enumerate(doc, 1):
    text = page.get_text()
    content.append(f"\n=== Page {page_num} ===\n")
    content.append(text)

doc.close()

# Save to file
output = "output.md"
with open(output, "w", encoding="utf-8") as f:
    f.write("# 师大校园安防升级改造项目\n\n")
    f.write("".join(content))

print(f"Saved to {output}")
