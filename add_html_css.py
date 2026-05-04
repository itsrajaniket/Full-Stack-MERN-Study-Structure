import re
import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

html_css_content = """
<div style="page-break-before: always;"></div>

## 🎨 Module 0: HTML & CSS Fundamentals

### Q1. What is Semantic HTML and why is it important?

---

#### ✅ The Core Answer
Semantic HTML uses tags that describe their meaning to both the browser and the developer (e.g., `<header>`, `<main>`, `<footer>`, `<article>`). It is important because it improves **Accessibility** (for screen readers), **SEO** (search engines understand content structure), and **Code Readability**.

---

#### 🧠 One Line to Remember
Semantic tags tell the browser **what** the content is, not just how it should look.

---

### Q2. What is the difference between Block, Inline, and Inline-Block elements?

---

#### ✅ The Core Answer
*   **Block**: Starts on a new line and takes up the full width available (e.g., `<div>`, `<h1>`, `<p>`).
*   **Inline**: Does not start on a new line and only takes as much width as necessary (e.g., `<span>`, `<a>`, `<strong>`). You cannot set width/height on them.
*   **Inline-Block**: Behaves like an inline element but allows you to set width and height.

---

#### 🧠 One Line to Remember
Blocks take the whole row; Inlines stay in the flow; Inline-blocks are hybrid.

---

### Q3. Explain the CSS Box Model.

---

#### ✅ The Core Answer
Every element is a rectangular box. The Box Model consists of:
1.  **Content**: The actual text or image.
2.  **Padding**: Space between content and border (inside).
3.  **Border**: Line surrounding the padding.
4.  **Margin**: Space outside the border (between elements).
By default, `box-sizing: content-box` adds padding/border to the width. `border-box` keeps the width fixed.

---

#### 🧠 One Line to Remember
Margin is outside, Border is the line, Padding is inside, and Content is the heart.

---

### Q4. What is the difference between `px`, `em`, and `rem`?

---

#### ✅ The Core Answer
*   **px (Pixels)**: Absolute units; fixed size that doesn't change.
*   **em**: Relative to the font-size of its **parent** element.
*   **rem (Root em)**: Relative to the font-size of the **root** (`<html>`) element (usually 16px).
Using `rem` is best practice for accessibility and responsive scaling.

---

#### 🧠 One Line to Remember
`px` is fixed; `em` is relative to parent; `rem` is relative to the root font size.

---

### Q5. What are the different types of CSS Positioning?

---

#### ✅ The Core Answer
*   **Static**: Default; follows normal document flow.
*   **Relative**: Positioned relative to its normal spot (without affecting others).
*   **Absolute**: Positioned relative to the nearest **non-static** parent.
*   **Fixed**: Positioned relative to the **browser window** (stays while scrolling).
*   **Sticky**: Toggles between relative and fixed based on scroll position.

---

#### 🧠 One Line to Remember
Positioning controls where an element sits relative to itself, its parent, or the screen.

---

### Q6. How do you center a `div` horizontally and vertically?

---

#### ✅ The Core Answer
The modern and easiest way is using **Flexbox**:
```css
.parent {
  display: flex;
  justify-content: center; /* Horizontal */
  align-items: center;     /* Vertical */
  height: 100vh;           /* Parent must have height */
}
```
Alternatively, using **Grid**: `display: grid; place-items: center;`.

---

#### 🧠 One Line to Remember
Flexbox is the most reliable way to center elements in modern web development.

---

### Q7. What is the difference between Flexbox and CSS Grid?

---

#### ✅ The Core Answer
*   **Flexbox**: One-dimensional (handles either rows **or** columns). Best for components and small layouts.
*   **Grid**: Two-dimensional (handles rows **and** columns at once). Best for full-page layouts and complex alignments.

---

#### 🧠 One Line to Remember
Flexbox is for 1D alignment; Grid is for 2D layout.

---

### Q8. What is CSS Specificity and how is it calculated?

---

#### ✅ The Core Answer
Specificity determines which CSS rule wins when multiple rules apply to the same element.
The Hierarchy:
1.  **Inline styles**: (e.g., `style="..."`) - Highest weight.
2.  **IDs**: (e.g., `#header`).
3.  **Classes, Attributes, Pseudo-classes**: (e.g., `.btn`, `[type="text"]`).
4.  **Elements and Pseudo-elements**: (e.g., `div`, `p`).
`!important` overrides everything but should be avoided.

---

#### 🧠 One Line to Remember
Specificity is a points system: IDs > Classes > Tags.

---

### Q9. What is the difference between `display: none` and `visibility: hidden`?

---

#### ✅ The Core Answer
*   **display: none**: Removes the element from the document flow. It takes up **zero space** (like it's not there).
*   **visibility: hidden**: Hides the element but it **still takes up space** in the layout (like an invisible box).

---

#### 🧠 One Line to Remember
`display: none` kills the space; `visibility: hidden` keeps the space.

---

### Q10. How do Media Queries work for responsive design?

---

#### ✅ The Core Answer
Media queries allow you to apply CSS styles based on device characteristics like width, height, or orientation.
```css
@media (max-width: 768px) {
  /* Styles for mobile/tablets */
  .container { flex-direction: column; }
}
```
This is the core of **Responsive Web Design**.

---

#### 🧠 One Line to Remember
Media queries are "IF" statements for CSS that trigger styles based on screen size.

---
"""

def process_file():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert Module 0 before Module 1
    # Find the end of TOC or the first ## Module 1
    split_point = content.find("##")
    if split_point == -1: split_point = 0
    
    # We want to insert it after the TOC and before the first Module
    # The first ## usually starts Module 1
    new_content = content[:split_point] + html_css_content + "\n" + content[split_point:]

    # Now re-generate TOC and Cheat Sheet using the logic from our previous script
    # This ensures everything stays synced
    
    # Clean up mangled characters (Emoji mojibake)
    replacements = {
        "—ï¸ ": "🛠️",
        "ðŸ”‘": "🔑", "ðŸ“–": "📖", "ðŸ’»": "💻", "ðŸ§ ": "🧠", "âœ…": "✅",
        "ðŸŒ ": "🌐", "ðŸŒƒ": "🍃", "ðŸ”": "🔐", "ðŸ›": "🛠️", "ðŸ¤": "🤝",
        "ðŸ’¡": "💡", "ðŸš€": "🚀", "ðŸ”¥": "🔥", "ðŸ“¦": "📦", "ðŸŒ ": "🌐",
    }
    for mangled, correct in replacements.items():
        new_content = new_content.replace(mangled, correct)

    # Re-generate TOC
    module_headers = re.findall(r'^## (.*)', new_content, re.MULTILINE)
    toc = "# 📑 Table of Contents\n\n"
    for module in module_headers:
        module_clean = module.replace('<div style="page-break-before: always;"></div>', '').strip()
        if not module_clean: continue
        slug = module_clean.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'\s+', '-', slug)
        toc += f"- [{module_clean}](#{slug.strip()})\n"

    # Re-generate Cheat Sheet
    sections = re.split(r'\n### ', new_content)
    cheat_sheet_items = []
    seen_questions = set()
    for section in sections[1:]:
        lines = section.split('\n')
        question_line = lines[0].strip()
        if not question_line: continue
        question = re.sub(r'^Q\d+\.\s*', '', question_line)
        if question in seen_questions: continue
        seen_questions.add(question)
        one_liner = ""
        for i, line in enumerate(lines):
            if "#### 🧠 One Line to Remember" in line or "#### 🧠 One Line to Remember" in line:
                if i + 1 < len(lines):
                    one_liner = lines[i+1].strip()
                    if not one_liner and i + 2 < len(lines):
                        one_liner = lines[i+2].strip()
                break
        if one_liner:
            cheat_sheet_items.append(f"- **{question_line}**: {one_liner}")

    cheat_sheet_text = "\n\n<div style='page-break-before: always;'></div>\n\n# 💡 Interview Quick-Recall Cheat Sheet\n\n"
    cheat_sheet_text += "This section contains only the 'One Line to Remember' for every question to help you review 5 minutes before the interview.\n\n"
    cheat_sheet_text += "\n".join(cheat_sheet_items)

    # Assemble final output
    # Remove old TOC and Cheat Sheet
    final_body = re.split(r'# 📑 Table of Contents', new_content)[-1]
    final_body = re.split(r'# 💡 Interview Quick-Recall Cheat Sheet', final_body)[0]
    
    # Remove the separators that might have been at the top of final_body
    final_body = re.sub(r'^.*?(?=##)', '', final_body, flags=re.DOTALL)
    
    final_output = "# 🚀 MERN Stack Interview Study Kit\n\n" + toc + "\n\n---\n\n" + final_body.strip() + cheat_sheet_text

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_output)
    
    print("Module 0 (HTML/CSS) added. TOC and Cheat Sheet updated.")

process_file()
