# Bootstrap (CSS Framework)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Core Components
- [x] Grid System – Containers, Rows, Cols
- [x] Forms – Inputs, Selects, Buttons, Checkboxes
- [x] Navbar & Sidebar – Navigation Components
- [x] Cards, Modals, Alerts
- [x] Theming & Customization
- [x] Bootstrap Variables & SASS
- [x] Customizing Colors & Components
- [x] Responsive Utilities
- [x] [Bootstrap Official Docs](https://getbootstrap.com/docs/)
- [x] [W3Schools Bootstrap](https://www.w3schools.com/bootstrap4/)

## 📝 Detailed Notes

### 1. The Grid System
Bootstrap’s grid system uses a series of containers, rows, and columns to layout and align content. It’s built with flexbox and is fully responsive.
- **Containers**: `.container` (fixed width) or `.container-fluid` (full width).
- **Rows**: `.row` acts as a wrapper for columns.
- **Columns**: Based on a 12-column layout. Use `.col-{breakpoint}-{number}` (e.g., `.col-md-6`).

### 2. Common Components
- **Navbar**: Responsive navigation header.
- **Cards**: Flexible content container with options for headers, footers, and images.
- **Modals**: Dialog prompts or overlays.
- **Buttons**: Pre-styled buttons (e.g., `.btn-primary`, `.btn-outline-danger`).

### 3. Utility Classes
Bootstrap provides hundreds of helper classes for spacing, colors, and typography.
- **Spacing**: `m-3` (margin 3), `pt-2` (padding-top 2).
- **Typography**: `.text-center`, `.fw-bold`, `.display-1`.
- **Colors**: `.text-primary`, `.bg-light`.

---

## 🎓 Important Interview Questions

### Q1: What are the different breakpoints in Bootstrap 5?
Bootstrap uses 6 default breakpoints:
1. `xs` (<576px)
2. `sm` (≥576px)
3. `md` (≥768px)
4. `lg` (≥992px)
5. `xl` (≥1200px)
6. `xxl` (≥1400px)

### Q2: What is the purpose of the `.container` class?
It provides a way to center your site's contents and horizontally pad them. It has a `max-width` at each responsive breakpoint.

### Q3: Explain the difference between `.row` and `.col`.
- `.row`: Used to wrap columns. It ensures columns are aligned properly using negative margins.
- `.col`: The actual content holders. They must be direct children of a `.row`.

### Q4: How do you make an image responsive in Bootstrap?
Use the `.img-fluid` class. It applies `max-width: 100%;` and `height: auto;` to the image so that it scales with the parent element.

### Q5: What is "Mobile First" design in Bootstrap?
It means Bootstrap styles are applied to the smallest devices first (using `min-width` media queries) and then scaled up for larger screens.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: CSS](../../MERN_Study_Structure/01_Web_Development_Fundamentals/02_CSS/02_CSS.md) | [🏠 Home](../../README.md) | [Next: Tailwind CSS ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/04_Tailwind_CSS/04_Tailwind_CSS.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>