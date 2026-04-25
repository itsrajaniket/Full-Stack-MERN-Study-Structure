# Features:
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Dashboard UI – List of tasks with Material UI Cards
- [x] Add/Edit/Delete Tasks – Use Material UI Dialog & Forms
- [x] Task Status – Checkbox for marking tasks as completed
- [x] Filter Tasks – Dropdown to filter by status
- [x] Dark Mode Support – Material UI ThemeProvider

## 📝 Detailed Notes

### 1. Dashboard UI — Task List with Material UI Cards
Each task is displayed as a `<Card>` from MUI. The dashboard is a `<Grid container>` that renders a `<Grid item>` (card) for every task in state.
```tsx
{tasks.map(task => (
    <Grid item xs={12} md={6} key={task.id}>
        <Card variant="outlined">
            <CardContent>
                <Typography variant="h6">{task.title}</Typography>
                <Typography variant="body2" color="text.secondary">{task.description}</Typography>
            </CardContent>
        </Card>
    </Grid>
))}
```

### 2. Add/Edit/Delete Tasks — Dialog & Forms
- **Add Task**: A floating action button (`<Fab>`) opens an MUI `<Dialog>` containing a form with `<TextField>` inputs.
- **Edit Task**: Clicking "Edit" opens the same Dialog, but pre-filled with the task's current data.
- **Delete Task**: Clicking "Delete" removes the task from the array using `filter()`.

### 3. Task Status — Checkbox for Marking Complete
Each card has an MUI `<Checkbox>`. When checked, the task's `completed` property is toggled to `true` via `useState` and the card UI changes (e.g., strikethrough text).

### 4. Filter Tasks — Dropdown to Filter by Status
An MUI `<Select>` component provides options: "All", "Completed", "Pending". The displayed task list is derived by filtering the main tasks array based on the selected filter value.

### 5. Dark Mode — Material UI ThemeProvider
```tsx
const [mode, setMode] = useState<'light' | 'dark'>('light');
const theme = createTheme({ palette: { mode } });

return (
    <ThemeProvider theme={theme}>
        <CssBaseline />   {/* Applies global dark background */}
        <App />
    </ThemeProvider>
);
```

---

## 🎓 Important Interview Questions

### Q1: How do you toggle dark mode in a React + MUI app?
Store the theme mode (`'light' | 'dark'`) in React state. Pass it to `createTheme({ palette: { mode } })` and wrap your app with `<ThemeProvider theme={theme}>`. A button that calls `setMode(prev => prev === 'light' ? 'dark' : 'light')` toggles the theme globally.

### Q2: How do you persist theme preference (dark/light) across page refreshes?
Save the user's choice to `localStorage` and read it on initial state load:
```javascript
const [mode, setMode] = useState(() => localStorage.getItem('theme') || 'light');
```


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Tech Stack HTML CSS JavaScript TypeScript Tailwind CSS](../../MERN_Study_Structure/01_Web_Development_Fundamentals/09_Tech_Stack_HTML_CSS_JavaScript_TypeScript_Tailwind_CSS/09_Tech_Stack_HTML_CSS_JavaScript_TypeScript_Tailwind_CSS.md) | [🏠 Home](../../README.md) | [Next: Reactjs ➡️](../../MERN_Study_Structure/02_Frontend_Development_React_N/01_Reactjs/01_Reactjs.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>