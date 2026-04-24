# HTML (Structure & Semantics)

## 📚 Curriculum Checklist
- [ ] HTML Boilerplate
- [ ] Headings, Paragraphs, Lists, Tables
- [ ] Forms (Inputs, Buttons, Textareas, Checkboxes, Radio Buttons)
- [ ] Semantic HTML (header, nav, article, section, aside, footer)
- [ ] Meta Tags & SEO Basics
- [ ] [MDN Web Docs - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)  (Official Documentation)
- [ ] [W3Schools - HTML](https://www.w3schools.com/html/)

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

### 6. Meta Tags & SEO Basics
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


## ❓ Questions & Doubts
- [ ]

---

`⬅️ Start` | [🏠 Home](../../README.md) | [Next: CSS ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/02_CSS/02_CSS.md)