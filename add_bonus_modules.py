import os
import re

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

new_sections = """
---

<div style="page-break-before: always;"></div>

## 🏗️ Module 14: The "STAR" Project Showcase

### Q1. How should I describe my MERN project in an interview?

---

#### ✅ The Core Answer
Use the **STAR Method**:
1.  **S (Situation)**: What was the project about? (e.g., "I built an E-commerce platform for small businesses.")
2.  **T (Task)**: What problem were you solving? (e.g., "I needed to handle real-time inventory and secure payments.")
3.  **A (Action)**: What exactly did YOU do? (e.g., "I implemented JWT for auth and Redux for the cart.")
4.  **R (Result)**: What was the outcome? (e.g., "The app handles 50+ concurrent users with sub-second response times.")

---

#### 🧠 One Line to Remember
Don't just say what you built; explain the **Problem** you solved and the **Impact** you made.

---

### Q2. What are the "Red Flags" when explaining a project?

---

#### ✅ The Core Answer
*   **"I followed a tutorial"**: Never say this. Say "I used [Tutorial Name] as a reference but added [Feature X] and [Feature Y] myself."
*   **"I don't know why I used MongoDB"**: Always have a reason (e.g., "I chose MongoDB for its flexible schema to handle diverse product categories").
*   **Vague Answers**: "I worked on the backend." (Bad) vs. "I designed 12 RESTful endpoints and optimized DB queries." (Good).

---

#### 🧠 One Line to Remember
Always provide a technical "Why" for every technology choice you made.

---

<div style="page-break-before: always;"></div>

## 🧩 Module 15: Tricky Code Snippets (Mental Models)

### Q1. What is the output of: `console.log(0.1 + 0.2 === 0.3)`?

---

#### ✅ The Core Answer
The output is **`false`**.
In JavaScript (and most languages), floating-point numbers are handled using the IEEE 754 standard. `0.1 + 0.2` actually equals `0.30000000000000004`. 

---

#### 🧠 One Line to Remember
Floating point math in JS isn't perfect; use `Math.round()` or libraries for money/precise math.

---

### Q2. What is the output of: `console.log(typeof NaN)`?

---

#### ✅ The Core Answer
The output is **`"number"`**.
Even though `NaN` stands for "Not a Number," it is technically a numeric data type in the IEEE 754 spec. It represents a value that is undefined or unrepresentable (like `0/0`).

---

#### 🧠 One Line to Remember
NaN is a "number" that isn't a number. Use `Number.isNaN()` to check for it.

---

### Q3. Explain the "Temporary Dead Zone" (TDZ).

---

#### ✅ The Core Answer
The TDZ is the period between the start of a block and the point where a variable is declared using `let` or `const`. If you try to access the variable before its declaration, you get a **ReferenceError**. This is different from `var`, which would give `undefined`.

---

#### 🧠 One Line to Remember
TDZ is the "danger zone" where `let` and `const` variables exist but cannot be touched yet.

---

<div style="page-break-before: always;"></div>

## 🗺️ Module 16: The MERN Developer Roadmap (Post-Interview)

### Q1. What should I learn AFTER I get my first MERN job?

---

#### ✅ The Core Answer
1.  **TypeScript**: 90% of professional MERN teams use TS for type safety.
2.  **Next.js**: The industry standard for production React apps (SSR/SSG).
3.  **Docker**: Learning how to "containerize" your MERN app.
4.  **Cloud (AWS/Azure)**: Understanding where the "N" (Node) actually lives in production.

---

#### 🧠 One Line to Remember
Transition from a MERN developer to a **Full-Stack Engineer** by learning TypeScript and Cloud.

---
"""

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert before the Cheat Sheet
    if "# 💡 Interview Quick-Recall Cheat Sheet" in content:
        content = content.replace("# 💡 Interview Quick-Recall Cheat Sheet", new_sections + "\n\n# 💡 Interview Quick-Recall Cheat Sheet")
    else:
        content += new_sections

    # Update TOC
    toc_match = re.search(r'# 📑 Table of Contents\n\n(.*?)\n---', content, re.DOTALL)
    if toc_match:
        old_toc = toc_match.group(1)
        new_toc_entries = "- [Module 14: The \"STAR\" Project Showcase](#module-14-the-star-project-showcase)\n"
        new_toc_entries += "- [Module 15: Tricky Code Snippets (Mental Models)](#module-15-tricky-code-snippets-mental-models)\n"
        new_toc_entries += "- [Module 16: The MERN Developer Roadmap (Post-Interview)](#module-16-the-mern-developer-roadmap-post-interview)\n"
        content = content.replace(old_toc, old_toc.strip() + "\n" + new_toc_entries)

    # Update Cheat Sheet (Need to run the polish logic again or just manually append for these new ones)
    # Actually, I'll just run the polish script again after this to update everything properly.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Bonus modules (STAR Method, Tricky Snippets, Roadmap) added.")
except Exception as e:
    print(f"Error: {e}")
