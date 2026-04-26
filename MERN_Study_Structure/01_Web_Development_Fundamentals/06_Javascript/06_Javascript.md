# Javascript (JS)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

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

**Full Answer:**
In JavaScript, `var`, `let`, and `const` define how variables are scoped and hoisted.
- **var**: Function-scoped and hoisted with a value of `undefined`. It can be redeclared and reassigned, which often leads to bugs like global namespace pollution or scope leakage.
- **let**: Introduced in ES6, it is **block-scoped** (exists only within `{}`). It is hoisted but remains in the **Temporal Dead Zone (TDZ)** until initialized. It can be reassigned but not redeclared.
- **const**: Also block-scoped and exists in the TDZ. It **must be initialized** at the time of declaration and cannot be reassigned. Note that for objects and arrays, the *reference* is constant, but the internal properties can still be mutated.
**MERN Context:** Always use `const` by default to ensure data integrity. Use `let` only for counters or variables that must change. Avoid `var` entirely.

**Trap Explained: `var` and Block Scoping**
A common interview question is: *"What happens if I declare a `var` inside an `if` block?"*
```javascript
if (true) {
  var leak = "I am everywhere";
  let stay = "I am stuck here";
}
console.log(leak); // Output: "I am everywhere" (var leaks out!)
console.log(stay); // Output: ReferenceError (let is safe)
```
This "leakage" is why `var` causes bugs in large MERN applications.

---

**Q2. What is the Temporal Dead Zone (TDZ)?** `[1-2 yrs]`

* Period between entering scope and the `let`/`const` declaration line being executed  
* Accessing variable in TDZ throws `ReferenceError`, not `undefined`  
* Why TDZ exists — prevents accessing variables before they are meaningfully initialized  
* TDZ applies to `let`, `const`, and `class` declarations  
* Does NOT apply to `var` — `var` is hoisted with `undefined` immediately

**Full Answer:**
The **Temporal Dead Zone (TDZ)** is the period between the start of a scope and the actual line where a `let`, `const`, or `class` is declared. During this time, the variable is "hoisted" in the sense that the engine knows it exists, but it is uninitialized.
- Accessing the variable in the TDZ throws a `ReferenceError`.
- This ensures that variables are always meaningfully initialized before use, unlike `var` which would simply return `undefined`.
- TDZ helps catch bugs where variables are used before they are ready.

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

**Full Answer:**
JavaScript has **7 Primitive types** and **1 Reference type** (Object).
- **Primitives**: `String`, `Number`, `Boolean`, `undefined`, `null`, `Symbol`, and `BigInt`. They are immutable and stored by value in the Stack memory.
- **Reference Types**: `Object` (including Arrays, Functions, Dates, etc.). They are mutable and stored in the Heap memory, with a reference address stored in the Stack.
**Key Interview Points:**
- `typeof null` returns `"object"` (a historical bug).
- `NaN` is technically a `"number"`.
- `undefined` means a variable has been declared but not assigned a value, while `null` is an intentional assignment representing "no value".

**Trap Explained: The `typeof` Quirk**
Interviews often ask: *"Why is `typeof null` an object?"*
- **The Answer:** It is a 30-year-old bug in JavaScript's original implementation. Values were stored in 32-bit units, with a "type tag" in the first few bits. The tag for objects was `000`. Since `null` was represented as the null pointer (all zeros), it was mistakenly identified as an object. It was never fixed to avoid breaking the existing web.

---

**Q4. What is the difference between primitive and reference types in memory?** `[1-2 yrs]`

* Primitives stored in **stack** — value itself is stored, copying creates independent copy  
* References stored in **heap** — variable holds memory address, copying copies the reference  
* Shallow copy problem with objects — `const b = a` means both point to same object  
* How to copy objects — spread `{...obj}`, `Object.assign()`, `JSON.parse(JSON.stringify())`, `structuredClone()`  
* Deep copy vs shallow copy — nested objects still share reference in shallow copy  
* `structuredClone()` — modern built-in deep clone, handles nested objects correctly  
* Why `===` comparison on objects always false for different object literals even with same content

**Full Answer:**
The primary difference lies in **how they are stored and copied in memory**:
- **Primitive Types**: Stored in the **Stack**. When you copy a primitive, a completely new, independent copy of the value is created.
- **Reference Types**: The actual data is stored in the **Heap**, but the variable holds a **pointer (reference)** in the Stack. When you copy an object, you are only copying the *reference*, not the object itself. Both variables now point to the same location in memory.
- **Comparison**: This is why `{} === {}` is `false`. Even though they look the same, they point to two different addresses in the Heap.
- **Copying**: To truly copy an object (Reference Type), you must perform a **Shallow Copy** (using `...` spread or `Object.assign`) or a **Deep Copy** (using `structuredClone()` or `JSON.stringify/parse`).

**Trap Explained: Why is `[] === []` false?**
Even though both are empty arrays, they are stored at **different memory addresses** in the Heap. When you use `===` on objects, JS compares the *reference (address)*, not the content. To compare contents, you must iterate through them or use `JSON.stringify(arr1) === JSON.stringify(arr2)`.

---

**Q5. What is `NaN` and how do you check for it?** `[Fresher]`

* `NaN` — "Not a Number", result of invalid numeric operation (e.g., `"abc" * 2`)  
* `typeof NaN === 'number'` — confusing but true  
* `NaN === NaN` is `false` — NaN is the only value not equal to itself  
* `isNaN("abc")` — returns `true` but also converts string to number first (coercion issue)  
* `Number.isNaN("abc")` — returns `false` because "abc" is not NaN, it's a string (preferred)  
* `Number.isNaN(NaN)` — returns `true` (correct and reliable)

**Full Answer:**
`NaN` stands for **Not-a-Number**. It is a special value in JavaScript that indicates an invalid mathematical operation (e.g., `0 / 0` or `parseInt("hello")`).
- **The Catch**: `typeof NaN` is actually `"number"`.
- **The Comparison Trap**: `NaN` is the only value in JS that is **not equal to itself** (`NaN === NaN` is `false`).
- **Checking for NaN**: 
  - `isNaN()` (global) is unreliable because it coerces the input to a number first (e.g., `isNaN("abc")` is `true`).
  - `Number.isNaN()` (ES6) is the **preferred way** because it checks if the value is *actually* NaN without coercion.

---

**Q6. What is the difference between `null` and `undefined`?** `[Fresher]`

* `undefined` — variable declared but not assigned, function that returns nothing, missing object property  
* `null` — intentional empty value, explicitly set by developer  
* `typeof undefined === 'undefined'`, `typeof null === 'object'` (bug)  
* `null == undefined` is `true` (loose equality), `null === undefined` is `false` (strict)  
* Nullish coalescing `??` — returns right side only for `null` or `undefined` (not for `0` or `""`)  
* Optional chaining `?.` — safely access nested properties without checking for null/undefined

**Full Answer:**
Both `null` and `undefined` represent "no value," but they are used in different contexts.
- **undefined**: Means a variable has been declared but has not yet been assigned a value. It is also the default return value of functions that don't explicitly return something.
- **null**: Is an **assignment value**. It is used by developers to explicitly indicate that a variable should be empty.
- **Comparison**: `null == undefined` is `true` because they are both falsy, but `null === undefined` is `false` because their types are different (`object` vs `undefined`).
**Modern Tip:** Use the **Nullish Coalescing Operator (`??`)** to provide defaults only for `null` or `undefined`, avoiding the pitfalls of using `||` which also triggers for `0` or `""`.

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

**Full Answer:**
Type Coercion is the automatic conversion of values from one data type to another (e.g., strings to numbers).
- **Implicit Coercion**: Happens automatically. For example, `"5" + 2` results in `"52"` (String concatenation), but `"5" - 2` results in `3` (Numeric subtraction).
- **Explicit Coercion**: When a developer intentionally converts types using `Number()`, `String()`, or `Boolean()`.
- **Falsy Values**: In JS, `false`, `0`, `""`, `null`, `undefined`, and `NaN` are all considered "falsy" when coerced to a boolean. Everything else is "truthy".

**Trap Explained: The `+` vs `-` Coercion**
*"What is the output of `"5" + 2` and `"5" - 2`?"*
- **`"5" + 2` → `"52"`**: The `+` operator is overloaded. If one operand is a string, it prefers **concatenation**.
- **`"5" - 2` → `3`**: The `-` operator only works for numbers, so it forces the string `"5"` to become a number.
- **Unary `+`**: Adding a `+` before a string (e.g., `+"5"`) is the fastest way to convert it to a number.

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

**Full Answer:**
- **`==` (Loose Equality)**: Compares two values for equality **after** performing type coercion. This can lead to unexpected results like `[] == false` being `true`.
- **`===` (Strict Equality)**: Compares both the **value and the type** without any conversion. If the types are different, it immediately returns `false`.
- **Recommendation**: In MERN development (and JS in general), **always use `===`**. It makes your code predictable and prevents subtle bugs caused by implicit coercion.

**Trap Explained: Why is `[] == ![]` true?**
This is a famous interview question that demonstrates complex coercion:
1.  **Logical NOT (`!`) has high priority**: `![]` is evaluated first. Since an array (even empty) is truthy, `![]` becomes `false`.
2.  **Comparison becomes `[] == false`**: When comparing an object (array) to a primitive (boolean), the object is converted to a primitive. `[].toString()` is `""`.
3.  **Comparison becomes `"" == false`**: When comparing a string to a boolean, both are converted to numbers.
4.  **Comparison becomes `0 == 0`**: Both empty string and `false` become `0`. Hence, `true`.

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

**Full Answer:**
JavaScript operators allow you to perform actions on variables. Key categories include:
- **Arithmetic**: Basic math plus `**` for exponentiation.
- **Comparison**: Use `===` and `!==` for reliability.
- **Logical**: `&&` (AND), `||` (OR), and `!` (NOT).
- **Nullish Coalescing (`??`)**: Returns the right-hand side only if the left-hand side is `null` or `undefined`.
- **Optional Chaining (`?.`)**: Allows you to read the value of a property located deep within a chain of connected objects without having to check if each reference in the chain is valid.
- **Logical Assignment**: `a ||= b` is shorthand for `a || (a = b)`.

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

**Full Answer:**
There are several ways to define functions, each with unique behaviors:
1. **Function Declaration**: `function name() {}`. These are **hoisted**, meaning you can call them before they are defined in the code.
2. **Function Expression**: `const name = function() {}`. These are not hoisted in the same way; they behave like variables.
3. **Arrow Functions (ES6)**: `const name = () => {}`. They provide a shorter syntax and **do not have their own `this` binding** (they inherit `this` from the lexical scope).
4. **IIFE**: A function that runs as soon as it is defined. Useful for creating private scopes.
5. **Generator Functions**: Defined with `function*`, they can pause execution using `yield`.
6. **Async Functions**: Functions marked with `async` always return a Promise and allow the use of `await`.

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

**Full Answer:**
Arrow functions (ES6) are not just a shorter syntax; they behave differently from regular functions:
- **`this` Binding**: Regular functions have a **dynamic `this`**, meaning `this` depends on how the function was called. Arrow functions have a **lexical `this`**, meaning they inherit `this` from the parent scope where they were defined.
- **Constructors**: Regular functions can be used as constructors (with `new`). Arrow functions cannot; they lack a `prototype` property.
- **Arguments**: Regular functions have an `arguments` object. Arrow functions do not; you must use rest parameters (`...args`) instead.
- **Methods**: Don't use arrow functions for object methods if you need to access other properties via `this`.

**Follow-up: When NOT to use Arrow Functions**
```javascript
const user = {
  name: "Aniket",
  // ❌ WRONG: Arrow function inherits 'this' from global scope
  greet: () => console.log(this.name), 
  // ✅ RIGHT: Regular function gets 'this' from the object call
  sayHi() { console.log(this.name); } 
};
```
Also, never use arrow functions as **Constructors**. `const p = new Person()` will throw an error if `Person` is an arrow function because they don't have a `prototype`.

---

**Q12. What is a callback function?** `[Fresher]`

* A function passed as argument to another function, called later (possibly asynchronously)  
* Synchronous callback — `[1,2,3].forEach(callback)` — called immediately during execution  
* Asynchronous callback — `setTimeout(callback, 1000)` — called later after delay  
* Callback hell — deeply nested callbacks, hard to read and maintain  
* How Promises and async/await solve callback hell  
* Error-first callbacks — Node.js convention `(err, data) => {}`, check error first

**Full Answer:**
A callback is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.
- **Synchronous**: Executed immediately (e.g., `map`, `filter`).
- **Asynchronous**: Executed after an async operation completes (e.g., `fetch`, `setTimeout`).
- **Callback Hell**: When callbacks are nested within callbacks, making code unreadable. This is why Promises and `async/await` were introduced—to "flatten" the structure of asynchronous code.

**Follow-up: What is an Error-First Callback?**
Common in Node.js, the first argument is always the error object.
```javascript
fs.readFile('file.txt', (err, data) => {
  if (err) {
    console.error("Failed to read:", err);
    return;
  }
  console.log("File content:", data);
});
```
This pattern ensures you never forget to handle potential errors before processing the data.

---

**Q13. What are higher-order functions?** `[1-2 yrs]`

* A function that takes a function as argument OR returns a function  
* Examples of built-in HOFs — `map`, `filter`, `reduce`, `forEach`, `sort`, `find`  
* Custom HOF example — function that returns another function (factory pattern)  
* Benefits — abstraction, reusability, composability  
* Currying — transforming `f(a, b)` into `f(a)(b)`, a form of higher-order function  
* Function composition — combining functions where output of one feeds into next

**Full Answer:**
A **Higher-Order Function (HOF)** is a function that does at least one of the following:
1. Takes one or more functions as arguments (e.g., `addEventListener`, `map`).
2. Returns a function as its result.
HOFs are a core concept in **Functional Programming**. They allow for high levels of abstraction, enabling you to write "pluggable" logic. For example, `array.sort()` is an HOF because it takes a comparison function to decide how to sort the elements.

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

**Full Answer:**
Scope determines the visibility or accessibility of variables.
- **Global Scope**: Variables defined outside any function or block.
- **Function Scope**: Variables defined with `var` inside a function are only accessible within that function.
- **Block Scope**: Variables defined with `let` or `const` inside a block `{}` (like `if` or `for`) are only accessible within those braces.
- **Scope Chain**: If JS can't find a variable in the current scope, it looks at the outer (parent) scope, and continues until it reaches the global scope. If still not found, it throws a `ReferenceError`.

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

**Full Answer:**
Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compilation phase.
- **Function Declarations**: Are fully hoisted. You can call the function even before it's defined in the code.
- **`var` Variables**: Are hoisted but initialized with `undefined`.
- **`let` and `const`**: Are hoisted but not initialized. They reside in the **Temporal Dead Zone (TDZ)**, and accessing them before declaration throws a `ReferenceError`.
- **Function Expressions**: Are NOT hoisted as functions. If defined with `var`, the variable is hoisted as `undefined`. If defined with `let/const`, it follows TDZ rules.

**Trap Explained: Predict the Output**
```javascript
console.log(x); // Output: undefined (var is hoisted and initialized with undefined)
var x = 5;

console.log(y); // Output: ReferenceError (let is in TDZ)
let y = 10;

foo(); // Output: "Hello" (Function declarations are fully hoisted)
function foo() { console.log("Hello"); }

bar(); // Output: TypeError (bar is undefined at this point)
var bar = function() { console.log("World"); };
```

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

**Full Answer:**
Destructuring is a convenient way of extracting values from arrays or properties from objects into distinct variables.
- **Object Destructuring**: `const { name, age } = person;`. You can also rename variables: `const { name: userName } = person;`.
- **Array Destructuring**: `const [first, second] = [10, 20];`.
- **Why it's useful**: It reduces the need for repetitive code (e.g., `person.name`, `person.age`) and makes function parameters much cleaner, especially in React where we destructure `props`.

**Trap Explained: Nested Destructuring & Defaults**
*"How do you extract `city` from a user object where `address` might be undefined?"*
```javascript
const user = { name: "Aniket" };

// This will throw: Cannot read property 'city' of undefined
const { address: { city } } = user; 

// The Fix: Provide a default empty object for address
const { address: { city } = {} } = user; 
console.log(city); // Output: undefined (no error!)
```
This is a lifesaver in MERN apps when dealing with deep API responses.

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

**Full Answer:**
Although they both use the `...` syntax, they serve opposite purposes:
- **Spread Operator**: "Expands" an array or object into its individual elements. It is commonly used for merging arrays `[...a, ...b]` or cloning objects `{...obj}`.
- **Rest Operator**: "Collects" multiple elements into a single array. It is used in function parameters to handle a variable number of arguments `function sum(...args) {}` or in destructuring to capture the remaining items `const [first, ...rest] = [1, 2, 3];`.
**Tip:** The Spread operator is used where you would otherwise write values separated by commas, while the Rest operator is used where you would define a variable name.

---

**Q18. What are template literals?** `[Fresher]`

* Backtick strings — `` ` `` instead of `'` or `"`  
* String interpolation — `${expression}` — embed any JS expression  
* Multi-line strings — no need for `\n`  
* Tagged templates — `tag\`string\`\` — function processes template literal parts  
  * Used by styled-components, GraphQL (`gql\`query\`\`)  
* Nested template literals — template inside template  
* Expression inside `${}` can be any JS expression — ternary, function call, arithmetic

**Full Answer:**
Template literals (ES6) are string literals that allow embedded expressions. They use **backticks** (`` ` ``) instead of quotes.
- **Interpolation**: You can embed variables or expressions directly using `${expression}`.
- **Multi-line**: They allow strings to span multiple lines without needing concatenation (`+`) or escape characters (`\n`).
- **Tagged Templates**: You can prefix a template literal with a function name (a "tag") to parse the template in a custom way (common in libraries like `styled-components`).

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

**Full Answer:**
Modern JavaScript (ES6+) introduced many features to make development more efficient:
- **Default Parameters**: Set default values for function arguments.
- **Enhanced Object Literals**: Shorthand for keys and values, and computed property names.
- **Optional Chaining (`?.`)**: Safely access deep object properties.
- **Nullish Coalescing (`??`)**: Provide defaults for `null`/`undefined` only.
- **Map and Set**: New data structures for unique collections and key-value pairs with any type of key.
- **Array.at()**: Allows negative indexing (e.g., `arr.at(-1)` for the last element).

**Trap Explained: Map vs Object**
*"Why use a `Map` when I can just use an `Object`?"*
- **Keys**: Objects only allow Strings or Symbols as keys. Maps allow **any type** (including functions or other objects).
- **Order**: Maps guarantee insertion order; Objects do not (consistently).
- **Size**: Maps have a `.size` property; for Objects, you must use `Object.keys(obj).length`.
- **Performance**: Maps are optimized for frequent additions and removals.

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

**Full Answer:**
A **Promise** is an object representing the eventual completion or failure of an asynchronous operation.
- **States**: Every promise starts in **Pending**. It then transitions to **Fulfilled** (success) or **Rejected** (failure). Once settled, it cannot change state.
- **Consuming**: We use `.then()` to handle success and `.catch()` to handle errors.
- **Chaining**: You can chain multiple `.then()` calls; the value returned from one is passed to the next.
- **Why use them?**: Promises solve the "Callback Hell" problem by allowing you to write asynchronous code in a more linear, readable fashion.

**Trap Explained: The Missing `return` in Chaining**
*"What happens if I don't return a value in a `.then()` block?"*
```javascript
Promise.resolve(1)
  .then(val => { val + 1; }) // ❌ Forgot 'return'
  .then(val => console.log(val)); // Output: undefined
```
In a Promise chain, the next `.then()` receives whatever the previous one **returns**. If you don't return anything, it receives `undefined`.

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

**Full Answer:**
JavaScript provides several static methods to handle multiple promises simultaneously:
- **`Promise.all()`**: Waits for all promises to resolve. If **any** promise rejects, the whole thing rejects immediately.
- **`Promise.allSettled()`**: Waits for all promises to finish (either resolve or reject) and returns an array of their results. This is useful when you want to continue even if some requests fail.
- **`Promise.race()`**: Returns the result of the first promise that settles (either resolves or rejects).
- **`Promise.any()`**: Returns the first promise that **resolves**. It only rejects if all promises in the array fail.

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

**Full Answer:**
`async` and `await` are syntactic sugar built on top of Promises, making asynchronous code look and behave like synchronous code.
- **`async`**: When placed before a function, it ensures the function always returns a promise.
- **`await`**: Can only be used inside an `async` function. It pauses the execution of the code until the promise resolves and returns the value.
- **Error Handling**: Unlike `.then().catch()`, we use standard `try...catch` blocks with `async/await`, which makes error handling much more intuitive.
**Performance Tip**: Be careful not to "sequentialize" independent promises. Instead of `await a(); await b();`, use `await Promise.all([a(), b()])` to run them in parallel.

**Trap Explained: Sequential vs Parallel Await**
```javascript
// ❌ SLOW: Takes 2 seconds
const user = await fetchUser(); // 1s
const posts = await fetchPosts(); // 1s

// ✅ FAST: Takes 1 second
const [user, posts] = await Promise.all([fetchUser(), fetchPosts()]);
```
Always look for opportunities to use `Promise.all` for independent requests in your React `useEffect` or Node.js controllers.

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

**Full Answer:**
The **Fetch API** is the modern, built-in way to make network requests in the browser.
- **Usage**: `fetch(url)` returns a promise that resolves to a `Response` object.
- **Two-Step Process**: Because the response body is a stream, you first `await` the fetch call to get the response headers, and then `await response.json()` to parse the actual data.
- **The "Gotcha"**: `fetch()` only rejects on network failure (like being offline). It **does not reject** on HTTP errors like 404 or 500. You must manually check `if (!response.ok)` to handle these cases.

**Trap Explained: The Fetch Error Trap**
Interviewers love this: *"Will `fetch` go into the `.catch()` block if the server returns a 500 Internal Server Error?"*
- **The Answer:** **No.** As long as the server responded, `fetch` considers it a success. You must write:
```javascript
fetch('/api')
  .then(res => {
    if (!res.ok) throw new Error("Server Error");
    return res.json();
  })
  .catch(err => console.log("Caught!", err));
```

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

**Full Answer:**
**Axios** is a popular third-party library for making HTTP requests. While `fetch` is built-in, Axios is often preferred in MERN projects because:
1. **Automatic JSON**: It automatically parses JSON responses.
2. **Error Handling**: It automatically rejects the promise for 4xx and 5xx status codes.
3. **Interceptors**: It allows you to define global request/response handlers (e.g., automatically attaching a JWT token to every request).
4. **Wide Support**: It works consistently in both browsers and Node.js environments.

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

**Full Answer:**
The **DOM (Document Object Model)** is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content.
- **Selectors**: Modern JS uses `querySelector` and `querySelectorAll` for flexible, CSS-like selection.
- **Manipulation**: You can update content via `textContent` or `innerHTML`, and change styles via the `style` property or `classList`.
- **Optimization**: Frequently touching the DOM is slow. In MERN apps, React handles this efficiently through the **Virtual DOM**, minimizing direct interaction with the real DOM.

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

**Full Answer:**
Events are actions that happen in the system you are programming, which the system tells you about so your code can respond to them.
- **Event Listeners**: The `addEventListener()` method is the modern way to handle events. It allows multiple handlers for the same event and provides fine-grained control (like `once: true`).
- **Event Object**: When an event fires, JS passes an `event` object to the handler. This object contains crucial information like `event.target` (who triggered it) and `event.type`.
- **Prevent Default**: `event.preventDefault()` is used to stop the browser's default behavior (like stopping a form from refreshing the page on submit).

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

**Full Answer:**
Understanding the event lifecycle is key to advanced JS:
- **Bubbling**: By default, an event starts at the target element and "bubbles up" through its parents.
- **Capturing**: The opposite of bubbling; the event starts at the top and goes down to the target.
- **Event Delegation**: This is a powerful pattern where instead of adding listeners to many individual items (like 100 list items), you add **one** listener to the parent. Because of bubbling, the parent will catch any event from its children. You then use `event.target` to see which child was actually clicked. This is better for memory and handles dynamically added items automatically.

**Trap Explained: `stopPropagation` vs `preventDefault`**
*"Do these two do the same thing?"*
- **`preventDefault()`**: Stops the **browser's default action** (e.g., following a link or submitting a form). The event still bubbles up.
- **`stopPropagation()`**: Stops the **event from moving** to parent elements. The browser's default action may still happen.
- Use `preventDefault` for logic control and `stopPropagation` for UI nesting control (like a "Delete" button inside a clickable "Card").

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

**Full Answer:**
JavaScript provides a robust way to handle runtime errors using `try...catch...finally`.
- **`try`**: You wrap the code that might fail.
- **`catch`**: If an error occurs, the code inside `catch` runs, giving you an `Error` object with a `message` and `stack` trace.
- **`finally`**: This block always runs, whether there was an error or not. It's great for cleanup (e.g., closing a database connection).
- **`throw`**: You can manually trigger an error using `throw new Error("Message")`.
**Note**: `try...catch` only works for synchronous code. For asynchronous code, you must use `.catch()` on a promise or use `try...catch` inside an `async` function.

---

**Q29. What are common patterns for async error handling?** `[1-2 yrs]`

* Async/await with try/catch — cleanest approach  
* `.catch()` on Promise chain  
* Wrapper utility — `const [err, data] = await to(promise)` (Go-style error handling pattern)  
* Global unhandled rejection handler — `process.on('unhandledRejection', handler)` in Node.js  
* Error boundaries in React — `componentDidCatch`, `ErrorBoundary` component  
* Axios error handling — `error.response` (server responded), `error.request` (no response), `error.message` (setup error)

**Full Answer:**
In modern MERN apps, most errors happen during network requests.
- **Async/Await**: The standard is to wrap `await` calls in `try...catch`.
- **Axios Errors**: Axios provides a rich error object. `error.response` tells you the server sent a 4xx or 5xx error, while `error.request` means the server never responded at all.
- **Global Handling**: In Node.js, you should listen for `unhandledRejection` to catch promises that failed without a `.catch()`. In React, you use **Error Boundaries** to catch errors in the UI component tree.

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

**Full Answer:**
A **Closure** is one of the most powerful features of JavaScript. It occurs when a function is defined inside another function and "remembers" its lexical environment (variables) even after the outer function has finished executing.
- **Data Privacy**: Closures allow you to create "private" variables that can't be accessed from the outside, only through the inner function.
- **State Maintenance**: They are used to maintain state in asynchronous callbacks or factory functions.
- **The Loop Trap**: If you use `var` in a loop with `setTimeout`, the closure captures the final value of the variable. Using `let` fixes this because `let` creates a new binding for every iteration of the loop.

**Trap Explained: The `var` in a loop problem**
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3
```
**Why?** Because `var` is function-scoped. By the time the `setTimeout` callbacks run (after 100ms), the loop has already finished, and the single variable `i` shared by all callbacks has been incremented to `3`.
**The Fix:** Use `let`. Since `let` is block-scoped, a **new** `i` is created for every single iteration of the loop, so each callback "remembers" its own version of `i`.

---

**Q31. What is lexical scope?** `[1-2 yrs]`

* Scope determined at code **write time** (not runtime)  
* A function's scope chain is determined by where it is **defined**, not where it is **called**  
* Inner functions have access to outer function variables — forms the basis of closures  
* Lexical environment — the surrounding context captured by a closure  
* Difference between lexical scope and dynamic scope (JS uses lexical, not dynamic)

**Full Answer:**
Lexical scope (also known as Static Scope) means that the scope of a variable is determined by its position within the source code.
- When you nest functions, the inner function has access to the variables declared in its outer scope.
- This "lookup" process is based on where the functions were **written**, not where they are executed.
- This is the fundamental mechanism that allows **Closures** to work.

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

**Full Answer:**
The **Event Loop** is what allows JavaScript to be non-blocking even though it is single-threaded.
1. **Call Stack**: Executes synchronous code.
2. **Web APIs**: Handles async tasks like timers or data fetching.
3. **Queue System**: When an async task finishes, its callback moves to a queue.
   - **Microtask Queue**: High priority (Promises, `queueMicrotask`).
   - **Macrotask Queue**: Lower priority (`setTimeout`, `setInterval`).
4. **The Loop**: Once the Call Stack is empty, the Event Loop first clears **all** pending microtasks, then moves **one** macrotask to the stack. This process repeats.

**Trap Explained: Predict the Execution Order**
```javascript
console.log("1"); // Synchronous

setTimeout(() => console.log("2"), 0); // Macrotask

Promise.resolve().then(() => console.log("3")); // Microtask

console.log("4"); // Synchronous
```
**Execution Steps:**
1.  Print **"1"** (Sync).
2.  Schedule **"2"** in Macrotask queue.
3.  Schedule **"3"** in Microtask queue.
4.  Print **"4"** (Sync).
5.  Call Stack is empty. Check Microtask queue. Print **"3"**.
6.  Microtask queue empty. Check Macrotask queue. Print **"2"**.
**Final Output: 1, 4, 3, 2**

---

**Q33. What is the difference between microtasks and macrotasks?** `[2-3 yrs]`

* **Macrotasks** — `setTimeout`, `setInterval`, `setImmediate` (Node), I/O, UI rendering  
* **Microtasks** — `Promise.then/catch/finally`, `queueMicrotask()`, `MutationObserver`, `async/await` continuations  
* After each macrotask — entire microtask queue is drained before next macrotask  
* Why this matters — Promise callbacks always run before the next setTimeout callback  
* `queueMicrotask(fn)` — directly enqueue a microtask  
* Node.js specific — `process.nextTick()` runs before microtasks (even higher priority)

**Full Answer:**
Not all asynchronous tasks are treated equally in the event loop:
- **Microtasks**: Have higher priority. They are executed immediately after the current task finishes and before the browser renders or moves to the next macrotask. Examples include `Promise.then()` and `MutationObserver`.
- **Macrotasks**: Have lower priority. They are executed one at a time, with the microtask queue being cleared in between. Examples include `setTimeout` and `I/O` operations.
**Interview Tip**: If you have a `setTimeout` and a `Promise.resolve()` both set to run "now," the Promise will always win because it is a microtask.

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

**Full Answer:**
These are timing functions provided by the browser:
- **`setTimeout`**: Executes a function once after a specified delay. It's often used for non-critical background tasks.
- **`setInterval`**: Repeatedly executes a function at a fixed time interval. 
- **The Issue with Intervals**: If the code inside `setInterval` takes longer than the interval itself, the calls can "stack up," leading to performance issues.
- **The Fix**: Use **Recursive `setTimeout`**. This ensures the next delay starts only *after* the previous execution has finished, providing a consistent gap between calls.

**Trap Explained: Why `setInterval` is dangerous**
If your code inside an interval takes **1.5s** to run, but your interval is set to **1s**:
- `setInterval`: The browser will queue the next call before the first one finishes, leading to "stacking" and lag.
- `Recursive setTimeout`: The next timer only starts **after** the code finishes. This guarantees the 1s gap you actually wanted.

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

**Full Answer:**
**ES Modules (ESM)** are the official standard for modularizing JavaScript code.
- **`export`**: You use `export` to make variables or functions available to other files. There are **Named Exports** (multiple allowed per file) and **Default Exports** (only one allowed).
- **`import`**: You use `import` to bring in those values.
- **Static Nature**: ESM is "static," meaning the imports are determined when the code is parsed, not when it runs. This allows for **Tree Shaking** (removing unused code from the final bundle), which is vital for performance in MERN apps.

**Trap Explained: Can I import inside an `if` statement?**
- **The Answer:** **No**, not with the standard `import` keyword. Because ESM is static, all imports must be at the top level.
- **The Solution:** If you need conditional loading, you must use **Dynamic Import**:
```javascript
if (userIsAdmin) {
  const module = await import('./adminPanel.js');
  module.show();
}
```
This returns a Promise and is great for **Code Splitting** in React.

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

**Full Answer:**
These are the two main module systems in JavaScript:
- **CommonJS (CJS)**: The original system for Node.js. It uses `require()` and `module.exports`. It is **synchronous**, meaning modules are loaded one by one.
- **ES Modules (ESM)**: The modern, official standard. It uses `import` and `export`. It is **asynchronous** and supports "static analysis," which allows tools to perform **Tree Shaking** (removing unused code).
**MERN Tip**: React (frontend) uses ESM. Node.js (backend) used to be CJS-only but now supports ESM if you set `"type": "module"` in your `package.json`.

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

**Full Answer:**
JavaScript is a **prototype-based** language. This means that every object has a private property called `[[Prototype]]` (commonly accessed via `__proto__`) which holds a link to another object.
- When you try to access a property that doesn't exist on an object, JS looks at its prototype.
- If it's not there, it looks at the prototype's prototype, and so on. This is the **Prototype Chain**.
- The chain ends when it reaches an object whose prototype is `null` (usually `Object.prototype`).
- This is how methods like `.toString()` are available on almost all objects—they are inherited from `Object.prototype`.

**Trap Explained: `prototype` vs `__proto__`**
Interviewers will ask: *"What is the difference between these two?"*
- **`prototype`**: This is a property on **Constructor Functions** (or Classes). It is the blueprint used for objects created by that function.
- **`__proto__`**: This is a property on **Object Instances**. It is the actual link that points to the prototype.
- **The Relationship**: `const myCar = new Car();` means `myCar.__proto__ === Car.prototype`.

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

**Full Answer:**
Introduced in ES6, **Classes** are primarily "syntactic sugar" over JavaScript's existing prototype-based inheritance.
- They provide a much cleaner and more familiar syntax for developers coming from languages like Java or C++.
- **`constructor`**: A special method for creating and initializing an object instance.
- **`super()`**: Used in a child class to call the constructor or methods of the parent class.
- **Private Fields**: Using the `#` prefix (e.g., `#name`) allows you to define truly private variables that cannot be accessed outside the class.

**Trap Explained: "Classes are just Sugar"**
Interviewers will ask: *"Are JS classes real classes like in Java or C#?"*
- **The Answer:** **No.** It is "Syntactic Sugar." Under the hood, JS still uses Prototypes. A `class` is actually just a special type of `function`.
- **Proof:** `typeof class MyClass {}` returns `"function"`.
- **Inheritance:** In Java, classes are copied. In JS, they are linked via the prototype chain.

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

**Full Answer:**
JavaScript implements the four core pillars of Object-Oriented Programming:
1. **Encapsulation**: Hiding data and only exposing what's necessary (achieved via closures or `#private` class fields).
2. **Inheritance**: Creating a new class based on an existing one (achieved via `extends`).
3. **Polymorphism**: The ability for different classes to be treated as instances of the same parent class, but with their own specific implementations of methods (overriding methods).
4. **Abstraction**: Hiding complex logic behind simple interfaces (achieved by defining methods that perform complex tasks internally).

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

**Full Answer:**
These are the three "workhorses" of functional programming in JavaScript:
- **`map()`**: Transforms every element in an array and returns a **new array** of the same length.
- **`filter()`**: Checks every element against a condition and returns a **new array** containing only the elements that passed (the result can be shorter).
- **`reduce()`**: "Reduces" the entire array into a **single value** (like a sum, a string, or even a new object). It takes an accumulator and the current value.
**Crucially**, none of these methods change the original array; they always return new data. This is called **Immutability**.

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

**Full Answer:**
Modern JavaScript arrays are incredibly powerful. Beyond `map/filter/reduce`, these methods are essential:
- **`find()` / `findIndex()`**: Used to locate a specific element or its index.
- **`some()` / `every()`**: Used for validation (e.g., "do some items match?" or "do all items match?").
- **`flat()`**: Useful for cleaning up nested arrays (common in API responses).
- **`sort()`**: **Warning**: It mutates the original array and sorts alphabetically by default. For numbers, always provide a comparator: `(a, b) => a - b`.
- **`slice()` vs `splice()`**: `slice` is immutable (returns a copy), while `splice` is mutable (changes the original).

**Trap Explained: The `sort()` behavior**
*"What is the output of `[1, 10, 2].sort()`?"*
- **The Answer:** `[1, 10, 2]`. By default, `sort()` converts everything to **Strings** and compares UTF-16 code units. Since "10" starts with "1", it comes before "2".
- **The Fix:** Always provide a compare function for numbers: `arr.sort((a, b) => a - b)`.

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

**Full Answer:**
These are foundational concepts in **Functional Programming**:
- **Pure Functions**: A function that always returns the same output for the same input and has **no side effects** (doesn't change outside variables or log to the console).
- **Immutability**: The idea that data should not be changed after it's created. Instead of modifying an existing object, you create a new one with the updated values.
**Why it matters in MERN**: React uses immutability to determine if a component should re-render. If you mutate an object directly, React might not "see" the change because the memory reference remains the same.

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

**Full Answer:**
Browsers provide three main ways to store data locally:
1. **`localStorage`**: Best for persistent data (like user theme) that stays even after the browser is closed. Large capacity (5MB+).
2. **`sessionStorage`**: Best for sensitive data during a single session. It's wiped as soon as the tab is closed.
3. **Cookies**: Small (4KB) and sent to the server with every request.
**MERN Security Note**: For storing Authentication Tokens (JWT), **HttpOnly Cookies** are the gold standard because they cannot be accessed by JavaScript, protecting you from XSS attacks.

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

**Full Answer:**
The `localStorage` API is simple but synchronous:
- **`setItem('key', 'value')`**: Stores data.
- **`getItem('key')`**: Retrieves data.
- **JSON handling**: Since `localStorage` only stores strings, you must use `JSON.stringify()` when saving objects and `JSON.parse()` when reading them back.
- **Events**: You can actually listen for changes to storage in other tabs using the `window.onstorage` event, which is useful for syncing state across multiple open tabs of your app.

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

**Full Answer:**
Web storage is convenient but has risks:
- **XSS (Cross-Site Scripting)**: If an attacker can run JS on your page, they can steal everything in `localStorage`. This is why you should never store passwords or raw sensitive data there.
- **CSRF (Cross-Site Request Forgery)**: Cookies are vulnerable to this. An attacker can trick a user's browser into sending a request with their cookies attached.
- **The Solution**: Use **HttpOnly** and **SameSite** flags on cookies for authentication. Use **Content Security Policy (CSP)** headers to prevent unauthorized scripts from running.

**Interview Comparison: JWT Storage**
| Feature | LocalStorage | HttpOnly Cookie |
| :--- | :--- | :--- |
| **XSS Protection** | ❌ Vulnerable (JS can read it) | ✅ Safe (JS cannot access) |
| **CSRF Protection** | ✅ Safe (Not sent automatically) | ❌ Vulnerable (Requires SameSite) |
| **Capacity** | 5MB - 10MB | ~4KB |
| **Ease of Use** | Simple JS API | Requires Backend config |

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

**Full Answer:**
This is about how nested objects are handled during a copy:
- **Shallow Copy**: Copies the top-level properties. If a property is an object, it only copies the **reference**, meaning the original and the copy still share the nested object.
- **Deep Copy**: Recursively copies every level of the object. The original and the copy are completely disconnected.
**Modern Fix**: Use `structuredClone(obj)` for deep copying in modern browsers. Avoid the old `JSON.parse(JSON.stringify(obj))` hack as it breaks with special types like Dates and Functions.

**Trap Explained: The Circular Reference**
A circular reference occurs when an object points to itself (directly or indirectly).
```javascript
const user = { name: "Aniket" };
user.self = user; // Circular reference!

JSON.stringify(user); // Output: TypeError: Converting circular structure to JSON
```
Most simple cloning methods will crash or hang when they hit a circular reference. `structuredClone()` is designed to handle these cases correctly.

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

**Full Answer:**
The `this` keyword is one of the most confusing parts of JS because its value is **determined by the call site** (how the function is called).
- In a **Method**: `this` refers to the object.
- In a **Function**: `this` refers to the global object (or `undefined` in strict mode).
- In an **Arrow Function**: `this` is lexically inherited from the surrounding scope.
- **Explicit Binding**: You can manually set `this` using `.call()`, `.apply()`, or `.bind()`.
**React Tip**: This is why we use arrow functions for event handlers in React class components—to ensure `this` correctly refers to the component instance.

**Trap Explained: Explicit vs Implicit Binding**
```javascript
const person = {
  name: "Aniket",
  greet: function() { console.log(this.name); }
};

const isolatedGreet = person.greet;
isolatedGreet(); // Output: undefined (this is now the global object)

// The Fix
const boundGreet = person.greet.bind(person);
boundGreet(); // Output: "Aniket"
```
In React Class Components, this is why you'd often see `this.handleClick = this.handleClick.bind(this)` in the constructor.

---

**Q48. What is memoization?** `[2-3 yrs]`

* Optimization technique — cache results of expensive function calls  
* If same input is called again, return cached result without re-executing  
* Implemented using closure to maintain cache object  
* `useMemo` and `useCallback` in React — memoization hooks  
* Pure functions are prerequisite for memoization (same input must always give same output)  
* Trade-off — memory usage increases to save computation time

**Full Answer:**
Memoization is an optimization technique where you **cache the results** of expensive function calls and return the cached result when the same inputs occur again.
- It requires the function to be **Pure** (same input = same output).
- In React, `useMemo` is used to cache expensive calculations, and `useCallback` is used to cache function references to prevent unnecessary re-renders.

**Trap Explained: Memoization Memory**
While memoization saves time, it **uses more memory** (since you are storing old results). In a real MERN app, you must be careful about the "Cache Size." If your function takes thousands of unique arguments, your cache object will grow until you run out of memory. This is why libraries like Lodash offer `_.memoize` with configurable cache limits.

---

**Q49. What is the difference between `for...in` and `for...of`?** `[Fresher]`

* `for...in` — iterates over **enumerable property keys** of an object (and inherited ones)  
  * Use `hasOwnProperty` check to skip inherited properties  
  * Works on arrays too but gives string indices — bad practice  
* `for...of` — iterates over **values** of any iterable (arrays, strings, Maps, Sets, generators)  
  * Does not work on plain objects (not iterable by default)  
  * Use `Object.keys()`, `Object.values()`, `Object.entries()` to loop over objects with `for...of`

**Full Answer:**
- **`for...in`**: Iterates over the **keys (indices)** of an object. It is generally used for plain objects. Be careful, as it also iterates over inherited properties from the prototype chain.
- **`for...of`**: Iterates over the **values** of any iterable (like an Array, String, Map, or Set). It is generally cleaner for looping through arrays and does not include prototype properties.

**Trap Explained: Looping Comparison**
```javascript
const arr = [10, 20];
arr.custom = "trap";

for (let key in arr) console.log(key); 
// Output: "0", "1", "custom" (Gets indices AND extra properties!)

for (let val of arr) console.log(val); 
// Output: 10, 20 (Gets only values, ignores extra properties)
```
In MERN, **always use `for...of`** for arrays to avoid accidental bugs from modified prototypes.

---

**Q50. What is a generator function?** `[2-3 yrs]`

* `function*` — can pause and resume execution  
* `yield` — pauses function, returns value to caller  
* Returns an iterator — call `.next()` to resume, returns `{value, done}`  
* `yield*` — delegates to another generator or iterable  
* Use cases — infinite sequences, lazy evaluation, custom iterators, `async` generator for streaming data  
* Generators behind the scenes of early async patterns (before async/await)

**Full Answer:**
Generators are special functions that can be **paused and resumed**.
- They are defined using the `function*` syntax and use the `yield` keyword to pause.
- When called, they return a **Generator Object** (an iterator). You call `.next()` on this object to execute the code until the next `yield`.
- They are useful for creating custom iterators, handling infinite data streams, or managing complex asynchronous flows (though `async/await` has largely replaced them for basic async tasks).

---

**Q51. What is Currying and Partial Application?** `[2-3 yrs]`

* **Currying**: Transforming a function that takes multiple arguments `f(a, b, c)` into a sequence of functions `f(a)(b)(c)`.
* **Partial Application**: Fixing a few arguments of a function, producing a new function of smaller arity.
* Use cases — event handling with preset data, configuration factories, functional pipelines.

**Full Answer:**
These are functional programming techniques used to create more flexible and reusable functions.
- **Currying**: It breaks down a function that takes multiple arguments into a series of nested functions that each take one argument. This allows you to "preload" a function with a specific value.
- **Partial Application**: Unlike currying, it doesn't have to be one argument at a time. You can fix two arguments of a 5-argument function to create a new 3-argument function.
- **Why use it?**: It helps in **Function Composition**, allowing you to build complex logic by combining simple, pre-configured functions.

---

**Q52. What is the difference between Debouncing and Throttling?** `[2-3 yrs]`

* **Debouncing**: Ensures that the function will only be executed after a certain amount of time has passed since it was last called (resetting the timer each time).
* **Throttling**: Ensures that the function is called at most once in a specified time period (limiting the rate of execution).
* Use cases:
  * Debounce: Search bar autocomplete, window resize.
  * Throttle: Scroll events, mouse move (gaming/animations).

**Full Answer:**
Both are techniques used to improve performance by limiting how often a function is executed in response to high-frequency events (like scrolling or typing).
- **Debounce**: Think of an elevator. The door won't close until everyone stops pushing the "open" button for 5 seconds. If someone pushes it again at second 4, the 5-second timer restarts. This is perfect for a search input where you only want to hit the API once the user finishes typing.
- **Throttle**: Think of a water faucet with a slow drip. No matter how much water is behind it, only one drop falls every second. This is perfect for scroll listeners where you want to update the UI at a steady rate, but not 100 times per second.

---

**Q53. What are Proxy and Reflect objects in JavaScript?** `[3+ yrs]`

* **Proxy**: Allows you to create a "wrapper" for another object, intercepting and redefining fundamental operations (like getting, setting, or deleting properties).
* **Reflect**: A built-in object that provides methods for interceptable JavaScript operations (like `Reflect.get`, `Reflect.set`).
* Use cases — validation, logging/profiling, data binding (reactive systems like Vue 3).

**Full Answer:**
- **Proxy**: A Proxy object wraps another object and allows you to intercept basic operations. You define "traps" (like `get` or `set`) to control how the object behaves. For example, you could create a proxy that prevents anyone from adding new properties to an object.
- **Reflect**: It's a companion to Proxy. While Proxy is for *intercepting* actions, Reflect is for *performing* those actions in the standard way. It's often used inside Proxy traps to ensure the original behavior still occurs after your custom logic.
**MERN Context**: Frameworks like Vue 3 and MobX use Proxies to create "reactive" data that automatically updates the UI when a value changes.

---

**Q54. How does Garbage Collection work in JavaScript?** `[3+ yrs]`

* **Memory Lifecycle**: Allocate → Use → Release.
* **Garbage Collection (GC)**: Automatic process of finding memory that is no longer reachable and reclaiming it.
* **Algorithms**:
  * **Reference Counting**: Reclaims if reference count is 0 (fails with circular refs).
  * **Mark-and-Sweep**: (Main algorithm) Starts from "roots" (global, local variables) and marks all reachable objects. Anything not marked is swept (deleted).
* **Memory Leaks**: Global variables, forgotten timers/callbacks, closures (if not managed), detached DOM nodes.

**Full Answer:**
JavaScript engines (like V8) use an automatic Garbage Collector so developers don't have to manually manage memory.
- **Mark-and-Sweep**: The engine periodically starts from the "Roots" (the global object and current execution stack) and "marks" every object it can reach. Then, it "sweeps" away any object that wasn't marked.
- **Memory Leaks**: Even with GC, you can have leaks. A common one is forgetting to clear a `setInterval`—the function remains "reachable" in the eyes of the engine, so it (and anything it closes over) is never deleted.
- **Best Practice**: Always clean up event listeners and intervals when they are no longer needed (especially in React's `useEffect` cleanup).

---

**Q55. What are the common Design Patterns in JavaScript?** `[3+ yrs]`

* **Module Pattern**: Encapsulating private and public members (pre-ESM).
* **Singleton Pattern**: Ensuring a class has only one instance (e.g., a database connection).
* **Factory Pattern**: Creating objects without specifying the exact class (e.g., a UI component factory).
* **Observer/Pub-Sub Pattern**: Objects subscribing to events/changes in another object (e.g., Redux, event listeners).
* **Decorator Pattern**: Dynamically adding behavior to an object.

**Full Answer:**
Design patterns are reusable solutions to common problems in software design.
- **Singleton**: Often used for global state managers or database connection pools in Node.js.
- **Observer**: This is the heart of the web. Every time you use `addEventListener`, you are using the Observer pattern. Redux also uses this to notify components when the store changes.
- **Module**: While we now have ES Modules (`import/export`), the "Module Pattern" using closures was the standard for years to keep code organized and private.
- **Strategy Pattern**: Useful in MERN when you have different ways to handle a task (e.g., different payment methods like Stripe vs PayPal) and want to swap them easily.

---

---

### **16. Advanced Industry-Standard Topics**

---

**Q56. What are Generators and Iterators in JavaScript?** `[3+ yrs]`

* **Iterators** — objects that define a sequence and return a value upon completion via the `.next()` method  
* **Generators** — special functions that can be paused and resumed using the `function*` syntax and `yield` keyword  
* Execution — calling a generator function doesn't run its code; it returns a Generator Object  
* Use cases — handling infinite data streams, custom iteration logic, async flow control (pre-async/await)

**Full Answer:**
Generators are functions that can "pause" their execution and "yield" multiple values over time. They are perfect for memory-efficient data processing. For example, if you need to process a 1GB file line by line, a Generator can yield one line at a time instead of loading the entire file into memory.

**Trap Explained: The "One-Time Use" Trap**
- **The Answer:** Generator objects are **one-time use**. Once you have iterated through a generator to the end, you cannot "reset" it or loop through it again. You must call the generator function again to create a new instance.

---

**Q57. What are Symbols and why are they used?** `[3+ yrs]`

* Primitive type — introduced in ES6, guaranteed to be unique  
* Hidden properties — Symbols are not enumerable in `for...in` loops or `Object.keys()`  
* **Well-known Symbols** — built-in symbols used by the JS engine (e.g., `Symbol.iterator`, `Symbol.toStringTag`)  
* Use cases — adding "private" metadata to objects, avoiding property name collisions in libraries

**Full Answer:**
A Symbol is a unique and immutable primitive value. Its primary purpose is to serve as a unique identifier for object properties. This ensures that even if two libraries add a property with the same "name" to an object, they won't overwrite each other if they use Symbols.

**Trap Explained: The "Private" Myth**
*"Are Symbols a way to create truly private properties in JS?"*
- **The Answer:** **No.** While Symbols are hidden from normal loops, they can still be accessed using `Object.getOwnPropertySymbols()`. They are for **avoiding collisions**, not for security or true privacy.

---

**Q58. What is the `Intl` API and why is it preferred for i18n?** `[2-3 yrs]`

* **Internationalization API** — provides language-sensitive string comparison, number formatting, and date/time formatting  
* **DateTimeFormat** — localized dates (e.g., `12/31/2025` vs `31/12/2025`)  
* **NumberFormat** — currency, percentages, and unit formatting  
* **RelativeTimeFormat** — "2 days ago", "in 3 months"  
* Benefit — built into the browser; no need for massive libraries like Moment.js or Intl.js

**Full Answer:**
The `Intl` object is the standard way to handle internationalization in modern MERN apps. Instead of manually formatting currency or dates, you use `new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(500)`, which automatically handles local symbols and decimal rules.

**Trap Explained: The "Node.js" Trap**
- **The Answer:** While `Intl` works perfectly in browsers, older versions of Node.js required a special "Full ICU" build to support all languages. Always verify your Node.js version and ICU support when doing server-side formatting in a MERN project.

---

**Q59. What are WeakMap and WeakSet and how do they help with memory management?** `[3+ yrs]`

* **WeakMap** — a Map where keys must be objects and are held "weakly"  
* **WeakSet** — a Set where values must be objects and are held "weakly"  
* Garbage Collection — if there are no other references to an object used as a key in a WeakMap, the object can be garbage collected  
* Key difference — you cannot iterate over WeakMap/WeakSet and they have no `size` property

**Full Answer:**
WeakMap and WeakSet are memory-efficient collections. They are used to associate data with an object without "protecting" that object from being deleted by the Garbage Collector. They are commonly used for caching metadata or managing private data for classes.

**Trap Explained: The "Primitive Key" Trap**
- **The Answer:** You **cannot** use primitives (strings, numbers) as keys in a WeakMap. Primitives are not garbage collected in the same way objects are, so they would defeat the purpose of a "weak" reference.

---

**Q60. What is the TC39 Process and how does JavaScript evolve?** `[3+ yrs]`

* **TC39** — the technical committee that maintains ECMAScript (the JS standard)  
* **The 5 Stages:**  
  * Stage 0 (Strawman): Initial idea  
  * Stage 1 (Proposal): Case for the feature  
  * Stage 2 (Draft): Initial spec  
  * Stage 3 (Candidate): Spec complete, awaiting implementation feedback  
  * Stage 4 (Finished): Ready to be added to the official standard  
* Babel — allows us to use Stage 1-3 features today by compiling them to Stage 4 or ES5

**Full Answer:**
JavaScript doesn't change randomly; it follows a rigorous 5-stage process managed by TC39. A senior developer keeps an eye on "Stage 3" proposals because those are the features that will land in browsers next (like the `Pipe Operator` or `Records and Tuples`).

**Trap Explained: The "EcmaScript Year" Trap**
*"What is the difference between ES6 and ES2025?"*
- **The Answer:** Since 2015, JS has moved to a yearly release cycle. ES6 (ES2015) was a massive leap, but subsequent versions (ES2016+) are smaller, incremental updates. Most people just refer to "ESNext" as the collection of all current Stage 4 features.

---

That's the complete **JavaScript** section — **60 questions** with full subtopic depth, ready to merge into your MERN Interview Kit.


[⬅️ Previous: Material UI](../../MERN_Study_Structure/01_Web_Development_Fundamentals/05_Material_UI/05_Material_UI.md) | [🏠 Home](../../README.md) | [Next: Typescript ➡️](../../MERN_Study_Structure/01_Web_Development_Fundamentals/07_Typescript/07_Typescript.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>