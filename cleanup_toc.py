import os
import re

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
seen_toc = set()
in_toc = False

for line in lines:
    if "# 📑 Table of Contents" in line:
        in_toc = True
        new_lines.append(line)
        continue
    
    if in_toc:
        if line.startswith("- ["):
            if line not in seen_toc:
                seen_toc.add(line)
                new_lines.append(line)
            continue
        elif line.strip() == "---":
            in_toc = False
            new_lines.append(line)
            continue
        elif line.strip() == "":
            new_lines.append(line)
            continue
        else:
            in_toc = False
            new_lines.append(line)
            continue
    
    new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("TOC duplicates removed.")
