import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def optimize_for_pdf(text):
    # 1. Fix Mojibake (Emoji Corruption)
    replacements = {
        "—ï¸ ": "🛠️",
        "🛠️🛠️": "🛠️", # Fix double cleanups
        "ðŸ”‘": "🔑", "ðŸ“–": "📖", "ðŸ’»": "💻", "ðŸ§ ": "🧠", "âœ…": "✅",
        "ðŸŒ ": "🌐", "ðŸŒƒ": "🍃", "ðŸ”": "🔐", "ðŸ›": "🛠️", "ðŸ¤": "🤝",
        "ðŸ’¡": "💡", "ðŸš€": "🚀", "ðŸ”¥": "🔥", "ðŸ“¦": "📦", "ðŸŒ ": "🌐",
        "🛠️ —ï¸ ": "🛠️", # Specific case found in TOC
        "🛠️Ÿ¢": "🛠️",
        "🛠️ —ï¸ ": "🛠️",
    }
    for mangled, correct in replacements.items():
        text = text.replace(mangled, correct)

    # 2. Fix multiple page breaks
    # Replace any sequence of page-break divs with just one
    text = re.sub(r'(<div style=["\']page-break-before: always;?["\']></div>\s*)+', '\n\n<div style="page-break-before: always;"></div>\n\n', text)
    
    # 3. Ensure every Module header (##) has a page break before it
    # But NOT the first one if it's right after the TOC
    text = re.sub(r'\n+(## Module)', r'\n\n<div style="page-break-before: always;"></div>\n\n\1', text)
    # Fix the case where we might have just added a duplicate page break
    text = re.sub(r'(<div style=["\']page-break-before: always;?["\']></div>\s*){2,}', '<div style="page-break-before: always;"></div>', text)

    # 4. Standardize horizontal rules (---)
    text = re.sub(r'\n+---\n+', '\n\n---\n\n', text)
    
    # 5. Deduplicate TOC
    lines = text.split('\n')
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
                # Extract the link target or text to identify duplicates
                match = re.search(r'\[(.*?)\]\((.*?)\)', line)
                if match:
                    key = match.group(2) # Use the anchor as key
                    if key not in seen_toc:
                        seen_toc.add(key)
                        new_lines.append(line)
                    continue
            elif line.startswith("---") or line.startswith("##") or line.strip() == "":
                if line.startswith("---") or line.startswith("##"):
                    in_toc = False
                new_lines.append(line)
                continue
        
        new_lines.append(line)
    
    text = '\n'.join(new_lines)

    # 6. Deduplicate Cheat Sheet items
    sections = re.split(r'(# 💡 Interview Quick-Recall Cheat Sheet)', text)
    if len(sections) > 1:
        header = sections[1]
        body = sections[2]
        body_lines = body.split('\n')
        unique_cheat = []
        seen_cheat = set()
        for line in body_lines:
            if line.startswith("- **Q"):
                # Identify by Question text
                q_match = re.search(r'\*\*Q\d+\.\s*(.*?)\*\*', line)
                if q_match:
                    q_text = q_match.group(1)
                    if q_text not in seen_cheat:
                        seen_cheat.add(q_text)
                        unique_cheat.append(line)
                    continue
            unique_cheat.append(line)
        text = sections[0] + header + '\n'.join(unique_cheat)

    return text

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    optimized_content = optimize_for_pdf(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(optimized_content)
    
    print("PDF Optimization Complete. All mojibake fixed, duplicates removed, and page-breaks standardized.")
except Exception as e:
    print(f"Error: {e}")
