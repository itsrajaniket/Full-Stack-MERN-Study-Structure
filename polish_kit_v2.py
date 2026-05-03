import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def polish_document(text):
    # 1. Remove existing TOC if present
    text = re.sub(r'# .*? Table of Contents.*?---', '', text, flags=re.DOTALL)
    
    # 2. Standardize spacing (exactly 1 newline between items, 2 between blocks)
    # First, collapse all whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 3. Ensure Page Breaks before Modules
    text = re.sub(r'(<div style="page-break-before: always;"></div>\n\n)+', '', text) # Remove existing ones to avoid duplicates
    text = re.sub(r'\n(## . Module)', r'\n\n<div style="page-break-before: always;"></div>\n\n\1', text)
    
    # 4. Fix formatting of "One Line to Remember" (ensure it has a horizontal rule before it)
    text = re.sub(r'\n+(#### . One Line to Remember)', r'\n\n---\n\n\1', text)
    
    return text

try:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Fix emojis first (the persistent mojibake)
    encoding_fixes = {
        "ðŸ”‘": "🔑", "ðŸ“–": "📖", "ðŸ’»": "💻", "ðŸ§ ": "🧠", "âœ…": "✅",
        "ðŸŒ ": "🌐", "ðŸŒƒ": "🍃", "ðŸ”": "🔐", "ðŸ›": "🛠️", "ðŸ¤": "🤝",
        "ðŸ’¡": "💡", "ðŸš€": "🚀", "ðŸ”¥": "🔥", "ðŸ“¦": "📦"
    }
    for mangled, correct in encoding_fixes.items():
        content = content.replace(mangled, correct)

    polished_content = polish_document(content)
    
    # 5. Generate Table of Contents (MODULES ONLY)
    modules = re.findall(r'## (.*)', polished_content)
    toc = "# 📑 Table of Contents\n\n"
    for module in modules:
        # Create a simple slug for the link
        slug = module.lower().replace(' ', '-').replace(':', '').replace('.', '')
        slug = re.sub(r'[^a-z0-9\-]', '', slug)
        toc += f"- [{module}](#{slug})\n"
    
    # 6. Add a "Interview Cheat Sheet" section at the end
    cheat_sheet = "\n\n<div style='page-break-before: always;'></div>\n\n# 💡 Interview Quick-Recall Cheat Sheet\n\n"
    cheat_sheet += "This section contains only the 'One Line to Remember' for every question to help you review 5 minutes before the interview.\n\n"
    
    one_liners = re.findall(r'### (.*?)\n.*?#### 🧠 One Line to Remember\n(.*?)\n', polished_content, re.DOTALL)
    for q, ans in one_liners:
        cheat_sheet += f"- **{q.strip()}**: {ans.strip()}\n"

    # Assemble
    final_output = "# 🚀 MERN Stack Interview Study Kit\n\n" + toc + "\n\n---\n\n" + polished_content + cheat_sheet

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    print("Polish complete: Table of Contents fixed, Cheat Sheet added, and formatting standardized.")
except Exception as e:
    print(f"Error: {e}")
