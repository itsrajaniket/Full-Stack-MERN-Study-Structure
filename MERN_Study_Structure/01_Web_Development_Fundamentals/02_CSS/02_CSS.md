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
## **CSS (Styling & Layouts) — MERN Stack Interview Kit**

---

### **1\. Selectors & Specificity**

---

**Q1. What are CSS selectors and what are the different types?** `[Fresher]`

* Universal selector `*` — selects all elements, lowest specificity  
* Type/Element selector — `div`, `p`, `h1` — selects by tag name  
* Class selector — `.classname` — reusable, most common  
* ID selector — `#idname` — unique per page, high specificity  
* Attribute selector — `[type="text"]`, `[href^="https"]`, `[class*="btn"]`  
* Pseudo-class selector — `:hover`, `:focus`, `:nth-child()`, `:first-child`, `:last-child`, `:not()`  
* Pseudo-element selector — `::before`, `::after`, `::placeholder`, `::first-line`, `::first-letter`  
* Combinator selectors:  
  * Descendant (space) — `div p` selects all `<p>` inside any `<div>`  
  * Child `>` — `div > p` selects direct children only  
  * Adjacent sibling `+` — `h1 + p` selects `<p>` immediately after `<h1>`  
  * General sibling `~` — `h1 ~ p` selects all `<p>` siblings after `<h1>`  
* Grouping selector `,` — apply same styles to multiple selectors

---

**Q2. What is CSS Specificity and how is it calculated?** `[Fresher]`

* Definition — when multiple rules target the same element, specificity decides which one wins  
* Specificity hierarchy from highest to lowest:  
  * Inline styles — `style="..."` → (1,0,0,0)  
  * ID selectors — `#id` → (0,1,0,0)  
  * Class, pseudo-class, attribute selectors → (0,0,1,0)  
  * Type/element selectors, pseudo-elements → (0,0,0,1)  
  * Universal selector `*` → (0,0,0,0)  
* How to calculate specificity of combined selectors — `div.card#header` \= (0,1,1,1)  
* What is `!important` — overrides all specificity, should be avoided  
* When is `!important` acceptable? (utility classes, third-party overrides)  
* What wins if two rules have equal specificity? — the one that appears later in the file (cascade)  
* Difference between specificity and cascade  
* Common interview trap — does `*` have any specificity? No — it's 0,0,0,0

---

**Q3. What are pseudo-classes and pseudo-elements? What is the difference?** `[Fresher]`

* Pseudo-class — targets element in a specific **state** using single colon `:`  
  * `:hover`, `:focus`, `:active`, `:visited`  
  * `:nth-child(n)`, `:nth-of-type(n)`, `:first-child`, `:last-child`  
  * `:checked`, `:disabled`, `:enabled`, `:required`, `:valid`, `:invalid`  
  * `:not(selector)` — negation pseudo-class  
* Pseudo-element — targets a **part** of an element using double colon `::`  
  * `::before`, `::after` — insert content before/after element (requires `content` property)  
  * `::placeholder` — style input placeholder text  
  * `::selection` — style text when user selects/highlights it  
  * `::first-line`, `::first-letter`  
* Single colon vs double colon — historical, browsers still support single colon for pseudo-elements but `::` is correct  
* Common use case — `::before` and `::after` for decorative elements without extra HTML

---

**Q4. What are attribute selectors and when are they useful?** `[1-2 yrs]`

* `[attr]` — element has the attribute (regardless of value)  
* `[attr="value"]` — exact match  
* `[attr^="value"]` — starts with value  
* `[attr$="value"]` — ends with value  
* `[attr*="value"]` — contains value anywhere  
* `[attr~="value"]` — value is one of space-separated words  
* Use cases — styling all external links `a[href^="http"]`, styling required inputs `input[required]`  
* Case-insensitive matching with `i` flag — `[type="text" i]`

---

### **2\. Box Model**

---

**Q5. What is the CSS Box Model and how does it work?** `[Fresher]`

* Every HTML element is a rectangular box  
* Four layers from inside out:  
  * **Content** — actual text/image area, controlled by `width` and `height`  
  * **Padding** — space between content and border, has background color of element  
  * **Border** — surrounds the padding  
  * **Margin** — space outside the border, always transparent  
* How total element width is calculated by default:  
  * Total width \= content width \+ left padding \+ right padding \+ left border \+ right border  
* `outline` vs `border` — outline does not affect layout, border does

---

**Q6. What is the difference between `box-sizing: content-box` and `box-sizing: border-box`?** `[Fresher]`

* `content-box` (default) — `width` applies to content only, padding and border add on top  
* `border-box` — `width` includes padding and border, much more predictable  
* Example — element with `width: 200px`, `padding: 20px`, `border: 2px`:  
  * `content-box` → actual rendered width \= 244px  
  * `border-box` → actual rendered width \= 200px (content shrinks to accommodate)  
* Best practice — apply `*, *::before, *::after { box-sizing: border-box; }` globally  
* Why `border-box` is preferred in modern CSS and frameworks like Bootstrap, Tailwind

---

**Q7. What is margin collapsing and when does it happen?** `[1-2 yrs]`

* When two vertical margins meet, they collapse into a single margin (the larger one wins)  
* Three cases where margin collapsing happens:  
  * Adjacent siblings — bottom margin of element 1 \+ top margin of element 2 \= larger of the two  
  * Parent and first/last child — if no border/padding separates them  
  * Empty blocks — top and bottom margin of empty element collapse  
* Margin collapsing only happens with **vertical** (top/bottom) margins, never horizontal  
* How to prevent margin collapsing:  
  * Add `padding` or `border` to parent  
  * Use `overflow: hidden` or `overflow: auto` on parent  
  * Use flexbox or grid container (collapsing doesn't happen inside flex/grid)  
* Common interview gotcha — why is there extra space at the top of the page? (`<body>` and `<h1>` margin collapsing)

---

**Q8. What is the difference between `margin: auto` and `padding: auto`?** `[Fresher]`

* `margin: auto` — browser calculates equal left and right margins, centers block elements horizontally  
* `padding: auto` — does NOT work, padding does not accept `auto`  
* Why `margin: 0 auto` works for centering — requires element to have a defined `width`  
* `margin: auto` in Flexbox — fills remaining space, used for pushing items to opposite end

---

**Q9. What is the difference between `padding` and `margin`?** `[Fresher]`

* Padding — inside the element, between content and border, inherits background color  
* Margin — outside the element, always transparent, creates space between elements  
* Negative margins — margin can be negative (pulls element), padding cannot be negative  
* Clicking area — padding area is clickable/hoverable, margin is not  
* Shorthand — `margin: top right bottom left` (clockwise), 1/2/3/4 value rules

---

### **3\. Display**

---

**Q10. What are the different values of the `display` property?** `[Fresher]`

* `block` — takes full width, starts on new line, respects width/height  
* `inline` — takes only content width, does not start new line, ignores width/height/top-bottom margin  
* `inline-block` — inline flow but respects width, height, and all margins  
* `none` — removes element from layout entirely (different from `visibility: hidden`)  
* `flex` — activates flexbox layout for children  
* `grid` — activates grid layout for children  
* `inline-flex`, `inline-grid` — flex/grid but the container itself is inline  
* `table`, `table-row`, `table-cell` — legacy, rarely used now  
* `contents` — element itself is not rendered, only its children are

---

**Q11. What is Flexbox and how does it work?** `[Fresher]`

* One-dimensional layout model — arranges items in a row or column  
* `display: flex` on parent (flex container) — children become flex items  
* **Container properties:**  
  * `flex-direction` — `row` (default), `row-reverse`, `column`, `column-reverse`  
  * `flex-wrap` — `nowrap` (default), `wrap`, `wrap-reverse`  
  * `justify-content` — alignment along **main axis** — `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`  
  * `align-items` — alignment along **cross axis** — `stretch` (default), `flex-start`, `flex-end`, `center`, `baseline`  
  * `align-content` — alignment of multiple lines (only when `flex-wrap: wrap`)  
  * `gap` — space between flex items (`row-gap`, `column-gap`)  
* **Item properties:**  
  * `flex-grow` — how much item grows relative to others (default `0`)  
  * `flex-shrink` — how much item shrinks (default `1`)  
  * `flex-basis` — initial size before grow/shrink is applied  
  * `flex` shorthand — `flex: grow shrink basis` (e.g., `flex: 1` \= `flex: 1 1 0`)  
  * `align-self` — override `align-items` for individual item  
  * `order` — change visual order without changing DOM order  
* Main axis vs cross axis — depends on `flex-direction`  
* What does `flex: 1` actually mean? (`flex: 1 1 0%`)  
* Common use case — centering an element perfectly: `display:flex; justify-content:center; align-items:center`

---

**Q12. What is CSS Grid and how is it different from Flexbox?** `[1-2 yrs]`

* Two-dimensional layout model — controls both rows AND columns simultaneously  
* `display: grid` on container  
* **Container properties:**  
  * `grid-template-columns` — defines column sizes (`px`, `fr`, `%`, `auto`, `repeat()`, `minmax()`)  
  * `grid-template-rows` — defines row sizes  
  * `grid-template-areas` — named layout regions  
  * `gap` / `row-gap` / `column-gap` — space between cells  
  * `justify-items` — horizontal alignment of items within their cell  
  * `align-items` — vertical alignment of items within their cell  
  * `justify-content` / `align-content` — alignment of the entire grid within container  
* **Item properties:**  
  * `grid-column: 1 / 3` — span from column line 1 to 3  
  * `grid-row: 1 / 2` — span rows  
  * `grid-column: span 2` — shorthand for spanning 2 columns  
  * `grid-area` — place item in named area  
* `fr` unit — fractional unit, takes remaining space proportionally  
* `repeat(3, 1fr)` — creates 3 equal columns  
* `minmax(200px, 1fr)` — column at least 200px but grows to fill space  
* `auto-fill` vs `auto-fit` in `repeat()` — difference explained  
* **Flexbox vs Grid:**  
  * Flexbox — one-dimensional, content-driven (size based on content)  
  * Grid — two-dimensional, layout-driven (size based on defined grid)  
  * Use Flexbox for components (nav, cards in a row)  
  * Use Grid for page-level layout (header, sidebar, main, footer)  
  * They can and should be combined

---

**Q13. What is the difference between `display: none` and `visibility: hidden`?** `[Fresher]`

* `display: none` — element is completely removed from layout, takes no space, not accessible  
* `visibility: hidden` — element is invisible but still occupies space in layout  
* `opacity: 0` — element is invisible, still occupies space, still interactive (clicks register)  
* All three make element invisible but behave very differently  
* Which one to use for accessible hide? — `display: none` removes from screen readers too; use `visibility: hidden` or specific ARIA techniques for accessible hiding

---

### **4\. Positioning**

---

**Q14. What are the different CSS position values and how do they work?** `[Fresher]`

* `static` (default) — normal document flow, `top/left/right/bottom/z-index` have no effect  
* `relative` — positioned relative to its own normal position, still in document flow, creates new stacking context  
* `absolute` — removed from document flow, positioned relative to nearest **positioned ancestor** (non-static)  
* `fixed` — removed from document flow, positioned relative to **viewport**, stays on screen when scrolling  
* `sticky` — hybrid of relative and fixed; acts relative until scroll threshold, then sticks  
* What is a "positioned ancestor"? — any ancestor with position other than `static`  
* If no positioned ancestor, absolute element positions relative to `<html>`

---

**Q15. What is the difference between `relative` and `absolute` positioning?** `[Fresher]`

* `relative` — element stays in flow, offset is from its own original position, surrounding elements unaffected  
* `absolute` — element leaves flow, surrounding elements fill its space, offset from nearest positioned ancestor  
* Common pattern — parent `position: relative` \+ child `position: absolute` for overlays, tooltips, badges  
* `top: 50%; left: 50%; transform: translate(-50%, -50%)` — centering with absolute positioning explained

---

**Q16. What is the difference between `fixed` and `sticky` positioning?** `[1-2 yrs]`

* `fixed` — always relative to viewport, always visible regardless of scroll, removed from flow  
* `sticky` — stays in normal flow until scroll reaches threshold, then "sticks" at defined offset  
* `sticky` requires a defined `top`, `bottom`, `left`, or `right` value to activate  
* `sticky` is scoped to its parent container — stops sticking when parent scrolls out of view  
* Browser support and common gotcha — `overflow: hidden` on a parent breaks `sticky`  
* Use cases — sticky headers, sticky table headers, sticky sidebar navigation

---

**Q17. What is `z-index` and how does it work?** `[1-2 yrs]`

* Controls stacking order of overlapping elements on the Z axis (toward/away from viewer)  
* Only works on positioned elements (`relative`, `absolute`, `fixed`, `sticky`) — not `static`  
* Higher `z-index` \= appears on top  
* Default `z-index` is `auto` (same as 0 in most cases)  
* **Stacking context** — new stacking context created by:  
  * `position` \+ any `z-index` value other than `auto`  
  * `opacity` less than 1  
  * `transform`, `filter`, `will-change`, `isolation: isolate`  
* Z-index only competes within the same stacking context — common confusion explained  
* `isolation: isolate` — creates new stacking context without any other side effects

---

### **5\. Media Queries**

---

**Q18. What are media queries and how do they enable responsive design?** `[Fresher]`

* `@media` rule — applies CSS only when certain conditions about the device/viewport are true  
* Syntax — `@media (max-width: 768px) { ... }`  
* Media types — `screen`, `print`, `all`  
* Media features — `width`, `min-width`, `max-width`, `height`, `orientation`, `resolution`, `prefers-color-scheme`, `prefers-reduced-motion`, `hover`  
* Logical operators — `and`, `not`, `,` (or)  
* Example — `@media screen and (min-width: 768px) and (max-width: 1024px)`

---

**Q19. What is the difference between mobile-first and desktop-first approach?** `[1-2 yrs]`

* Mobile-first — base styles are for mobile, use `min-width` media queries to add styles for larger screens  
* Desktop-first — base styles are for desktop, use `max-width` media queries to override for smaller screens  
* Why mobile-first is preferred:  
  * Better performance — mobile loads minimal CSS, desktop adds on top  
  * Forces prioritization of essential content  
  * Aligns with Google's mobile-first indexing  
* Common breakpoints (not fixed standards, adapt to content):  
  * 320px — small phones  
  * 480px — large phones  
  * 768px — tablets  
  * 1024px — small laptops  
  * 1280px / 1440px — desktops  
* Tailwind CSS breakpoint system — `sm:`, `md:`, `lg:`, `xl:` — all mobile-first `min-width`

---

**Q20. What is the viewport meta tag and why is it required for responsive design?** `[Fresher]`

* Without it — mobile browsers render page at desktop width (\~980px) and scale down  
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">` — tells browser to match device's actual width  
* `initial-scale=1.0` — no zoom on load  
* `user-scalable=no` — disables user zoom (accessibility concern, avoid this)  
* Without this tag, media queries behave incorrectly on mobile

---

**Q21. What are CSS custom properties (CSS variables) and how do they help with responsive design?** `[1-2 yrs]`

* Declared with `--variable-name: value` inside a selector (usually `:root` for global)  
* Used with `var(--variable-name)` — with optional fallback `var(--color, red)`  
* Scoped — variables declared on an element are available to its descendants  
* Can be changed with media queries — redefine variable value inside `@media` block  
* Can be changed with JavaScript — `element.style.setProperty('--color', 'blue')`  
* Difference from SASS/LESS variables — CSS variables are live in the DOM, SASS variables are compiled away  
* Use case in MERN/React — theming, dark mode toggle

---

### **6\. Transitions & Animations**

---

**Q22. What is the difference between CSS transitions and CSS animations?** `[Fresher]`

* **Transitions** — smooth change from one state to another, triggered by state change (hover, focus, class change)  
  * Properties — `transition-property`, `transition-duration`, `transition-timing-function`, `transition-delay`  
  * Shorthand — `transition: property duration timing delay`  
  * Can only go from A → B (two states)  
  * Require a trigger — cannot run on page load automatically  
* **Animations** — define keyframes, can loop, can auto-play, more control  
  * `@keyframes` — defines animation steps with `from/to` or percentage values  
  * `animation-name`, `animation-duration`, `animation-timing-function`, `animation-delay`  
  * `animation-iteration-count` — number of times (`infinite` for looping)  
  * `animation-direction` — `normal`, `reverse`, `alternate`, `alternate-reverse`  
  * `animation-fill-mode` — `forwards`, `backwards`, `both`, `none` — state of element before/after animation  
  * `animation-play-state` — `running` or `paused`

---

**Q23. What are timing functions and how do they affect animations?** `[1-2 yrs]`

* Controls the speed curve of transition/animation  
* `linear` — constant speed throughout  
* `ease` (default) — slow start, fast middle, slow end  
* `ease-in` — slow start, fast end  
* `ease-out` — fast start, slow end  
* `ease-in-out` — slow start, slow end, fast middle  
* `cubic-bezier(x1, y1, x2, y2)` — custom curve with full control  
* `steps(n, start|end)` — jumpy/frame-by-frame animation (used for sprite animations)  
* Tool to visualize — cubic-bezier.com

---

**Q24. Which CSS properties are best to animate for performance?** `[2-3 yrs]`

* **GPU-accelerated properties (preferred):**  
  * `transform` — `translate`, `scale`, `rotate`, `skew` — no layout recalculation  
  * `opacity` — only affects compositing layer  
* **Expensive properties to animate (avoid):**  
  * `width`, `height`, `margin`, `padding` — trigger layout/reflow  
  * `top`, `left` (with position) — trigger layout  
  * `background-color`, `color` — trigger repaint (not reflow, but still costly)  
* Browser rendering pipeline — Layout → Paint → Composite  
  * Animating `transform` and `opacity` only triggers Composite (cheapest)  
  * Animating layout properties triggers the entire pipeline (slowest)  
* `will-change: transform` — hints browser to promote element to own compositor layer  
  * Use sparingly — overuse wastes memory  
* `requestAnimationFrame` in JS vs CSS animation — when to use which

---

**Q25. What is the `transform` property and what can it do?** `[1-2 yrs]`

* Does not affect surrounding elements or document flow  
* Functions:  
  * `translate(x, y)` / `translateX()` / `translateY()` / `translateZ()` / `translate3d()`  
  * `scale(x, y)` / `scaleX()` / `scaleY()`  
  * `rotate(deg)` / `rotateX()` / `rotateY()` / `rotateZ()`  
  * `skew(x, y)` / `skewX()` / `skewY()`  
  * `matrix()` — combines all transforms in one function (used by animation libraries)  
* `transform-origin` — pivot point for transform (default `50% 50%` center)  
* 3D transforms — `perspective`, `rotateX()`, `rotateY()`, `translateZ()`, `backface-visibility`  
* `translate(-50%, -50%)` trick — centering absolutely positioned elements

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q26. What is the difference between `em`, `rem`, `px`, `%`, `vh`, `vw`?** `[Fresher]`

* `px` — absolute unit, fixed size regardless of parent or settings  
* `em` — relative to the **parent** element's font size (compounds in nested elements)  
* `rem` — relative to the **root** (`<html>`) font size, consistent and predictable  
* `%` — relative to parent element (for width, height, font-size differently)  
* `vh` — 1% of viewport height, `vw` — 1% of viewport width  
* `vmin` / `vmax` — smaller/larger of vh or vw  
* `ch` — width of the `0` character in current font  
* Best practice — use `rem` for font sizes, `px` for borders, `%` / `fr` for layouts  
* Mobile gotcha — `100vh` on mobile includes browser chrome, causes overflow (use `dvh` in modern CSS)

---

**Q27. What is the `overflow` property and what are its values?** `[Fresher]`

* `visible` (default) — content overflows outside element, not clipped  
* `hidden` — overflow is clipped, not scrollable  
* `scroll` — always shows scrollbars even if no overflow  
* `auto` — scrollbars appear only when content overflows  
* `overflow-x` and `overflow-y` — control horizontal and vertical independently  
* Setting `overflow: hidden` on parent creates new block formatting context — fixes margin collapse and float issues  
* Text overflow — `overflow: hidden; white-space: nowrap; text-overflow: ellipsis` — truncate text with `...`

---

**Q28. What is a CSS preprocessor? What is SASS/SCSS?** `[1-2 yrs]`

* Preprocessor — extends CSS with programming features, compiled into plain CSS  
* SASS/SCSS features:  
  * Variables — `$primary-color: #333`  
  * Nesting — write child selectors inside parent  
  * Mixins — reusable style blocks with optional parameters  
  * Extends/Inheritance — `@extend` to share styles  
  * Functions and operators — math operations in CSS  
  * Partials and `@import` / `@use` — split CSS into modules  
* SASS vs SCSS — SCSS uses `{}` and `;` (CSS-compatible syntax), SASS uses indentation  
* In MERN projects — often replaced by CSS Modules, Tailwind, or Styled Components  
* CSS custom properties vs SASS variables — key difference (already covered in Q21)

---

**Q29. What is Tailwind CSS and how does it differ from traditional CSS?** `[1-2 yrs]`

* Utility-first CSS framework — pre-built single-purpose classes applied directly in HTML  
* No custom CSS files needed for most styling  
* Traditional CSS — write semantic class names, define styles in CSS file  
* Tailwind — compose styles using utility classes like `flex`, `mt-4`, `text-center`, `bg-blue-500`  
* Benefits — no naming things, no unused CSS (purged in production), consistent design system  
* Drawbacks — HTML can get verbose, learning curve for utility names  
* JIT (Just-In-Time) compiler — generates only the CSS classes actually used  
* How it integrates in a React/MERN project — `tailwind.config.js`, PostCSS setup  
* `@apply` directive — use Tailwind utilities inside CSS classes

---

**Q30. What is CSS specificity conflict resolution in real projects?** `[2-3 yrs]`

* Common scenario — third-party library styles conflicting with your styles  
* Solutions in order of preference:  
  * Increase specificity of your selector  
  * Use CSS Modules (scoped styles per component)  
  * Use `!important` as last resort  
  * Use `all: revert` or `all: unset` to reset inherited styles  
* CSS Modules in React — `styles.module.css` — class names are locally scoped, auto-hashed  
* Styled Components / Emotion — CSS-in-JS, styles are scoped to component by default  
* BEM methodology — Block Element Modifier naming convention to avoid conflicts  
* Cascade layers `@layer` — new CSS feature to control specificity at a structural level

---

That's the complete **CSS (Styling & Layouts)** section — **30 questions** with full subtopic depth, ready to merge into your MERN Interview Kit.

[⬅️ Previous: HTML](../../MERN_Study_Structure/01_Web_Development_Fundamentals/01_HTML/01_HTML.md) | [🏠 Home](../../README.md) | [Next: Bootstrap ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/03_Bootstrap/03_Bootstrap.md)
