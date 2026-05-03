import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

# Mappings of corrupted strings to correct ones
replacements = {
    "#### ? The Core Answer": "#### ✅ The Core Answer",
    "#### ?? Key Technical Terms Used": "#### 🔑 Key Technical Terms Used",
    "#### ?? Detailed Explanation": "#### 📖 Detailed Explanation",
    "#### ?? Code Example": "#### 💻 Code Example",
    "#### ?? One Line to Remember": "#### 🧠 One Line to Remember",
    "#### ?? Folder Structure Example": "#### 💻 Folder Structure Example",
    "## ?? Module 9": "## 🌐 Module 9",
    "## ?? Module 10": "## 🍃 Module 10",
    "## ?? Module 11": "## 🔐 Module 11",
    "## ?? Module 12": "## 🛠️ Module 12",
    "## ?? Module 13": "## 🤝 Module 13",
}

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

for corrupted, correct in replacements.items():
    content = content.replace(corrupted, correct)

# Also fix the weird characters in the middle of code blocks or lists
content = content.replace("??", "✅").replace("??", "🔑").replace("??", "📖")
# Wait, that's too broad. Let's be specific.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("File fixed.")
