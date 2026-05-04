import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

def super_sanitize(text):
    # 1. Fix the Module Headers and TOC entries
    # Replace anything that looks like mangled emojis in front of Modules
    text = re.sub(r'\[.*?Module 0:', '[🎨 Module 0:', text)
    text = re.sub(r'## .*?Module 0:', '## 🎨 Module 0:', text)
    
    # Modules 1, 2, 3, 4, 6, 7, 12 use 🛠️
    for i in [1, 2, 3, 4, 6, 7, 12]:
        text = re.sub(fr'\[.*?Module {i}:', f'[🛠️ Module {i}:', text)
        text = re.sub(fr'## .*?Module {i}:', f'## 🛠️ Module {i}:', text)
    
    # Module 5: 📦
    text = re.sub(r'\[.*?Module 5:', '[📦 Module 5:', text)
    text = re.sub(r'## .*?Module 5:', '## 📦 Module 5:', text)
    
    # Module 8: 🚀
    text = re.sub(r'\[.*?Module 8:', '[🚀 Module 8:', text)
    text = re.sub(r'## .*?Module 8:', '## 🚀 Module 8:', text)
    
    # Module 9: 🌐
    text = re.sub(r'\[.*?Module 9:', '[🌐 Module 9:', text)
    text = re.sub(r'## .*?Module 9:', '## 🌐 Module 9:', text)
    
    # Module 10: 🍃
    text = re.sub(r'\[.*?Module 10:', '[🍃 Module 10:', text)
    text = re.sub(r'## .*?Module 10:', '## 🍃 Module 10:', text)
    
    # Module 11: 🔐
    text = re.sub(r'\[.*?Module 11:', '[🔐 Module 11:', text)
    text = re.sub(r'## .*?Module 11:', '## 🔐 Module 11:', text)
    
    # Module 13: 🤝
    text = re.sub(r'\[.*?Module 13:', '[🤝 Module 13:', text)
    text = re.sub(r'## .*?Module 13:', '## 🤝 Module 13:', text)
    
    # Module 14: 🏗️
    text = re.sub(r'\[.*?Module 14:', '[🏗️ Module 14:', text)
    text = re.sub(r'## .*?Module 14:', '## 🏗️ Module 14:', text)
    
    # Module 15: 🧩
    text = re.sub(r'\[.*?Module 15:', '[🧩 Module 15:', text)
    text = re.sub(r'## .*?Module 15:', '## 🧩 Module 15:', text)
    
    # Module 16: 🗺️
    text = re.sub(r'\[.*?Module 16:', '[🗺️ Module 16:', text)
    text = re.sub(r'## .*?Module 16:', '## 🗺️ Module 16:', text)

    # 2. Fix Section Headers inside modules
    text = text.replace("#### o. The Core Answer", "#### ✅ The Core Answer")
    text = text.replace("#### dY  One Line to Remember", "#### 🧠 One Line to Remember")
    text = text.replace("#### 🧠 One Line to Remember", "#### 🧠 One Line to Remember") # Double check
    
    # 3. Fix Title and TOC Header
    text = re.sub(r'^# .*?MERN Stack Interview Study Kit', '# 🚀 MERN Stack Interview Study Kit', text, flags=re.MULTILINE)
    text = re.sub(r'^# .*?Table of Contents', '# 📑 Table of Contents', text, flags=re.MULTILINE)
    text = re.sub(r'^# .*?Interview Quick-Recall Cheat Sheet', '# 💡 Interview Quick-Recall Cheat Sheet', text, flags=re.MULTILINE)

    # 4. Global replacement for any remaining mangled strings
    mangled_patterns = {
        "—ï¸ ": "🛠️",
        "????-,?": "🛠️",
        "o.": "✅",
        "dY ": "🧠",
        "dYs?": "🚀",
        "dY\"": "📦",
        "dY`\"": "📑",
        "dYZ\"": "🎨",
    }
    for mangled, correct in mangled_patterns.items():
        text = text.replace(mangled, correct)

    return text

try:
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    sanitized_content = super_sanitize(content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(sanitized_content)
    
    print("Super Sanitize Complete. All symbols should now be seeing properly.")
except Exception as e:
    print(f"Error: {e}")
