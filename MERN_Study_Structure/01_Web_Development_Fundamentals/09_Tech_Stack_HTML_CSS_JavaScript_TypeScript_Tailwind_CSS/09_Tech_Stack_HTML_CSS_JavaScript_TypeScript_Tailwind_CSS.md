# Tech Stack: HTML, CSS, JavaScript, TypeScript, Tailwind CSS

## 📚 Curriculum Checklist
- [ ] Blog Listing – Grid layout with images and short descriptions
- [ ] Blog Details Page – Full blog content with an author profile
- [ ] Dark Mode Toggle – Use Tailwind's dark mode feature
- [ ] Responsive Design – Mobile-friendly

## 📝 Detailed Notes

### Project 1: Task Manager App
This project focuses on integrating the fundamental web technologies to build a functional CRUD application.

### Technical Implementation
- **Frontend**: Built with **React** (Vite) and **TypeScript** for type safety.
- **Styling**: **Tailwind CSS** for rapid UI development and **ShadCN** for accessible, pre-built components (Buttons, Dialogs, Inputs).
- **State Management**: Using React Hooks (`useState`, `useEffect`) to manage tasks locally.
- **Data Persistence**: Storing tasks in `localStorage` so they persist after a page refresh.

### Core Features
- Create, Read, Update, and Delete (CRUD) tasks.
- Filter tasks by status (Completed, Pending).
- Responsive design for mobile and desktop.

---

## 🎓 Important Interview Questions

### Q1: Why did you choose TypeScript for this project?
To ensure type safety, which prevents common bugs like passing the wrong data to a component or trying to access properties on an undefined object. It also makes the code easier to maintain and understand.

### Q2: How did you handle data persistence?
I used the `localStorage` API. I wrote a `useEffect` hook to save the task array to `localStorage` whenever it changed, and another `useEffect` to load the data when the application first mounted.

### Q3: What were the advantages of using Tailwind CSS instead of plain CSS?
- Faster development because I didn't have to switch between HTML and CSS files.
- Consistent design system (colors, spacing) out of the box.
- Smaller CSS bundle size in production.

### Q4: How do you manage complex states in a React application?
For this project, `useState` was sufficient. However, if the state became more complex (e.g., deeply nested or shared across many components), I would consider using the `useReducer` hook or a state management library like `Zustand` or `Redux Toolkit`.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Git GitHub](../../MERN_Study_Structure/01_Web_Development_Fundamentals/08_Git_GitHub/08_Git_GitHub.md) | [🏠 Home](../../README.md) | [Next: Features ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/10_Features/10_Features.md)