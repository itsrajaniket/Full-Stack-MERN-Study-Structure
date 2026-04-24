# Next.js for Full-Stack Development

## 📚 Curriculum Checklist
- [x] Pages & Routing – App Router (new), File-based routing
- [x] Server Components vs. Client Components
- [x] Data Fetching – getServerSideProps, getStaticProps, API Routes
- [x] Middleware & Authentication – NextAuth.js
- [x] Optimizations – Image Optimization, ISR, SSR, CSR
- [ ] [Next.js Official Docs](https://nextjs.org/docs)
- [ ] [Next.js Tutorial](https://nextjs.org/learn) (Video)

## 📝 Detailed Notes

### 1. Pages & Routing — App Router (Next.js 13+)
Next.js uses **file-based routing**. Each folder inside `app/` is a route segment.
```
app/
├── page.tsx          → /
├── about/page.tsx    → /about
├── blog/[slug]/page.tsx → /blog/my-post  (dynamic)
└── layout.tsx        → Shared layout wrapper
```
- **`layout.tsx`**: Shared UI (navbar, footer). Doesn't re-render on navigation.
- **`loading.tsx`**: Automatic loading UI (Suspense boundary).
- **`error.tsx`**: Automatic error boundary for that route segment.
- **`not-found.tsx`**: Custom 404 page.

### 2. Server Components vs. Client Components
This is the **most important** Next.js concept.

| | Server Component | Client Component |
|---|---|---|
| **Default** | Yes | No (add `'use client'`) |
| **Runs on** | Server only | Client (browser) |
| **Can use** | async/await, DB calls | useState, useEffect, browser APIs |
| **Bundle size** | Not sent to browser | Sent to browser |

```tsx
// app/users/page.tsx — Server Component (default)
async function UsersPage() {
    const users = await db.query('SELECT * FROM users'); // Direct DB access!
    return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;
}

// components/Counter.tsx — Client Component
'use client';
import { useState } from 'react';
export default function Counter() {
    const [count, setCount] = useState(0);
    return <button onClick={() => setCount(c => c+1)}>{count}</button>;
}
```

### 3. Data Fetching
#### Server Component (Recommended — Next.js 13+)
```tsx
// Fetch directly in a server component
async function ProductPage({ params }) {
    const product = await fetch(`/api/products/${params.id}`).then(r => r.json());
    return <div>{product.name}</div>;
}
```

#### `getServerSideProps` (Pages Router — Legacy)
Runs on **every request** (SSR).
```tsx
export async function getServerSideProps(context) {
    const data = await fetchData();
    return { props: { data } };
}
```

#### `getStaticProps` (Pages Router — Legacy)
Runs at **build time** (SSG). Use `revalidate` for ISR.
```tsx
export async function getStaticProps() {
    return { props: { data }, revalidate: 60 }; // ISR: re-generate every 60s
}
```

#### API Routes
Backend endpoints inside a Next.js app.
```tsx
// app/api/users/route.ts
import { NextRequest, NextResponse } from 'next/server';
export async function GET(req: NextRequest) {
    const users = await db.findAll();
    return NextResponse.json(users);
}
```

### 4. Middleware & NextAuth.js
**Middleware** runs before a request is completed — used for auth, redirects, etc.
```tsx
// middleware.ts (at project root)
import { NextResponse } from 'next/server';
export function middleware(req) {
    const token = req.cookies.get('token');
    if (!token) return NextResponse.redirect(new URL('/login', req.url));
    return NextResponse.next();
}
export const config = { matcher: ['/dashboard/:path*'] };
```

**NextAuth.js**: Full-featured authentication for Next.js.
- Supports: Google, GitHub, Credentials, and 40+ providers.
- Provides `useSession()` hook and `getServerSession()`.

### 5. Rendering Strategies & Optimizations
- **SSR** (Server-Side Rendering): HTML generated per-request. Always fresh.
- **SSG** (Static Site Generation): HTML generated at build time. Super fast.
- **ISR** (Incremental Static Regeneration): SSG + automatic background revalidation.
- **CSR** (Client-Side Rendering): Data fetched in the browser. Good for dashboards.
- **Image Optimization**: `<Image>` component auto-resizes, lazy-loads, and serves WebP.
```tsx
import Image from 'next/image';
<Image src="/hero.jpg" alt="Hero" width={800} height={600} priority />
```

### 6. Server Actions (Next.js 13.4+)
Server Actions are asynchronous functions that are executed on the server. They can be defined in Server Components and/or called from Client Components to handle form submissions and data mutations.
```tsx
// app/actions.ts
'use server'

export async function createInvoice(formData: FormData) {
  const rawFormData = {
    customerId: formData.get('customerId'),
    amount: formData.get('amount'),
  }
  // Mutate data
  // Revalidate cache
}
```

### 7. Environment Variables
Next.js has built-in support for environment variables.
- `.env.local`: Local development.
- `NEXT_PUBLIC_`: Variables prefixed with this are exposed to the browser.
- Private variables (no prefix) are only available on the server.

### 8. Dynamic Metadata (SEO)
For pages where metadata depends on dynamic data (like a blog post):
```tsx
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);
  return { title: product.name, description: product.details };
}
```

### 9. Handling Hydration Errors
A common Next.js error where the server-rendered HTML doesn't match the client-rendered HTML.
- **Causes**: Using `window` or `Date.now()` directly in the component body.
- **Fix**: Use `useEffect` to ensure code only runs on the client, or use `dynamic(() => import(...), { ssr: false })`.

### 10. Advanced Middleware Pattern (Auth & Redirects)
```tsx
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  const isPublicPath = path === '/login' || path === '/signup';
  const token = request.cookies.get('token')?.value || '';

  if (isPublicPath && token) {
    return NextResponse.redirect(new URL('/', request.nextUrl));
  }
  if (!isPublicPath && !token) {
    return NextResponse.redirect(new URL('/login', request.nextUrl));
  }
}
```

---

## 🎓 Important Interview Questions

### Q1: What is the difference between SSR, SSG, and ISR?
- **SSR**: Page built on every request. Good for highly dynamic data (e.g., user dashboards).
- **SSG**: Page built once at deploy. Good for blogs, marketing pages.
- **ISR**: A mix — page is static but automatically regenerated in the background after `revalidate` seconds.

### Q2: What is the difference between Server Components and Client Components?
Server Components run only on the server, have zero client-side JS, and can directly access databases. Client Components run in the browser, can use hooks and event listeners. You opt into Client Components with `'use client'` at the top of the file.

### Q3: When should you use `useRouter` vs `redirect()`?
- **`useRouter` (Client)**: Used inside Client Components for programmatic navigation after events (e.g., form submission).
- **`redirect()` (Server)**: Used inside Server Components, server actions, or middleware to redirect before the response is sent.

### Q4: What is `layout.tsx` and why is it powerful?
A `layout.tsx` wraps all page segments within its folder without re-rendering on navigation. This means the layout (e.g., navbar, sidebar) persists between page navigations, giving a Single Page App-like feel while using SSR.

### Q5: How does Next.js handle SEO?
- **`metadata` export**: Define `title`, `description`, `openGraph` per page from Server Components.
- **`generateMetadata()`**: Dynamic metadata (e.g., blog post title from DB).
```tsx
export const metadata = { title: 'My Page', description: '...' };
```


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Reactjs](../../MERN_Study_Structure/02_Frontend_Development_React_N/01_Reactjs/01_Reactjs.md) | [🏠 Home](../../README.md) | [Next: ShadCN ➡️](../../MERN_Study_Structure/02_Frontend_Development_React_N/03_ShadCN/03_ShadCN.md)