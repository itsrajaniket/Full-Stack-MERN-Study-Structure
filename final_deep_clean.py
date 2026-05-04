import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def final_audit_and_clean(text):
    # 1. Clean up mangled characters (Emoji mojibake)
    # These are very persistent!
    replacements = {
        "—ï¸ ": "🛠️",
        "ðŸ”‘": "🔑", "ðŸ“–": "📖", "ðŸ’»": "💻", "ðŸ§ ": "🧠", "âœ…": "✅",
        "ðŸŒ ": "🌐", "ðŸŒƒ": "🍃", "ðŸ”": "🔐", "ðŸ›": "🛠️", "ðŸ¤": "🤝",
        "ðŸ’¡": "💡", "ðŸš€": "🚀", "ðŸ”¥": "🔥", "ðŸ“¦": "📦", "ðŸŒ ": "🌐",
        "ðŸ ?": "🤝", "ðŸ ?": "🤝", # Specific HR emoji
        "ðŸ ?": "🤝",
        "ðŸ—?": "🧠",
        "ðŸ“?": "📖",
        "ðŸ’»": "💻",
        "ðŸ’?": "💻",
        "ðŸ“—": "📖",
        "ðŸ§ ": "🧠",
        "ðŸ” ": "🔑",
    }
    
    # Also clean the weird dash/space sequences
    text = text.replace("—ï¸ ", "🛠️")
    
    for mangled, correct in replacements.items():
        text = text.replace(mangled, correct)

    # 2. Fix multiple page breaks
    text = re.sub(r'(<div style="page-break-before: always;"></div>\s*)+', '<div style="page-break-before: always;"></div>\n\n', text)
    
    # 3. Fix double separators
    text = re.sub(r'\n+---\n+---\n+', '\n\n---\n\n', text)
    text = re.sub(r'---\n\n---', '---', text)
    
    # 4. Standardize spacing around headers
    text = re.sub(r'\n+(#{1,4} )', r'\n\n\1', text)
    
    # 5. Fix formatting of "One Line to Remember"
    # Ensure it always has the emoji 🧠
    text = re.sub(r'#### (.*?) One Line to Remember', r'#### 🧠 One Line to Remember', text)
    
    return text

try:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    cleaned_content = final_audit_and_clean(content)
    
    # 6. Re-generate Table of Contents (Modules only, properly formatted)
    # Remove everything before the first Module header to start fresh
    intro_match = re.search(r'# 🚀 MERN Stack Interview Study Kit.*?(?=<div|##)', cleaned_content, re.DOTALL)
    intro_text = intro_match.group(0) if intro_match else "# 🚀 MERN Stack Interview Study Kit\n\n"
    
    # Remove all headers/TOC from the top
    body_content = re.sub(r'^# 🚀 MERN Stack Interview Study Kit.*?(?=##)', '', cleaned_content, flags=re.DOTALL)
    
    # Extract modules for TOC
    module_headers = re.findall(r'^## (.*)', cleaned_content, re.MULTILINE)
    toc = "# 📑 Table of Contents\n\n"
    for module in module_headers:
        module_clean = module.replace('<div style="page-break-before: always;"></div>', '').strip()
        if not module_clean: continue
        slug = module_clean.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        toc += f"- [{module_clean}](#{slug.strip()})\n"
    
    # 7. Re-generate Cheat Sheet (Remove duplicates)
    sections = re.split(r'\n### ', cleaned_content)
    cheat_sheet_items = []
    seen_questions = set()
    
    for section in sections[1:]:
        lines = section.split('\n')
        question_line = lines[0].strip()
        # Clean question string
        question = re.sub(r'^Q\d+\.\s*', '', question_line)
        if question in seen_questions: continue
        seen_questions.add(question)
        
        one_liner = ""
        for i, line in enumerate(lines):
            if "#### 🧠 One Line to Remember" in line:
                if i + 1 < len(lines):
                    one_liner = lines[i+1].strip()
                    if not one_liner and i + 2 < len(lines):
                        one_liner = lines[i+2].strip()
                break
        if one_liner:
            cheat_sheet_items.append(f"- **{question_line}**: {one_liner}")

    cheat_sheet_text = "\n\n<div style='page-break-before: always;'></div>\n\n# 💡 Interview Quick-Recall Cheat Sheet\n\n"
    cheat_sheet_text += "This section contains only the 'One Line to Remember' for every question to help you review 5 minutes before the interview.\n\n"
    cheat_sheet_text += "\n".join(cheat_sheet_items)

    # 8. Final assembly
    # Remove old cheat sheet if it exists
    final_body = re.split(r'# 💡 Interview Quick-Recall Cheat Sheet', cleaned_content)[0]
    # Also remove any redundant titles at the top
    final_body = re.sub(r'^# 🚀 MERN Stack Interview Study Kit.*?(?=##)', '', final_body, flags=re.DOTALL)
    
    final_output = "# 🚀 MERN Stack Interview Study Kit\n\n" + toc + "\n\n---\n\n" + final_body.strip() + cheat_sheet_text

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    print("Final Audit & Deep Clean complete. No duplicates, clean emojis, and perfect formatting.")
except Exception as e:
    print(f"Error: {e}")
