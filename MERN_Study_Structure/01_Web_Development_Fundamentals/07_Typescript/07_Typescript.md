# Typescript (TS)

## 📚 Curriculum Checklist
- [x] What is TypeScript & Why Use It?
- [x] Type Annotations (string, number, boolean, any, void, never)
- [x] Type Inference
- [x] Interfaces & Types
- [x] Enums
- [x] Functions with TypeScript (Return Types, Optional & Default Parameters)
- [x] Type Aliases vs. Interfaces
- [x] Union & Intersection Types
- [x] Generics (Array<T>, Promise<T>, Function<T>)
- [x] Type Assertion (as, <T>)
- [x] Utility Types (Partial<>, Readonly<>, Record<>)
- [x] Mapped & Conditional Types
- [x] Working with Modules (export / import)
- [x] TS with React & Next.js
- [x] TS with Node.js & Express
- [x] Error Handling & Debugging
- [x] Typescript Official Docs
- [x] Typescript (Video tutorial)

## 📝 Detailed Notes

### 1. What is TypeScript?
TypeScript is a strongly typed superset of JavaScript. It provides a way to describe the shape of an object, providing better documentation and allowing TypeScript to validate that your code is working correctly.

### 2. Basic Types
- **Boolean, Number, String**: Basic primitives.
- **Arrays**: `number[]` or `Array<number>`.
- **Tuples**: Fixed length array with specific types `[string, number]`.
- **Enums**: Set of named constants `enum Color {Red, Green, Blue}`.
- **Any, Unknown, Void, Never**: Special types for flexibility and strictness.

### 3. Interfaces & Types
- **Interfaces**: Used to define the structure of objects. Supports inheritance (`extends`).
- **Type Aliases**: Can define primitives, unions, and intersections.
```typescript
interface User { id: number; name: string; }
type ID = string | number;
```

### 4. Unions & Intersections
- **Unions**: `string | number`.
- **Intersections**: Combining multiple types `TypeA & TypeB`.

### 5. Generics
Generics provide a way to make components work over a variety of types rather than a single one.
```typescript
function wrapInArray<T>(val: T): T[] { return [val]; }
```

### 6. Casting (Type Assertions)
Telling the compiler "trust me, I know what I'm doing".
- `(someValue as string)` or `<string>someValue`.

### 7. Optional & Readonly Properties
- **Optional**: `property?: type`.
- **Readonly**: `readonly property: type`.

### 8. Functions with TypeScript
```typescript
// Return type + optional param + default param
function add(a: number, b: number = 10): number { return a + b; }
function greet(name: string, greeting?: string): string {
    return `${greeting ?? 'Hello'} ${name}`;
}
```

### 9. Utility Types
Built-in generic types that transform other types:
- **`Partial<T>`**: Makes all properties optional.
- **`Required<T>`**: Makes all properties required.
- **`Readonly<T>`**: Makes all properties read-only.
- **`Record<K, V>`**: Creates a type with keys of type K and values of type V.
- **`Pick<T, K>`**: Picks specific properties from a type.
- **`Omit<T, K>`**: Removes specific properties from a type.

### 10. Mapped & Conditional Types
```typescript
// Mapped Type - make all props nullable
type Nullable<T> = { [K in keyof T]: T[K] | null };

// Conditional Type
type IsString<T> = T extends string ? 'yes' : 'no';
```

### 11. Working with Modules (export / import)
```typescript
// utils.ts
export interface User { id: number; name: string; }
export const greet = (u: User): string => `Hello ${u.name}`;

// main.ts
import { User, greet } from './utils';
```

### 12. TypeScript with React
```tsx
// Typing component props
interface ButtonProps {
    label: string;
    onClick: () => void;
    disabled?: boolean;
}
const Button: React.FC<ButtonProps> = ({ label, onClick, disabled }) => (
    <button onClick={onClick} disabled={disabled}>{label}</button>
);
```

### 13. TypeScript with Node.js & Express
```typescript
import express, { Request, Response } from 'express';
const app = express();
app.get('/users', (req: Request, res: Response) => {
    res.json({ users: [] });
});
```

---

## 🎓 Important Interview Questions

### Q1: What are the benefits of using TypeScript?
1. Catch errors early during compilation.
2. Better IntelliSense and autocomplete in editors.
3. Makes code more readable and self-documenting.
4. Easier refactoring of large codebases.

### Q2: What is the difference between `any` and `unknown`?
- **`any`**: Turns off type checking. You can do anything with it. (Avoid using this).
- **`unknown`**: A type-safe version of `any`. You must perform type checking (narrowing) before you can perform operations on an `unknown` value.

### Q3: What is "Type Inference"?
TypeScript can often guess (infer) the type of a variable based on its initial value, so you don't always have to write types explicitly.

### Q4: What are "Generics"?
Generics allow you to create reusable components/functions that work with a variety of types while still maintaining type safety.
```typescript
function identity<T>(arg: T): T { return arg; }
```

### Q5: How do you handle optional properties in an Interface?
Use the question mark (`?`) suffix after the property name.
```typescript
interface Car { brand: string; model?: string; }
```


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Javascript](../../MERN_Study_Structure/01_Web_Development_Fundamentals/06_Javascript/06_Javascript.md) | [🏠 Home](../../README.md) | [Next: Git GitHub ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/08_Git_GitHub/08_Git_GitHub.md)
