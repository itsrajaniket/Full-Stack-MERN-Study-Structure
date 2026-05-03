import re
import os

filepath = r"C:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Kit_By_(RajAniket.com).md"
react_scratch = r"c:\Users\ANIKET\Desktop\MERN QNA\react_section_scratch.md" # Note: This has my latest 31-q assembly

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(react_scratch, 'r', encoding='utf-8') as f:
    react_content = f.read()

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
    "## Next.js (Full-Stack React Framework)",
    "## CRUD Operations (Data Manipulation)",
    "## SQL Deep Dive (Relational Mastery)"
]

page_break = '<div style="page-break-after: always;"></div>\n\n'

# Track if we are inside the React section to replace it
in_react_section = False
react_replaced = False

for line in lines:
    clean_line = line.strip()
    
    # Page Break Logic
    if clean_line in major_chapters or clean_line in sub_modules:
        # Don't add page break before the very first header if it's right after TOC
        if clean_line != "# 1. 🌐 Web Development Fundamentals":
            new_lines.append(page_break)

    # React Section Replacement Logic
    if clean_line == "# 4. ⚛️ Frontend Mastery":
        in_react_section = True
        new_lines.append(line)
        new_lines.append(react_content)
        new_lines.append("\n\n")
        react_replaced = True
        continue
    
    if in_react_section:
        if clean_line == "## Next.js (Full-Stack React Framework)":
            in_react_section = False
            # Fall through to add Next.js header
        else:
            continue

    # Standardize Question Headers
    # Pattern: **Q1. or **Q1: or Q1. at start of line
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

print("Done! File standardized and React section updated.")
