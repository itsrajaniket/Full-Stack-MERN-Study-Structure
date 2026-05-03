import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def polish_document(text):
    # 1. Standardize spacing (max 2 newlines)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 2. Fix spacing around horizontal rules
    text = re.sub(r'\n+---\n+', '\n\n---\n\n', text)
    
    # 3. Ensure every Module header has a page break before it (except the first one)
    # Using <div style="page-break-before: always;"></div> for professional PDF conversion
    text = re.sub(r'(?<!^)(## . Module)', r'<div style="page-break-before: always;"></div>\n\n\1', text)
    
    # 4. Standardize header spacing
    text = re.sub(r'\n(#{2,4} .)', r'\n\n\1', text)
    
    # 5. Fix double separators (if any)
    text = re.sub(r'---\n\n---', '---', text)
    
    return text

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    polished_content = polish_document(content)
    
    # 6. Generate Table of Contents
    modules = re.findall(r'## (.*)', polished_content)
    toc = "# 📑 Table of Contents\n\n"
    for module in modules:
        # Create a basic anchor (strip emojis and special chars)
        anchor = module.lower().replace(' ', '-').replace(':', '').replace('.', '')
        # Remove non-alphanumeric chars for the anchor
        anchor = re.sub(r'[^a-z0-9\-]', '', anchor)
        toc += f"- [{module}](#{anchor})\n"
    
    # Insert TOC at the top (after the main title)
    final_content = polished_content
    if "# 🚀 MERN Stack Interview Study Kit" in final_content:
        final_content = final_content.replace("# 🚀 MERN Stack Interview Study Kit", "# 🚀 MERN Stack Interview Study Kit\n\n" + toc + "\n---\n")
    else:
        final_content = toc + "\n---\n" + final_content

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("Polish complete: Table of Contents added, whitespace cleaned, and page breaks inserted.")
except Exception as e:
    print(f"Error: {e}")
