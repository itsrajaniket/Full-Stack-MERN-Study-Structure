import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def polish_document(text):
    # 1. Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 2. Page breaks for Modules only
    text = re.sub(r'\n+(## .*? Module)', r'\n\n<div style="page-break-before: always;"></div>\n\n\1', text)
    
    # 3. Standardize Q sections
    text = re.sub(r'\n+(### Q)', r'\n\n\1', text)
    
    return text

try:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Global encoding fix
    encoding_fixes = {
        "ðŸ”‘": "🔑", "ðŸ“–": "📖", "ðŸ’»": "💻", "ðŸ§ ": "🧠", "âœ…": "✅",
        "ðŸŒ ": "🌐", "ðŸŒƒ": "🍃", "ðŸ”": "🔐", "ðŸ›": "🛠️", "ðŸ¤": "🤝",
        "ðŸ’¡": "💡", "ðŸš€": "🚀", "ðŸ”¥": "🔥", "ðŸ“¦": "📦"
    }
    for mangled, correct in encoding_fixes.items():
        content = content.replace(mangled, correct)

    polished_content = polish_document(content)
    
    # 4. Generate Table of Contents (MODULES ONLY - Stricter)
    # Find all lines starting with '##' that contain 'Module'
    modules = re.findall(r'^## (.*Module.*)', polished_content, re.MULTILINE)
    toc = "# 📑 Table of Contents\n\n"
    for module in modules:
        # Create slug
        slug = module.lower().strip()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        toc += f"- [{module.strip()}](#{slug})\n"
    
    # 5. Extract "One Line Takeaways" for Cheat Sheet
    # Pattern: Look for ### Question, then some content, then #### 🧠 One Line to Remember, then the answer line
    cheat_sheet_items = []
    # Using a more robust splitting method
    sections = re.split(r'\n### ', polished_content)
    for section in sections[1:]: # Skip the intro
        lines = section.split('\n')
        question = lines[0].strip()
        one_liner = ""
        for i, line in enumerate(lines):
            if "#### 🧠 One Line to Remember" in line:
                if i + 1 < len(lines):
                    one_liner = lines[i+1].strip()
                    if not one_liner and i + 2 < len(lines): # Check one more line if empty
                        one_liner = lines[i+2].strip()
                break
        if one_liner:
            cheat_sheet_items.append(f"- **{question}**: {one_liner}")

    cheat_sheet = "\n\n<div style='page-break-before: always;'></div>\n\n# 💡 Interview Quick-Recall Cheat Sheet\n\n"
    cheat_sheet += "This section contains only the 'One Line to Remember' for every question to help you review 5 minutes before the interview.\n\n"
    cheat_sheet += "\n".join(cheat_sheet_items)

    # 6. Final Assembly (Clear out old TOC/Title if duplicate)
    # Remove any existing titles/TOCs that might have been prepended
    polished_content = re.sub(r'^# 🚀 MERN Stack Interview Study Kit.*?(?=##)', '', polished_content, flags=re.DOTALL)
    
    final_output = "# 🚀 MERN Stack Interview Study Kit\n\n" + toc + "\n\n---\n\n" + polished_content.strip() + cheat_sheet

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    print("Final Polish complete.")
except Exception as e:
    print(f"Error: {e}")
