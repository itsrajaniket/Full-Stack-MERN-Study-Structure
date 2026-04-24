# Features:

## 📚 Curriculum Checklist
- [x] Task List with CRUD (Create, Update, Delete)
- [x] ShadCN Components (Dialog, Toast, Modal)
- [x] Local Storage for Data Persistence

## 📝 Detailed Notes

### 1. E-Commerce Product CRUD
Full product management with ShadCN UI components:
- **Listing** products using `<Card>` grid.
- **Adding** products via a `<Dialog>` form.
- **Editing** with pre-filled dialog (pass `selectedProduct` to state).
- **Deleting** with `<AlertDialog>` for a confirmation prompt.
```tsx
<AlertDialog>
    <AlertDialogTrigger asChild>
        <Button variant="destructive" size="sm">Delete</Button>
    </AlertDialogTrigger>
    <AlertDialogContent>
        <AlertDialogHeader>
            <AlertDialogTitle>Are you sure?</AlertDialogTitle>
            <AlertDialogDescription>This action cannot be undone.</AlertDialogDescription>
        </AlertDialogHeader>
        <AlertDialogFooter>
            <AlertDialogCancel>Cancel</AlertDialogCancel>
            <AlertDialogAction onClick={() => deleteProduct(id)}>Delete</AlertDialogAction>
        </AlertDialogFooter>
    </AlertDialogContent>
</AlertDialog>
```

### 2. ShadCN Modal (Dialog) for Product Form
Use a single `<Dialog>` component for both Add and Edit by setting a shared `isOpen` state and an optional `selectedProduct`.

### 3. Local Storage Persistence
```tsx
const STORAGE_KEY = 'products';
// Initial load
const [products, setProducts] = useState<Product[]>(() => {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : [];
});
// Auto-save on change
useEffect(() => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(products));
}, [products]);
```

---

## 🎓 Important Interview Questions

### Q1: How do you pre-fill a form for editing?
When the user clicks "Edit", set the selected item into state. Pass it to your form component as `defaultValues`. Use React Hook Form's `reset()` in a `useEffect` when `defaultValues` changes.

### Q2: What is the difference between `Dialog` and `AlertDialog` in ShadCN?
- **`Dialog`**: General purpose modal (forms, details).
- **`AlertDialog`**: Specifically designed for destructive confirmation prompts. Follows accessibility patterns where the Cancel action is focused first.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Features](../../MERN_Study_Structure/02_Frontend_Development_React_N/05_Features/05_Features.md) | [🏠 Home](../../README.md) | [Next: Nodejs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/01_Nodejs/01_Nodejs.md)