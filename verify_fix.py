import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

encoding_fixes = {
    "ðŸ”‘": "🔑",
    "ðŸ“–": "📖",
    "ðŸ’»": "💻",
    "ðŸ§ ": "🧠",
}

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

for mangled, correct in encoding_fixes.items():
    m_count = content.count(mangled)
    c_count = content.count(correct)
    print(f"Mangled '{mangled}': {m_count}, Correct '{correct}': {c_count}")
