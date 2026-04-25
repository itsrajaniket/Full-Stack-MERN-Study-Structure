# Javascript (JS)

## 📚 Curriculum Checklist
- [x] Variables (var, let, const)
- [x] Data Types (String, Number, Boolean, Object, Array)
- [x] Operators & Type Coercion
- [x] Functions (Regular, Arrow, Callback, Higher-Order)
- [x] Scope & Hoisting
- [x] ES6+ Features (Destructuring, Spread/Rest, Template Literals)
- [x] Promises & Async/Await
- [x] Fetch API & Axios
- [x] DOM Manipulation & Events
- [x] Error Handling (Try/Catch, Throw)
- [x] Closures & Lexical Scope
- [x] Event Loop & Asynchronous JS
- [x] Modules (import / export)
- [x] Object-Oriented Programming (OOP) – Prototypes, Classes
- [x] Functional Programming – Map, Reduce, Filter
- [x] Web Storage (LocalStorage, SessionStorage, Cookies)

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

### 14. Garbage Collection & Memory Management
JavaScript automatically manages memory using **Garbage Collection**. 
- **Mark-and-Sweep Algorithm**: The engine "marks" objects that are reachable and "sweeps" the rest.
- **Memory Leaks**: Avoid global variables, forgotten timers (`setInterval`), and removed DOM elements that still have active event listeners.

### 15. Prototypal Inheritance (The Core)
Every object in JS has a hidden `[[Prototype]]` property that links to another object.
- **Prototype Chain**: If a property isn't found on an object, JS looks up the chain.
- `Array.prototype`, `Object.prototype` are the roots of most objects.

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
- [x]

---
## **JavaScript (JS) — MERN Stack Interview Kit**

---

### **1\. Variables (var, let, const)**

---

**Q1. What is the difference between `var`, `let`, and `const`?** `[Fresher]`

* `var` — function-scoped, hoisted with `undefined`, can be re-declared and re-assigned  
* `let` — block-scoped, hoisted but in Temporal Dead Zone (TDZ), cannot be re-declared, can be re-assigned  
* `const` — block-scoped, hoisted but in TDZ, cannot be re-declared or re-assigned  
* Block scope vs function scope — what counts as a block `{}`  
* Why `var` is considered problematic — leaks out of `if`/`for` blocks, global pollution  
* `const` with objects and arrays — the binding is constant, not the value (properties can still change)  
* When to use which — prefer `const` by default, use `let` when reassignment needed, avoid `var`

---

**Q2. What is the Temporal Dead Zone (TDZ)?** `[1-2 yrs]`

* Period between entering scope and the `let`/`const` declaration line being executed  
* Accessing variable in TDZ throws `ReferenceError`, not `undefined`  
* Why TDZ exists — prevents accessing variables before they are meaningfully initialized  
* TDZ applies to `let`, `const`, and `class` declarations  
* Does NOT apply to `var` — `var` is hoisted with `undefined` immediately

---

### **2\. Data Types**

---

**Q3. What are the data types in JavaScript?** `[Fresher]`

* **Primitive types** (immutable, stored by value):  
  * `String` — sequence of characters  
  * `Number` — integers and floats, `NaN`, `Infinity`  
  * `Boolean` — `true` / `false`  
  * `undefined` — declared but not assigned  
  * `null` — intentional absence of value  
  * `Symbol` — unique and immutable identifier (ES6)  
  * `BigInt` — integers beyond `Number.MAX_SAFE_INTEGER` (ES2020)  
* **Reference types** (mutable, stored by reference):  
  * `Object` — key-value pairs  
  * `Array` — ordered list (technically an object)  
  * `Function` — callable object  
  * `Date`, `Map`, `Set`, `WeakMap`, `WeakSet`  
* `typeof` operator — returns type as string, quirk: `typeof null === 'object'` (historical bug)  
* `typeof NaN === 'number'` — another common interview trap  
* Difference between `null` and `undefined` — null is explicit empty, undefined is absence of assignment

---

**Q4. What is the difference between primitive and reference types in memory?** `[1-2 yrs]`

* Primitives stored in **stack** — value itself is stored, copying creates independent copy  
* References stored in **heap** — variable holds memory address, copying copies the reference  
* Shallow copy problem with objects — `const b = a` means both point to same object  
* How to copy objects — spread `{...obj}`, `Object.assign()`, `JSON.parse(JSON.stringify())`, `structuredClone()`  
* Deep copy vs shallow copy — nested objects still share reference in shallow copy  
* `structuredClone()` — modern built-in deep clone, handles nested objects correctly  
* Why `===` comparison on objects always false for different object literals even with same content

---

**Q5. What is `NaN` and how do you check for it?** `[Fresher]`

* `NaN` — "Not a Number", result of invalid numeric operation (e.g., `"abc" * 2`)  
* `typeof NaN === 'number'` — confusing but true  
* `NaN === NaN` is `false` — NaN is the only value not equal to itself  
* `isNaN("abc")` — returns `true` but also converts string to number first (coercion issue)  
* `Number.isNaN("abc")` — returns `false` because "abc" is not NaN, it's a string (preferred)  
* `Number.isNaN(NaN)` — returns `true` (correct and reliable)

---

**Q6. What is the difference between `null` and `undefined`?** `[Fresher]`

* `undefined` — variable declared but not assigned, function that returns nothing, missing object property  
* `null` — intentional empty value, explicitly set by developer  
* `typeof undefined === 'undefined'`, `typeof null === 'object'` (bug)  
* `null == undefined` is `true` (loose equality), `null === undefined` is `false` (strict)  
* Nullish coalescing `??` — returns right side only for `null` or `undefined` (not for `0` or `""`)  
* Optional chaining `?.` — safely access nested properties without checking for null/undefined

---

### **3\. Operators & Type Coercion**

---

**Q7. What is type coercion in JavaScript?** `[Fresher]`

* Implicit type conversion done automatically by JS engine  
* **String coercion** — `"5" + 2 = "52"` (number converted to string because of `+`)  
* **Number coercion** — `"5" - 2 = 3` (string converted to number because of `-`)  
* Falsy values — `false`, `0`, `""`, `null`, `undefined`, `NaN`  
* Truthy values — everything else, including `[]`, `{}`, `"0"`, `"false"`  
* `+` is overloaded — string concatenation AND numeric addition, coercion depends on operands  
* Unary `+` operator — converts value to number: `+"5"` \= `5`, `+""` \= `0`, `+null` \= `0`, `+undefined` \= `NaN`

---

**Q8. What is the difference between `==` and `===`?** `[Fresher]`

* `==` (loose equality) — performs type coercion before comparing  
* `===` (strict equality) — no coercion, both value AND type must match  
* Tricky `==` results:  
  * `0 == false` → `true`  
  * `"" == false` → `true`  
  * `null == undefined` → `true`  
  * `null == 0` → `false`  
  * `[] == false` → `true`  
  * `[] == ![]` → `true` (classic interview trap)  
* Always prefer `===` in production code  
* `Object.is(a, b)` — like `===` but treats `NaN === NaN` as true and `-0 !== +0`

---

**Q9. What are all the JavaScript operators you should know?** `[Fresher]`

* Arithmetic — `+`, `-`, `*`, `/`, `%`, `**` (exponentiation)  
* Assignment — `=`, `+=`, `-=`, `*=`, `/=`, `**=`, `??=`, `||=`, `&&=`  
* Comparison — `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`  
* Logical — `&&`, `||`, `!`, `??` (nullish coalescing)  
* Bitwise — `&`, `|`, `^`, `~`, `<<`, `>>`  
* Ternary — `condition ? valueIfTrue : valueIfFalse`  
* Optional chaining — `?.` — safe property access  
* Spread — `...` — expand iterables  
* `typeof`, `instanceof`, `in`, `delete`, `void`  
* Logical assignment operators — `||=`, `&&=`, `??=` — ES2021

---

### **4\. Functions**

---

**Q10. What are the different ways to define a function in JavaScript?** `[Fresher]`

* **Function Declaration** — `function foo() {}` — hoisted fully  
* **Function Expression** — `const foo = function() {}` — not hoisted  
* **Arrow Function** — `const foo = () => {}` — no own `this`, `arguments`, `super`  
* **Named Function Expression** — `const foo = function bar() {}` — name only accessible inside  
* **IIFE** — Immediately Invoked Function Expression — `(function() {})()`  
* **Generator Function** — `function* gen() { yield value }` — returns iterator  
* **Async Function** — `async function foo() {}` — always returns a Promise  
* **Method shorthand in objects** — `{ foo() {} }`

---

**Q11. What is the difference between regular functions and arrow functions?** `[Fresher]`

* `this` binding:  
  * Regular function — `this` is determined by how function is **called** (dynamic)  
  * Arrow function — `this` is inherited from **enclosing lexical scope** (static)  
* Arrow functions do NOT have their own:  
  * `this`  
  * `arguments` object  
  * `prototype`  
  * Cannot be used as constructors with `new`  
* When to use arrow functions — callbacks, array methods, short expressions  
* When NOT to use arrow functions — object methods (if you need `this`), prototype methods, event handlers where `this` should refer to element, constructors  
* `arguments` object — only in regular functions, use rest `...args` in arrow functions

---

**Q12. What is a callback function?** `[Fresher]`

* A function passed as argument to another function, called later (possibly asynchronously)  
* Synchronous callback — `[1,2,3].forEach(callback)` — called immediately during execution  
* Asynchronous callback — `setTimeout(callback, 1000)` — called later after delay  
* Callback hell — deeply nested callbacks, hard to read and maintain  
* How Promises and async/await solve callback hell  
* Error-first callbacks — Node.js convention `(err, data) => {}`, check error first

---

**Q13. What are higher-order functions?** `[1-2 yrs]`

* A function that takes a function as argument OR returns a function  
* Examples of built-in HOFs — `map`, `filter`, `reduce`, `forEach`, `sort`, `find`  
* Custom HOF example — function that returns another function (factory pattern)  
* Benefits — abstraction, reusability, composability  
* Currying — transforming `f(a, b)` into `f(a)(b)`, a form of higher-order function  
* Function composition — combining functions where output of one feeds into next

---

### **5\. Scope & Hoisting**

---

**Q14. What is scope in JavaScript?** `[Fresher]`

* Scope — determines where variables are accessible  
* **Global scope** — accessible everywhere  
* **Function scope** — `var` variables, only accessible inside the function  
* **Block scope** — `let`/`const`, only accessible inside `{}`  
* **Module scope** — variables in ES modules are scoped to the module, not global  
* Scope chain — when variable not found in current scope, JS looks up the chain to outer scopes  
* Lexical scope — scope is determined at code-writing time (not runtime)

---

**Q15. What is hoisting in JavaScript?** `[Fresher]`

* JS engine moves declarations to top of their scope during compile phase  
* `var` declarations — hoisted AND initialized with `undefined`  
* `function` declarations — hoisted AND fully initialized (function body is available)  
* `let` / `const` — hoisted but NOT initialized (in TDZ until declaration line)  
* `class` declarations — hoisted but in TDZ (cannot use before declaration)  
* Function expression `const fn = function() {}` — only the `const fn` part is hoisted, not the function  
* Common interview question — what is output of `console.log(x)` before `var x = 5`? → `undefined`  
* What is output of calling a function declaration before its definition? → Works fine (fully hoisted)  
* What is output of calling a function expression before its definition? → `TypeError` or `ReferenceError`

---

### **6\. ES6+ Features**

---

**Q16. What is destructuring in JavaScript?** `[Fresher]`

* Syntax to unpack values from arrays or properties from objects into variables  
* **Array destructuring:**  
  * `const [a, b] = [1, 2]`  
  * Skip elements — `const [a, , c] = [1, 2, 3]`  
  * Default values — `const [a = 10] = []`  
  * Swap variables — `[a, b] = [b, a]`  
  * Rest in array — `const [first, ...rest] = [1, 2, 3, 4]`  
* **Object destructuring:**  
  * `const { name, age } = person`  
  * Renaming — `const { name: fullName } = person`  
  * Default values — `const { name = "Anonymous" } = {}`  
  * Nested destructuring — `const { address: { city } } = user`  
  * Rest in object — `const { a, ...others } = obj`  
* In function parameters — `function greet({ name, age }) {}`  
* In React — used heavily for props destructuring and hooks like `const [state, setState] = useState()`

---

**Q17. What is the difference between spread and rest operators?** `[Fresher]`

* Both use `...` syntax but in different contexts  
* **Spread** — expands an iterable into individual elements  
  * In arrays — `const merged = [...arr1, ...arr2]`  
  * In objects — `const merged = {...obj1, ...obj2}` — later keys overwrite earlier  
  * In function calls — `Math.max(...numbers)`  
  * Shallow copy — `const copy = [...arr]` or `const copy = {...obj}`  
* **Rest** — collects remaining arguments into an array  
  * In function parameters — `function sum(...args) {}` — must be last parameter  
  * In destructuring — `const [first, ...rest] = arr`  
* Common mistake — trying to spread non-iterables (plain objects not iterable, only work in object spread)

---

**Q18. What are template literals?** `[Fresher]`

* Backtick strings — `` ` `` instead of `'` or `"`  
* String interpolation — `${expression}` — embed any JS expression  
* Multi-line strings — no need for `\n`  
* Tagged templates — `tag\`string\`\` — function processes template literal parts  
  * Used by styled-components, GraphQL (`gql\`query\`\`)  
* Nested template literals — template inside template  
* Expression inside `${}` can be any JS expression — ternary, function call, arithmetic

---

**Q19. What are other important ES6+ features every developer should know?** `[1-2 yrs]`

* **Default parameters** — `function greet(name = "World") {}`  
* **Enhanced object literals:**  
  * Shorthand properties — `{ name, age }` instead of `{ name: name, age: age }`  
  * Computed property names — `{ [dynamicKey]: value }`  
  * Method shorthand — `{ greet() {} }`  
* **`for...of` loop** — iterate over iterables (arrays, strings, Maps, Sets)  
* **`for...in` loop** — iterate over object keys (also gets inherited enumerable properties — use with caution)  
* **`Map`** — key-value store, any type as key, maintains insertion order  
* **`Set`** — collection of unique values  
* **`WeakMap` / `WeakSet`** — keys are weakly held (garbage collected when no other references)  
* **Optional chaining `?.`** — `user?.address?.city` — no error if intermediate is null/undefined  
* **Nullish coalescing `??`** — returns right side only if left is `null` or `undefined`  
* **`Promise.all`, `Promise.allSettled`, `Promise.race`, `Promise.any`**  
* **`globalThis`** — consistent global object across environments (browser, Node.js, workers)  
* **Logical assignment operators** — `||=`, `&&=`, `??=` (ES2021)  
* **`structuredClone()`** — deep clone built-in (ES2022)  
* **`Array.at(-1)`** — access from end of array (ES2022)  
* **`Object.hasOwn(obj, key)`** — safer than `obj.hasOwnProperty(key)` (ES2022)

---

### **7\. Promises & Async/Await**

---

**Q20. What is a Promise in JavaScript?** `[Fresher]`

* An object representing eventual completion or failure of an async operation  
* Three states — `pending`, `fulfilled`, `rejected`  
* Once settled (fulfilled or rejected), state cannot change  
* Created with `new Promise((resolve, reject) => {})`  
* `.then(onFulfilled, onRejected)` — handle resolution  
* `.catch(onRejected)` — handle rejection  
* `.finally(callback)` — runs regardless of outcome  
* Promise chaining — each `.then()` returns a new Promise  
* Return value from `.then()` becomes value passed to next `.then()`  
* Throwing inside `.then()` passes to next `.catch()`

---

**Q21. What is the difference between `Promise.all`, `Promise.allSettled`, `Promise.race`, and `Promise.any`?** `[1-2 yrs]`

* `Promise.all(promises)`:  
  * Resolves when **all** promises resolve  
  * Rejects immediately if **any** promise rejects (fail-fast)  
  * Use when all results are needed and any failure should abort  
* `Promise.allSettled(promises)`:  
  * Waits for **all** promises to settle (resolve or reject)  
  * Always resolves, returns array of `{status, value/reason}` objects  
  * Use when you need all results regardless of failures  
* `Promise.race(promises)`:  
  * Settles with the **first** promise to settle (resolve or reject)  
  * Use for timeout pattern — race actual request vs a timeout promise  
* `Promise.any(promises)`:  
  * Resolves with the **first** promise to **resolve**  
  * Rejects only if **all** promises reject (with `AggregateError`)  
  * Opposite of `Promise.race` for error handling

---

**Q22. What is async/await and how does it work?** `[Fresher]`

* Syntactic sugar over Promises — makes async code look synchronous  
* `async` keyword — marks a function as async, always returns a Promise  
* `await` keyword — pauses execution inside async function until Promise resolves  
* `await` can only be used inside `async` function (or top-level in ES modules)  
* Error handling — wrap in `try/catch` block (equivalent to `.catch()`)  
* `await` on non-Promise value — just returns the value (no error)  
* Running promises in parallel with async/await:  
  * Wrong (sequential) — `await p1; await p2` — waits one then other  
  * Right (parallel) — `const [r1, r2] = await Promise.all([p1, p2])`  
* Async/await vs Promises — async/await is not replacement, it's built on top of Promises  
* Common mistake — forgetting `await` keyword, function returns Promise not value

---

### **8\. Fetch API & Axios**

---

**Q23. What is the Fetch API and how do you use it?** `[Fresher]`

* Built-in browser API for making HTTP requests  
* Returns a Promise that resolves to a `Response` object  
* Two-step process — first `await fetch(url)`, then `await response.json()`  
* Why two awaits — first await gets the Response header/status, second reads the body stream  
* `response.ok` — true if status is 200-299  
* `response.status` — HTTP status code  
* Fetch does NOT reject on HTTP errors (404, 500\) — must manually check `response.ok`  
* Sending data:

 fetch(url, {  
    method: 'POST',  
    headers: { 'Content-Type': 'application/json' },  
    body: JSON.stringify(data)  
  })

* Setting headers — pass `headers` object in options  
* `AbortController` — cancel a fetch request in progress

---

**Q24. What is Axios and how is it different from Fetch?** `[1-2 yrs]`

* Third-party HTTP client library, works in browser and Node.js  
* Differences from Fetch:  
  * Axios automatically parses JSON response — no second `.json()` call needed  
  * Axios rejects on HTTP errors (4xx, 5xx) — easier error handling  
  * Axios has built-in request/response interceptors  
  * Axios supports request cancellation with `CancelToken` / `AbortController`  
  * Axios automatically sets `Content-Type: application/json`  
  * Axios works in Node.js, Fetch needs polyfill in older Node versions  
* Axios interceptors — `axios.interceptors.request.use()`, `axios.interceptors.response.use()`  
  * Use cases — attach auth token to every request, global error handling, refresh token logic  
* Axios instance — `axios.create({ baseURL, headers })` for shared config  
* Axios in MERN — commonly used in React frontend for API calls to Express backend

---

### **9\. DOM Manipulation & Events**

---

**Q25. What is the DOM and how do you manipulate it with JavaScript?** `[Fresher]`

* DOM — Document Object Model, tree representation of HTML as JS objects  
* Selecting elements:  
  * `document.getElementById('id')`  
  * `document.querySelector('.class')` — first match  
  * `document.querySelectorAll('div')` — NodeList of all matches  
  * `document.getElementsByClassName()`, `document.getElementsByTagName()`  
* Modifying elements:  
  * `element.textContent` — get/set text content (safer, no HTML parsing)  
  * `element.innerHTML` — get/set HTML (XSS risk if setting user input)  
  * `element.setAttribute('attr', 'value')` / `element.getAttribute('attr')`  
  * `element.classList.add()`, `.remove()`, `.toggle()`, `.contains()`  
  * `element.style.property = 'value'` — inline styles  
* Creating and inserting elements:  
  * `document.createElement('div')`  
  * `parent.appendChild(child)`, `parent.insertBefore(newNode, refNode)`  
  * `element.append()`, `element.prepend()`, `element.before()`, `element.after()`  
  * `element.remove()` — remove element from DOM  
* `innerHTML` vs `textContent` vs `innerText`:  
  * `innerHTML` — parses HTML, XSS risk  
  * `textContent` — raw text, no HTML parsing, faster  
  * `innerText` — respects CSS visibility, triggers reflow

---

**Q26. What are DOM events and how does event handling work?** `[Fresher]`

* Events — signals that something happened (click, keypress, form submit, etc.)  
* `addEventListener(event, handler, options)` — preferred way  
* `removeEventListener(event, handler)` — same reference required to remove  
* Inline event handlers `onclick="..."` — avoid, mixes HTML and JS  
* `event` object — passed to handler, contains `target`, `currentTarget`, `type`, `preventDefault()`, `stopPropagation()`  
* `event.target` — element that triggered the event  
* `event.currentTarget` — element that has the event listener attached  
* Common events — `click`, `dblclick`, `mouseover`, `mouseout`, `mouseenter`, `mouseleave`, `keydown`, `keyup`, `keypress`, `submit`, `change`, `input`, `focus`, `blur`, `scroll`, `resize`, `load`, `DOMContentLoaded`

---

**Q27. What is event bubbling, capturing, and delegation?** `[1-2 yrs]`

* **Event bubbling** — event triggers on target, then bubbles UP to ancestors (default)  
* **Event capturing** — event triggers from root DOWN to target (capture phase)  
* `addEventListener(event, handler, true)` — third argument `true` enables capture phase  
* `event.stopPropagation()` — stops event from bubbling/capturing further  
* `event.stopImmediatePropagation()` — stops propagation AND prevents other handlers on same element  
* `event.preventDefault()` — prevents default browser behavior (form submit, link navigation)  
* **Event delegation** — attach one listener on parent, handle events for multiple children  
  * Use `event.target` to identify which child was clicked  
  * Benefits — fewer listeners (performance), works for dynamically added elements  
  * Common pattern in React-like dynamic lists

---

### **10\. Error Handling**

---

**Q28. How does error handling work in JavaScript?** `[Fresher]`

* `try` — wrap code that might throw  
* `catch(error)` — handle the error, `error.message`, `error.name`, `error.stack`  
* `finally` — always runs regardless of error  
* `throw` — manually throw any value (best practice: throw `Error` objects)  
* Built-in error types — `Error`, `TypeError`, `ReferenceError`, `SyntaxError`, `RangeError`, `URIError`, `EvalError`  
* Custom errors — extend `Error` class: `class ValidationError extends Error {}`  
* `try/catch` does NOT catch async errors — must use inside `async` function or `.catch()` on Promise  
* Global error handling — `window.onerror`, `window.onunhandledrejection`  
* Error handling in Express (backend) — next(err) pattern

---

**Q29. What are common patterns for async error handling?** `[1-2 yrs]`

* Async/await with try/catch — cleanest approach  
* `.catch()` on Promise chain  
* Wrapper utility — `const [err, data] = await to(promise)` (Go-style error handling pattern)  
* Global unhandled rejection handler — `process.on('unhandledRejection', handler)` in Node.js  
* Error boundaries in React — `componentDidCatch`, `ErrorBoundary` component  
* Axios error handling — `error.response` (server responded), `error.request` (no response), `error.message` (setup error)

---

### **11\. Closures & Lexical Scope**

---

**Q30. What is a closure in JavaScript?** `[1-2 yrs]`

* A function that remembers the variables from its outer scope even after the outer function has returned  
* Every function in JS creates a closure over its surrounding scope  
* How it works — inner function holds a reference to outer scope's variable environment  
* Practical use cases:  
  * Data encapsulation / private variables  
  * Factory functions — functions that return configured functions  
  * Memoization — caching results using closure  
  * Event handlers that remember state  
  * Module pattern (pre-ES6)  
* Classic closure interview question:

 for (var i \= 0; i \< 3; i++) {  
    setTimeout(() \=\> console.log(i), 100\)  
  }  
  // prints 3, 3, 3 — not 0, 1, 2

* Fix with `let` (block scoped) or IIFE wrapping  
* Closure memory — variables in closure are kept in memory (potential memory leak if not careful)

---

**Q31. What is lexical scope?** `[1-2 yrs]`

* Scope determined at code **write time** (not runtime)  
* A function's scope chain is determined by where it is **defined**, not where it is **called**  
* Inner functions have access to outer function variables — forms the basis of closures  
* Lexical environment — the surrounding context captured by a closure  
* Difference between lexical scope and dynamic scope (JS uses lexical, not dynamic)

---

### **12\. Event Loop & Asynchronous JS**

---

**Q32. How does the JavaScript Event Loop work?** `[1-2 yrs]`

* JS is single-threaded — one call stack, executes one thing at a time  
* **Components:**  
  1. **Call Stack** — LIFO stack of currently executing functions  
  2. **Web APIs** — browser-provided environment for async ops (setTimeout, fetch, DOM events)  
  3. **Callback Queue (Task Queue / Macrotask Queue)** — completed async callbacks wait here  
  4. **Microtask Queue** — Promise callbacks, `queueMicrotask()`, `MutationObserver`  
  5. **Event Loop** — continuously checks if call stack is empty, then processes queues  
* **Execution order:**  
  1. All synchronous code runs (call stack)  
  2. All microtasks run (Promise `.then`, `await` continuations) — entire queue drained  
  3. One macrotask runs (setTimeout, setInterval, I/O)  
  4. All microtasks again  
  5. Repeat  
* Microtasks have priority over macrotasks  
* `setTimeout(fn, 0)` — doesn't run immediately, runs after current stack AND microtasks clear  
* Classic question — predict output of mixed sync, Promise, and setTimeout code

---

**Q33. What is the difference between microtasks and macrotasks?** `[2-3 yrs]`

* **Macrotasks** — `setTimeout`, `setInterval`, `setImmediate` (Node), I/O, UI rendering  
* **Microtasks** — `Promise.then/catch/finally`, `queueMicrotask()`, `MutationObserver`, `async/await` continuations  
* After each macrotask — entire microtask queue is drained before next macrotask  
* Why this matters — Promise callbacks always run before the next setTimeout callback  
* `queueMicrotask(fn)` — directly enqueue a microtask  
* Node.js specific — `process.nextTick()` runs before microtasks (even higher priority)

---

**Q34. What is `setTimeout`, `setInterval`, and `clearTimeout`?** `[Fresher]`

* `setTimeout(fn, delay)` — run function once after delay (ms), returns timer ID  
* `clearTimeout(id)` — cancel before it fires  
* `setInterval(fn, delay)` — run function repeatedly every delay ms  
* `clearInterval(id)` — stop the interval  
* Minimum delay — HTML spec minimum is 4ms for nested timeouts  
* `setTimeout(fn, 0)` — defers execution to after current call stack clears  
* Why interval may drift — if callback takes longer than interval, next call is delayed  
* Better than `setInterval` for recurring tasks — recursive `setTimeout` gives consistent delay

---

### **13\. Modules**

---

**Q35. What are ES Modules and how do they work?** `[Fresher]`

* `export` — named exports and default export  
* Named export — `export const fn = () => {}`, import as `import { fn } from './module'`  
* Default export — `export default fn`, import as `import fn from './module'` (any name)  
* One default export per module, multiple named exports allowed  
* Re-exporting — `export { fn } from './other'`  
* Export all — `export * from './other'`  
* `import * as module from './file'` — namespace import  
* Dynamic import — `import('./module').then(m => m.fn())` — lazy loading  
* ES Modules are static — imports are resolved at compile time, not runtime  
* ES Modules are always in strict mode  
* `import.meta` — metadata about the module (e.g., `import.meta.url`)

---

**Q36. What is the difference between CommonJS and ES Modules?** `[1-2 yrs]`

* **CommonJS** (Node.js traditional):  
  * `require()` / `module.exports` / `exports`  
  * Synchronous — loaded at runtime  
  * Dynamic — `require()` can be inside conditionals  
  * `.js` extension default in Node  
* **ES Modules:**  
  * `import` / `export`  
  * Asynchronous-capable — resolved at parse time (static)  
  * Cannot use inside conditionals (except dynamic `import()`)  
  * `.mjs` extension or `"type": "module"` in `package.json`  
* Tree-shaking — only possible with ES Modules (static analysis of imports)  
* Interop — using CommonJS module inside ESM and vice versa — nuances in Node.js  
* React uses ES Modules, Node.js traditionally used CommonJS (now supports both)

---

### **14\. Object-Oriented Programming (OOP)**

---

**Q37. What is prototypal inheritance in JavaScript?** `[1-2 yrs]`

* Every object has a hidden `[[Prototype]]` property pointing to another object  
* Property lookup — if not found on object, JS walks up the prototype chain  
* `Object.getPrototypeOf(obj)` — access prototype  
* `obj.__proto__` — non-standard but widely supported  
* `Object.create(proto)` — create object with specified prototype  
* All objects eventually inherit from `Object.prototype` (top of chain)  
* `null` — end of prototype chain (`Object.prototype.__proto__ === null`)  
* `hasOwnProperty()` — checks if property belongs to object itself, not prototype  
* `in` operator — checks own AND inherited properties

---

**Q38. What are ES6 Classes and how do they work?** `[1-2 yrs]`

* Syntactic sugar over prototypal inheritance — cleaner syntax, same behavior underneath  
* `class` declaration — `class Animal {}`  
* `constructor()` — called when `new` is used  
* Instance methods — defined in class body, stored on `prototype`  
* `static` methods — called on the class itself, not instances  
* `extends` — class inheritance  
* `super()` — call parent constructor, must be called in child constructor before `this`  
* `super.method()` — call parent class methods  
* Getters and setters — `get name() {}`, `set name(val) {}`  
* Private fields — `#fieldName` (ES2022) — truly private, not accessible outside class  
* Public class fields — `fieldName = value`  
* Class expressions — `const Foo = class {}`  
* Classes are NOT hoisted (in TDZ) — unlike function declarations

---

**Q39. What are the four pillars of OOP and how are they achieved in JavaScript?** `[2-3 yrs]`

* **Encapsulation** — bundling data and methods, hiding internal state  
  * Achieved via closures, private class fields `#`, WeakMap pattern  
* **Inheritance** — child class inherits from parent  
  * Achieved via `extends`, `Object.create()`, prototype chain  
* **Polymorphism** — same method name, different behavior in subclasses  
  * Achieved via method overriding in subclasses  
* **Abstraction** — hide complex implementation, expose simple interface  
  * Achieved via private fields/methods, closures, abstract-like base classes  
* JavaScript is prototype-based OOP, not class-based (classes are syntactic sugar)  
* Composition over Inheritance — prefer mixing in behaviors over deep inheritance chains

---

### **15\. Functional Programming**

---

**Q40. What are `map`, `filter`, and `reduce`?** `[Fresher]`

* **`map(callback)`** — transforms each element, returns new array of same length  
  * `callback(currentValue, index, array)` — return transformed value  
  * Does not mutate original array  
* **`filter(callback)`** — keeps elements where callback returns `true`, returns new array  
  * `callback(currentValue, index, array)` — return boolean  
  * Result array can be shorter than original  
* **`reduce(callback, initialValue)`** — accumulates all elements into single value  
  * `callback(accumulator, currentValue, index, array)` — return new accumulator  
  * Can produce any type — number, string, object, array  
  * `initialValue` — always provide it to avoid edge cases with empty arrays  
* Chaining — `arr.filter(...).map(...).reduce(...)`  
* Performance note — chaining creates multiple intermediate arrays, sometimes a single `reduce` is more efficient

---

**Q41. What are other important array methods for functional programming?** `[Fresher]`

* `forEach(callback)` — iterate, returns `undefined`, cannot break out early  
* `find(callback)` — returns **first** element matching condition, or `undefined`  
* `findIndex(callback)` — returns index of first match, or `-1`  
* `some(callback)` — returns `true` if at least one element matches  
* `every(callback)` — returns `true` if all elements match  
* `flat(depth)` — flatten nested arrays  
* `flatMap(callback)` — map then flatten one level  
* `sort(compareFn)` — sorts in place (mutates\!), default converts to string  
  * Numeric sort — `arr.sort((a, b) => a - b)`  
* `splice(start, deleteCount, ...items)` — mutates original array  
* `slice(start, end)` — returns new array, does not mutate  
* `includes(value)` — check if value exists  
* `indexOf(value)` — first index of value, `-1` if not found  
* `Array.from(iterable)` — create array from iterable or array-like  
* `Array.isArray(value)` — check if value is an array

---

**Q42. What are pure functions and immutability in functional programming?** `[2-3 yrs]`

* **Pure function** — same input always produces same output, no side effects  
* Side effects — modifying external state, API calls, DOM manipulation, logging  
* Immutability — do not mutate data, create new versions instead  
* Benefits — predictable, testable, easier to reason about  
* Immutable array patterns — use `map`, `filter`, `spread` instead of `push`, `splice`, `sort`  
* Immutable object patterns — `{...obj, updatedKey: newValue}` instead of `obj.key = value`  
* `Object.freeze()` — prevents modification of object (shallow freeze only)  
* Why React cares about immutability — state updates require new references for change detection

---

### **16\. Web Storage**

---

**Q43. What are the differences between `localStorage`, `sessionStorage`, and Cookies?** `[Fresher]`

* **`localStorage`:**  
  * Persists until explicitly cleared  
  * 5-10MB storage limit  
  * Accessible only on client (JS)  
  * Same origin only  
  * Not sent with HTTP requests  
* **`sessionStorage`:**  
  * Cleared when browser tab is closed  
  * 5MB storage limit  
  * Same origin, same tab only  
  * Not sent with HTTP requests  
* **Cookies:**  
  * Expiry can be set (session or specific date)  
  * \~4KB limit per cookie  
  * Sent with every HTTP request to the server (can be used for auth)  
  * Can be `HttpOnly` (not accessible by JS) — important for security  
  * Can be `Secure` (HTTPS only)  
  * `SameSite` attribute — controls cross-site sending (`Strict`, `Lax`, `None`)  
  * Can be set by server via `Set-Cookie` header  
* All three are origin-specific — different domains cannot access each other's storage

---

**Q44. How do you work with `localStorage` in JavaScript?** `[Fresher]`

* `localStorage.setItem('key', 'value')` — value must be string  
* `localStorage.getItem('key')` — returns string or `null`  
* `localStorage.removeItem('key')`  
* `localStorage.clear()` — removes all items for the origin  
* `localStorage.length` — number of stored items  
* `localStorage.key(index)` — get key by index  
* Storing objects — must `JSON.stringify()` on save, `JSON.parse()` on read  
* Common mistake — storing objects without stringifying, getting `"[object Object]"`  
* `storage` event — fires in OTHER tabs/windows when localStorage changes (not same tab)  
* Use cases in MERN — store JWT token (controversial), user preferences, cart data, theme

---

**Q45. What are the security concerns around Web Storage?** `[2-3 yrs]`

* **localStorage XSS vulnerability** — if attacker injects JS, they can read localStorage including JWT tokens  
* `HttpOnly` cookies cannot be read by JS — why they are preferred for storing auth tokens  
* Never store sensitive data (passwords, credit card info) in localStorage  
* JWT in localStorage vs HttpOnly cookie — hot debate:  
  * localStorage — vulnerable to XSS  
  * HttpOnly cookie — protected from XSS but vulnerable to CSRF (mitigated with `SameSite`)  
* CSRF attack — forged requests that include cookies automatically  
* `SameSite=Strict` or `Lax` — mitigates CSRF for cookie-based auth  
* Content Security Policy (CSP) — reduces XSS risk, helps protect localStorage indirectly  
* Best practice in production MERN apps — use `HttpOnly`, `Secure`, `SameSite=Strict` cookies for auth tokens

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q46. What is the difference between deep copy and shallow copy?** `[1-2 yrs]`

* Already detailed in Q4 — here focus on methods and when each fails  
* Shallow copy methods — spread, `Object.assign()`, `Array.slice()`  
* Deep copy methods:  
  * `JSON.parse(JSON.stringify(obj))` — fails with functions, `undefined`, `Date`, `RegExp`, circular refs  
  * `structuredClone(obj)` — handles `Date`, `Map`, `Set`, circular refs, but not functions  
  * Lodash `_.cloneDeep()` — most comprehensive  
* Circular reference — object that references itself, breaks most copy methods

---

**Q47. What is `this` keyword in JavaScript?** `[1-2 yrs]`

* `this` refers to the object that is the **execution context** of the function  
* Value of `this` depends on how function is called:  
  * Regular function — `this` is the calling object, or `global`/`undefined` in strict mode  
  * Arrow function — `this` is lexically bound (enclosing context)  
  * Constructor with `new` — `this` is the newly created object  
  * Explicit binding — `call()`, `apply()`, `bind()`  
  * Object method — `this` is the object before the dot  
  * Class method — `this` is the instance  
* `call(thisArg, arg1, arg2)` — call with specified `this`, arguments individually  
* `apply(thisArg, [argsArray])` — call with specified `this`, arguments as array  
* `bind(thisArg)` — returns NEW function with permanently bound `this`  
* Common issue in React — `this` in class component event handlers (need to bind or use arrow function)

---

**Q48. What is memoization?** `[2-3 yrs]`

* Optimization technique — cache results of expensive function calls  
* If same input is called again, return cached result without re-executing  
* Implemented using closure to maintain cache object  
* `useMemo` and `useCallback` in React — memoization hooks  
* Pure functions are prerequisite for memoization (same input must always give same output)  
* Trade-off — memory usage increases to save computation time

---

**Q49. What is the difference between `for...in` and `for...of`?** `[Fresher]`

* `for...in` — iterates over **enumerable property keys** of an object (and inherited ones)  
  * Use `hasOwnProperty` check to skip inherited properties  
  * Works on arrays too but gives string indices — bad practice  
* `for...of` — iterates over **values** of any iterable (arrays, strings, Maps, Sets, generators)  
  * Does not work on plain objects (not iterable by default)  
  * Use `Object.keys()`, `Object.values()`, `Object.entries()` to loop over objects with `for...of`

---

**Q50. What is a generator function?** `[2-3 yrs]`

* `function*` — can pause and resume execution  
* `yield` — pauses function, returns value to caller  
* Returns an iterator — call `.next()` to resume, returns `{value, done}`  
* `yield*` — delegates to another generator or iterable  
* Use cases — infinite sequences, lazy evaluation, custom iterators, `async` generator for streaming data  
* Generators behind the scenes of early async patterns (before async/await)

---

That's the complete **JavaScript** section — **50 questions** with full subtopic depth, ready to merge into your MERN Interview Kit.

[⬅️ Previous: Material UI](../../MERN_Study_Structure/01_Web_Development_Fundamentals/05_Material_UI/05_Material_UI.md) | [🏠 Home](../../README.md) | [Next: Typescript ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/07_Typescript/07_Typescript.md)
/07_Typescript/07_Typescript.md)
