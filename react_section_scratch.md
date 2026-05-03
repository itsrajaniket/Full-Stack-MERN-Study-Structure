# ⚛️ React.js (Vite / Next.js)
> 🚀 **Modern Frontend Development with React**

<div align='center'>
  <img src='https://img.shields.io/badge/React-19-61DAFB?style=for-the-badge&logo=react&logoColor=black' />
  <img src='https://img.shields.io/badge/Level-Fresher_to_Pro-FF4500?style=for-the-badge&logo=target&logoColor=white' />
  <img src='https://img.shields.io/badge/Stack-MERN-green?style=for-the-badge&logo=mongodb&logoColor=white' />
  <img src='https://img.shields.io/badge/Frequency-High-red?style=for-the-badge&logo=fire&logoColor=white' />
</div>

---

| ✍️ Author | 📅 Last Updated | 🎓 Level | ⏱️ Est. Read Time |
| :--- | :--- | :--- | :--- |
| [Aniket Raj](https://github.com/itsrajaniket) | April 2025 | Intermediate | 30 mins |

---

## 📌 Table of Contents
1. [📚 Curriculum Checklist](#-curriculum-checklist)
2. [🏗️ Core Fundamentals](#️-core-fundamentals)
3. [🎣 Hooks — The Complete Guide](#-hooks--the-complete-guide)
4. [🚦 React Router](#-react-router)
5. [🌐 State Management](#-state-management)
6. [📡 API Handling](#-api-handling)
7. [⚡ Performance Optimization](#-performance-optimization)
8. [🛠️ Custom Hooks](#️-custom-hooks)
9. [🛡️ Advanced Patterns & Security](#️-advanced-patterns--security)
10. [🚀 React 19 & Beyond](#-react-19--beyond)
11. [🧪 Testing](#-testing)
12. [❓ Interview Questions](#-interview-questions)

---

## 📚 Curriculum Checklist
- [x] React Basics – JSX, Components, Props, State
- [x] Event Handling & Forms
- [x] Hooks – useState, useEffect, useRef, useContext, useReducer
- [x] React Router – Navigation & Route Parameters
- [x] State Management – Context API, Redux Toolkit, Zustand
- [x] API Handling – Fetch, Axios, React Query (TanStack)
- [x] Performance Optimization – Memoization, Lazy Loading
- [ ] [React Docs](https://react.dev/reference/react)
- [ ] [React Tutorial](https://react.dev/learn) (Video)

---

## 🏗️ Core Fundamentals

### 1. JSX, Components, Props & State
**JSX** is a syntax extension that looks like HTML but compiles to `React.createElement()`. It allows us to write HTML-like structures inside JavaScript.
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

> [!TIP]
> **Virtual DOM Visualization**
> React uses a "diffing" algorithm to update the DOM efficiently.
> ```mermaid
> graph TD
>   A[State Change] --> B[New Virtual DOM]
>   B --> C{Diffing Algorithm}
>   D[Old Virtual DOM] --> C
>   C --> E[Compute Minimal Changes]
>   E --> F[Update Real DOM]
> ```

---

## 🎣 Hooks — The Complete Guide

Hooks are functions that let you "hook into" React state and lifecycle features from function components.

#### `useState` — Local State
Used for tracking data that changes over time within a component.
```tsx
const [count, setCount] = useState(0);

// ❌ Incorrect: setCount(count + 1);
// ✅ Correct: Use functional form for dependent updates
setCount(prev => prev + 1); 
```

#### `useEffect` — Side Effects
Always include a dependency array to avoid infinite loops!
```tsx
useEffect(() => {
    // 1. Setup Logic (API calls, subscriptions)
    const timer = setInterval(() => console.log('Tick'), 1000);

    // 2. Cleanup Logic (Runs on unmount)
    return () => clearInterval(timer);
}, []); // [] = Mount only | [val] = Run on change | No array = Every render
```

---

## 🎓 Important Interview Questions

### **Q1. What is React and why is it used?** `[Fresher]`

* React — open-source JavaScript library for building user interfaces, developed by Facebook (Meta)  
* Library not framework — handles only the view layer, pair with other tools for routing, state, data fetching  
* Component-based — UI split into reusable, independent pieces  
* Virtual DOM — React maintains lightweight copy of real DOM, diffs changes, updates only what changed  
* Declarative — describe what UI should look like for a given state, React handles DOM updates  
* Unidirectional data flow — data flows down from parent to child via props  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "React is a declarative, component-based JavaScript library used for building highly interactive user interfaces. Its core strength lies in the Virtual DOM, which allows it to update the UI efficiently by calculating the minimal set of changes required. In a MERN stack, React handles the entire front-end 'View' layer, providing a seamless single-page application experience by communicating with the Node/Express backend via APIs."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Components**: Think of them as custom HTML elements (e.g., `<Navbar />`, `<ProfileCard />`) that can be reused across the app.
    - **Declarative UI**: Instead of telling the browser *how* to change (imperative), you tell React *what* you want the UI to look like based on current state, and React handles the "how."

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: To truly stand out, you must understand **React Fiber**. Fiber is the reconciliation engine that allows React to pause, abort, or reuse work. This is what enables **Concurrent Rendering** in React 18/19. Instead of the browser getting "stuck" during a heavy render, React can prioritize user interactions (like typing) over background rendering.

### 4. 🪤 The "Trap" & The "Escape" (Common Pitfalls)
- **The Trap**: Interviewers often ask, "Since React is so popular, why not just call it a Framework?"
- **The Escape**: "React is strictly a **Library** because it only manages the UI (the View). Unlike a Framework (like Angular), it doesn't dictate how you handle routing or state management. However, when used within the **Next.js ecosystem**, it effectively becomes part of a framework. This distinction highlights React's modularity."

### 5. 🔄 Dynamic Follow-Up Flow (Topic Mastery)
- **Follow-up Q1**: "What is Reconciliation?"
    - **A**: It is the "diffing" process where React compares the new Virtual DOM with the previous one to calculate the minimal set of changes needed for the real DOM.
- **Follow-up Q2**: "How does React 18's Automatic Batching improve performance?"
    - **A**: It groups multiple state updates (even in async code) into a single re-render, reducing the "work" the browser has to do.

---

### **Q2. What is JSX and how does it work?** `[Fresher]`

* JSX — JavaScript XML, syntax extension that looks like HTML but is JavaScript  
* Babel transpiles JSX to React.createElement() calls at build time  
* JSX rules:  
  * Must return single root element — wrap in fragment <> </> or parent element if multiple  
  * All tags must be closed — <br />, <img />, <input />  
  * className instead of class — class is reserved keyword in JS  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "JSX (JavaScript XML) is syntactic sugar that allows us to write HTML-like structures inside JavaScript. Under the hood, tools like Babel or SWC transpile JSX into `React.createElement()` function calls, which return plain JavaScript objects representing the UI."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Transpilation**: Since browsers can't read JSX, we need build tools to convert it into browser-readable JavaScript.
    - **The Virtual DOM Link**: Each JSX element represents a node in the Virtual DOM tree.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: A pro knows about the **New JSX Transform** introduced in React 17. Previously, you had to `import React from 'react'` in every file because JSX was compiled to `React.createElement`. Now, the compiler automatically imports the necessary functions from `react/jsx-runtime`, resulting in smaller bundle sizes and cleaner code.

### 4. 🪤 The "Trap" & The "Escape" (Common Pitfalls)
- **The Trap**: Interviewers might ask, "Can the browser read JSX directly? And why do we need a single root element?"
- **The Escape**: "No, browsers only understand plain JavaScript. JSX must be transpiled. We need a single root because JSX is converted into a function call, and a JavaScript function can only return **one** value (one object). If we need multiple elements, we use `<Fragment>` to avoid adding unnecessary nodes to the DOM."

---

### **Q3. What are React components and what are the types?** `[Fresher]`

* Component — reusable, self-contained piece of UI, returns JSX  
* Function components — plain JavaScript functions returning JSX, modern standard  
* Hooks (React 16.8+) made function components as powerful as class components  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "Components are the building blocks of a React app. They are independent, reusable pieces of UI. Historically, we had Class Components, but modern React almost exclusively uses **Functional Components** because they are more concise and use Hooks for logic."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Functional vs Class**: Class components use `this` and lifecycle methods (like `componentDidMount`), whereas Functional components use Hooks (like `useEffect`) for the same tasks.
    - **Naming Convention**: Always use **PascalCase** for components (e.g., `MyProfile`) to distinguish them from standard HTML tags.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: A senior-lite candidate understands **Component Composition over Inheritance**. Instead of trying to build complex hierarchies, we use patterns like **Compound Components** (like a `Select` and its `Options`) and **Higher-Order Components (HOCs)** to share logic. You should also mention **Pure Components** (or `React.memo`), which prevent re-renders if props haven't changed.

---

### **Q4. What are Props in React and how do they work?** `[Fresher]`

* Props — short for properties, read-only data passed from parent to child component  
* Unidirectional — props flow down, never up (to change parent state, pass callback function as prop)  
* Props are immutable — child cannot modify received props  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "Props (properties) are used to pass data from a parent component to a child. They are **read-only** (immutable) and follow a one-way data flow. If a child needs to 'talk back' to the parent, the parent must pass a function as a prop."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **One-Way Flow**: Data always moves from Parent to Child. This makes the application state predictable and easier to debug.
    - **Immutability**: A component should never modify its own props. If you need mutable data, use **State**.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: Experience shows that props can cause performance issues if not handled carefully. Mention **Referential Integrity**: if you pass a new object or function as a prop on every render, the child will re-render even if the data is the same. Use `useCallback` or `useMemo` to stabilize these props. Also, mention the power of the **`children` prop** for creating flexible wrapper components (Layouts).

---

### **Q5. What is State in React and how does it work?** `[Fresher]`

* State — data that changes over time and causes component to re-render when updated  
* useState hook — primary way to add state to function components  
* State updates are asynchronous — React batches multiple state updates for performance  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "State is the 'internal memory' of a component. Unlike props, state is managed within the component and can be updated using the `useState` hook. When state changes, React triggers a re-render to update the UI."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Reactive Data**: State is what makes a React app interactive. When the user types or clicks, we update state, and React handles the UI updates.
    - **Persistence**: Unlike local variables within the function, state is preserved between re-renders by React.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: A pro knows that **State is Asynchronous**. If you call `setCount(count + 1)` and immediately `console.log(count)`, you'll see the old value. To fix this, we use the **functional update pattern** (`prev => prev + 1`). Also, talk about **State Batching** in React 18, where React groups multiple updates into one render even inside promises or timeouts.

---

### **Q6. What is "Lifting State Up" and why is it important?** `[Fresher]`

* Moving state to the closest common ancestor of components that need it.  
* Ensures multiple components stay in sync.  
* Fundamental for React's unidirectional data flow.  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "'Lifting State Up' is a pattern where you move shared state to the nearest common parent component. This allows sibling components to stay in sync because they both receive the same 'source of truth' via props."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Shared State**: If Component A and Component B need the same data, don't store it in both. Store it in Parent C.
    - **Callbacks**: The parent passes the state to children as props, and passes "setter functions" as callbacks so children can request changes.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: A pro understands that lifting state up is the first step toward avoiding complex state management libraries. However, if you lift state too high (e.g., to the root), you might cause **Prop Drilling**. In those cases, we switch to **Context API** or **Zustand**. A senior tip is to keep state "as local as possible" to minimize unnecessary re-renders.

---

### **Q7. How does event handling work in React?** `[Fresher]`

* React uses synthetic events — cross-browser wrapper around native DOM events  
* camelCase event names — onClick, onChange, onSubmit  
* Pass function reference, not call — onClick={handleClick}  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "React uses **SyntheticEvents**, which are cross-browser wrappers around the browser's native events. This ensures that your code works consistently across Chrome, Firefox, and Safari. Events in React are named in camelCase (e.g., `onClick`, `onChange`) and you pass a function reference rather than a string."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Synthetic vs Native**: While it feels like native JS, React wraps events to normalize behavior across browsers (e.g., how `onChange` works on an input).
    - **Performance**: React 17+ attaches events to the root container rather than `document`, improving integration with other libraries.

---

### **Q8. How do you handle forms in React?** `[Fresher]`

* Controlled components — React state controls input values, recommended approach.  
* Uncontrolled components — DOM manages input values, access via ref.  
* e.preventDefault() — used to stop page reload on submit.  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "Forms in React are primarily **Controlled Components**, where the input value is tied to React state. Every keystroke updates the state, and the state drives the UI. This makes the form predictable and easy to validate."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Controlled**: React is the "source of truth." It's easier to implement features like instant feedback or disabling buttons.
    - **Uncontrolled**: The DOM is the "source of truth." It's faster to implement for simple forms or when performance is a critical bottleneck.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: While controlled forms are standard, they can be slow for very large forms because every keystroke re-renders the component. For high-performance forms, use **Uncontrolled Components** with `useRef` or a library like **React Hook Form**. React Hook Form uses refs internally to minimize re-renders, which is the industry standard for complex MERN dashboards.

---

### **Q9. What is the difference between Library and Framework?** `[Fresher]`

* **Library (React)**: You are in control. You choose the routing, state management, and structure. "You call the library."  
* **Framework (Angular/Next.js)**: The framework is in control. It dictates the structure and flow. "The framework calls you."  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "React is a library because it only handles the UI (the View). You have to choose other libraries for routing (React Router) and state (Redux). Next.js, on the other hand, is a framework built on top of React that provides built-in routing, optimization, and server-side features out of the box."

---

### **Q10. How do you handle Conditional Rendering in React?** `[Fresher]`

* **Ternary Operator**: `{isLoggedIn ? <UserMenu /> : <LoginButton />}`  
* **Logical AND (&&)**: `{hasNotifications && <Badge />}`  
* **Switch / If-Else**: Used inside the function body to return different JSX blocks.  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "Conditional rendering in React works just like JavaScript. You can use `if` statements or ternary operators to decide which JSX to return. For simple 'show/hide' logic, the `&&` operator is the most concise way to render an element only if a condition is true."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Ternary**: Best for "Either/Or" scenarios.
    - **AND (&&)**: Best for "Show or Nothing" scenarios.
    - **Early Return**: You can return `null` if you want a component to render nothing at all.

### 3. 💎 The "Stand-Out" Edge (Junior-to-Mid Level Insight)
- **The Pro Perspective**: A pro avoids "Nested Ternaries" which are hard to read. Instead, they extract conditional logic into variables or small helper components. A common trap with `&&` is rendering the number `0` (e.g., `{items.length && <List />}` will render `0` if the list is empty). A senior developer always uses boolean checks like `{items.length > 0 && <List />}`.

---

### **Q11. Why are "Keys" important in React lists?** `[Fresher]`

* Keys help React identify which items have changed, been added, or been removed.  
* Must be unique among siblings.  
* Avoid using array index as a key for dynamic lists.  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "Keys are unique identifiers that help React's **Reconciliation** algorithm track list items efficiently. Without keys, React has to re-render the entire list whenever one item changes. With keys, it only updates the specific DOM node that was modified."

### 2. 🟢 The Strong Foundation (Concept Expansion)
- **Concept Breakdown**: 
    - **Stability**: Keys should be stable (don't change on re-renders) and unique (like an ID from the database).
    - **The Index Trap**: Using the array index as a key can lead to bugs in sorting, filtering, or deleting items, as the index of an item changes when others are removed.

---

### **Q12. What is useState and how does it work?** `[Fresher]`

* Returns array with current state and setter function.  
* Triggers re-render on update.  
* Functional updates prevent stale closures.  

### 1. 🎙️ The "Interview-Ready" Script
- **How to Answer It**: "`useState` allows you to track data that changes over time. It returns the current state and a setter function. A common pattern is **Lazy Initialization**, where you pass a function to `useState` to perform expensive logic (like reading from `localStorage`) only once during the initial mount."

---

### **Q13. What is useEffect and how does it work?** `[Fresher]`

* Performs side effects (API calls, subscriptions).  
* Runs after render.  
* Dependency array controls when it re-runs.  
* Cleanup function prevents memory leaks.  

---

### **Q14. What is useRef and what are its use cases?** `[Fresher]`

* Persists values across renders without triggering re-render.  
* Accesses DOM elements directly.  
* Stores mutable values (timer IDs, WebSockets).  

---

### **Q15. What is useContext and how does it solve prop drilling?** `[Fresher]`

* Consumes Context API data without nesting.  
* Shares "global" data like themes or auth.  
* Pair with `useMemo` to optimize performance.  

---

### **Q16. What is useReducer and when to use it over useState?** `[1-2 yrs]`

* Managed complex state with Reducer/Action pattern.  
* Best for state with multiple sub-values or complex transitions.  

---

### **Q17. What is React Router and how to set up routing?** `[Fresher]`

* Enables client-side navigation (SPA).  
* `BrowserRouter`, `Routes`, `Route`, `Link`.  
* `useNavigate` for programmatic navigation.  

---

### **Q18. How do you handle route parameters and protected routes?** `[1-2 yrs]`

* `useParams()` for dynamic segments (`/user/:id`).  
* Wrapper components for authentication guards.  

---

### **Q19. What is Redux Toolkit and how does it work?** `[1-2 yrs]`

* Centralized global store.  
* `createSlice` reduces boilerplate.  
* `useSelector` and `useDispatch` hooks.  

---

### **Q20. What is RTK Query and how does it simplify API calls?** `[2-3 yrs]`

* Data fetching and caching built into Redux.  
* Tag-based cache invalidation.  

---

### **Q21. How do you handle API calls in React?** `[Fresher]`

* Fetch/Axios in `useEffect`.  
* AbortController for cleanups.  
* Centralized Axios instances with interceptors.  

---

### **Q22. What is React Query (TanStack Query) and why use it?** `[1-2 yrs]`

* Server state management.  
* Automatic caching and background refetching.  

---

### **Q23. What is React.memo and when should you use it?** `[1-2 yrs]`

* HOC that skips re-render if props are same.  
* Pair with `useCallback` and `useMemo`.  

---

### **Q24. What are useMemo and useCallback?** `[1-2 yrs]`

* `useMemo`: Caches calculated value.  
* `useCallback`: Caches function instance.  

---

### **Q25. What is code splitting and lazy loading?** `[1-2 yrs]`

* `React.lazy` and `Suspense`.  
* Reduces initial bundle size.  

---

### **Q26. What is the React component lifecycle?** `[1-2 yrs]`

* Mount, Update, Unmount.  
* Mapping class methods to hooks.  

---

### **Q27. What are React Portals and when to use them?** `[2-3 yrs]`

* Render outside parent DOM hierarchy.  
* Modals, tooltips, dropdowns.  

---

### **Q28. What are Error Boundaries?** `[2-3 yrs]`

* Class components that catch JS errors in children.  
* Prevent entire app from crashing on one error.  

---

### **Q29. What is the difference between Shadow DOM and Virtual DOM?** `[2-3 yrs]`

* **Virtual DOM**: React's internal blueprint for performance.  
* **Shadow DOM**: Browser's tool for CSS encapsulation (Web Components).  

---

### **Q30. What's new in React 18/19?** `[Fresher]`

* **React 18**: Concurrent Rendering, Automatic Batching, Transitions.  
* **React 19**: Actions API, `use` hook, Document Metadata.  

---

### **Q31. How do you handle SEO in a React app?** `[1-2 yrs]`

* **SSR (Next.js)** is the best solution.  
* `react-helmet` for dynamic meta tags.  
* Prerendering services.  

---

That is the complete React.js section — 31 questions with full subtopic depth, ready to merge into your MERN Interview Kit.
