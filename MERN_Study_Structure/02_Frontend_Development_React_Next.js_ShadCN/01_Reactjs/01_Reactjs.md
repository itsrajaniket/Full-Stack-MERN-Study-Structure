# React.js (Vite/CRA)

## 📚 Curriculum Checklist
- [ ] React Basics – JSX, Components, Props, State
- [ ] Event Handling & Forms
- [ ] Hooks – useState, useEffect, useRef, useContext, useReducer
- [ ] React Router – Navigation & Route Parameters
- [ ] State Management – Context API, Redux Toolkit (optional)
- [ ] API Handling – Fetch, Axios, React Query
- [ ] Performance Optimization – Memoization, Lazy Loading
- [ ] [React Docs](https://react.dev/reference/react)
- [ ] [React Tutorial](https://react.dev/learn) (Video)

## 📝 Detailed Notes

### 1. JSX, Components, Props & State
**JSX** is a syntax extension that looks like HTML but compiles to `React.createElement()`.
```tsx
// Functional Component with Props
interface CardProps { title: string; count: number; }
const Card = ({ title, count }: CardProps) => (
    <div className="card">
        <h2>{title}</h2>
        <p>{count}</p>
    </div>
);
```
- **Props**: Read-only data passed from parent → child.
- **State**: Local mutable data managed with `useState`.

### 2. Event Handling & Forms
```tsx
const [value, setValue] = useState('');

const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // Prevent page reload
    console.log(value);
};

return (
    <form onSubmit={handleSubmit}>
        <input value={value} onChange={(e) => setValue(e.target.value)} />
        <button type="submit">Submit</button>
    </form>
);
```

### 3. Hooks — The Complete Guide

#### `useState` — Local State
```tsx
const [count, setCount] = useState(0);
setCount(prev => prev + 1); // Always use functional form for dependent updates
```

#### `useEffect` — Side Effects
```tsx
useEffect(() => {
    // Runs after every render (no deps)
    // Add cleanup by returning a function
    return () => { /* cleanup */ };
}, []); // Empty array = run only once on mount
// [dep] = run when dep changes
```

#### `useRef` — DOM Reference / Persistent Value
```tsx
const inputRef = useRef<HTMLInputElement>(null);
inputRef.current?.focus(); // Focus the input
```

#### `useContext` — Consume Context
```tsx
const theme = useContext(ThemeContext);
```

#### `useReducer` — Complex State Logic
```tsx
const reducer = (state, action) => {
    switch(action.type) {
        case 'increment': return { count: state.count + 1 };
        default: return state;
    }
};
const [state, dispatch] = useReducer(reducer, { count: 0 });
dispatch({ type: 'increment' });
```

#### `useMemo` & `useCallback` — Performance
- **`useMemo`**: Memoizes a **value** (avoids expensive recalculations).
- **`useCallback`**: Memoizes a **function** (avoids unnecessary re-renders in child components).
```tsx
const expensiveValue = useMemo(() => computeHeavy(data), [data]);
const handleClick = useCallback(() => doSomething(id), [id]);
```

### 4. React Router — Navigation & Route Parameters
```tsx
import { BrowserRouter, Routes, Route, Link, useParams } from 'react-router-dom';

function App() {
    return (
        <BrowserRouter>
            <nav><Link to="/users/1">User 1</Link></nav>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/users/:id" element={<UserDetail />} />
                <Route path="*" element={<NotFound />} />
            </Routes>
        </BrowserRouter>
    );
}

// Reading URL params
const UserDetail = () => {
    const { id } = useParams();
    return <p>User: {id}</p>;
};
```

### 5. State Management — Context API & Redux Toolkit

#### Context API (Built-in)
```tsx
const ThemeContext = createContext<'light' | 'dark'>('light');

// Provider wraps the app
<ThemeContext.Provider value="dark"><App /></ThemeContext.Provider>

// Consumer in any child
const theme = useContext(ThemeContext);
```

#### Redux Toolkit (RTK)
```tsx
// store/counterSlice.ts
import { createSlice } from '@reduxjs/toolkit';
const counterSlice = createSlice({
    name: 'counter',
    initialState: { value: 0 },
    reducers: {
        increment: state => { state.value += 1; },
    },
});
export const { increment } = counterSlice.actions;
export default counterSlice.reducer;

// In component
const count = useSelector(state => state.counter.value);
const dispatch = useDispatch();
dispatch(increment());
```

### 6. API Handling — Fetch, Axios, React Query
```tsx
// React Query (TanStack) — Best Practice
import { useQuery } from '@tanstack/react-query';

const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => axios.get('/api/users').then(r => r.data),
});
// Auto caching, refetching, loading states — no boilerplate
```

### 7. Performance Optimization
- **`React.memo`**: Wraps a component to prevent re-render if props didn't change.
- **`useMemo` / `useCallback`**: Memoize values and functions.
- **Lazy Loading**: Load components only when needed.
```tsx
const HeavyChart = React.lazy(() => import('./HeavyChart'));

<Suspense fallback={<Spinner />}>
    <HeavyChart />
</Suspense>
```
- **Code Splitting**: React automatically splits at lazy() boundaries.
- **Avoid unnecessary state**: Derived data should not be in state.

---

## 🎓 Important Interview Questions

### Q1: What is the Virtual DOM and how does React use it?
React keeps a lightweight in-memory copy of the real DOM (Virtual DOM). When state changes, React re-renders the Virtual DOM, diffs it against the previous version (reconciliation), and only updates the **real** DOM nodes that actually changed — making updates very fast.

### Q2: Difference between `useEffect` with `[]`, `[dep]`, and no array?
- `[]`: Runs **once** on mount.
- `[dep]`: Runs on mount **and** whenever `dep` changes.
- No array: Runs after **every** render (usually a bug).

### Q3: What is "prop drilling" and how do you solve it?
Prop drilling is passing data through many intermediate components that don't need it, just to get it to a deeply nested child. Solutions: **Context API**, **Redux**, or **Zustand**.

### Q4: What is the difference between controlled and uncontrolled components?
- **Controlled**: Form value is stored in React state (`value={val}`). React is the single source of truth.
- **Uncontrolled**: Form value is stored in the DOM, accessed via a `ref`.

### Q5: When would you use `useReducer` over `useState`?
When state logic is complex (multiple sub-values, next state depends on previous), or when multiple state updates need to happen together. It also makes testing easier.

### Q6: What is React's reconciliation algorithm?
React's "diffing" algorithm that compares the new Virtual DOM tree to the old one. Rules:
1. Different element types → rebuild the whole tree.
2. Same element type → update changed attributes.
3. Lists → use `key` prop to identify which items changed.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Features](../../MERN_Study_Structure/01_Web_Development_Fundamentals/10_Features/10_Features.md) | [🏠 Home](../../README.md) | [Next: Nextjs for Full-Stack Development ➡️](../../MERN_Study_Structure/02_Frontend_Development_React_N/02_Nextjs_for_Full-Stack_Development/02_Nextjs_for_Full-Stack_Development.md)