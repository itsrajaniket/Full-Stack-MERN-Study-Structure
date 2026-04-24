# CSS (Styling & Layouts)

## 📚 Curriculum Checklist
- [x] Selectors & Specificity
- [x] Box Model (Margin, Padding, Border)
- [x] Display (Block, Inline, Inline-block, Flex, Grid)
- [x] Positioning (Relative, Absolute, Fixed, Sticky)
- [x] Media Queries (Responsive Design)
- [x] Transitions & Animations

## 📝 Detailed Notes

### 1. Selectors & Specificity
CSS selectors are used to "find" (or select) the HTML elements you want to style.
- **Universal Selector**: `*` (selects everything).
- **Element Selector**: `p`, `h1`, `div`.
- **Class Selector**: `.className`.
- **ID Selector**: `#idName`.
- **Attribute Selector**: `input[type="text"]`.
- **Specificity Calculation**: `Inline (1000) > ID (100) > Class/Attribute (10) > Element (1)`.

### 2. The Box Model
Every element is considered a box.
- **Content**: Where text/images appear.
- **Padding**: Clears an area around the content. It is inside the border.
- **Border**: A border that goes around the padding and content.
- **Margin**: Clears an area outside the border.
- **`box-sizing: border-box`**: Total width = width + padding + border.

### 3. Display Property
- **Block**: Takes full width, starts on a new line (e.g., `<div>`, `<p>`).
- **Inline**: Takes only necessary width, no new line (e.g., `<span>`, `<a>`).
- **Inline-Block**: Like inline, but you can set width/height.
- **Flex**: Flexible box layout (1D).
- **Grid**: Grid layout (2D).
- **None**: Hides the element completely.

### 4. Positioning
- **Static**: Default; follows normal document flow.
- **Relative**: Relative to its original position.
- **Absolute**: Relative to its nearest *positioned* ancestor.
- **Fixed**: Relative to the browser window.
- **Sticky**: Toggles between relative and fixed based on scroll.

### 5. Flexbox (1D Layout)
- `flex-direction`: row, column.
- `justify-content`: flex-start, center, flex-end, space-between, space-around.
- `align-items`: flex-start, center, flex-end, stretch.
- `flex-grow`, `flex-shrink`, `flex-basis`.

### 6. CSS Grid (2D Layout)
- `grid-template-columns`: e.g., `repeat(3, 1fr)`.
- `grid-template-rows`.
- `gap`: Space between grid items.
- `grid-area`: Naming and placing items.

### 7. Flexbox vs. Grid: When to use what?
| Feature | Flexbox (1D) | CSS Grid (2D) |
| :--- | :--- | :--- |
| **Axis** | Either Row OR Column. | Row AND Column simultaneously. |
| **Alignment** | Content-first (item size determines layout). | Layout-first (grid cells determine item size). |
| **Complexity** | Best for small components (Navbars, Buttons). | Best for page layouts and complex dashboards. |
| **Gaps** | `gap` (recent support), otherwise margins. | Native `gap` support since inception. |

### 8. Responsive Design & Media Queries
```css
/* Tablet and Mobile styles */
@media (max-width: 768px) {
    .container { flex-direction: column; }
}
```
- **Mobile First**: Writing styles for small screens first, then adding media queries for larger screens.

### 9. Transitions & Animations
- **Transitions**: Smoothly changing a property (e.g., `transition: background 0.3s ease;`).
- **Keyframe Animations**:
```css
@keyframes slideIn {
    from { transform: translateX(-100%); }
    to { transform: translateX(0); }
}
.box { animation: slideIn 1s forwards; }
```

---

## 🎓 Important Interview Questions

### Q1: What is the difference between `reset.css` and `normalize.css`?
- **Reset**: Removes all default browser styling (starts from a blank slate).
- **Normalize**: Preserves useful defaults and fixes common browser inconsistencies.

### Q2: Explain the `z-index` and Stacking Context.
`z-index` controls the vertical stacking order of elements. It only works on positioned elements (`relative`, `absolute`, `fixed`, `sticky`). A new stacking context is created by opacity < 1, transforms, or `z-index` values.

### Q3: How do you center a `div` both horizontally and vertically?
- **Flexbox**:
  ```css
  .parent { display: flex; justify-content: center; align-items: center; height: 100vh; }
  ```
- **Grid**:
  ```css
  .parent { display: grid; place-items: center; height: 100vh; }
  ```
- **Absolute Position**:
  ```css
  .child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  ```

### Q4: What are CSS Variables (Custom Properties)?
They allow you to store values (like colors or spacing) in one place and reuse them throughout the stylesheet using the `var()` function.
```css
:root { --primary-color: #3498db; }
.btn { background-color: var(--primary-color); }
```

### Q5: What is the difference between `em` and `rem` units?
- **em**: Relative to the font-size of its **parent**.
- **rem**: Relative to the font-size of the **root** (`<html>`) element. (Recommended for accessibility).

### Q6: Explain "Pseudo-classes" vs "Pseudo-elements".
- **Pseudo-class**: Targets a specific *state* of an element (e.g., `:hover`, `:nth-child(2)`, `:focus`).
- **Pseudo-element**: Targets a specific *part* of an element (e.g., `::before`, `::after`, `::first-letter`).


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: HTML](../../MERN_Study_Structure/01_Web_Development_Fundamentals/01_HTML/01_HTML.md) | [🏠 Home](../../README.md) | [Next: Bootstrap ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/03_Bootstrap/03_Bootstrap.md)

---

## 🎓 Important Interview Questions

### Q1: What is the difference between `reset.css` and `normalize.css`?
- **Reset**: Removes all default browser styling (starts from a blank slate).
- **Normalize**: Preserves useful defaults and fixes common browser inconsistencies.

### Q2: Explain the `z-index` and Stacking Context.
`z-index` controls the vertical stacking order of elements. It only works on positioned elements (`relative`, `absolute`, `fixed`, `sticky`). A new stacking context is created by opacity < 1, transforms, or `z-index` values.

### Q3: How do you center a `div` both horizontally and vertically?
- **Flexbox**:
  ```css
  .parent { display: flex; justify-content: center; align-items: center; height: 100vh; }
  ```
- **Grid**:
  ```css
  .parent { display: grid; place-items: center; height: 100vh; }
  ```
- **Absolute Position**:
  ```css
  .child { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }
  ```

### Q4: What are CSS Variables (Custom Properties)?
They allow you to store values (like colors or spacing) in one place and reuse them throughout the stylesheet using the `var()` function.
```css
:root { --primary-color: #3498db; }
.btn { background-color: var(--primary-color); }
```

### Q5: What is the difference between `em` and `rem` units?
- **em**: Relative to the font-size of its **parent**.
- **rem**: Relative to the font-size of the **root** (`<html>`) element. (Recommended for accessibility).

### Q6: Explain "Pseudo-classes" vs "Pseudo-elements".
- **Pseudo-class**: Targets a specific *state* of an element (e.g., `:hover`, `:nth-child(2)`, `:focus`).
- **Pseudo-element**: Targets a specific *part* of an element (e.g., `::before`, `::after`, `::first-letter`).


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: HTML](../../MERN_Study_Structure/01_Web_Development_Fundamentals/01_HTML/01_HTML.md) | [🏠 Home](../../README.md) | [Next: Bootstrap ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/03_Bootstrap/03_Bootstrap.md)
