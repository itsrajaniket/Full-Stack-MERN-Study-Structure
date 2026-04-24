# Material UI (MUI)

## 📚 Curriculum Checklist
- [ ] Core Components
- [ ] Layout – Box, Grid, Stack, Container
- [ ] Navigation – AppBar, Drawer, Tabs
- [ ] Forms – TextField, Select, Checkbox, Radio, Autocomplete, Validations
- [ ] Buttons – Button, IconButton, Floating Action Button
- [ ] Feedback – Snackbar, Alert, Progress
- [ ] Surfaces – Card, Paper, Dialog
- [ ] Tables – Table, List, Avatar, Badge
- [ ] Theming & Customization
- [ ] Custom Theme – Colors, Typography, Shadows
- [ ] Prop & Styled API – Inline styling
- [ ] Dark Mode Switching
- [ ] Breakpoints & Responsiveness
- [ ] Material UI Official Docs (Comprehensive Guide)

## 📝 Detailed Notes

### 1. What is Material UI (MUI)?
MUI is a comprehensive library of React components that implement Google's Material Design. It's one of the most popular UI frameworks for React.

### 2. Layout Components
MUI provides specialized components for structure:
- **Box**: A wrapper component for all your CSS utility needs.
- **Grid**: A powerful responsive layout system based on a 12-column grid.
- **Stack**: A 1D layout component for arranging items vertically or horizontally with spacing.
- **Container**: Centers your content horizontally.

### 3. Navigation & Surfaces
- **AppBar**: The top navigation bar.
- **Drawer**: A sliding sidebar.
- **Card**: A container for content and actions about a single subject.
- **Paper**: A physical layer that looks like paper (elevated background).
- **Dialog**: A modal popup.

### 4. Forms & Buttons
- **TextField**: A complete form input component.
- **Buttons**: `Button` (text, outlined, contained) and `IconButton`.
- **Selection**: `Select`, `Checkbox`, `Radio`, and `Autocomplete` (for searchable lists).

### 5. Feedback & Tables
- **Snackbar**: Brief messages about an app's process (toasts).
- **Alert**: Displays important messages.
- **LinearProgress / CircularProgress**: Loading indicators.
- **Table**: Highly customizable tables with headers and bodies.

### 6. Theming & Customization
MUI's `createTheme` and `ThemeProvider` allow you to define a global design system.
```javascript
const theme = createTheme({
  palette: {
    primary: { main: '#1976d2' },
  },
});
```
- **Styled API**: `styled(Component)({ ...styles })` for custom-styled components.
- **sx Prop**: Fast way to apply styles directly to components: `<Box sx={{ p: 2, m: 1 }} />`.

---

## 🎓 Important Interview Questions

### Q1: What is the purpose of the `sx` prop in MUI?
The `sx` prop is a shortcut for defining custom styles that has access to the theme. It allows you to write CSS-in-JS directly on the component without creating a separate styled component.

### Q2: How does the MUI Grid system work?
The Grid system is based on a 12-column layout. You use a `<Grid container>` wrapper and `<Grid item>` children. You define the width using props like `xs`, `sm`, `md`, `lg` (e.g., `<Grid item xs={6}>` takes half the width on extra-small screens).

### Q3: What is the difference between `Paper` and `Card`?
- **Paper**: A simple container that provides elevation (shadow) to give a sense of depth.
- **Card**: A more complex component that follows Material Design's card specification, often including sections like `CardHeader`, `CardContent`, and `CardActions`.

### Q4: How do you implement Dark Mode in MUI?
You use the `createTheme` function with the `mode` property set to 'dark' or 'light'. You then wrap your app in a `ThemeProvider` and pass the generated theme.

### Q5: What is the `ThemeProvider`?
It is a wrapper component that provides the theme configuration to all child components via the React Context API. Without it, MUI components use the default theme.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Tailwind CSS](../../MERN_Study_Structure/01_Web_Development_Fundamentals/04_Tailwind_CSS/04_Tailwind_CSS.md) | [🏠 Home](../../README.md) | [Next: Javascript ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/06_Javascript/06_Javascript.md)