import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

encoding_fixes = {
    "ðŸ”‘": "key",
    "ðŸ“–": "book",
    "ðŸ’»": "laptop",
    "ðŸ§ ": "brain",
    "âœ…": "check",
}

with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

for mangled, label in encoding_fixes.items():
    m_count = content.count(mangled)
    print(f"Mangled '{label}' count: {m_count}")

# Check correct emojis (hardcoded check)
print(f"Correct 'check' count: {content.count('✅')}")
print(f"Correct 'key' count: {content.count('🔑')}")
print(f"Correct 'book' count: {content.count('📖')}")
print(f"Correct 'laptop' count: {content.count('💻')}")
print(f"Correct 'brain' count: {content.count('🧠')}")
