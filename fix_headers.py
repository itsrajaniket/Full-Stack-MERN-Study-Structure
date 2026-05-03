import re
import os

filepath = r"C:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Kit_By_(RajAniket.com).md"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []

# Header to remove
redundant_header = "# ⚛️ React.js (Vite / Next.js)"

for line in lines:
    clean_line = line.strip()
    
    if clean_line == redundant_header:
        # Check if previous line was Frontend Mastery
        if new_lines and "# 4. ⚛️ Frontend Mastery" in new_lines[-1]:
            continue # Skip this redundant header
            
    new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done! Redundant header removed.")
