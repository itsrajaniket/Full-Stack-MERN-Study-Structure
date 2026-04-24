# Javascript (JS)

## 📚 Curriculum Checklist
- [ ] Variables (var, let, const)
- [ ] Data Types (String, Number, Boolean, Object, Array)
- [ ] Operators & Type Coercion
- [ ] Functions (Regular, Arrow, Callback, Higher-Order)
- [ ] Scope & Hoisting
- [ ] ES6+ Features (Destructuring, Spread/Rest, Template Literals)
- [ ] Promises & Async/Await
- [ ] Fetch API & Axios
- [ ] DOM Manipulation & Events
- [ ] Error Handling (Try/Catch, Throw)
- [ ] Closures & Lexical Scope
- [ ] Event Loop & Asynchronous JS
- [ ] Modules (import / export)
- [ ] Object-Oriented Programming (OOP) – Prototypes, Classes
- [ ] Functional Programming – Map, Reduce, Filter
- [ ] Web Storage (LocalStorage, SessionStorage, Cookies)
- [ ] Javascript Docs
- [ ] Javascript (Video Tutorial)

## 📝 Detailed Notes

### 1. Variables, Scopes & Closures
- **`var` vs `let` vs `const`**: `var` is function-scoped; `let`/`const` are block-scoped.
- **Closures**: A function having access to its parent scope even after the parent function has closed.
- **Hoisting**: Variable and function declarations are moved to the top of their containing scope.

### 2. Data Types (Deep Dive)
- **Strings**: Immutable. Methods: `slice()`, `replace()`, `toLowerCase()`, `split()`.
- **Arrays**: `push()`, `pop()`, `shift()`, `unshift()`, `splice()`, `slice()`.
- **Objects**: Key-value pairs. `Object.assign()`, `Object.keys()`, `delete`.
- **Primitives**: `null`, `undefined`, `boolean`, `number`, `string`, `symbol`, `bigint`.

### 3. Operators & Conditionals
- **Operators**: 
  - Arithmetic: `+`, `-`, `*`, `/`, `%`, `**`.
  - Logic: `&&` (AND), `||` (OR), `!` (NOT), `??` (Nullish coalescing).
  - Comparison: `==`, `===`, `!=`, `!==`.
- **Conditionals**: `if...else`, `switch`, `Ternary (condition ? val1 : val2)`.

### 4. Loops
- **`for`**: Traditional loop.
- **`for...of`**: Iterates over values (best for Arrays).
- **`for...in`**: Iterates over keys (best for Objects).
- **`while` / `do...while`**: Conditional loops.

### 5. ES6+ Modern Syntax
- **Arrow Functions**: `() => {}`.
- **Destructuring**: `const { a, b } = obj;`.
- **Spread/Rest**: `...`.
- **Template Literals**: `` `Backticks` ``.

### 6. Functions & Asynchrony
- **Callbacks**: Functions as arguments.
- **Promises**: `.then()`, `.catch()`.
- **Async/Await**: Clean async code.
- **Event Loop**: How JS handles concurrency.

### 7. DOM Manipulation
- **Selectors**: `querySelector`, `getElementById`.
- **Events**: `addEventListener('click', ...)`.
- **Style**: `el.style.display = 'none'`.
- **Content**: `el.innerText`, `el.innerHTML`.

### 8. Fetch API & Axios
Making HTTP requests from the browser.
```javascript
// Fetch API (built-in)
const res = await fetch('https://api.example.com/data');
const data = await res.json();

// Axios (library - cleaner syntax)
const { data } = await axios.get('https://api.example.com/data');
```
- **Axios advantages**: Auto JSON parsing, request/response interceptors, better error handling.

### 9. Error Handling (try/catch/throw)
```javascript
try {
    const result = riskyOperation();
} catch (error) {
    console.error(error.message);
} finally {
    console.log('Always runs');
}
// Custom errors:
throw new Error('Something went wrong');
```

### 10. Object-Oriented Programming (OOP)
JavaScript uses prototype-based inheritance. ES6 `class` is syntactic sugar.
```javascript
class Animal {
    constructor(name) { this.name = name; }
    speak() { return `${this.name} makes a noise.`; }
}
class Dog extends Animal {
    speak() { return `${this.name} barks.`; }
}
```
- **Pillars**: Encapsulation, Inheritance, Polymorphism, Abstraction.

### 11. Functional Programming
- **Pure Functions**: Same input → same output, no side effects.
- **map()**: Transform every item → new array of same length.
- **filter()**: Keep items that pass a test → smaller array.
- **reduce()**: Boil array down to a single value.
```javascript
const doubled = [1,2,3].map(n => n * 2);       // [2,4,6]
const evens   = [1,2,3,4].filter(n => n % 2 === 0); // [2,4]
const sum     = [1,2,3].reduce((acc, n) => acc + n, 0); // 6
```

### 12. Modules (import / export)
Split code into reusable files.
```javascript
// Named export
export const greet = (name) => `Hello ${name}`;
// Default export
export default function main() {}

// Import
import { greet } from './utils.js';
import main from './main.js';
```

### 13. Web Storage (localStorage, sessionStorage, Cookies)
- **localStorage**: Persists forever, 5MB limit, sync.
- **sessionStorage**: Cleared when tab closes.
- **Cookies**: Sent with every HTTP request, useful for auth tokens.
```javascript
localStorage.setItem('user', JSON.stringify({ name: 'Aniket' }));
const user = JSON.parse(localStorage.getItem('user'));
localStorage.removeItem('user');
```

---

## 🎓 Important Interview Questions

### Q1: What is a "Closure" in JavaScript?
A closure is the combination of a function bundled together with references to its surrounding state (the lexical environment). It allows an inner function to access the scope of an outer function even after the outer function has finished executing.

### Q2: Explain Hoisting.
Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope.
- `var` is hoisted and initialized with `undefined`.
- `let` and `const` are hoisted but not initialized (leads to "Temporal Dead Zone").

### Q3: Difference between `==` and `===`?
- `==` (Abstract Equality): Checks for value after performing type conversion.
- `===` (Strict Equality): Checks for both value and type without conversion.

### Q4: What is the "Event Loop"?
The mechanism that allows JavaScript to perform non-blocking I/O operations by offloading tasks to the system kernel and then picking them up from the callback queue when the call stack is empty.

### Q5: Difference between `map()`, `filter()`, and `forEach()`?
- `forEach()`: Iterates over items (returns `undefined`).
- `map()`: Transforms each item and returns a **new** array of the same length.
- `filter()`: Returns a **new** array containing only items that pass a test.

### Q6: What is the `this` keyword?
The value of `this` is determined by how a function is called (the call site). In arrow functions, `this` is lexically inherited from the parent scope.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: Material UI](../../MERN_Study_Structure/01_Web_Development_Fundamentals/05_Material_UI/05_Material_UI.md) | [🏠 Home](../../README.md) | [Next: Typescript ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/07_Typescript/07_Typescript.md)