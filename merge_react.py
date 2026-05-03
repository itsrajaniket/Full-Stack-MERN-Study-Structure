import re
import os

master_file = r"C:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Kit_By_(RajAniket.com).md"
react_module = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Study_Structure\02_Frontend_Development_React_Next.js_ShadCN\01_Reactjs\01_Reactjs.md"
extra_questions = r"c:\Users\ANIKET\Desktop\MERN QNA\react_extra_questions.md"
scratch_header = r"c:\Users\ANIKET\Desktop\MERN QNA\react_section_scratch.md"

# 1. Read Q1-Q26 from react_module
with open(react_module, 'r', encoding='utf-8') as f:
    module_lines = f.readlines()
    # Find start of Q1 (line 392) to end of Q26 (before line 1854)
    react_q_content = "".join(module_lines[391:1853])

# 2. Read Extra Questions
with open(extra_questions, 'r', encoding='utf-8') as f:
    extra_content = f.read()

# 3. Read Header/TOC from scratch
with open(scratch_header, 'r', encoding='utf-8') as f:
    scratch_lines = f.readlines()
    # Take header up to line 106 (start of questions)
    react_header = "".join(scratch_lines[:106])

# 4. Combine
full_react_section = react_header + "\n\n" + react_q_content + "\n\n" + extra_content

# 5. Replace in Master File
with open(master_file, 'r', encoding='utf-8') as f:
    master_content = f.read()

# Pattern to find the section to replace
# We want to replace from "# 4. ⚛️ Frontend Mastery" until "## Next.js (Full-Stack React Framework)"
start_marker = "# 4. ⚛️ Frontend Mastery"
end_marker = "## Next.js (Full-Stack React Framework)"

start_idx = master_content.find(start_marker)
end_idx = master_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_master = master_content[:start_idx] + start_marker + "\n" + full_react_section + "\n\n" + master_content[end_idx:]
    
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(new_master)
    print("React section fully updated with 31 questions!")
else:
    print(f"Error: Markers not found. Start: {start_idx}, End: {end_idx}")
