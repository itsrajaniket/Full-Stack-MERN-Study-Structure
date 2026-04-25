### **1\. HTML Boilerplate**

---

**Q1. What is an HTML boilerplate and why is it important?** `[Fresher]`

* What does `<!DOCTYPE html>` do and why must it be the first line?  
* Difference between HTML4 doctype and HTML5 doctype declaration  
* What happens if you omit `<!DOCTYPE html>`? (Quirks mode vs Standards mode)  
* Role of the `<html lang="en">` attribute — accessibility and SEO impact  
* Why is `<meta charset="UTF-8">` important? What is UTF-8?  
* What does `<meta name="viewport" content="width=device-width, initial-scale=1.0">` do?  
* Why is viewport meta tag critical for responsive design?  
* Difference between `<head>` and `<body>` — what goes where and why  
* Role of `<title>` tag — SEO \+ browser tab display  
* Where should `<script>` tags be placed — in `<head>` vs end of `<body>` vs using `defer`/`async`  
* What is the `defer` attribute on a script tag? How is it different from `async`?  
* What is render-blocking and how does script placement affect page load?

---

**Q2. What is the difference between `defer` and `async` in script loading?** `[1-2 yrs]`

* How does the browser parse HTML normally without defer/async?  
* `async` — when does the script execute? Does it block HTML parsing?  
* `defer` — when does the script execute? How is execution order maintained?  
* Which one should you use for third-party scripts like analytics?  
* Which one is safer for scripts that depend on the DOM being ready?  
* What happens with multiple `async` scripts — is order guaranteed?  
* What happens with multiple `defer` scripts — is order guaranteed?

---

### **2\. Headings, Paragraphs, Lists, Tables**

---

**Q3. What are HTML headings and how should they be used correctly?** `[Fresher]`

* Available heading tags `<h1>` to `<h6>` and their hierarchy  
* Should there be only one `<h1>` per page? Why?  
* Impact of heading structure on SEO and screen readers  
* Common mistake — using headings for styling instead of structure  
* Difference between heading hierarchy and visual size (CSS handles size, not the tag)

---

**Q4. What is the difference between `<ol>`, `<ul>`, and `<dl>`?** `[Fresher]`

* When to use ordered vs unordered list  
* What is a definition list `<dl>` — `<dt>` and `<dd>` explained  
* Can lists be nested? Any best practices?  
* Accessibility role of lists — screen readers announce list count  
* Styling lists with CSS — removing default bullets/numbers

---

**Q5. How do HTML tables work and when should you use them?** `[Fresher]`

* Core table tags — `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`  
* Difference between `<th>` and `<td>` — semantic \+ accessibility meaning  
* `colspan` and `rowspan` attributes — how do they work?  
* `scope` attribute on `<th>` — why it matters for accessibility  
* When NOT to use tables — common mistake of using tables for layout  
* `<caption>` tag — purpose and accessibility benefit

---

### **3\. Forms**

---

**Q6. What are HTML forms and how do they work?** `[Fresher]`

* Basic structure — `<form>`, `action`, `method` attributes  
* Difference between `GET` and `POST` method in forms  
* When would you use `GET` vs `POST` for form submission?  
* What is the default method of a form if not specified?  
* What happens when a form is submitted — full page reload vs AJAX  
* Role of `name` attribute on inputs — why it's required for form data  
* `<label>` tag — how to associate with input using `for` and `id`  
* Why is `<label>` important for accessibility?

---

**Q7. What are all the different input types available in HTML5?** `[Fresher]`

* Text inputs — `text`, `email`, `password`, `search`, `url`, `tel`, `number`  
* Date/time inputs — `date`, `time`, `datetime-local`, `month`, `week`  
* Selection inputs — `checkbox`, `radio`, `range`, `color`, `file`  
* Action inputs — `submit`, `reset`, `button`, `image`  
* Hidden input — `type="hidden"`, use case in forms  
* Difference between `<input type="button">` and `<button>` tag  
* New HTML5 input types and their built-in validation behavior  
* Browser support differences for newer input types

---

**Q8. What is the difference between `<input>`, `<textarea>`, and `<select>`?** `[Fresher]`

* `<input>` — single line, self-closing  
* `<textarea>` — multiline text, `rows` and `cols` attributes  
* `<select>` with `<option>` and `<optgroup>` — dropdown behavior  
* `multiple` attribute on `<select>` — allows multi-selection  
* `<datalist>` vs `<select>` — autocomplete suggestion vs strict dropdown  
* How to set a default selected value in `<select>`  
* How to disable individual options in a dropdown

---

**Q9. How do checkboxes and radio buttons differ in behavior and usage?** `[Fresher]`

* Radio buttons — grouped by same `name`, only one can be selected  
* Checkboxes — independent, multiple can be selected  
* How to group radio buttons correctly  
* How form submission sends checkbox/radio data to the server  
* What happens if no checkbox is checked — the field is absent from form data  
* `checked` attribute — setting default selection  
* Difference between `checked` attribute and `checked` property in JS

---

### **4\. Semantic HTML**

---

**Q10. What is Semantic HTML and why does it matter?** `[Fresher]`

* Definition — tags that carry meaning beyond just visual presentation  
* Non-semantic tags — `<div>`, `<span>` carry no meaning  
* Semantic tags — `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`  
* How semantic HTML helps screen readers and assistive technologies  
* SEO benefit — search engines understand page structure better  
* Maintainability benefit — code is easier to read and understand  
* Common mistake of using only `<div>` for everything (`div soup`)

---

**Q11. What is the difference between `<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>`?** `[Fresher]`

* `<header>` — introductory content, can appear inside `<article>` too, not just page-level  
* `<nav>` — navigation links block, can have multiple `<nav>` on a page  
* `<main>` — unique main content of the page, only one per page  
* `<section>` — thematic grouping of content, should ideally have a heading  
* `<article>` — self-contained, independently distributable content (blog post, news item)  
* `<aside>` — tangentially related content (sidebar, pull quotes, ads)  
* `<footer>` — closing content, can also appear inside `<article>` or `<section>`  
* Difference between `<section>` and `<article>` — when to use which  
* Can `<header>` and `<footer>` appear inside `<article>`? Yes — explain why

---

**Q12. What is the difference between `<div>` and `<section>` and `<article>`?** `[1-2 yrs]`

* `<div>` — purely presentational, no semantic meaning  
* `<section>` — semantic grouping, implies a themed block of related content  
* `<article>` — fully standalone content that could be syndicated on its own  
* Rule of thumb — if content makes sense on its own when taken out of context, use `<article>`  
* If content is part of a larger whole but thematically grouped, use `<section>`  
* If you just need a styling/layout wrapper, use `<div>`

---

**Q13. What is the `<figure>` and `<figcaption>` element used for?** `[Fresher]`

* `<figure>` — self-contained content like images, diagrams, code blocks  
* `<figcaption>` — caption associated with the figure  
* Why is this better than just using `<img>` with a `<p>` below it?  
* Accessibility and semantic benefit

---

**Q14. What is the difference between `<strong>`, `<b>`, `<em>`, and `<i>`?** `[Fresher]`

* `<strong>` — semantic importance, screen readers may stress it  
* `<b>` — visually bold, no semantic meaning  
* `<em>` — semantic emphasis, screen readers may change tone  
* `<i>` — visually italic, used for technical terms, foreign words, no semantic emphasis  
* When to use which — interview trick question

---

### **5\. Meta Tags & SEO Basics**

---

**Q15. What are meta tags and what role do they play in HTML?** `[Fresher]`

* `<meta>` tag — provides metadata about the HTML document  
* `charset` — character encoding declaration  
* `viewport` — controls layout on mobile browsers  
* `description` — page summary shown in search engine results  
* `keywords` — mostly deprecated, no longer used by Google  
* `robots` — tells crawlers to index or not (`index`, `noindex`, `follow`, `nofollow`)  
* `author` — document author  
* Open Graph tags (`og:title`, `og:description`, `og:image`) — for social media sharing  
* Twitter Card meta tags  
* How many characters should a meta description ideally be?  
* Can meta tags alone guarantee good SEO ranking? (No — content quality matters more)

---

**Q16. What is the difference between `<meta name="description">` and `<title>` for SEO?** `[Fresher]`

* `<title>` — shown in browser tab and as the clickable link in search results  
* `<meta description>` — shown as the snippet under the title in search results  
* Impact on CTR (click-through rate) — description affects clicks, not directly ranking  
* Ideal title length — 50–60 characters  
* Ideal description length — 150–160 characters

---

**Q17. What are Open Graph meta tags and why are they important?** `[1-2 yrs]`

* What is Open Graph protocol — developed by Facebook  
* `og:title`, `og:description`, `og:image`, `og:url`, `og:type`  
* Where are OG tags used — Facebook, LinkedIn, WhatsApp link previews  
* Twitter Cards — separate from OG, uses `twitter:card`, `twitter:title`, etc.  
* How to test OG tags — Facebook Sharing Debugger, Twitter Card Validator  
* Why this matters in MERN projects — when building full-stack apps with public pages

---

### **6\. HTML5 Form Validation**

---

**Q18. What is HTML5 built-in form validation and how does it work?** `[Fresher]`

* `required` attribute — field must not be empty before submission  
* `minlength` / `maxlength` — character length constraints  
* `min` / `max` — numeric or date range constraints  
* `pattern` attribute — regex-based validation  
* `type` validation — `email`, `url`, `number` types auto-validate format  
* Browser default error messages — how they appear  
* `novalidate` attribute on `<form>` — disables all HTML5 validation  
* `:valid` and `:invalid` CSS pseudo-classes — style fields based on validity state

---

**Q19. What is the difference between HTML5 validation and JavaScript validation?** `[1-2 yrs]`

* HTML5 validation — client-side, built-in, zero JS needed  
* JS validation — custom logic, better UX control, custom error messages  
* Server-side validation — always required, never trust client alone  
* Why HTML5 validation alone is NOT enough for production apps  
* `setCustomValidity()` — how to use JS to set custom validation messages on native elements  
* `checkValidity()` and `reportValidity()` methods on form elements  
* Libraries like React Hook Form, Formik, Yup — how they handle validation in MERN projects

---

**Q20. What is the `pattern` attribute and how is it used?** `[1-2 yrs]`

* `pattern` takes a regex without delimiters  
* Example — validating Indian phone number: `pattern="[6-9][0-9]{9}"`  
* How to combine `pattern` with `title` for a custom hint message  
* Difference between `pattern` on `<input>` vs full JS regex validation  
* Common regex patterns — email, phone, password strength, pincode

---

**Q21. What are `autocomplete`, `autofocus`, and `placeholder` attributes?** `[Fresher]`

* `placeholder` — hint text inside input, disappears on typing  
* Common mistake — using `placeholder` instead of `<label>` (accessibility issue)  
* `autofocus` — automatically focuses the input when page loads  
* `autocomplete` — hints browser to suggest saved values (`on`, `off`, specific values like `email`, `username`)  
* Security concern — `autocomplete="off"` for sensitive fields like OTP, CVV  
* `autocomplete="new-password"` — prevents browser from autofilling old passwords

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q22. What is the difference between `id` and `class` attributes?** `[Fresher]`

* `id` — unique per page, used for JS targeting and anchor links  
* `class` — reusable, multiple elements can share a class  
* Can one element have multiple classes? Yes — space-separated  
* Can one element have multiple ids? No  
* CSS specificity — `id` has higher specificity than `class`

---

**Q23. What is the difference between block-level and inline elements?** `[Fresher]`

* Block-level — takes full width, starts on new line (`<div>`, `<p>`, `<h1>`, `<section>`)  
* Inline — takes only as much width as content, does not start new line (`<span>`, `<a>`, `<strong>`)  
* Inline-block — behaves inline but respects width/height  
* Can you put a block element inside an inline element? (Not valid HTML — e.g., `<a>` wrapping `<div>` is invalid in HTML4 but allowed in HTML5)

---

**Q24. What is `data-*` attribute in HTML5?** `[1-2 yrs]`

* Custom data attributes — store extra data on DOM elements without using non-standard attributes  
* Syntax — `data-user-id="123"`, accessed via `element.dataset.userId` in JS  
* Use case in React/MERN — passing data to event handlers, storing ids on list items  
* Does `data-*` appear in HTTP requests? No — purely client-side

---

**Q25. What is the difference between `<script>`, `<link>`, and `<style>` in the `<head>`?** `[Fresher]`

* `<link rel="stylesheet">` — external CSS file, non-blocking for HTML parsing  
* `<style>` — inline CSS directly in HTML  
* `<script>` — JS, blocks parsing unless `defer`/`async` used  
* Why external CSS is preferred over inline `<style>` for large projects  
* `rel="preload"` on `<link>` — hint browser to fetch resource early

---

**Q26. What is the `<picture>` element and how is it different from `<img>`?** `[2-3 yrs]`

* `<picture>` — allows multiple source images based on conditions  
* `<source media="...">` — serves different images at different screen sizes  
* `<source type="image/webp">` — serves modern formats with fallback  
* `srcset` and `sizes` on `<img>` — responsive image without `<picture>`  
* When to use `<picture>` vs `srcset` on `<img>`  
* Performance benefit — serving smaller images to mobile users

---

**Q27. What is accessibility (a11y) in HTML and why does it matter?** `[1-2 yrs]`

* ARIA — Accessible Rich Internet Applications  
* `role` attribute — defines the role of an element (`role="button"`, `role="dialog"`)  
* `aria-label` — provides accessible name for elements with no visible text  
* `aria-hidden="true"` — hides element from screen readers  
* `aria-expanded`, `aria-selected`, `aria-checked` — dynamic state attributes  
* `tabindex` — controls keyboard navigation order  
* `alt` attribute on images — must describe the image, empty `alt=""` for decorative images  
* Why does accessibility matter in interviews — companies increasingly test for this

---

That's the complete **HTML (Structure & Semantics)** section — **27 questions** with full subtopic depth, ready to merge into your MERN Interview Kit.

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

## **JavaScript (JS) — MERN Stack Interview Kit**

---

### **1\. Variables (var, let, const)**

---

**Q1. What is the difference between `var`, `let`, and `const`?** `[Fresher]`

* `var` — function-scoped, hoisted with `undefined`, can be re-declared and re-assigned  
* `let` — block-scoped, hoisted but in Temporal Dead Zone (TDZ), cannot be re-declared, can be re-assigned  
* `const` — block-scoped, hoisted but in TDZ, cannot be re-declared or re-assigned  
* Block scope vs function scope — what counts as a block `{}`  
* Why `var` is considered problematic — leaks out of `if`/`for` blocks, global pollution  
* `const` with objects and arrays — the binding is constant, not the value (properties can still change)  
* When to use which — prefer `const` by default, use `let` when reassignment needed, avoid `var`

---

**Q2. What is the Temporal Dead Zone (TDZ)?** `[1-2 yrs]`

* Period between entering scope and the `let`/`const` declaration line being executed  
* Accessing variable in TDZ throws `ReferenceError`, not `undefined`  
* Why TDZ exists — prevents accessing variables before they are meaningfully initialized  
* TDZ applies to `let`, `const`, and `class` declarations  
* Does NOT apply to `var` — `var` is hoisted with `undefined` immediately

---

### **2\. Data Types**

---

**Q3. What are the data types in JavaScript?** `[Fresher]`

* **Primitive types** (immutable, stored by value):  
  * `String` — sequence of characters  
  * `Number` — integers and floats, `NaN`, `Infinity`  
  * `Boolean` — `true` / `false`  
  * `undefined` — declared but not assigned  
  * `null` — intentional absence of value  
  * `Symbol` — unique and immutable identifier (ES6)  
  * `BigInt` — integers beyond `Number.MAX_SAFE_INTEGER` (ES2020)  
* **Reference types** (mutable, stored by reference):  
  * `Object` — key-value pairs  
  * `Array` — ordered list (technically an object)  
  * `Function` — callable object  
  * `Date`, `Map`, `Set`, `WeakMap`, `WeakSet`  
* `typeof` operator — returns type as string, quirk: `typeof null === 'object'` (historical bug)  
* `typeof NaN === 'number'` — another common interview trap  
* Difference between `null` and `undefined` — null is explicit empty, undefined is absence of assignment

---

**Q4. What is the difference between primitive and reference types in memory?** `[1-2 yrs]`

* Primitives stored in **stack** — value itself is stored, copying creates independent copy  
* References stored in **heap** — variable holds memory address, copying copies the reference  
* Shallow copy problem with objects — `const b = a` means both point to same object  
* How to copy objects — spread `{...obj}`, `Object.assign()`, `JSON.parse(JSON.stringify())`, `structuredClone()`  
* Deep copy vs shallow copy — nested objects still share reference in shallow copy  
* `structuredClone()` — modern built-in deep clone, handles nested objects correctly  
* Why `===` comparison on objects always false for different object literals even with same content

---

**Q5. What is `NaN` and how do you check for it?** `[Fresher]`

* `NaN` — "Not a Number", result of invalid numeric operation (e.g., `"abc" * 2`)  
* `typeof NaN === 'number'` — confusing but true  
* `NaN === NaN` is `false` — NaN is the only value not equal to itself  
* `isNaN("abc")` — returns `true` but also converts string to number first (coercion issue)  
* `Number.isNaN("abc")` — returns `false` because "abc" is not NaN, it's a string (preferred)  
* `Number.isNaN(NaN)` — returns `true` (correct and reliable)

---

**Q6. What is the difference between `null` and `undefined`?** `[Fresher]`

* `undefined` — variable declared but not assigned, function that returns nothing, missing object property  
* `null` — intentional empty value, explicitly set by developer  
* `typeof undefined === 'undefined'`, `typeof null === 'object'` (bug)  
* `null == undefined` is `true` (loose equality), `null === undefined` is `false` (strict)  
* Nullish coalescing `??` — returns right side only for `null` or `undefined` (not for `0` or `""`)  
* Optional chaining `?.` — safely access nested properties without checking for null/undefined

---

### **3\. Operators & Type Coercion**

---

**Q7. What is type coercion in JavaScript?** `[Fresher]`

* Implicit type conversion done automatically by JS engine  
* **String coercion** — `"5" + 2 = "52"` (number converted to string because of `+`)  
* **Number coercion** — `"5" - 2 = 3` (string converted to number because of `-`)  
* Falsy values — `false`, `0`, `""`, `null`, `undefined`, `NaN`  
* Truthy values — everything else, including `[]`, `{}`, `"0"`, `"false"`  
* `+` is overloaded — string concatenation AND numeric addition, coercion depends on operands  
* Unary `+` operator — converts value to number: `+"5"` \= `5`, `+""` \= `0`, `+null` \= `0`, `+undefined` \= `NaN`

---

**Q8. What is the difference between `==` and `===`?** `[Fresher]`

* `==` (loose equality) — performs type coercion before comparing  
* `===` (strict equality) — no coercion, both value AND type must match  
* Tricky `==` results:  
  * `0 == false` → `true`  
  * `"" == false` → `true`  
  * `null == undefined` → `true`  
  * `null == 0` → `false`  
  * `[] == false` → `true`  
  * `[] == ![]` → `true` (classic interview trap)  
* Always prefer `===` in production code  
* `Object.is(a, b)` — like `===` but treats `NaN === NaN` as true and `-0 !== +0`

---

**Q9. What are all the JavaScript operators you should know?** `[Fresher]`

* Arithmetic — `+`, `-`, `*`, `/`, `%`, `**` (exponentiation)  
* Assignment — `=`, `+=`, `-=`, `*=`, `/=`, `**=`, `??=`, `||=`, `&&=`  
* Comparison — `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`  
* Logical — `&&`, `||`, `!`, `??` (nullish coalescing)  
* Bitwise — `&`, `|`, `^`, `~`, `<<`, `>>`  
* Ternary — `condition ? valueIfTrue : valueIfFalse`  
* Optional chaining — `?.` — safe property access  
* Spread — `...` — expand iterables  
* `typeof`, `instanceof`, `in`, `delete`, `void`  
* Logical assignment operators — `||=`, `&&=`, `??=` — ES2021

---

### **4\. Functions**

---

**Q10. What are the different ways to define a function in JavaScript?** `[Fresher]`

* **Function Declaration** — `function foo() {}` — hoisted fully  
* **Function Expression** — `const foo = function() {}` — not hoisted  
* **Arrow Function** — `const foo = () => {}` — no own `this`, `arguments`, `super`  
* **Named Function Expression** — `const foo = function bar() {}` — name only accessible inside  
* **IIFE** — Immediately Invoked Function Expression — `(function() {})()`  
* **Generator Function** — `function* gen() { yield value }` — returns iterator  
* **Async Function** — `async function foo() {}` — always returns a Promise  
* **Method shorthand in objects** — `{ foo() {} }`

---

**Q11. What is the difference between regular functions and arrow functions?** `[Fresher]`

* `this` binding:  
  * Regular function — `this` is determined by how function is **called** (dynamic)  
  * Arrow function — `this` is inherited from **enclosing lexical scope** (static)  
* Arrow functions do NOT have their own:  
  * `this`  
  * `arguments` object  
  * `prototype`  
  * Cannot be used as constructors with `new`  
* When to use arrow functions — callbacks, array methods, short expressions  
* When NOT to use arrow functions — object methods (if you need `this`), prototype methods, event handlers where `this` should refer to element, constructors  
* `arguments` object — only in regular functions, use rest `...args` in arrow functions

---

**Q12. What is a callback function?** `[Fresher]`

* A function passed as argument to another function, called later (possibly asynchronously)  
* Synchronous callback — `[1,2,3].forEach(callback)` — called immediately during execution  
* Asynchronous callback — `setTimeout(callback, 1000)` — called later after delay  
* Callback hell — deeply nested callbacks, hard to read and maintain  
* How Promises and async/await solve callback hell  
* Error-first callbacks — Node.js convention `(err, data) => {}`, check error first

---

**Q13. What are higher-order functions?** `[1-2 yrs]`

* A function that takes a function as argument OR returns a function  
* Examples of built-in HOFs — `map`, `filter`, `reduce`, `forEach`, `sort`, `find`  
* Custom HOF example — function that returns another function (factory pattern)  
* Benefits — abstraction, reusability, composability  
* Currying — transforming `f(a, b)` into `f(a)(b)`, a form of higher-order function  
* Function composition — combining functions where output of one feeds into next

---

### **5\. Scope & Hoisting**

---

**Q14. What is scope in JavaScript?** `[Fresher]`

* Scope — determines where variables are accessible  
* **Global scope** — accessible everywhere  
* **Function scope** — `var` variables, only accessible inside the function  
* **Block scope** — `let`/`const`, only accessible inside `{}`  
* **Module scope** — variables in ES modules are scoped to the module, not global  
* Scope chain — when variable not found in current scope, JS looks up the chain to outer scopes  
* Lexical scope — scope is determined at code-writing time (not runtime)

---

**Q15. What is hoisting in JavaScript?** `[Fresher]`

* JS engine moves declarations to top of their scope during compile phase  
* `var` declarations — hoisted AND initialized with `undefined`  
* `function` declarations — hoisted AND fully initialized (function body is available)  
* `let` / `const` — hoisted but NOT initialized (in TDZ until declaration line)  
* `class` declarations — hoisted but in TDZ (cannot use before declaration)  
* Function expression `const fn = function() {}` — only the `const fn` part is hoisted, not the function  
* Common interview question — what is output of `console.log(x)` before `var x = 5`? → `undefined`  
* What is output of calling a function declaration before its definition? → Works fine (fully hoisted)  
* What is output of calling a function expression before its definition? → `TypeError` or `ReferenceError`

---

### **6\. ES6+ Features**

---

**Q16. What is destructuring in JavaScript?** `[Fresher]`

* Syntax to unpack values from arrays or properties from objects into variables  
* **Array destructuring:**  
  * `const [a, b] = [1, 2]`  
  * Skip elements — `const [a, , c] = [1, 2, 3]`  
  * Default values — `const [a = 10] = []`  
  * Swap variables — `[a, b] = [b, a]`  
  * Rest in array — `const [first, ...rest] = [1, 2, 3, 4]`  
* **Object destructuring:**  
  * `const { name, age } = person`  
  * Renaming — `const { name: fullName } = person`  
  * Default values — `const { name = "Anonymous" } = {}`  
  * Nested destructuring — `const { address: { city } } = user`  
  * Rest in object — `const { a, ...others } = obj`  
* In function parameters — `function greet({ name, age }) {}`  
* In React — used heavily for props destructuring and hooks like `const [state, setState] = useState()`

---

**Q17. What is the difference between spread and rest operators?** `[Fresher]`

* Both use `...` syntax but in different contexts  
* **Spread** — expands an iterable into individual elements  
  * In arrays — `const merged = [...arr1, ...arr2]`  
  * In objects — `const merged = {...obj1, ...obj2}` — later keys overwrite earlier  
  * In function calls — `Math.max(...numbers)`  
  * Shallow copy — `const copy = [...arr]` or `const copy = {...obj}`  
* **Rest** — collects remaining arguments into an array  
  * In function parameters — `function sum(...args) {}` — must be last parameter  
  * In destructuring — `const [first, ...rest] = arr`  
* Common mistake — trying to spread non-iterables (plain objects not iterable, only work in object spread)

---

**Q18. What are template literals?** `[Fresher]`

* Backtick strings — `` ` `` instead of `'` or `"`  
* String interpolation — `${expression}` — embed any JS expression  
* Multi-line strings — no need for `\n`  
* Tagged templates — `tag\`string\`\` — function processes template literal parts  
  * Used by styled-components, GraphQL (`gql\`query\`\`)  
* Nested template literals — template inside template  
* Expression inside `${}` can be any JS expression — ternary, function call, arithmetic

---

**Q19. What are other important ES6+ features every developer should know?** `[1-2 yrs]`

* **Default parameters** — `function greet(name = "World") {}`  
* **Enhanced object literals:**  
  * Shorthand properties — `{ name, age }` instead of `{ name: name, age: age }`  
  * Computed property names — `{ [dynamicKey]: value }`  
  * Method shorthand — `{ greet() {} }`  
* **`for...of` loop** — iterate over iterables (arrays, strings, Maps, Sets)  
* **`for...in` loop** — iterate over object keys (also gets inherited enumerable properties — use with caution)  
* **`Map`** — key-value store, any type as key, maintains insertion order  
* **`Set`** — collection of unique values  
* **`WeakMap` / `WeakSet`** — keys are weakly held (garbage collected when no other references)  
* **Optional chaining `?.`** — `user?.address?.city` — no error if intermediate is null/undefined  
* **Nullish coalescing `??`** — returns right side only if left is `null` or `undefined`  
* **`Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.any`**  
* **`globalThis`** — consistent global object across environments (browser, Node.js, workers)  
* **Logical assignment operators** — `||=`, `&&=`, `??=` (ES2021)  
* **`structuredClone()`** — deep clone built-in (ES2022)  
* **`Array.at(-1)`** — access from end of array (ES2022)  
* **`Object.hasOwn(obj, key)`** — safer than `obj.hasOwnProperty(key)` (ES2022)

---

### **7\. Promises & Async/Await**

---

**Q20. What is a Promise in JavaScript?** `[Fresher]`

* An object representing eventual completion or failure of an async operation  
* Three states — `pending`, `fulfilled`, `rejected`  
* Once settled (fulfilled or rejected), state cannot change  
* Created with `new Promise((resolve, reject) => {})`  
* `.then(onFulfilled, onRejected)` — handle resolution  
* `.catch(onRejected)` — handle rejection  
* `.finally(callback)` — runs regardless of outcome  
* Promise chaining — each `.then()` returns a new Promise  
* Return value from `.then()` becomes value passed to next `.then()`  
* Throwing inside `.then()` passes to next `.catch()`

---

**Q21. What is the difference between `Promise.all`, `Promise.allSettled`, `Promise.race`, and `Promise.any`?** `[1-2 yrs]`

* `Promise.all(promises)`:  
  * Resolves when **all** promises resolve  
  * Rejects immediately if **any** promise rejects (fail-fast)  
  * Use when all results are needed and any failure should abort  
* `Promise.allSettled(promises)`:  
  * Waits for **all** promises to settle (resolve or reject)  
  * Always resolves, returns array of `{status, value/reason}` objects  
  * Use when you need all results regardless of failures  
* `Promise.race(promises)`:  
  * Settles with the **first** promise to settle (resolve or reject)  
  * Use for timeout pattern — race actual request vs a timeout promise  
* `Promise.any(promises)`:  
  * Resolves with the **first** promise to **resolve**  
  * Rejects only if **all** promises reject (with `AggregateError`)  
  * Opposite of `Promise.race` for error handling

---

**Q22. What is async/await and how does it work?** `[Fresher]`

* Syntactic sugar over Promises — makes async code look synchronous  
* `async` keyword — marks a function as async, always returns a Promise  
* `await` keyword — pauses execution inside async function until Promise resolves  
* `await` can only be used inside `async` function (or top-level in ES modules)  
* Error handling — wrap in `try/catch` block (equivalent to `.catch()`)  
* `await` on non-Promise value — just returns the value (no error)  
* Running promises in parallel with async/await:  
  * Wrong (sequential) — `await p1; await p2` — waits one then other  
  * Right (parallel) — `const [r1, r2] = await Promise.all([p1, p2])`  
* Async/await vs Promises — async/await is not replacement, it's built on top of Promises  
* Common mistake — forgetting `await` keyword, function returns Promise not value

---

### **8\. Fetch API & Axios**

---

**Q23. What is the Fetch API and how do you use it?** `[Fresher]`

* Built-in browser API for making HTTP requests  
* Returns a Promise that resolves to a `Response` object  
* Two-step process — first `await fetch(url)`, then `await response.json()`  
* Why two awaits — first await gets the Response header/status, second reads the body stream  
* `response.ok` — true if status is 200-299  
* `response.status` — HTTP status code  
* Fetch does NOT reject on HTTP errors (404, 500\) — must manually check `response.ok`  
* Sending data:

 fetch(url, {  
    method: 'POST',  
    headers: { 'Content-Type': 'application/json' },  
    body: JSON.stringify(data)  
  })

* Setting headers — pass `headers` object in options  
* `AbortController` — cancel a fetch request in progress

---

**Q24. What is Axios and how is it different from Fetch?** `[1-2 yrs]`

* Third-party HTTP client library, works in browser and Node.js  
* Differences from Fetch:  
  * Axios automatically parses JSON response — no second `.json()` call needed  
  * Axios rejects on HTTP errors (4xx, 5xx) — easier error handling  
  * Axios has built-in request/response interceptors  
  * Axios supports request cancellation with `CancelToken` / `AbortController`  
  * Axios automatically sets `Content-Type: application/json`  
  * Axios works in Node.js, Fetch needs polyfill in older Node versions  
* Axios interceptors — `axios.interceptors.request.use()`, `axios.interceptors.response.use()`  
  * Use cases — attach auth token to every request, global error handling, refresh token logic  
* Axios instance — `axios.create({ baseURL, headers })` for shared config  
* Axios in MERN — commonly used in React frontend for API calls to Express backend

---

### **9\. DOM Manipulation & Events**

---

**Q25. What is the DOM and how do you manipulate it with JavaScript?** `[Fresher]`

* DOM — Document Object Model, tree representation of HTML as JS objects  
* Selecting elements:  
  * `document.getElementById('id')`  
  * `document.querySelector('.class')` — first match  
  * `document.querySelectorAll('div')` — NodeList of all matches  
  * `document.getElementsByClassName()`, `document.getElementsByTagName()`  
* Modifying elements:  
  * `element.textContent` — get/set text content (safer, no HTML parsing)  
  * `element.innerHTML` — get/set HTML (XSS risk if setting user input)  
  * `element.setAttribute('attr', 'value')` / `element.getAttribute('attr')`  
  * `element.classList.add()`, `.remove()`, `.toggle()`, `.contains()`  
  * `element.style.property = 'value'` — inline styles  
* Creating and inserting elements:  
  * `document.createElement('div')`  
  * `parent.appendChild(child)`, `parent.insertBefore(newNode, refNode)`  
  * `element.append()`, `element.prepend()`, `element.before()`, `element.after()`  
  * `element.remove()` — remove element from DOM  
* `innerHTML` vs `textContent` vs `innerText`:  
  * `innerHTML` — parses HTML, XSS risk  
  * `textContent` — raw text, no HTML parsing, faster  
  * `innerText` — respects CSS visibility, triggers reflow

---

**Q26. What are DOM events and how does event handling work?** `[Fresher]`

* Events — signals that something happened (click, keypress, form submit, etc.)  
* `addEventListener(event, handler, options)` — preferred way  
* `removeEventListener(event, handler)` — same reference required to remove  
* Inline event handlers `onclick="..."` — avoid, mixes HTML and JS  
* `event` object — passed to handler, contains `target`, `currentTarget`, `type`, `preventDefault()`, `stopPropagation()`  
* `event.target` — element that triggered the event  
* `event.currentTarget` — element that has the event listener attached  
* Common events — `click`, `dblclick`, `mouseover`, `mouseout`, `mouseenter`, `mouseleave`, `keydown`, `keyup`, `keypress`, `submit`, `change`, `input`, `focus`, `blur`, `scroll`, `resize`, `load`, `DOMContentLoaded`

---

**Q27. What is event bubbling, capturing, and delegation?** `[1-2 yrs]`

* **Event bubbling** — event triggers on target, then bubbles UP to ancestors (default)  
* **Event capturing** — event triggers from root DOWN to target (capture phase)  
* `addEventListener(event, handler, true)` — third argument `true` enables capture phase  
* `event.stopPropagation()` — stops event from bubbling/capturing further  
* `event.stopImmediatePropagation()` — stops propagation AND prevents other handlers on same element  
* `event.preventDefault()` — prevents default browser behavior (form submit, link navigation)  
* **Event delegation** — attach one listener on parent, handle events for multiple children  
  * Use `event.target` to identify which child was clicked  
  * Benefits — fewer listeners (performance), works for dynamically added elements  
  * Common pattern in React-like dynamic lists

---

### **10\. Error Handling**

---

**Q28. How does error handling work in JavaScript?** `[Fresher]`

* `try` — wrap code that might throw  
* `catch(error)` — handle the error, `error.message`, `error.name`, `error.stack`  
* `finally` — always runs regardless of error  
* `throw` — manually throw any value (best practice: throw `Error` objects)  
* Built-in error types — `Error`, `TypeError`, `ReferenceError`, `SyntaxError`, `RangeError`, `URIError`, `EvalError`  
* Custom errors — extend `Error` class: `class ValidationError extends Error {}`  
* `try/catch` does NOT catch async errors — must use inside `async` function or `.catch()` on Promise  
* Global error handling — `window.onerror`, `window.onunhandledrejection`  
* Error handling in Express (backend) — next(err) pattern

---

**Q29. What are common patterns for async error handling?** `[1-2 yrs]`

* Async/await with try/catch — cleanest approach  
* `.catch()` on Promise chain  
* Wrapper utility — `const [err, data] = await to(promise)` (Go-style error handling pattern)  
* Global unhandled rejection handler — `process.on('unhandledRejection', handler)` in Node.js  
* Error boundaries in React — `componentDidCatch`, `ErrorBoundary` component  
* Axios error handling — `error.response` (server responded), `error.request` (no response), `error.message` (setup error)

---

### **11\. Closures & Lexical Scope**

---

**Q30. What is a closure in JavaScript?** `[1-2 yrs]`

* A function that remembers the variables from its outer scope even after the outer function has returned  
* Every function in JS creates a closure over its surrounding scope  
* How it works — inner function holds a reference to outer scope's variable environment  
* Practical use cases:  
  * Data encapsulation / private variables  
  * Factory functions — functions that return configured functions  
  * Memoization — caching results using closure  
  * Event handlers that remember state  
  * Module pattern (pre-ES6)  
* Classic closure interview question:

 for (var i \= 0; i \< 3; i++) {  
    setTimeout(() \=\> console.log(i), 100\)  
  }  
  // prints 3, 3, 3 — not 0, 1, 2

* Fix with `let` (block scoped) or IIFE wrapping  
* Closure memory — variables in closure are kept in memory (potential memory leak if not careful)

---

**Q31. What is lexical scope?** `[1-2 yrs]`

* Scope determined at code **write time** (not runtime)  
* A function's scope chain is determined by where it is **defined**, not where it is **called**  
* Inner functions have access to outer function variables — forms the basis of closures  
* Lexical environment — the surrounding context captured by a closure  
* Difference between lexical scope and dynamic scope (JS uses lexical, not dynamic)

---

### **12\. Event Loop & Asynchronous JS**

---

**Q32. How does the JavaScript Event Loop work?** `[1-2 yrs]`

* JS is single-threaded — one call stack, executes one thing at a time  
* **Components:**  
  1. **Call Stack** — LIFO stack of currently executing functions  
  2. **Web APIs** — browser-provided environment for async ops (setTimeout, fetch, DOM events)  
  3. **Callback Queue (Task Queue / Macrotask Queue)** — completed async callbacks wait here  
  4. **Microtask Queue** — Promise callbacks, `queueMicrotask()`, `MutationObserver`  
  5. **Event Loop** — continuously checks if call stack is empty, then processes queues  
* **Execution order:**  
  1. All synchronous code runs (call stack)  
  2. All microtasks run (Promise `.then`, `await` continuations) — entire queue drained  
  3. One macrotask runs (setTimeout, setInterval, I/O)  
  4. All microtasks again  
  5. Repeat  
* Microtasks have priority over macrotasks  
* `setTimeout(fn, 0)` — doesn't run immediately, runs after current stack AND microtasks clear  
* Classic question — predict output of mixed sync, Promise, and setTimeout code

---

**Q33. What is the difference between microtasks and macrotasks?** `[2-3 yrs]`

* **Macrotasks** — `setTimeout`, `setInterval`, `setImmediate` (Node), I/O, UI rendering  
* **Microtasks** — `Promise.then/catch/finally`, `queueMicrotask()`, `MutationObserver`, `async/await` continuations  
* After each macrotask — entire microtask queue is drained before next macrotask  
* Why this matters — Promise callbacks always run before the next setTimeout callback  
* `queueMicrotask(fn)` — directly enqueue a microtask  
* Node.js specific — `process.nextTick()` runs before microtasks (even higher priority)

---

**Q34. What is `setTimeout`, `setInterval`, and `clearTimeout`?** `[Fresher]`

* `setTimeout(fn, delay)` — run function once after delay (ms), returns timer ID  
* `clearTimeout(id)` — cancel before it fires  
* `setInterval(fn, delay)` — run function repeatedly every delay ms  
* `clearInterval(id)` — stop the interval  
* Minimum delay — HTML spec minimum is 4ms for nested timeouts  
* `setTimeout(fn, 0)` — defers execution to after current call stack clears  
* Why interval may drift — if callback takes longer than interval, next call is delayed  
* Better than `setInterval` for recurring tasks — recursive `setTimeout` gives consistent delay

---

### **13\. Modules**

---

**Q35. What are ES Modules and how do they work?** `[Fresher]`

* `export` — named exports and default export  
* Named export — `export const fn = () => {}`, import as `import { fn } from './module'`  
* Default export — `export default fn`, import as `import fn from './module'` (any name)  
* One default export per module, multiple named exports allowed  
* Re-exporting — `export { fn } from './other'`  
* Export all — `export * from './other'`  
* `import * as module from './file'` — namespace import  
* Dynamic import — `import('./module').then(m => m.fn())` — lazy loading  
* ES Modules are static — imports are resolved at compile time, not runtime  
* ES Modules are always in strict mode  
* `import.meta` — metadata about the module (e.g., `import.meta.url`)

---

**Q36. What is the difference between CommonJS and ES Modules?** `[1-2 yrs]`

* **CommonJS** (Node.js traditional):  
  * `require()` / `module.exports` / `exports`  
  * Synchronous — loaded at runtime  
  * Dynamic — `require()` can be inside conditionals  
  * `.js` extension default in Node  
* **ES Modules:**  
  * `import` / `export`  
  * Asynchronous-capable — resolved at parse time (static)  
  * Cannot use inside conditionals (except dynamic `import()`)  
  * `.mjs` extension or `"type": "module"` in `package.json`  
* Tree-shaking — only possible with ES Modules (static analysis of imports)  
* Interop — using CommonJS module inside ESM and vice versa — nuances in Node.js  
* React uses ES Modules, Node.js traditionally used CommonJS (now supports both)

---

### **14\. Object-Oriented Programming (OOP)**

---

**Q37. What is prototypal inheritance in JavaScript?** `[1-2 yrs]`

* Every object has a hidden `[[Prototype]]` property pointing to another object  
* Property lookup — if not found on object, JS walks up the prototype chain  
* `Object.getPrototypeOf(obj)` — access prototype  
* `obj.__proto__` — non-standard but widely supported  
* `Object.create(proto)` — create object with specified prototype  
* All objects eventually inherit from `Object.prototype` (top of chain)  
* `null` — end of prototype chain (`Object.prototype.__proto__ === null`)  
* `hasOwnProperty()` — checks if property belongs to object itself, not prototype  
* `in` operator — checks own AND inherited properties

---

**Q38. What are ES6 Classes and how do they work?** `[1-2 yrs]`

* Syntactic sugar over prototypal inheritance — cleaner syntax, same behavior underneath  
* `class` declaration — `class Animal {}`  
* `constructor()` — called when `new` is used  
* Instance methods — defined in class body, stored on `prototype`  
* `static` methods — called on the class itself, not instances  
* `extends` — class inheritance  
* `super()` — call parent constructor, must be called in child constructor before `this`  
* `super.method()` — call parent class methods  
* Getters and setters — `get name() {}`, `set name(val) {}`  
* Private fields — `#fieldName` (ES2022) — truly private, not accessible outside class  
* Public class fields — `fieldName = value`  
* Class expressions — `const Foo = class {}`  
* Classes are NOT hoisted (in TDZ) — unlike function declarations

---

**Q39. What are the four pillars of OOP and how are they achieved in JavaScript?** `[2-3 yrs]`

* **Encapsulation** — bundling data and methods, hiding internal state  
  * Achieved via closures, private class fields `#`, WeakMap pattern  
* **Inheritance** — child class inherits from parent  
  * Achieved via `extends`, `Object.create()`, prototype chain  
* **Polymorphism** — same method name, different behavior in subclasses  
  * Achieved via method overriding in subclasses  
* **Abstraction** — hide complex implementation, expose simple interface  
  * Achieved via private fields/methods, closures, abstract-like base classes  
* JavaScript is prototype-based OOP, not class-based (classes are syntactic sugar)  
* Composition over Inheritance — prefer mixing in behaviors over deep inheritance chains

---

### **15\. Functional Programming**

---

**Q40. What are `map`, `filter`, and `reduce`?** `[Fresher]`

* **`map(callback)`** — transforms each element, returns new array of same length  
  * `callback(currentValue, index, array)` — return transformed value  
  * Does not mutate original array  
* **`filter(callback)`** — keeps elements where callback returns `true`, returns new array  
  * `callback(currentValue, index, array)` — return boolean  
  * Result array can be shorter than original  
* **`reduce(callback, initialValue)`** — accumulates all elements into single value  
  * `callback(accumulator, currentValue, index, array)` — return new accumulator  
  * Can produce any type — number, string, object, array  
  * `initialValue` — always provide it to avoid edge cases with empty arrays  
* Chaining — `arr.filter(...).map(...).reduce(...)`  
* Performance note — chaining creates multiple intermediate arrays, sometimes a single `reduce` is more efficient

---

**Q41. What are other important array methods for functional programming?** `[Fresher]`

* `forEach(callback)` — iterate, returns `undefined`, cannot break out early  
* `find(callback)` — returns **first** element matching condition, or `undefined`  
* `findIndex(callback)` — returns index of first match, or `-1`  
* `some(callback)` — returns `true` if at least one element matches  
* `every(callback)` — returns `true` if all elements match  
* `flat(depth)` — flatten nested arrays  
* `flatMap(callback)` — map then flatten one level  
* `sort(compareFn)` — sorts in place (mutates\!), default converts to string  
  * Numeric sort — `arr.sort((a, b) => a - b)`  
* `splice(start, deleteCount, ...items)` — mutates original array  
* `slice(start, end)` — returns new array, does not mutate  
* `includes(value)` — check if value exists  
* `indexOf(value)` — first index of value, `-1` if not found  
* `Array.from(iterable)` — create array from iterable or array-like  
* `Array.isArray(value)` — check if value is an array

---

**Q42. What are pure functions and immutability in functional programming?** `[2-3 yrs]`

* **Pure function** — same input always produces same output, no side effects  
* Side effects — modifying external state, API calls, DOM manipulation, logging  
* Immutability — do not mutate data, create new versions instead  
* Benefits — predictable, testable, easier to reason about  
* Immutable array patterns — use `map`, `filter`, `spread` instead of `push`, `splice`, `sort`  
* Immutable object patterns — `{...obj, updatedKey: newValue}` instead of `obj.key = value`  
* `Object.freeze()` — prevents modification of object (shallow freeze only)  
* Why React cares about immutability — state updates require new references for change detection

---

### **16\. Web Storage**

---

**Q43. What are the differences between `localStorage`, `sessionStorage`, and Cookies?** `[Fresher]`

* **`localStorage`:**  
  * Persists until explicitly cleared  
  * 5-10MB storage limit  
  * Accessible only on client (JS)  
  * Same origin only  
  * Not sent with HTTP requests  
* **`sessionStorage`:**  
  * Cleared when browser tab is closed  
  * 5MB storage limit  
  * Same origin, same tab only  
  * Not sent with HTTP requests  
* **Cookies:**  
  * Expiry can be set (session or specific date)  
  * \~4KB limit per cookie  
  * Sent with every HTTP request to the server (can be used for auth)  
  * Can be `HttpOnly` (not accessible by JS) — important for security  
  * Can be `Secure` (HTTPS only)  
  * `SameSite` attribute — controls cross-site sending (`Strict`, `Lax`, `None`)  
  * Can be set by server via `Set-Cookie` header  
* All three are origin-specific — different domains cannot access each other's storage

---

**Q44. How do you work with `localStorage` in JavaScript?** `[Fresher]`

* `localStorage.setItem('key', 'value')` — value must be string  
* `localStorage.getItem('key')` — returns string or `null`  
* `localStorage.removeItem('key')`  
* `localStorage.clear()` — removes all items for the origin  
* `localStorage.length` — number of stored items  
* `localStorage.key(index)` — get key by index  
* Storing objects — must `JSON.stringify()` on save, `JSON.parse()` on read  
* Common mistake — storing objects without stringifying, getting `"[object Object]"`  
* `storage` event — fires in OTHER tabs/windows when localStorage changes (not same tab)  
* Use cases in MERN — store JWT token (controversial), user preferences, cart data, theme

---

**Q45. What are the security concerns around Web Storage?** `[2-3 yrs]`

* **localStorage XSS vulnerability** — if attacker injects JS, they can read localStorage including JWT tokens  
* `HttpOnly` cookies cannot be read by JS — why they are preferred for storing auth tokens  
* Never store sensitive data (passwords, credit card info) in localStorage  
* JWT in localStorage vs HttpOnly cookie — hot debate:  
  * localStorage — vulnerable to XSS  
  * HttpOnly cookie — protected from XSS but vulnerable to CSRF (mitigated with `SameSite`)  
* CSRF attack — forged requests that include cookies automatically  
* `SameSite=Strict` or `Lax` — mitigates CSRF for cookie-based auth  
* Content Security Policy (CSP) — reduces XSS risk, helps protect localStorage indirectly  
* Best practice in production MERN apps — use `HttpOnly`, `Secure`, `SameSite=Strict` cookies for auth tokens

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q46. What is the difference between deep copy and shallow copy?** `[1-2 yrs]`

* Already detailed in Q4 — here focus on methods and when each fails  
* Shallow copy methods — spread, `Object.assign()`, `Array.slice()`  
* Deep copy methods:  
  * `JSON.parse(JSON.stringify(obj))` — fails with functions, `undefined`, `Date`, `RegExp`, circular refs  
  * `structuredClone(obj)` — handles `Date`, `Map`, `Set`, circular refs, but not functions  
  * Lodash `_.cloneDeep()` — most comprehensive  
* Circular reference — object that references itself, breaks most copy methods

---

**Q47. What is `this` keyword in JavaScript?** `[1-2 yrs]`

* `this` refers to the object that is the **execution context** of the function  
* Value of `this` depends on how function is called:  
  * Regular function — `this` is the calling object, or `global`/`undefined` in strict mode  
  * Arrow function — `this` is lexically bound (enclosing context)  
  * Constructor with `new` — `this` is the newly created object  
  * Explicit binding — `call()`, `apply()`, `bind()`  
  * Object method — `this` is the object before the dot  
  * Class method — `this` is the instance  
* `call(thisArg, arg1, arg2)` — call with specified `this`, arguments individually  
* `apply(thisArg, [argsArray])` — call with specified `this`, arguments as array  
* `bind(thisArg)` — returns NEW function with permanently bound `this`  
* Common issue in React — `this` in class component event handlers (need to bind or use arrow function)

---

**Q48. What is memoization?** `[2-3 yrs]`

* Optimization technique — cache results of expensive function calls  
* If same input is called again, return cached result without re-executing  
* Implemented using closure to maintain cache object  
* `useMemo` and `useCallback` in React — memoization hooks  
* Pure functions are prerequisite for memoization (same input must always give same output)  
* Trade-off — memory usage increases to save computation time

---

**Q49. What is the difference between `for...in` and `for...of`?** `[Fresher]`

* `for...in` — iterates over **enumerable property keys** of an object (and inherited ones)  
  * Use `hasOwnProperty` check to skip inherited properties  
  * Works on arrays too but gives string indices — bad practice  
* `for...of` — iterates over **values** of any iterable (arrays, strings, Maps, Sets, generators)  
  * Does not work on plain objects (not iterable by default)  
  * Use `Object.keys()`, `Object.values()`, `Object.entries()` to loop over objects with `for...of`

---

**Q50. What is a generator function?** `[2-3 yrs]`

* `function*` — can pause and resume execution  
* `yield` — pauses function, returns value to caller  
* Returns an iterator — call `.next()` to resume, returns `{value, done}`  
* `yield*` — delegates to another generator or iterable  
* Use cases — infinite sequences, lazy evaluation, custom iterators, `async` generator for streaming data  
* Generators behind the scenes of early async patterns (before async/await)

---

That's the complete **JavaScript** section — **50 questions** with full subtopic depth, ready to merge into your MERN Interview Kit.

### **1\. Node.js Fundamentals**

---

**Q1. What is Node.js and how does it work?** `[Fresher]`

* Node.js — open-source, cross-platform JavaScript runtime built on Chrome's V8 engine  
* Allows running JavaScript outside the browser — on the server side  
* Built on top of libuv — C library that provides the event loop, async I/O, thread pool  
* Single-threaded — one main thread for JS execution, but async operations run via libuv thread pool  
* Non-blocking I/O — doesn't wait for file/network/database operations to complete  
* Event-driven — actions trigger events, event loop processes them  
* Node.js is NOT a framework — it's a runtime environment  
* Node.js is NOT multi-threaded for JS — but libuv uses thread pool for heavy I/O (file system, crypto, DNS)  
* What Node.js is good for:  
  * REST APIs and backend services  
  * Real-time applications (chat, live updates)  
  * Streaming applications  
  * Microservices  
  * CLI tools  
* What Node.js is NOT good for:  
  * CPU-intensive tasks (image processing, ML, video encoding) — blocks the event loop  
  * Heavy computation — use worker threads or separate services  
* Node.js version — LTS (Long Term Support) vs Current — always use LTS in production  
  ---

**Q2. What is the V8 engine and what role does it play in Node.js?** `[1-2 yrs]`

* V8 — open-source JavaScript engine developed by Google, written in C++  
* Compiles JavaScript directly to native machine code (JIT — Just-In-Time compilation)  
* Responsibilities in Node.js:  
  * Parsing JavaScript code  
  * Compiling to machine code  
  * Memory allocation (heap)  
  * Garbage collection  
* V8 does NOT handle I/O, file system, network — that is libuv's job  
* Hidden classes — V8 optimization for object property access  
* Inline caching — V8 optimization for repeated function calls  
* Garbage collection — Mark and Sweep algorithm, Generational GC (young/old generation)  
  ---

**Q3. What is the difference between Node.js and browser JavaScript?** `[Fresher]`

* Same — both run JS on V8, share language features, ES6+ support  
* Different:

| Feature | Browser JS | Node.js |
| ----- | ----- | ----- |
| Global object | `window` | `global` / `globalThis` |
| DOM access | Available | Not available |
| `document`, `navigator` | Available | Not available |
| `fs`, `http`, `path` | Not available | Available |
| Module system | ES Modules | CommonJS \+ ESM |
| `process` object | Not available | Available |
| `__dirname` / `__filename` | Not available | Available (CommonJS only) |
| OS access | Sandboxed | Full access |

* `globalThis` — works in both environments (ES2020)  
* Browser JS runs in sandbox — limited OS access by design  
* Node.js has full OS access — file system, network, processes  
  ---

**Q4. What is the `process` object in Node.js?** `[1-2 yrs]`

* Global object — available without requiring any module  
* Key properties and methods:  
  * `process.env` — access environment variables  
  * `process.argv` — array of command-line arguments (`[node, scriptPath, ...args]`)  
  * `process.cwd()` — current working directory  
  * `process.exit(code)` — exit process (`0` \= success, non-zero \= error)  
  * `process.pid` — process ID  
  * `process.version` — Node.js version string  
  * `process.platform` — OS platform (`'win32'`, `'linux'`, `'darwin'`)  
  * `process.memoryUsage()` — heap used, heap total, RSS  
  * `process.uptime()` — seconds the process has been running  
  * `process.hrtime()` — high-resolution time for benchmarking  
  * `process.nextTick(callback)` — schedule callback before next event loop iteration  
* `process.stdin`, `process.stdout`, `process.stderr` — standard I/O streams  
  ---

  ### **2\. NPM & Yarn**

  ---

**Q5. What is NPM and what is it used for?** `[Fresher]`

* NPM — Node Package Manager, default package manager bundled with Node.js  
* Used for:  
  * Installing third-party packages/libraries  
  * Managing project dependencies  
  * Running scripts (`npm start`, `npm test`, `npm run build`)  
  * Publishing packages to npm registry  
* `npm init` — create `package.json`  
* `npm init -y` — skip questions, use defaults  
* `npm install <package>` — install and add to `dependencies`  
* `npm install <package> --save-dev` — add to `devDependencies`  
* `npm install -g <package>` — global install  
* `npm uninstall <package>` — remove package  
* `npm update` — update packages to latest compatible version  
* `npm list` — list installed packages  
* `npm audit` — check for security vulnerabilities  
* `npm audit fix` — auto-fix vulnerabilities  
* `npm ci` — clean install from `package-lock.json` (used in CI/CD — faster, deterministic)  
  ---

**Q6. What is `package.json` and what are its key fields?** `[Fresher]`

* JSON file at root of project — manifest for the project  
* Key fields:  
  * `name` — package name (must be lowercase, no spaces)  
  * `version` — semantic version (`major.minor.patch`)  
  * `main` — entry point file  
  * `scripts` — custom command shortcuts (`start`, `test`, `build`, `dev`)  
  * `dependencies` — packages needed in production  
  * `devDependencies` — packages only needed during development  
  * `peerDependencies` — packages consumer must install (used by libraries)  
  * `engines` — specify required Node.js version  
  * `private: true` — prevent accidental publish to npm registry  
  * `type: "module"` — treat `.js` files as ES Modules  
  * `license` — project license  
* Semantic versioning (SemVer):  
  * `^1.2.3` — compatible with `1.x.x` (minor and patch updates allowed)  
  * `~1.2.3` — only patch updates `1.2.x`  
  * `1.2.3` — exact version only  
  * `*` — any version (dangerous)

  ---

**Q7. What is `package-lock.json` and why is it important?** `[1-2 yrs]`

* Auto-generated file — locks exact versions of ALL dependencies (direct \+ transitive)  
* Ensures reproducible installs across machines and environments  
* Should be committed to version control — guarantees same dependency tree for entire team  
* `npm install` — uses `package-lock.json` if present to install exact versions  
* `npm ci` — strictly uses `package-lock.json`, fails if it doesn't match `package.json`  
* `package-lock.json` vs `package.json` — `package.json` has version ranges, lock file has exact versions  
* Yarn equivalent — `yarn.lock`  
* Common mistake — adding `package-lock.json` to `.gitignore` — never do this  
  ---

**Q8. What is the difference between `dependencies` and `devDependencies`?** `[Fresher]`

* `dependencies` — required for application to run in production (Express, React, Mongoose)  
* `devDependencies` — only needed during development and build (nodemon, Jest, ESLint, Webpack, TypeScript)  
* `npm install --production` — installs only `dependencies`, skips `devDependencies`  
* In CI/CD and Docker production builds — set `NODE_ENV=production` to skip devDependencies  
* `peerDependencies` — library declares what version of host package it needs (e.g., React component library requiring React 18\)  
* `optionalDependencies` — install if possible, don't fail if can't install  
  ---

**Q9. What is the difference between NPM and Yarn?** `[1-2 yrs]`

* Both are package managers for Node.js ecosystem  
* NPM — ships with Node.js, `package-lock.json`, workspaces support from v7+  
* Yarn Classic (v1) / Berry (v2+) — must install separately, `yarn.lock`, historically faster parallel downloads, better monorepo support  
* Yarn Berry — Plug'n'Play mode, no `node_modules` folder  
* pnpm — third alternative, uses hard links/symlinks, most disk-space efficient  
* In MERN projects — npm is most common, Yarn used in some enterprise/monorepo setups

| Action | NPM | Yarn |
| ----- | ----- | ----- |
| Install all deps | `npm install` | `yarn` |
| Add package | `npm install pkg` | `yarn add pkg` |
| Add dev dep | `npm i pkg --save-dev` | `yarn add pkg --dev` |
| Remove package | `npm uninstall pkg` | `yarn remove pkg` |
| Run script | `npm run script` | `yarn script` |
| Clean install | `npm ci` | `yarn install --frozen-lockfile` |

  ---

  ### **3\. Node.js Modules (CommonJS vs ES Modules)**

  ---

**Q10. What is the CommonJS module system in Node.js?** `[Fresher]`

* Default module system in Node.js  
* `require()` — synchronously loads a module  
* `module.exports` — what the module exposes  
* `exports` — shorthand for `module.exports` (same reference initially)  
* Module caching — once a module is loaded, it's cached — subsequent `require()` calls return cached version  
* `require.cache` — object of all cached modules  
* Circular dependency — two modules requiring each other — Node handles it but partial exports issue  
* `__dirname` — absolute path of the directory of current file  
* `__filename` — absolute path of current file  
* `require('./file')` — relative path, `.js` extension optional  
* `require('express')` — looks in `node_modules`  
* Module resolution order — core modules → node\_modules → file path  
  ---

**Q11. What is the difference between `module.exports` and `exports`?** `[1-2 yrs]`

* Initially both point to the same empty object `{}`  
* `exports.fn = fn` — adds property to the shared object — works correctly  
* `module.exports = fn` — replaces the export entirely — works correctly  
* `exports = fn` — BREAKS — reassigns local variable, loses reference to `module.exports`  
* What actually gets exported is always `module.exports` — not `exports`  
* Rule of thumb — use `module.exports` when exporting a single value/class/function  
* Use `exports.x = x` when exporting multiple named things  
  ---

**Q12. What are the differences between CommonJS and ES Modules in Node.js?** `[1-2 yrs]`

| Feature | CommonJS | ES Modules |
| ----- | ----- | ----- |
| Syntax | `require()` / `module.exports` | `import` / `export` |
| Loading | Synchronous | Asynchronous-capable |
| When resolved | Runtime | Parse time (static) |
| `__dirname` | Available | Not available (use `import.meta.url`) |
| Top-level await | Not supported | Supported |
| Tree shaking | Not possible | Possible |
| File extension | `.js` / `.cjs` | `.mjs` or `.js` with `"type":"module"` |
| Dynamic import | Not applicable | `import()` function |

* Enable ES Modules in Node.js:  
  * Add `"type": "module"` to `package.json` — all `.js` files treated as ESM  
  * Use `.mjs` extension — always treated as ESM regardless of `package.json`  
  * Use `.cjs` extension — always treated as CommonJS  
* In ESM — `__dirname` and `__filename` are NOT available, use `fileURLToPath(import.meta.url)` instead  
* `require()` not available in ESM — use dynamic `import()` instead  
* Top-level `await` — works in ESM, not in CommonJS  
* Interop — ESM can import CJS with default import, CJS cannot `require()` ESM synchronously  
  ---

**Q13. What are Node.js core built-in modules?** `[Fresher]`

* No install needed — bundled with Node.js  
* Key modules:  
  * `fs` — file system operations  
  * `path` — file path utilities  
  * `http` / `https` — create HTTP servers and clients  
  * `os` — operating system info  
  * `events` — EventEmitter  
  * `stream` — streaming data  
  * `crypto` — cryptographic functions (hashing, encryption)  
  * `url` — URL parsing and formatting  
  * `querystring` — parse/stringify query strings  
  * `child_process` — spawn subprocesses (`exec`, `spawn`, `fork`)  
  * `cluster` — multiple Node.js processes sharing same port  
  * `worker_threads` — true parallelism for CPU-intensive tasks  
  * `util` — utility functions (`promisify`, `inspect`, `format`)  
  * `buffer` — handle binary data  
  * `net` — TCP/IPC networking  
  * `dns` — DNS lookups  
  * `readline` — line-by-line reading of streams  
  * `zlib` — compression (gzip, deflate)  
* Import with `require('fs')` or `import fs from 'node:fs'` (node: prefix preferred in ESM)  
  ---

  ### **4\. Asynchronous JavaScript in Node.js**

  ---

**Q14. How does asynchronous programming work in Node.js?** `[Fresher]`

* Node.js uses non-blocking I/O — instead of waiting for operation, registers a callback and moves on  
* Three patterns for async code:  
  * Callbacks — original Node.js pattern, error-first convention `(err, data) => {}`  
  * Promises — cleaner chaining, no callback hell  
  * Async/Await — modern, cleanest approach  
* `util.promisify(fn)` — converts callback-based function to Promise-based  
* `fs.promises` — built-in promise versions of fs methods (no need to promisify manually)  
* Error-first callback convention — `(err, data) => {}` — always check `err` first  
* Why Node.js can handle thousands of concurrent requests — single thread plus non-blocking I/O means it doesn't create a thread per request like traditional servers  
  ---

**Q15. What is `util.promisify` and when would you use it?** `[1-2 yrs]`

* Converts Node.js error-first callback functions to Promises  
* Works with functions following `(err, value) => {}` callback pattern  
* `util.callbackify()` — opposite direction, converts async function to callback style  
* Custom promisify — for functions that don't follow convention, use `util.promisify.custom` symbol  
* When to use — working with older Node.js APIs or third-party libs that use callbacks  
* Most modern Node.js APIs now have native Promise versions (`fs.promises`, `dns.promises`)  
  ---

  ### **5\. Event Loop & Streams**

  ---

**Q16. How does the Node.js Event Loop work?** `[1-2 yrs]`

* Same fundamental concept as browser event loop — but Node.js has more defined phases  
* Node.js Event Loop Phases in order:  
  * Timers — executes `setTimeout` and `setInterval` callbacks whose threshold has passed  
  * Pending callbacks — I/O callbacks deferred to next iteration  
  * Idle, Prepare — internal use only  
  * Poll — retrieve new I/O events, execute I/O callbacks (most time spent here)  
  * Check — `setImmediate()` callbacks execute here  
  * Close callbacks — `socket.on('close', ...)` type callbacks  
* Between each phase — microtask queue is drained:  
  * `process.nextTick()` callbacks — highest priority, run before Promise microtasks  
  * Promise microtasks — `then`, `catch`, `finally`, `await` continuations  
* `process.nextTick(fn)` — runs before next event loop iteration, before any I/O  
* `setImmediate(fn)` — runs in Check phase, after I/O callbacks  
* `setTimeout(fn, 0)` vs `setImmediate(fn)`:  
  * Outside I/O — order is non-deterministic  
  * Inside I/O callback — `setImmediate` always fires first  
* libuv thread pool — handles DNS, crypto, fs (default 4 threads), configurable via `UV_THREADPOOL_SIZE`  
  ---

**Q17. What are Streams in Node.js?** `[1-2 yrs]`

* Streams — abstract interface for working with data in chunks instead of all at once  
* Why streams — memory efficient (no need to load entire file), time efficient (process as data arrives)  
* Four types of streams:  
  * Readable — data can be read from (`fs.createReadStream`, `http.IncomingMessage`)  
  * Writable — data can be written to (`fs.createWriteStream`, `http.ServerResponse`)  
  * Duplex — both readable and writable (`net.Socket`, TCP connection)  
  * Transform — duplex stream that transforms data (`zlib.createGzip`, `crypto.createCipher`)  
* Streams extend EventEmitter — emit events:  
  * Readable events — `data`, `end`, `error`, `close`  
  * Writable events — `drain`, `finish`, `error`, `close`  
* Piping — `readable.pipe(writable)` — connect streams, handles backpressure automatically  
* Backpressure — when writable stream can't keep up with readable, pipe handles slowing down producer  
* `pipeline(src, transform, dest, callback)` — from `stream` module, better than pipe (handles errors properly)  
* Stream modes — flowing (data pushed automatically) vs paused (must call `.read()`)  
* `highWaterMark` — buffer size threshold, default 16KB for bytes, 16 objects for object mode  
* Practical use cases — reading large CSV file, video streaming, file compression on the fly  
  ---

**Q18. What is the EventEmitter in Node.js?** `[1-2 yrs]`

* Core class from `events` module — backbone of Node.js event-driven architecture  
* Many built-in Node.js objects extend EventEmitter (streams, HTTP server, etc.)  
* Key methods:  
  * `emitter.on(event, listener)` — register persistent listener  
  * `emitter.once(event, listener)` — listener fires once then auto-removed  
  * `emitter.emit(event, ...args)` — trigger event, pass arguments to listeners  
  * `emitter.off(event, listener)` — remove specific listener  
  * `emitter.removeAllListeners(event)` — remove all listeners for event  
  * `emitter.listeners(event)` — get array of listeners for event  
  * `emitter.listenerCount(event)` — number of listeners  
  * `emitter.setMaxListeners(n)` — default max is 10, increase to avoid memory leak warning  
* `error` event — special event, if emitted with no listener, throws uncaught error  
* Memory leak warning — adding too many listeners without removing them is a common bug  
  ---

  ### **6\. File System (fs module)**

  ---

**Q19. How do you work with the file system in Node.js?** `[Fresher]`

* `fs` module — built-in, no install needed  
* Every method has three versions:  
  * Synchronous — `fs.readFileSync()` — blocks event loop, avoid in production servers  
  * Callback async — `fs.readFile(path, callback)` — non-blocking, older style  
  * Promise async — `fs.promises.readFile(path)` — non-blocking, modern preferred  
* Common operations:  
  * Read file — `fs.promises.readFile(path, 'utf8')`  
  * Write file — `fs.promises.writeFile(path, data)` — creates or overwrites  
  * Append file — `fs.promises.appendFile(path, data)`  
  * Delete file — `fs.promises.unlink(path)`  
  * Rename/Move — `fs.promises.rename(oldPath, newPath)`  
  * Check if exists — `fs.promises.access(path, fs.constants.F_OK)`  
  * Get file info — `fs.promises.stat(path)` — returns Stats object (size, dates, isFile, isDirectory)  
  * Create directory — `fs.promises.mkdir(path, { recursive: true })`  
  * Read directory — `fs.promises.readdir(path)` — returns array of filenames  
  * Remove directory — `fs.promises.rm(path, { recursive: true })` (Node 14.14+)  
* `fs.watch(path, callback)` — watch file/directory for changes  
* Encoding — always specify `'utf8'` for text files, omit for raw Buffer  
  ---

**Q20. What is the `path` module and why is it important?** `[Fresher]`

* Built-in module for working with file and directory paths  
* Critical because path separators differ by OS — `/` on Unix, `\` on Windows  
* Key methods:  
  * `path.join(...segments)` — joins path segments using OS separator  
  * `path.resolve(...segments)` — resolves absolute path from given segments  
  * `path.dirname(filePath)` — directory part of path  
  * `path.basename(filePath)` — filename with extension  
  * `path.basename(filePath, ext)` — filename without extension  
  * `path.extname(filePath)` — extension (`.js`, `.json`)  
  * `path.parse(filePath)` — returns object with `root`, `dir`, `base`, `name`, `ext`  
  * `path.sep` — OS path separator (`/` or `\`)  
* `path.join` vs `path.resolve`:  
  * `join` — simple concatenation with OS separator  
  * `resolve` — builds absolute path, processes `..` and `.`, uses `cwd()` as base  
* Common pattern — `path.join(__dirname, 'public', 'index.html')`  
  ---

**Q21. What is the difference between reading a file synchronously vs asynchronously?** `[Fresher]`

* Sync — `fs.readFileSync(path, 'utf8')` — blocks entire event loop until done  
  * Acceptable during app startup (config loading, before server starts)  
  * Never use inside request handlers — blocks all other requests  
* Async callback — `fs.readFile(path, 'utf8', (err, data) => {})` — non-blocking  
* Async Promise — `await fs.promises.readFile(path, 'utf8')` — non-blocking, cleanest  
* Stream — `fs.createReadStream(path)` — best for large files, most memory efficient  
* Rule of thumb — sync only at startup, Promises or streams everywhere else  
  ---

  ### **7\. Environment Variables & Configuration**

  ---

**Q22. What are environment variables and why are they used in Node.js?** `[Fresher]`

* Key-value pairs stored in the OS environment, accessible to processes  
* Why use them:  
  * Keep secrets out of source code (DB passwords, API keys, JWT secrets)  
  * Different config for different environments (dev, staging, production)  
  * 12-Factor App methodology — config in environment, not in code  
* Access in Node.js — `process.env.VARIABLE_NAME`  
* Returns `undefined` if variable not set  
* All values are strings — parse numbers with `parseInt(process.env.PORT)`  
* Set in terminal — `PORT=3000 node app.js` (Unix) or `set PORT=3000 && node app.js` (Windows)  
* Never commit `.env` files — always add to `.gitignore`  
  ---

**Q23. What is `dotenv` and how do you use it?** `[Fresher]`

* Third-party package — loads environment variables from `.env` file into `process.env`  
* `npm install dotenv`  
* Usage — `require('dotenv').config()` at very top of entry file before anything else  
* `.env` file format:  
  * `PORT=3000`  
  * `DB_URI=mongodb://localhost:27017/mydb`  
  * `JWT_SECRET=mysecretkey`  
  * `NODE_ENV=development`  
* `dotenv` only loads variables not already set — won't override system environment variables  
* Multiple environments — `.env.development`, `.env.production`, `.env.test`  
* `dotenv-expand` — allows variable interpolation inside `.env`  
* Production best practice — use actual environment variables from hosting platform, not `.env` files  
* `.env.example` — commit this with dummy values to document required variables without exposing secrets  
* Node 20+ built-in — `node --env-file=.env app.js` — no dotenv package needed  
  ---

**Q24. What is `NODE_ENV` and why is it important?** `[1-2 yrs]`

* Convention for specifying the runtime environment  
* Common values — `development`, `production`, `test`  
* Not automatically set by Node.js — must be set explicitly  
* How it affects application behavior:  
  * Express — disables detailed error messages in production  
  * React/Webpack — enables optimizations and minification in production build  
  * Many libraries change internal behavior based on `NODE_ENV`  
* Check in code — `if (process.env.NODE_ENV === 'production') {}`  
* `cross-env` npm package — set `NODE_ENV` consistently across Windows and Unix  
* Never run production with `NODE_ENV=development` — disables caching, enables verbose logging, exposes stack traces to clients  
  ---

**Q25. How do you manage configuration for different environments in a MERN app?** `[2-3 yrs]`

* Simple approach — single `.env` file, different values per environment  
* Better approach — centralized config module:  
  * `config/index.js` exports object with all config values with fallbacks  
  * `port: process.env.PORT || 3000`  
* Validation at startup — use `joi` or `zod` to validate all required env vars, fail fast if missing  
* `convict` — configuration management library with schema validation and environment awareness  
* Secrets management in production:  
  * AWS Secrets Manager  
  * HashiCorp Vault  
  * Heroku Config Vars / Railway / Render environment settings  
  * Docker secrets  
* Never log `process.env` — may expose secrets in log output  
  ---

  ### **8\. Debugging & Logging**

  ---

**Q26. How do you debug a Node.js application?** `[1-2 yrs]`

* `console.log()` — basic, works but messy in production  
* Node.js built-in debugger:  
  * `node inspect app.js` — CLI debugger  
  * `node --inspect app.js` — starts inspector, connect with Chrome DevTools via `chrome://inspect`  
  * `node --inspect-brk app.js` — pauses on first line, useful for startup bugs  
* VS Code debugger:  
  * Launch config in `.vscode/launch.json`  
  * Set breakpoints directly in editor  
  * Can attach to running process or launch fresh  
  * Most common debugging approach in day-to-day development  
* `debugger` statement — pauses execution when debugger is attached  
* `util.inspect(obj, { depth: null })` — deep inspect nested objects better than `console.log`  
* `console.trace()` — print stack trace at a specific point  
* `console.time('label')` / `console.timeEnd('label')` — measure execution time of a block  
  ---

**Q27. What is logging in Node.js and why is `console.log` not enough for production?** `[1-2 yrs]`

* `console.log` problems in production:  
  * No log levels (debug, info, warn, error)  
  * No timestamps  
  * No structured format — hard to parse or search  
  * Synchronous in some contexts — can block event loop  
  * Cannot be easily turned off or filtered by level  
  * No file output or external transport support  
* Production logging requirements:  
  * Log levels — ERROR, WARN, INFO, HTTP, DEBUG  
  * Timestamps on every log entry  
  * Structured JSON format — easy to parse by log management tools  
  * Multiple transport options — console, file, external services  
  * Async logging — no blocking the event loop

  ---

**Q28. What is Winston and how do you use it?** `[1-2 yrs]`

* Most popular Node.js logging library  
* `npm install winston`  
* Key concepts:  
  * Levels — `error`, `warn`, `info`, `http`, `verbose`, `debug`, `silly` (highest to lowest priority)  
  * Transports — where logs go (Console, File, HTTP, custom)  
  * Formats — how logs look (`json`, `simple`, `colorize`, `timestamp`, `combine`)  
* Basic setup:  
  * Create logger with `winston.createLogger()`  
  * Set `level` — only logs at this level and above are output  
  * Combine formats with `winston.format.combine(timestamp(), json())`  
  * Add multiple transports — console for dev, file for production  
* Use `logger.info()`, `logger.error()`, `logger.warn()` instead of `console.log`  
* In production — set level to `warn` or `error` to reduce noise  
* `morgan` — HTTP request logging middleware for Express, commonly combined with Winston  
  ---

**Q29. What is Morgan and how is it used with Express?** `[1-2 yrs]`

* HTTP request logger middleware for Express  
* `npm install morgan`  
* Logs every incoming request — method, URL, status code, response time  
* Predefined formats:  
  * `'dev'` — colorized, concise output for development  
  * `'combined'` — Apache combined log format for production  
  * `'tiny'` — minimal output  
  * `'common'` — standard Apache common log format  
* Usage — `app.use(morgan('dev'))` — place before route handlers  
* Stream to Winston — pass `{ stream: logger.stream }` as second argument  
* Skip function — log only errors: `skip: (req, res) => res.statusCode < 400`  
* Custom tokens — `morgan.token('user', (req) => req.user?.id)` — add custom fields  
  ---

**Q30. What are best practices for error handling and logging in production Node.js apps?** `[2-3 yrs]`

* Operational errors vs Programmer errors:  
  * Operational — expected failures (DB down, file not found, invalid input) — handle gracefully  
  * Programmer — bugs, type errors, logic errors — let crash and restart via PM2  
* Centralized error handling:  
  * Express error middleware `(err, req, res, next)` — single place to handle all errors  
  * `process.on('uncaughtException', handler)` — last resort, app state may be corrupted, always exit after  
  * `process.on('unhandledRejection', handler)` — catch unhandled Promise rejections  
* Never expose stack traces to clients — log internally, send generic message to client  
* Log enough context — user ID, request ID, route, input that caused the error  
* Request ID — generate unique ID per request with `uuid` or `nanoid`, attach to all logs for tracing  
* Log aggregation tools — Datadog, Logtail, Papertrail, ELK Stack, Grafana Loki  
* PM2 — process manager, auto-restarts on crash, cluster mode, built-in log management  
* Health check endpoint — `/health` route to verify app is running, used by load balancers and Docker  
  ---

  ### **Bonus Questions**

  ---

**Q31. What is `nodemon` and why is it used?** `[Fresher]`

* Development tool — automatically restarts Node.js server when file changes are detected  
* `npm install -D nodemon`  
* Usage — `nodemon app.js` instead of `node app.js`  
* `nodemon.json` — config file for ignored paths, watched extensions, restart delay  
* In `package.json` scripts — `"dev": "nodemon app.js"`  
* Node.js v18+ built-in alternative — `node --watch app.js` — no package needed  
  ---

**Q32. What are Worker Threads in Node.js?** `[2-3 yrs]`

* `worker_threads` module — run JavaScript in parallel threads  
* Use for CPU-intensive tasks — image processing, heavy computation, encryption  
* Workers have their own V8 instance and event loop  
* Share memory via `SharedArrayBuffer` — high-performance data sharing between threads  
* Communication via `parentPort.postMessage()` and `workerData`  
* Worker threads vs `child_process.fork()`:  
  * Worker threads — share memory, lower overhead, same process  
  * Child processes — separate memory space, separate process, higher isolation  
* `cluster` module — multiple processes sharing same port for scaling HTTP servers  
  ---

**Q33. What is the `child_process` module in Node.js?** `[2-3 yrs]`

* Spawn separate OS processes from Node.js  
* Four methods:  
  * `exec(command, callback)` — run shell command, buffer entire output, 200KB default limit  
  * `execFile(file, args, callback)` — directly run a file, safer than exec (no shell)  
  * `spawn(command, args)` — stream output, better for large data or long-running processes  
  * `fork(modulePath)` — special spawn for Node.js scripts, built-in IPC channel between parent and child  
* Use cases — running shell scripts, calling Python/Go services, executing OS commands  
* Security — never pass user input directly to `exec` — shell injection risk  
  ---

**Q34. What is clustering in Node.js and why is it needed?** `[2-3 yrs]`

* Node.js is single-threaded — by default uses only one CPU core  
* `cluster` module — create multiple worker processes that share the same port  
* Master process — manages workers, distributes incoming connections via round-robin  
* Worker processes — each handles actual requests independently  
* `os.cpus().length` — number of CPU cores, typically create one worker per core  
* Workers crash independently — master detects crash and restarts the worker  
* PM2 cluster mode — handles clustering automatically with `pm2 start app.js -i max`  
* Modern alternative — run multiple Docker containers behind a load balancer (preferred in cloud deployments)  
  ---

That's the complete **Node.js** section — **34 questions**, all clean with fixed tables.

