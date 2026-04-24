# ShadCN

## 📚 Curriculum Checklist
- [x] Installation & Setup
- [x] Using UI Components (Button, Card, Dialog, Forms, Tables, etc.)
- [x] Customizing Components (Theming & Styling)
- [x] Using with Tailwind CSS
- [ ] [ShadCN Docs](https://ui.shadcn.com/docs)

## 📝 Detailed Notes

### 1. What is ShadCN/UI?
ShadCN is **not** a component library you install as a package. It is a **collection of re-usable components** that you copy directly into your project and own completely. Built on top of **Radix UI** (accessible primitives) and **Tailwind CSS**.

### 2. Installation & Setup
```bash
npx shadcn-ui@latest init
# Configures: tailwind, tsconfig paths, components.json
# Then add individual components:
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card dialog form table
```
This creates the component file in `components/ui/button.tsx` which you can edit freely.

### 3. Using Core Components
```tsx
import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Dialog, DialogTrigger, DialogContent, DialogHeader, DialogTitle } from '@/components/ui/dialog';

// Button variants
<Button variant="default">Save</Button>
<Button variant="destructive">Delete</Button>
<Button variant="outline" size="sm">Cancel</Button>

// Dialog
<Dialog>
    <DialogTrigger asChild>
        <Button>Open</Button>
    </DialogTrigger>
    <DialogContent>
        <DialogHeader><DialogTitle>Edit Profile</DialogTitle></DialogHeader>
        {/* Form content */}
    </DialogContent>
</Dialog>
```

### 4. Forms with ShadCN + react-hook-form + Zod
ShadCN's `Form` component is a wrapper around `react-hook-form` with Zod validation.
```tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import * as z from 'zod';

const schema = z.object({ email: z.string().email() });

const form = useForm({ resolver: zodResolver(schema) });

<Form {...form}>
    <form onSubmit={form.handleSubmit(onSubmit)}>
        <FormField name="email" control={form.control} render={({ field }) => (
            <FormItem>
                <FormLabel>Email</FormLabel>
                <FormControl><Input {...field} /></FormControl>
                <FormMessage />  {/* Shows Zod validation errors */}
            </FormItem>
        )} />
        <Button type="submit">Submit</Button>
    </form>
</Form>
```

### 5. Customizing with Tailwind CSS
Since you own the component files, you can edit them directly. The design tokens are CSS variables in `globals.css`.
```css
/* globals.css */
:root {
    --primary: 221.2 83.2% 53.3%; /* Blue */
}
.dark {
    --primary: 217.2 91.2% 59.8%; /* Lighter blue in dark mode */
}
```
Change the `--primary` variable to instantly re-theme your entire app.

### 6. Typography & Icons
- **Typography**: ShadCN doesn't have a specific Typography component like MUI, but it provides a set of styles you can copy to your `globals.css` or create a reusable `Typography` component using Tailwind classes.
- **Icons**: ShadCN uses **Lucide React** by default.
```tsx
import { User, Settings, LogOut } from "lucide-react";

<Button><User className="mr-2 h-4 w-4" /> Profile</Button>
```

---

## 🎓 Important Interview Questions

### Q1: What is the fundamental difference between ShadCN and component libraries like MUI or Ant Design?
With MUI, you install a package and use components you don't control. With ShadCN, you **copy the component source code** into your project. This means full ownership, no version conflicts, and complete customizability — but also more responsibility.

### Q2: What is Radix UI and why does ShadCN use it?
Radix UI provides **unstyled, accessible, and composable** UI primitives (Dialog, Tooltip, Select, etc.) that handle all the complex ARIA attributes, keyboard navigation, and focus management. ShadCN wraps Radix primitives with Tailwind styles.

### Q3: How does ShadCN handle form validation?
ShadCN's Form component integrates with `react-hook-form` for state management and `zod` for schema-based validation. Errors are automatically displayed via the `<FormMessage />` component.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Nextjs for Full-Stack Development](../../MERN_Study_Structure/02_Frontend_Development_React_N/02_Nextjs_for_Full-Stack_Development/02_Nextjs_for_Full-Stack_Development.md) | [🏠 Home](../../README.md) | [Next: Integrating Tailwind Material UI and ShadCN in React Nextjs ➡️](../../MERN_Study_Structure/02_Frontend_Development_React_N/04_Integrating_Tailwind_Material_UI_and_ShadCN_in_React_Nextjs/04_Integrating_Tailwind_Material_UI_and_ShadCN_in_React_Nextjs.md)