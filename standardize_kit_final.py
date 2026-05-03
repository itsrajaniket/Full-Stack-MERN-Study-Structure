import re
import os

filepath = r"C:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Kit_By_(RajAniket.com).md"

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []

# Major chapter headers for page breaks
major_chapters = [
    "# 1. 🌐 Web Development Fundamentals",
    "# 2. ⚙️ Backend Mastery",
    "# 3. 🗄️ Database Systems",
    "# 4. ⚛️ Frontend Mastery",
    "# 5. 🛠️ Operations & Patterns"
]

# Sub-module headers for page breaks
sub_modules = [
    "# HTML (Structure & Semantics)",
    "# CSS (Styling & Layout)",
    "# Javascript (JS)",
    "# Node.js (Runtime Environment)",
    "# Express.js",
    "# Authentication & Authorization",
    "# Advanced Express.js",
    "# NestJS (Enterprise Backend Development)",
    "# Building REST APIs",
    "# Database & ORM",
    "# Authentication & Security",
    "# MongoDB (NoSQL Database)",
    "# PostgreSQL (Relational Database)",
    "# ⚛️ React.js (Vite / Next.js)",
    "## Next.js (Full-Stack React Framework)",
    "## CRUD Operations (Data Manipulation)",
    "## SQL Deep Dive (Relational Mastery)"
]

page_break = '<div style="page-break-after: always;"></div>\n\n'

for line in lines:
    clean_line = line.strip()
    
    # Page Break Logic
    if clean_line in major_chapters or clean_line in sub_modules:
        if clean_line != "# 1. 🌐 Web Development Fundamentals":
            # Avoid duplicate page breaks
            if not (new_lines and new_lines[-1].strip() == '<div style="page-break-after: always;"></div>'):
                new_lines.append(page_break)

    # Standardize Question Headers
    q_match = re.match(r'^(\*\*Q\d+[\.:].+?\*\*)', clean_line)
    if q_match:
        if not line.startswith("###"):
            line = "### " + line.lstrip()
    
    # Fix double ###
    if line.startswith("### ###"):
        line = line.replace("### ###", "###")

    new_lines.append(line)

# Save the result
with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Done! Global formatting standardized.")
