# Frontend Development Overview (React, Next.js, ShadCN)

## 📚 Core Topics Covered

1. **React.js**
   - JSX, functional components, props & state (`useState`).
   - Event handling, controlled/uncontrolled forms.
   - Hooks: `useEffect`, `useRef`, `useContext`, `useReducer`, `useMemo`, `useCallback`.
   - React Router v6 (nested routes, `useParams`).
   - State management: Context API **and** Redux Toolkit (store, slices, `useSelector`, `useDispatch`).
   - Data fetching: Fetch API, Axios, React Query (caching, stale‑while‑revalidate).
   - Performance: `React.memo`, lazy loading (`React.lazy` + `Suspense`), code‑splitting.
   - **Testing**: React Testing Library basics – rendering, querying, fire events, asserting.
   - **Accessibility**: ARIA roles, keyboard navigation, using `role` and `aria-*` attributes.

2. **Next.js (v13+ App Router)**
   - File‑based routing (`app/page.tsx`, dynamic segments `app/blog/[slug]/page.tsx`).
   - Layout hierarchy (`layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`).
   - Server vs Client components (`'use client'`).
   - Data fetching strategies: Server Component fetch, `getServerSideProps`, `getStaticProps` with ISR (`revalidate`).
   - API Routes (`app/api/.../route.ts`).
   - Middleware for auth/redirects; NextAuth.js integration.
   - Rendering strategies: SSR, SSG, ISR, CSR.
   - Image Optimization (`next/image`).
   - SEO: `metadata` export, `generateMetadata()` for dynamic SEO.
   - Environment variables (`process.env.NEXT_PUBLIC_…`).
   - Deployment basics (Vercel, CI/CD).

3. **ShadCN/UI**
   - Installation via `npx shadcn-ui@latest init` and `add` commands.
   - Core components: `Button`, `Card`, `Dialog`, `AlertDialog`, `Form` (with `react-hook-form` + `zod`).
   - Tailwind CSS theming with CSS variables (`--primary`, `--background`).
   - Utility `cn()` for class merging.
   - Customizing components by editing the generated TSX files.

4. **Integration of Tailwind, MUI & ShadCN**
   - Unified design system: MUI theming (`createTheme`) + ShadCN CSS variables.
   - Choosing one UI framework per project to avoid CSS conflicts.
   - Reusable component pattern (`children`, `className`, TypeScript generics).

5. **Project Features (Task Manager & E‑Commerce)**
   - CRUD with TypeScript types, `crypto.randomUUID()` IDs.
   - Drag‑and‑drop via `react-beautiful-dnd`.
   - Toast notifications (`useToast`).
   - Local storage persistence (`useEffect` with lazy initializer).
   - Modal dialogs (`Dialog`) and destructive confirmations (`AlertDialog`).

## 🎓 Quick Interview Questions

- **React**: Explain the Virtual DOM and reconciliation algorithm.
- **Hooks**: When to prefer `useReducer` over multiple `useState` calls?
- **React Router**: What is prop drilling and how to solve it?
- **Testing**: How do you test async UI updates with React Testing Library?
- **Next.js**: Differences between Server, Client, and Shared components?
- **ISR**: How does Incremental Static Regeneration work?
- **Middleware**: What is the order of execution for middleware vs API routes?
- **ShadCN**: Why is ShadCN considered “copy‑and‑own” compared to MUI?
- **Performance**: How does `React.memo` differ from `useMemo`?
- **SEO**: How to generate dynamic Open Graph tags in Next.js?
- **Deployment**: What environment variables are safe to expose to the browser?

---

## ❓ Questions & Doubts
- [ ] Add any further topics you feel need deeper coverage.
