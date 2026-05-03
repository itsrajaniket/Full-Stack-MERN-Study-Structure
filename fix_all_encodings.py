import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

# Mapping of mangled CP1252 sequences back to UTF-8 emojis
encoding_fixes = {
    "ðŸ”‘": "🔑",
    "ðŸ“–": "📖",
    "ðŸ’»": "💻",
    "ðŸ§ ": "🧠",
    "âœ…": "✅",
    "ðŸŒ": "🌐",
    "ðŸŒƒ": "🍃",
    "ðŸ”": "🔐",
    "ðŸ›": "🛠️",
    "ðŸ¤": "🤝",
    "ðŸ’¡": "💡",
    "ðŸš€": "🚀",
    "ðŸ”¥": "🔥",
    "ðŸ“¦": "📦",
    "ðŸ": "🛠️", # Duplicate for safety
}

try:
    # Read as bytes to handle potential encoding mix
    with open(file_path, 'rb') as f:
        content_bytes = f.read()
    
    # Try to decode as UTF-8 first
    try:
        content = content_bytes.decode('utf-8')
    except UnicodeDecodeError:
        # If it fails, it might be CP1252 or a mix
        content = content_bytes.decode('cp1252', errors='replace')

    # Apply fixes
    for mangled, correct in encoding_fixes.items():
        content = content.replace(mangled, correct)

    # Write back as clean UTF-8
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Full file encoding fix applied.")
except Exception as e:
    print(f"Error: {e}")
