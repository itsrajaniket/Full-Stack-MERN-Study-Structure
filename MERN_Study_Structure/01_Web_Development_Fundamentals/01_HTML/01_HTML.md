# HTML (Structure & Semantics)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] HTML Boilerplate
- [x] Headings, Paragraphs, Lists, Tables
- [x] Forms (Inputs, Buttons, Textareas, Checkboxes, Radio Buttons)
- [x] Semantic HTML (header, nav, article, section, aside, footer)
- [x] Meta Tags & SEO Basics
- [x] HTML5 Form Validation
- [x] [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)  (Official Documentation)
- [x] [W3Schools - HTML](https://www.w3schools.com/html/)

## 📝 Detailed Notes

### 1. HTML5 Boilerplate & Root Elements
The minimum structure required for a valid HTML document.
```html
<!DOCTYPE html> <!-- Tells browser to use HTML5 standards -->
<html lang="en"> <!-- Root element; 'lang' helps search engines and screen readers -->
<head>
    <meta charset="UTF-8"> <!-- Character set for international text -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Critical for mobile responsiveness -->
    <title>My Professional Page</title> <!-- Appears in browser tab and SEO results -->
</head>
<body>
    <!-- Content goes here -->
</body>
</html>
```

### 2. Text Content: Headings, Paragraphs, Lists
- **Headings**: `<h1>` to `<h6>`. Use only one `<h1>` per page for SEO.
- **Paragraphs**: `<p>` for blocks of text.
- **Unordered Lists**: `<ul>` with `<li>` (bullet points).
- **Ordered Lists**: `<ol>` with `<li>` (numbered points).
- **Description Lists**: `<dl>` with `<dt>` (term) and `<dd>` (description).

### 3. Tables (Data Representation)
Tables should be used for data, not layout.
```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Role</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Aniket</td>
            <td>Full Stack Developer</td>
        </tr>
    </tbody>
</table>
```
- **Tags**: `<table>`, `<tr>` (row), `<th>` (header cell), `<td>` (data cell).

### 4. Semantic HTML (The "Modern" Way)
Semantic tags tell the browser/search engine exactly what the content is.
- `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`.
- **Benefit**: Improves accessibility (screen readers) and SEO rankings.

### 5. Forms (User Interaction)
Forms are the core of interactive web apps.
- **Inputs**: `<input type="text|password|email|number|date">`.
- **Choices**: `<input type="checkbox">` (multiple) and `<input type="radio">` (single choice).
- **Selection**: `<select>` with `<option>`.
- **Long Text**: `<textarea>`.
- **Buttons**: `<button type="submit|button|reset">`.
- **Labels**: Always use `<label for="id">` for accessibility.

### 6. HTML5 Form Validation
HTML5 provides built-in validation without JavaScript:
- `required`: Field must be filled.
- `pattern`: Regex validation (e.g., `pattern="[0-9]{10}"`).
- `min`, `max`, `step`: For number/date inputs.
- `minlength`, `maxlength`: For text inputs.

### 7. Meta Tags & SEO Basics
Meta tags provide metadata about the HTML document.
- **Description**: `<meta name="description" content="Detailed page description">`.
- **OG Tags**: Used for social media previews (Open Graph).
- **Favicon**: `<link rel="icon" href="favicon.ico">`.
- **Viewport**: Essential for mobile rendering.

---

## 🎓 Important Interview Questions

### Q1: What is the difference between Block and Inline elements?
- **Block**: Starts on a new line, takes up full width (e.g., `<div>`, `<h1>`, `<p>`, `<section>`).
- **Inline**: Does not start on a new line, only takes as much width as necessary (e.g., `<span>`, `<a>`, `<img>`, `<strong>`).

### Q2: What is the purpose of the `alt` attribute in images?
It provides alternative text if the image fails to load and is used by screen readers for accessibility. It is also a factor in SEO.

### Q3: What are "Void Elements" in HTML?
Elements that do not have a closing tag and cannot contain any content. Examples: `<img>`, `<br>`, `<hr>`, `<input>`, `<meta>`, `<link>`.

### Q4: Difference between `<script>`, `<script async>`, and `<script defer>`?
- **Normal**: HTML parsing stops while script is fetched and executed.
- **Async**: Script is fetched in parallel and executed as soon as it's ready (stops HTML parsing then).
- **Defer**: Script is fetched in parallel and executed only after HTML parsing is complete.

### Q5: What is the `<!DOCTYPE html>` declaration?
It is an instruction to the web browser about what version of HTML the page is written in. It ensures the browser renders the page in "Standards Mode" rather than "Quirks Mode".

### Q6: How do you optimize a website for SEO using only HTML?
- Use semantic tags (`<header>`, `<main>`, `<footer>`).
- Proper heading hierarchy (`<h1>` to `<h6>`).
- Descriptive `<title>` and `<meta name="description">`.
- Using `alt` text for images.
- Using `<link rel="canonical">` to prevent duplicate content issues.

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

## ❓ Questions & Doubts
- [x]

---

`⬅️ Start` | [🏠 Home](../../README.md) | [Next: CSS ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/02_CSS/02_CSS.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>