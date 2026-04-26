# Node.js
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] [Node.js](https://nodejs.org/docs/latest/api/) Fundamentals
- [x] Introduction to Node.js & NPM/Yarn
- [x] [Node.js](https://nodejs.org/docs/latest/api/) Modules (CommonJS vs. ES Modules)
- [x] Asynchronous JavaScript (Callbacks, Promises, Async/Await)
- [x] Event Loop & Streams
- [x] File System (fs module)
- [x] Environment Variables & Configuration
- [x] Debugging & Logging (Winston, Morgan)

## 📝 Detailed Notes

### 1. Introduction to Node.js
Node.js is a **cross-platform, open-source JavaScript runtime environment** that can run on Windows, Linux, Unix, macOS, and more. Node.js runs on the **V8 JavaScript engine**, and executes JavaScript code outside a web browser.
- **NPM/Yarn**: Package managers used to install and manage dependencies. `npm init -y` creates a `package.json`.

### 2. Modules (CommonJS vs. ES Modules)
- **CommonJS (CJS)**: Legacy system using `require()` and `module.exports`. Default in Node.js.
- **ES Modules (ESM)**: Modern system using `import` and `export`. Enabled via `"type": "module"` in `package.json` or `.mjs` extension.

### 3. Asynchronous JavaScript
Node is non-blocking. It handles operations via:
- **Callbacks**: Functions passed as arguments (leads to callback hell).
- **Promises**: Objects representing the eventual completion of an async operation.
- **Async/Await**: Syntactic sugar over promises for cleaner code.

### 4. Event Loop & Streams
- **Event Loop**: The secret behind Node's scalability. It allows Node to perform non-blocking I/O operations despite JS being single-threaded. Phases include: Timers, I/O callbacks, Idle/Prepare, Poll, Check, and Close callbacks.
- **Streams**: Efficient way to handle large data. Instead of loading a 1GB file into memory, you read it in small "chunks".
  - `fs.createReadStream()`, `fs.createWriteStream()`.

### 5. File System (fs module)
```javascript
const fs = require('fs');

// Synchronous (Blocks the thread - Avoid)
const data = fs.readFileSync('test.txt', 'utf8');

// Asynchronous (Recommended)
fs.readFile('test.txt', 'utf8', (err, data) => {
    if (err) throw err;
    consoleapp.use(helmet());
app.enableCors();

### 6. NoSQL Injection & Data Sanitization
Attackers can send malicious queries in `req.body`. Use `mongo-sanitize` to remove any keys starting with `$`.
```javascript
const sanitize = require('mongo-sanitize');
const cleanBody = sanitize(req.body);
```
Also, use **express-validator** or **Zod** to ensure inputs match expected types (e.g., string, email).

// Using Promises (Best)
const fsPromises = require('fs').promises;
const readData = await fsPromises.readFile('test.txt', 'utf8');
```

### 8. Clustering & Multi-threading
Node.js is single-threaded, but you can utilize multi-core systems.
- **Cluster Module**: Allows you to create child processes (workers) that share the same server port.
- **Worker Threads**: Useful for CPU-intensive tasks without blocking the main event loop.

### 9. Process Management (PM2)
In production, you need a way to keep your app alive forever.
- **PM2 Features**: Auto-restart on crash, load balancing (cluster mode), logs management, and monitoring.
```bash
npm install pm2 -g
pm2 start index.js -i max  # Start in cluster mode using all cores
### 10. Graceful Shutdown
In production, you should handle process termination signals to close database connections and finish pending requests before the app exits.
```javascript
process.on('SIGTERM', () => {
  server.close(() => {
    mongoose.connection.close(false, () => {
      console.log('Http server closed.');
      process.exit(0);
    });
  });
});
```

### 10. Graceful Shutdown
Handle process termination signals to close database connections and finish ongoing requests.
```javascript
process.on('SIGTERM', async () => {
  await server.close();
  await db.disconnect();
  process.exit(0);
});
```

### 6. Environment Variables
Stored in `.env` files. Access via `process.env`. Use the `dotenv` package.
```bash
PORT=5000
DB_URI=mongodb://...
```

### 7. Debugging & Logging
- **Winston**: A versatile logging library for Node.js.
- **Morgan**: HTTP request logger middleware for node.js.
- **Debug**: `node --inspect index.js` for Chrome DevTools debugging.

---

## 🎓 Important Interview Questions

### Q1: Is Node.js single-threaded or multi-threaded?
JavaScript execution in Node.js is **single-threaded** (the Event Loop). However, Node.js is **multi-threaded** behind the scenes because the libuv library provides a thread pool for handling heavy I/O operations (like File System or Cryptography).

### Q2: What is the "Event Loop" in Node.js?
It's a loop that picks up tasks from the callback queue and pushes them into the call stack when it's empty. It  @SubscribeMessage('message')
  handleMessage(client: any, payload: any): string {
    return 'Hello world!';
  }

  // Namespaces & Rooms
  @SubscribeMessage('joinRoom')
  handleJoinRoom(client: Socket, room: string) {
    client.join(room);
  }
}
```

### 6. Docker for Backend
Containerization ensures your backend runs the same everywhere.
```dockerfile
# Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD ["npm", "start"]
```

### Q3: Difference between `setImmediate()` and `setTimeout(fn, 0)`?
- `setTimeout(fn, 0)`: Executed in the **Timers** phase after the minimum threshold.
- `setImmediate()`: Executed in the **Check** phase (immediately after the Poll phase).

### Q4: What are "Streams" and why use them?
Streams are objects that let you read data from a source or write data to a destination in a continuous fashion. Use them for large files or network responses to keep memory usage low (avoiding "Buffer overflow").

### Q5: What is the purpose of `package-lock.json`?
It locks the exact version of all dependencies and their sub-dependencies. This ensures that the app runs the same way on every machine, preventing "it works on my machine" bugs caused by minor version updates.


## ❓ Questions & Doubts
- [x]

---

### **1\. Node.js Fundamentals**

---

**Q1. What is Node.js and how does it work?** `[Fresher]`

* Node.js — open-source, cross-platform JavaScript runtime built on Chrome's V8 engine  
* Allows running JavaScript outside the browser — on the server side  
* Built on top of libuv — C library that provides the event loop, async I/O, thread pool  
* Single-threaded — one main thread for JS execution, but async operations run via libuv thread pool  
* Non-blocking I/O — doesn't wait for file/network/database operations to complete  
* Event-driven — actions trigger events, event loop processes them  
* Node.js is NOT a framework — it's a runtime environment  
* Node.js is NOT multi-threaded for JS — but libuv uses thread pool for heavy I/O (file system, crypto, DNS)  
* What Node.js is good for:  
  * REST APIs and backend services  
  * Real-time applications (chat, live updates)  
  * Streaming applications  
  * Microservices  
  * CLI tools  
* What Node.js is NOT good for:  
  * CPU-intensive tasks (image processing, ML, video encoding) — blocks the event loop  
  * Heavy computation — use worker threads or separate services  
* Node.js version — LTS (Long Term Support) vs Current — always use LTS in production  

**Full Answer:**
Node.js is a runtime environment built on Chrome's V8 engine that allows you to run JavaScript on the server.
- **How it works:** It uses an asynchronous, event-driven architecture. While the main JavaScript execution thread is single-threaded, it delegates heavy tasks (like I/O) to the underlying system or its own internal thread pool (libuv).
- **Scalability:** Because it doesn't create a new thread for every request, it is extremely lightweight and perfect for I/O-intensive apps (like Chat apps or REST APIs) but poor for CPU-heavy tasks (like Video Processing).

**Trap Explained: The "Single-Threaded" Myth**
Interviewers will ask: *"If Node.js is single-threaded, how can it handle 10,000 concurrent requests?"*
- **The Answer:** Node.js uses **Non-blocking I/O**. When a request for a file or database comes in, Node doesn't wait (block). It sends the request to the OS or the **Libuv Thread Pool** and moves to the next request. When the data is ready, a callback is pushed to the queue.
- **Crucial Distinction:** The *JavaScript execution* is single-threaded, but the *environment (Node.js)* is multi-threaded.
  ---

**Q2. What is the V8 engine and what role does it play in Node.js?** `[1-2 yrs]`

* V8 — open-source JavaScript engine developed by Google, written in C++  
* Compiles JavaScript directly to native machine code (JIT — Just-In-Time compilation)  
* Responsibilities in Node.js:  
  * Parsing JavaScript code  
  * Compiling to machine code  
  * Memory allocation (heap)  
  * Garbage collection  
* V8 does NOT handle I/O, file system, network — that is libuv's job  
* Hidden classes — V8 optimization for object property access  
* Inline caching — V8 optimization for repeated function calls  
* Garbage collection — Mark and Sweep algorithm, Generational GC (young/old generation)  

**Full Answer:**
V8 is Google’s high-performance open-source JavaScript and WebAssembly engine, written in C++. 
- **Role:** It compiles your JavaScript code directly into **Native Machine Code** (Just-In-Time compilation) instead of interpreting it line-by-line, which makes execution incredibly fast.
- **Memory:** It manages the Heap memory and handles **Garbage Collection**. 
- **Optimization:** It uses techniques like "Hidden Classes" and "Inline Caching" to optimize property access and function calls.
  ---

**Q3. What is the difference between Node.js and browser JavaScript?** `[Fresher]`

* Same — both run JS on V8, share language features, ES6+ support  
* Different:

| Feature | Browser JS | Node.js |
| ----- | ----- | ----- |
| Global object | `window` | `global` / `globalThis` |
| DOM access | Available | Not available |
| `document`, `navigator` | Available | Not available |
| `fs`, `http`, `path` | Not available | Available |
| Module system | ES Modules | CommonJS \+ ESM |
| `process` object | Not available | Available |
| `__dirname` / `__filename` | Not available | Available (CommonJS only) |
| OS access | Sandboxed | Full access |

* `globalThis` — works in both environments (ES2020)  
* Browser JS runs in sandbox — limited OS access by design  
* Node.js has full OS access — file system, network, processes  

**Full Answer:**
While they both use the same JavaScript language, the environments differ significantly:
- **Global Object:** Browser has `window`; Node has `global`.
- **APIs:** Browsers have DOM/BOM APIs; Node has OS-level APIs like `fs` (File System) and `path`.
- **Security:** Browsers run in a **Sandbox** for security (you can't read a user's hard drive); Node has full access to the machine it's running on.

**Follow-up: Why is `globalThis` important?**
Historically, you had to check if you were in a browser (`window`) or Node (`global`). `globalThis` (ES2020) provides a standard way to access the global object in **any** environment, making your shared utility libraries truly "Universal/Isomorphic."
  ---

**Q4. What is the `process` object in Node.js?** `[1-2 yrs]`

* Global object — available without requiring any module  
* Key properties and methods:  
  * `process.env` — access environment variables  
  * `process.argv` — array of command-line arguments (`[node, scriptPath, ...args]`)  
  * `process.cwd()` — current working directory  
  * `process.exit(code)` — exit process (`0` \= success, non-zero \= error)  
  * `process.pid` — process ID  
  * `process.version` — Node.js version string  
  * `process.platform` — OS platform (`'win32'`, `'linux'`, `'darwin'`)  
  * `process.memoryUsage()` — heap used, heap total, RSS  
  * `process.uptime()` — seconds the process has been running  
  * `process.hrtime()` — high-resolution time for benchmarking  
  * `process.nextTick(callback)` — schedule callback before next event loop iteration  
* `process.stdin`, `process.stdout`, `process.stderr` — standard I/O streams  

**Full Answer:**
The `process` object is a global object that provides information about, and control over, the current Node.js process.
- **Usage:** It's used to read environment variables (`process.env`), handle exit codes, and listen for system signals like `SIGTERM` (useful for graceful shutdowns).
- **Efficiency:** You can check memory usage (`process.memoryUsage()`) to debug leaks or get the current working directory (`process.cwd()`).
  ---

  ### **2\. NPM & Yarn**

  ---

**Q5. What is NPM and what is it used for?** `[Fresher]`

* NPM — Node Package Manager, default package manager bundled with Node.js  
* Used for:  
  * Installing third-party packages/libraries  
  * Managing project dependencies  
  * Running scripts (`npm start`, `npm test`, `npm run build`)  
  * Publishing packages to npm registry  
* `npm init` — create `package.json`  
* `npm init -y` — skip questions, use defaults  
* `npm install <package>` — install and add to `dependencies`  
* `npm install <package> --save-dev` — add to `devDependencies`  
* `npm install -g <package>` — global install  
* `npm uninstall <package>` — remove package  
* `npm update` — update packages to latest compatible version  
* `npm list` — list installed packages  
* `npm audit` — check for security vulnerabilities  
* `npm audit fix` — auto-fix vulnerabilities  
* `npm ci` — clean install from `package-lock.json` (used in CI/CD — faster, deterministic)  

**Full Answer:**
NPM is the package manager for Node.js. It allows you to download, manage, and update external libraries (packages) for your project.
- **Key Commands:** `npm init` sets up the project; `npm install` fetches dependencies.
- **Automation:** It allows you to define custom scripts like `npm start` or `npm dev` to automate your workflow.
  ---

**Q6. What is `package.json` and what are its key fields?** `[Fresher]`

* JSON file at root of project — manifest for the project  
* Key fields:  
  * `name` — package name (must be lowercase, no spaces)  
  * `version` — semantic version (`major.minor.patch`)  
  * `main` — entry point file  
  * `scripts` — custom command shortcuts (`start`, `test`, `build`, `dev`)  
  * `dependencies` — packages needed in production  
  * `devDependencies` — packages only needed during development  
  * `peerDependencies` — packages consumer must install (used by libraries)  
  * `engines` — specify required Node.js version  
  * `private: true` — prevent accidental publish to npm registry  
  * `type: "module"` — treat `.js` files as ES Modules  
  * `license` — project license  
* Semantic versioning (SemVer):  
  * `^1.2.3` — compatible with `1.x.x` (minor and patch updates allowed)  
  * `~1.2.3` — only patch updates `1.2.x`  
  * `1.2.3` — exact version only  
  * `*` — any version (dangerous)

**Full Answer:**
The `package.json` file is the heart of any Node.js project. It acts as a manifest that includes:
- **Metadata:** Name, version, and license of your app.
- **Dependencies:** A list of all external libraries your app needs to run.
- **Scripts:** Custom commands (like `start`, `test`) that you can run via `npm run <name>`.
- **Main:** Defines the entry point of your application (usually `index.js`).

  ---

**Q7. What is `package-lock.json` and why is it important?** `[1-2 yrs]`

* Auto-generated file — locks exact versions of ALL dependencies (direct \+ transitive)  
* Ensures reproducible installs across machines and environments  
* Should be committed to version control — guarantees same dependency tree for entire team  
* `npm install` — uses `package-lock.json` if present to install exact versions  
* `npm ci` — strictly uses `package-lock.json`, fails if it doesn't match `package.json`  
* `package-lock.json` vs `package.json` — `package.json` has version ranges, lock file has exact versions  
* Yarn equivalent — `yarn.lock`  
* Common mistake — adding `package-lock.json` to `.gitignore` — never do this  

**Full Answer:**
`package-lock.json` is automatically generated when you install a package. It describes the **exact** dependency tree that was generated, including the exact versions of every sub-dependency.
- **Purpose:** It ensures that every time someone runs `npm install`, they get the exact same `node_modules` structure, preventing "works on my machine" bugs.

**Trap Explained: Why must we commit the lock file?**
If you only commit `package.json` with `^1.2.3`, a teammate might run `npm install` a week later and get version `1.2.9` (which might have a bug). 
The `package-lock.json` ensures that **every developer and the production server** uses the exact same version of every dependency, down to the last patch.
  ---

**Q8. What is the difference between `dependencies` and `devDependencies`?** `[Fresher]`

* `dependencies` — required for application to run in production (Express, React, Mongoose)  
* `devDependencies` — only needed during development and build (nodemon, Jest, ESLint, Webpack, TypeScript)  
* `npm install --production` — installs only `dependencies`, skips `devDependencies`  
* In CI/CD and Docker production builds — set `NODE_ENV=production` to skip devDependencies  
* `peerDependencies` — library declares what version of host package it needs (e.g., React component library requiring React 18\)  
* `optionalDependencies` — install if possible, don't fail if can't install  

**Full Answer:**
- **Dependencies**: These are essential libraries needed for the application to function in production (e.g., Express, Mongoose).
- **DevDependencies**: These are tools only needed during the development or build phase (e.g., Nodemon, Jest, ESLint). They are **not** bundled into the production environment.
  ---

**Q9. What is the difference between NPM and Yarn?** `[1-2 yrs]`

* Both are package managers for Node.js ecosystem  
* NPM — ships with Node.js, `package-lock.json`, workspaces support from v7+  
* Yarn Classic (v1) / Berry (v2+) — must install separately, `yarn.lock`, historically faster parallel downloads, better monorepo support  
* Yarn Berry — Plug'n'Play mode, no `node_modules` folder  
* pnpm — third alternative, uses hard links/symlinks, most disk-space efficient  
* In MERN projects — npm is most common, Yarn used in some enterprise/monorepo setups

| Action | NPM | Yarn |
| ----- | ----- | ----- |
| Install all deps | `npm install` | `yarn` |
| Add package | `npm install pkg` | `yarn add pkg` |
| Add dev dep | `npm i pkg --save-dev` | `yarn add pkg --dev` |
| Remove package | `npm uninstall pkg` | `yarn remove pkg` |
| Run script | `npm run script` | `yarn script` |
| Clean install | `npm ci` | `yarn install --frozen-lockfile` |

**Full Answer:**
Both are package managers that aim to solve the same problem but with different approaches.
- **NPM**: The standard bundled with Node.js. It is fast and robust in modern versions (v7+).
- **Yarn**: Created by Facebook to address NPM's historical speed and security issues. It popularized features like `yarn.lock` and parallel installations.
- **Key Difference:** Yarn has better support for monorepos (Workspaces) and "Zero Installs" in its newer versions.

  ---

  ### **3\. Node.js Modules (CommonJS vs ES Modules)**

  ---

**Q10. What is the CommonJS module system in Node.js?** `[Fresher]`

* Default module system in Node.js  
* `require()` — synchronously loads a module  
* `module.exports` — what the module exposes  
* `exports` — shorthand for `module.exports` (same reference initially)  
* Module caching — once a module is loaded, it's cached — subsequent `require()` calls return cached version  
* `require.cache` — object of all cached modules  
* Circular dependency — two modules requiring each other — Node handles it but partial exports issue  
* `__dirname` — absolute path of the directory of current file  
* `__filename` — absolute path of current file  
* `require('./file')` — relative path, `.js` extension optional  
* `require('express')` — looks in `node_modules`  
* Module resolution order — core modules → node\_modules → file path  

**Full Answer:**
CommonJS is the original module system for Node.js. It uses `require()` to import modules and `module.exports` to export them. 
- **Caching:** One of its most important features is that modules are cached after the first `require()`. Any subsequent `require()` call to the same file returns the exact same object.

**Trap Explained: Module Caching Pitfall**
*"What happens if I require the same file twice?"*
```javascript
// counter.js
let count = 0;
module.exports = ++count;

// main.js
const a = require('./counter');
const b = require('./counter');
console.log(a, b); // Output: 1, 1 (Not 1, 2)
```
**Reason:** Node.js caches the *result* of the first `require`. If you need a fresh value every time, the module should export a **function** instead of a raw value.
  ---

**Q11. What is the difference between `module.exports` and `exports`?** `[1-2 yrs]`

* Initially both point to the same empty object `{}`  
* `exports.fn = fn` — adds property to the shared object — works correctly  
* `module.exports = fn` — replaces the export entirely — works correctly  
* `exports = fn` — BREAKS — reassigns local variable, loses reference to `module.exports`  
* What actually gets exported is always `module.exports` — not `exports`  
* Rule of thumb — use `module.exports` when exporting a single value/class/function  
* Use `exports.x = x` when exporting multiple named things  

**Full Answer:**
`exports` is simply a shorthand reference to `module.exports`. Initially, they both point to the same empty object `{}`. 
- **Named Exports:** Adding properties to `exports` works because you are modifying the shared object.
- **The Source of Truth:** Node.js *only* actually exports the value of `module.exports`.

**Trap Explained: Reassigning `exports`**
Interviewers will ask: *"Why does `exports = { myFunc };` fail?"*
- **The Reason:** Because you are making the `exports` variable point to a **new** object, but the original `module.exports` still points to `{}`. 
- **The Rule:** Never reassign `exports`. If you want to export a single object or function, always use `module.exports = ...`.
  ---

**Q12. What are the differences between CommonJS and ES Modules in Node.js?** `[1-2 yrs]`

| Feature | CommonJS | ES Modules |
| ----- | ----- | ----- |
| Syntax | `require()` / `module.exports` | `import` / `export` |
| Loading | Synchronous | Asynchronous-capable |
| When resolved | Runtime | Parse time (static) |
| `__dirname` | Available | Not available (use `import.meta.url`) |
| Top-level await | Not supported | Supported |
| Tree shaking | Not possible | Possible |
| File extension | `.js` / `.cjs` | `.mjs` or `.js` with `"type":"module"` |
| Dynamic import | Not applicable | `import()` function |

* Enable ES Modules in Node.js:  
  * Add `"type": "module"` to `package.json` — all `.js` files treated as ESM  
  * Use `.mjs` extension — always treated as ESM regardless of `package.json`  
  * Use `.cjs` extension — always treated as CommonJS  
* In ESM — `__dirname` and `__filename` are NOT available, use `fileURLToPath(import.meta.url)` instead  
* `require()` not available in ESM — use dynamic `import()` instead  
* Top-level `await` — works in ESM, not in CommonJS  
* Interop — ESM can import CJS with default import, CJS cannot `require()` ESM synchronously  

**Full Answer:**
CommonJS (CJS) is the legacy system (`require`), while ES Modules (ESM) is the modern standard (`import`).
- **Enabling ESM:** Add `"type": "module"` in `package.json`.
- **Differences:** CJS is synchronous; ESM is asynchronous and allows "Top-level await."

**Trap Explained: No `__dirname` in ESM**
If you switch to ESM, `__dirname` and `__filename` are **not defined**.
- **The Fix:** You must derive them using `import.meta.url`:
```javascript
import { fileURLToPath } from 'url';
import { dirname } from 'path';
const __dirname = dirname(fileURLToPath(import.meta.url));
```
  ---

**Q13. What are Node.js core built-in modules?** `[Fresher]`

* No install needed — bundled with Node.js  
* Key modules:  
  * `fs` — file system operations  
  * `path` — file path utilities  
  * `http` / `https` — create HTTP servers and clients  
  * `os` — operating system info  
  * `events` — EventEmitter  
  * `stream` — streaming data  
  * `crypto` — cryptographic functions (hashing, encryption)  
  * `url` — URL parsing and formatting  
  * `querystring` — parse/stringify query strings  
  * `child_process` — spawn subprocesses (`exec`, `spawn`, `fork`)  
  * `cluster` — multiple Node.js processes sharing same port  
  * `worker_threads` — true parallelism for CPU-intensive tasks  
  * `util` — utility functions (`promisify`, `inspect`, `format`)  
  * `buffer` — handle binary data  
  * `net` — TCP/IPC networking  
  * `dns` — DNS lookups  
  * `readline` — line-by-line reading of streams  
  * `zlib` — compression (gzip, deflate)  
* Import with `require('fs')` or `import fs from 'node:fs'` (node: prefix preferred in ESM)  

**Full Answer:**
Node.js comes with built-in modules that provide essential OS-level functionality.
- **Core Modules:** `fs` (File System), `path`, `os`, `http`, `events`, `crypto`.
- **Usage:** In ESM, it is now recommended to use the `node:` prefix (e.g., `import fs from 'node:fs'`) to distinguish core modules from `node_modules` packages.
  ---

  ### **4\. Asynchronous JavaScript in Node.js**

  ---

**Q14. How does asynchronous programming work in Node.js?** `[Fresher]`

* Node.js uses non-blocking I/O — instead of waiting for operation, registers a callback and moves on  
* Three patterns for async code:  
  * Callbacks — original Node.js pattern, error-first convention `(err, data) => {}`  
  * Promises — cleaner chaining, no callback hell  
  * Async/Await — modern, cleanest approach  
* `util.promisify(fn)` — converts callback-based function to Promise-based  
* `fs.promises` — built-in promise versions of fs methods (no need to promisify manually)  
* Error-first callback convention — `(err, data) => {}` — always check `err` first  
* Why Node.js can handle thousands of concurrent requests — single thread plus non-blocking I/O means it doesn't create a thread per request like traditional servers  

**Full Answer:**
Node.js relies on the libuv library to handle asynchronous tasks. 
- **The Strategy:** Instead of blocking the thread for I/O, Node registers a callback and continues. When the I/O is done, the callback is queued for execution.
- **Error-First Callback:** This is the standard Node.js convention where the first argument is reserved for an error object (e.g., `(err, data) => {}`). Always check `err` before processing `data`.
  ---

**Q15. What is `util.promisify` and when would you use it?** `[1-2 yrs]`

* Converts Node.js error-first callback functions to Promises  
* Works with functions following `(err, value) => {}` callback pattern  
* `util.callbackify()` — opposite direction, converts async function to callback style  
* Custom promisify — for functions that don't follow convention, use `util.promisify.custom` symbol  
* When to use — working with older Node.js APIs or third-party libs that use callbacks  
* Most modern Node.js APIs now have native Promise versions (`fs.promises`, `dns.promises`)  
  ---

  ### **5\. Event Loop & Streams**

  ---

**Q16. How does the Node.js Event Loop work?** `[1-2 yrs]`

* Same fundamental concept as browser event loop — but Node.js has more defined phases  
* Node.js Event Loop Phases in order:  
  * Timers — executes `setTimeout` and `setInterval` callbacks whose threshold has passed  
  * Pending callbacks — I/O callbacks deferred to next iteration  
  * Idle, Prepare — internal use only  
  * Poll — retrieve new I/O events, execute I/O callbacks (most time spent here)  
  * Check — `setImmediate()` callbacks execute here  
  * Close callbacks — `socket.on('close', ...)` type callbacks  
* Between each phase — microtask queue is drained:  
  * `process.nextTick()` callbacks — highest priority, run before Promise microtasks  
  * Promise microtasks — `then`, `catch`, `finally`, `await` continuations  
* `process.nextTick(fn)` — runs before next event loop iteration, before any I/O  
* `setImmediate(fn)` — runs in Check phase, after I/O callbacks  
* `setTimeout(fn, 0)` vs `setImmediate(fn)`:  
  * Outside I/O — order is non-deterministic  
  * Inside I/O callback — `setImmediate` always fires first  
* libuv thread pool — handles DNS, crypto, fs (default 4 threads), configurable via `UV_THREADPOOL_SIZE`  

**Full Answer:**
The Event Loop consists of phases like Timers, Poll (I/O), and Check (setImmediate).
- **Poll Phase:** This is where Node spends most of its time, waiting for new I/O events.
- **Check Phase:** Specifically for `setImmediate` callbacks.

**Trap Explained: The `process.nextTick` Priority**
*"Where does `nextTick` fit in the loop?"*
- **The Answer:** It **doesn't**. `process.nextTick` is not part of the loop phases. It runs **immediately** after the current operation, before the loop moves to the *next* phase. 
- **Warning:** If you use `nextTick` recursively, you can starve the event loop, stopping it from ever reaching I/O or Timers!
  ---

**Q17. What are Streams in Node.js?** `[1-2 yrs]`

* Streams — abstract interface for working with data in chunks instead of all at once  
* Why streams — memory efficient (no need to load entire file), time efficient (process as data arrives)  
* Four types of streams:  
  * Readable — data can be read from (`fs.createReadStream`, `http.IncomingMessage`)  
  * Writable — data can be written to (`fs.createWriteStream`, `http.ServerResponse`)  
  * Duplex — both readable and writable (`net.Socket`, TCP connection)  
  * Transform — duplex stream that transforms data (`zlib.createGzip`, `crypto.createCipher`)  
* Streams extend EventEmitter — emit events:  
  * Readable events — `data`, `end`, `error`, `close`  
  * Writable events — `drain`, `finish`, `error`, `close`  
* Piping — `readable.pipe(writable)` — connect streams, handles backpressure automatically  
* Backpressure — when writable stream can't keep up with readable, pipe handles slowing down producer  
* `pipeline(src, transform, dest, callback)` — from `stream` module, better than pipe (handles errors properly)  
* Stream modes — flowing (data pushed automatically) vs paused (must call `.read()`)  
* `highWaterMark` — buffer size threshold, default 16KB for bytes, 16 objects for object mode  
* Practical use cases — reading large CSV file, video streaming, file compression on the fly  

**Full Answer:**
Streams allow you to process data in chunks. This is vital for memory efficiency in MERN apps (e.g., uploading a large image to S3).
- **Types:** Readable, Writable, Duplex, and Transform.

**Trap Explained: Backpressure**
*"What is backpressure?"*
- **The Problem:** When a Readable stream sends data faster than the Writable stream (e.g., slow database) can handle it.
- **The Fix:** Use `.pipe()` or the modern `pipeline()` utility. They automatically pause the reader when the writer is overwhelmed.
  ---

**Q18. What is the EventEmitter in Node.js?** `[1-2 yrs]`

* Core class from `events` module — backbone of Node.js event-driven architecture  
* Many built-in Node.js objects extend EventEmitter (streams, HTTP server, etc.)  
* Key methods:  
  * `emitter.on(event, listener)` — register persistent listener  
  * `emitter.once(event, listener)` — listener fires once then auto-removed  
  * `emitter.emit(event, ...args)` — trigger event, pass arguments to listeners  
  * `emitter.off(event, listener)` — remove specific listener  
  * `emitter.removeAllListeners(event)` — remove all listeners for event  
  * `emitter.listeners(event)` — get array of listeners for event  
  * `emitter.listenerCount(event)` — number of listeners  
  * `emitter.setMaxListeners(n)` — default max is 10, increase to avoid memory leak warning  
* `error` event — special event, if emitted with no listener, throws uncaught error  
* Memory leak warning — adding too many listeners without removing them is a common bug  
  ---

  ### **6\. File System (fs module)**

  ---

**Q19. How do you work with the file system in Node.js?** `[Fresher]`

* `fs` module — built-in, no install needed  
* Every method has three versions:  
  * Synchronous — `fs.readFileSync()` — blocks event loop, avoid in production servers  
  * Callback async — `fs.readFile(path, callback)` — non-blocking, older style  
  * Promise async — `fs.promises.readFile(path)` — non-blocking, modern preferred  
* Common operations:  
  * Read file — `fs.promises.readFile(path, 'utf8')`  
  * Write file — `fs.promises.writeFile(path, data)` — creates or overwrites  
  * Append file — `fs.promises.appendFile(path, data)`  
  * Delete file — `fs.promises.unlink(path)`  
  * Rename/Move — `fs.promises.rename(oldPath, newPath)`  
  * Check if exists — `fs.promises.access(path, fs.constants.F_OK)`  
  * Get file info — `fs.promises.stat(path)` — returns Stats object (size, dates, isFile, isDirectory)  
  * Create directory — `fs.promises.mkdir(path, { recursive: true })`  
  * Read directory — `fs.promises.readdir(path)` — returns array of filenames  
  * Remove directory — `fs.promises.rm(path, { recursive: true })` (Node 14.14+)  
* `fs.watch(path, callback)` — watch file/directory for changes  
* Encoding — always specify `'utf8'` for text files, omit for raw Buffer  
  ---

**Q20. What is the `path` module and why is it important?** `[Fresher]`

* Built-in module for working with file and directory paths  
* Critical because path separators differ by OS — `/` on Unix, `\` on Windows  
* Key methods:  
  * `path.join(...segments)` — joins path segments using OS separator  
  * `path.resolve(...segments)` — resolves absolute path from given segments  
  * `path.dirname(filePath)` — directory part of path  
  * `path.basename(filePath)` — filename with extension  
  * `path.basename(filePath, ext)` — filename without extension  
  * `path.extname(filePath)` — extension (`.js`, `.json`)  
  * `path.parse(filePath)` — returns object with `root`, `dir`, `base`, `name`, `ext`  
  * `path.sep` — OS path separator (`/` or `\`)  
* `path.join` vs `path.resolve`:  
  * `join` — simple concatenation with OS separator  
  * `resolve` — builds absolute path, processes `..` and `.`, uses `cwd()` as base  
* Common pattern — `path.join(__dirname, 'public', 'index.html')`  

**Full Answer:**
The `path` module ensures your code works on both Windows (`\`) and Linux (`/`).
- **`path.join`:** Concatenates segments using the correct OS separator.
- **`path.resolve`:** Always returns an **absolute** path by resolving segments against the current working directory.

**Trap Explained: `join` vs `resolve`**
```javascript
path.join('/a', '/b'); // Output: "/a/b"
path.resolve('/a', '/b'); // Output: "/b" (It treats /b as the root and restarts!)
```
Always use `path.join` for relative building and `path.resolve` when you need a guaranteed full path from root.
  ---

**Q21. What is the difference between reading a file synchronously vs asynchronously?** `[Fresher]`

* Sync — `fs.readFileSync(path, 'utf8')` — blocks entire event loop until done  
  * Acceptable during app startup (config loading, before server starts)  
  * Never use inside request handlers — blocks all other requests  
* Async callback — `fs.readFile(path, 'utf8', (err, data) => {})` — non-blocking  
* Async Promise — `await fs.promises.readFile(path, 'utf8')` — non-blocking, cleanest  
* Stream — `fs.createReadStream(path)` — best for large files, most memory efficient  
* Rule of thumb — sync only at startup, Promises or streams everywhere else  

**Full Answer:**
- **Synchronous (`readFileSync`):** Blocks the entire Event Loop until the file is read. No other requests can be processed.
- **Asynchronous (`readFile`):** Offloads the task to the Libuv thread pool and continues. When done, it triggers a callback or resolves a promise.

**Trap Explained: The Production Freeze**
Interviewers will ask: *"What happens if you use `readFileSync` in a route with 1,000 concurrent users?"*
- **The Answer:** One single user reading a large file will stop the server for **everyone else**. Node.js is "single-threaded" for JS, so blocking that thread is a fatal performance error in production.
  ---

  ### **7\. Environment Variables & Configuration**

  ---

**Q22. What are environment variables and why are they used in Node.js?** `[Fresher]`

* Key-value pairs stored in the OS environment, accessible to processes  
* Why use them:  
  * Keep secrets out of source code (DB passwords, API keys, JWT secrets)  
  * Different config for different environments (dev, staging, production)  
  * 12-Factor App methodology — config in environment, not in code  
* Access in Node.js — `process.env.VARIABLE_NAME`  
* Returns `undefined` if variable not set  
* All values are strings — parse numbers with `parseInt(process.env.PORT)`  
* Set in terminal — `PORT=3000 node app.js` (Unix) or `set PORT=3000 && node app.js` (Windows)  
* Never commit `.env` files — always add to `.gitignore`  

**Full Answer:**
Environment variables allow you to externalize configuration so you don't hardcode sensitive information.
- **Security:** Prevents API keys and DB credentials from being pushed to Git.
- **Flexibility:** Allows the same code to run in development and production environments by just changing environment variables.

**Trap Explained: The "Type" Trap**
*"What is the type of `process.env.PORT`?"*
- **The Answer:** It is always a **string**. If your code tries to do math on it without converting (e.g., `process.env.PORT + 1`), it will perform string concatenation. Always use `parseInt()` or `Number()`.
  ---

**Q23. What is `dotenv` and how do you use it?** `[Fresher]`

* Third-party package — loads environment variables from `.env` file into `process.env`  
* `npm install dotenv`  
* Usage — `require('dotenv').config()` at very top of entry file before anything else  
* `.env` file format:  
  * `PORT=3000`  
  * `DB_URI=mongodb://localhost:27017/mydb`  
  * `JWT_SECRET=mysecretkey`  
  * `NODE_ENV=development`  
* `dotenv` only loads variables not already set — won't override system environment variables  
* Multiple environments — `.env.development`, `.env.production`, `.env.test`  
* `dotenv-expand` — allows variable interpolation inside `.env`  
* Production best practice — use actual environment variables from hosting platform, not `.env` files  
* `.env.example` — commit this with dummy values to document required variables without exposing secrets  
* Node 20+ built-in — `node --env-file=.env app.js` — no dotenv package needed  

**Full Answer:**
`dotenv` reads from a `.env` file and adds those variables to `process.env`.
- **Initialization:** Must be called as early as possible in your entry file.

**Trap Explained: Overriding Variables**
*"If I have a system variable `PORT` and a `.env` file with `PORT`, which one wins?"*
- **The Answer:** By default, `dotenv` does **not** override existing environment variables. If the host environment has already set `PORT`, the `.env` value is ignored.
  ---

**Q24. What is `NODE_ENV` and why is it important?** `[1-2 yrs]`

* Convention for specifying the runtime environment  
* Common values — `development`, `production`, `test`  
* Not automatically set by Node.js — must be set explicitly  
* How it affects application behavior:  
  * Express — disables detailed error messages in production  
  * React/Webpack — enables optimizations and minification in production build  
  * Many libraries change internal behavior based on `NODE_ENV`  
* Check in code — `if (process.env.NODE_ENV === 'production') {}`  
* `cross-env` npm package — set `NODE_ENV` consistently across Windows and Unix  
* Never run production with `NODE_ENV=development` — disables caching, enables verbose logging, exposes stack traces to clients  

**Full Answer:**
`NODE_ENV` is the standard variable used to toggle between production and development logic.
- **Production Mode:** Disables heavy debugging, enables caching, and compresses output.

**Trap Explained: The Performance Hit**
*"Why is running a MERN app with `NODE_ENV=development` dangerous?"*
- **The Answer:** Because libraries like Express and React will include extra warnings, logging, and full error stack traces in every response, which is a massive performance bottleneck and a significant **security risk** for production apps.
  ---

**Q25. How do you manage configuration for different environments in a MERN app?** `[2-3 yrs]`

* Simple approach — single `.env` file, different values per environment  
* Better approach — centralized config module:  
  * `config/index.js` exports object with all config values with fallbacks  
  * `port: process.env.PORT || 3000`  
* Validation at startup — use `joi` or `zod` to validate all required env vars, fail fast if missing  
* `convict` — configuration management library with schema validation and environment awareness  
* Secrets management in production:  
  * AWS Secrets Manager  
  * HashiCorp Vault  
  * Heroku Config Vars / Railway / Render environment settings  
  * Docker secrets  
* Never log `process.env` — may expose secrets in log output  

**Full Answer:**
Centralize your config in one place rather than spreading `process.env` calls throughout your codebase.
- **Fail Fast:** If a required variable like `DB_URI` is missing, the app should throw an error during bootup, not during the first request.

**Trap Explained: Secrets in Logs**
*"Why is `console.log(process.env)` bad practice?"*
- **The Answer:** It dumps all your secret keys and database passwords directly into your log files (which are often pushed to 3rd-party services like Datadog). Only log individual safe variables if absolutely necessary.
  ---

  ### **8\. Debugging & Logging**

  ---

**Q26. How do you debug a Node.js application?** `[1-2 yrs]`

* `console.log()` — basic, works but messy in production  
* Node.js built-in debugger:  
  * `node inspect app.js` — CLI debugger  
  * `node --inspect app.js` — starts inspector, connect with Chrome DevTools via `chrome://inspect`  
  * `node --inspect-brk app.js` — pauses on first line, useful for startup bugs  
* VS Code debugger:  
  * Launch config in `.vscode/launch.json`  
  * Set breakpoints directly in editor  
  * Can attach to running process or launch fresh  
  * Most common debugging approach in day-to-day development  
* `debugger` statement — pauses execution when debugger is attached  
* `util.inspect(obj, { depth: null })` — deep inspect nested objects better than `console.log`  
* `console.trace()` — print stack trace at a specific point  
* `console.time('label')` / `console.timeEnd('label')` — measure execution time of a block  

**Full Answer:**
You can debug via `console.log`, the built-in `--inspect` flag (for Chrome DevTools), or the VS Code integrated debugger.
- **The Professional Way:** Use VS Code's `launch.json` so you can set breakpoints without editing code.

**Trap Explained: `console.log` vs `util.inspect`**
*"How do you print a deeply nested object that only shows `[Object]` in the console?"*
- **The Answer:** Use `console.log(util.inspect(myObj, { depth: null, colors: true }))`. `console.log` has a default depth limit that truncates nested data, but `util.inspect` lets you see everything.
  ---

**Q27. What is logging in Node.js and why is `console.log` not enough for production?** `[1-2 yrs]`

* `console.log` problems in production:  
  * No log levels (debug, info, warn, error)  
  * No timestamps  
  * No structured format — hard to parse or search  
  * Synchronous in some contexts — can block event loop  
  * Cannot be easily turned off or filtered by level  
  * No file output or external transport support  
* Production logging requirements:  
  * Log levels — ERROR, WARN, INFO, HTTP, DEBUG  
  * Timestamps on every log entry  
  * Structured JSON format — easy to parse by log management tools  
  * Multiple transport options — console, file, external services  
  * Async logging — no blocking the event loop

**Full Answer:**
`console.log` is synchronous in Node.js (writing to stdout/stderr can block), lacks levels, and output is unstructured text.
- **Requirements:** Structured JSON logs, log levels (INFO/WARN/ERROR), and timestamps.

**Trap Explained: Log Bloat**
*"How do you manage 10GB of logs on a server?"*
- **The Answer:** Use a logging library like **Winston** to stream logs to an external aggregator (like Datadog or ELK stack). Never keep log files permanently on the server's disk; use log rotation tools.
  ---

**Q28. What is Winston and how do you use it?** `[1-2 yrs]`

* Most popular Node.js logging library  
* `npm install winston`  
* Key concepts:  
  * Levels — `error`, `warn`, `info`, `http`, `verbose`, `debug`, `silly` (highest to lowest priority)  
  * Transports — where logs go (Console, File, HTTP, custom)  
  * Formats — how logs look (`json`, `simple`, `colorize`, `timestamp`, `combine`)  
* Basic setup:  
  * Create logger with `winston.createLogger()`  
  * Set `level` — only logs at this level and above are output  
  * Combine formats with `winston.format.combine(timestamp(), json())`  
  * Add multiple transports — console for dev, file for production  
* Use `logger.info()`, `logger.error()`, `logger.warn()` instead of `console.log`  
* In production — set level to `warn` or `error` to reduce noise  
* `morgan` — HTTP request logging middleware for Express, commonly combined with Winston  

**Full Answer:**
Winston is a logger that allows you to define multiple "Transports" (e.g., log errors to a file and general info to the console).
- **Structure:** Always use JSON format for production logs so they can be easily parsed by searching tools.

**Trap Explained: Log Levels**
*"What is the difference between `silly` and `error`?"*
- **The Answer:** Levels are prioritized. If you set the logger to `warn`, it will ignore `info`, `debug`, and `silly` logs. This allows you to log everything during development and filter for only important stuff in production.
  ---

**Q29. What is Morgan and how is it used with Express?** `[1-2 yrs]`

* HTTP request logger middleware for Express  
* `npm install morgan`  
* Logs every incoming request — method, URL, status code, response time  
* Predefined formats:  
  * `'dev'` — colorized, concise output for development  
  * `'combined'` — Apache combined log format for production  
  * `'tiny'` — minimal output  
  * `'common'` — standard Apache common log format  
* Usage — `app.use(morgan('dev'))` — place before route handlers  
* Stream to Winston — pass `{ stream: logger.stream }` as second argument  
* Skip function — log only errors: `skip: (req, res) => res.statusCode < 400`  
* Custom tokens — `morgan.token('user', (req) => req.user?.id)` — add custom fields  

**Full Answer:**
Morgan is a middleware that logs details about incoming HTTP requests.
- **Usage:** It sits in your Express pipeline and records the Method, URL, Response Status, and Response Time.

**Trap Explained: Logging Every Single Request**
*"Should you use Morgan in production?"*
- **The Answer:** Yes, but only with appropriate log formats (like `combined`). Using `dev` format in production can be too verbose. Also, pipe Morgan's output into your central logging system (like Winston/Datadog) rather than letting it print to the console.
  ---

**Q30. What are best practices for error handling and logging in production Node.js apps?** `[2-3 yrs]`

* Operational errors vs Programmer errors:  
  * Operational — expected failures (DB down, file not found, invalid input) — handle gracefully  
  * Programmer — bugs, type errors, logic errors — let crash and restart via PM2  
* Centralized error handling:  
  * Express error middleware `(err, req, res, next)` — single place to handle all errors  
  * `process.on('uncaughtException', handler)` — last resort, app state may be corrupted, always exit after  
  * `process.on('unhandledRejection', handler)` — catch unhandled Promise rejections  
* Never expose stack traces to clients — log internally, send generic message to client  
* Log enough context — user ID, request ID, route, input that caused the error  
* Request ID — generate unique ID per request with `uuid` or `nanoid`, attach to all logs for tracing  
* Log aggregation tools — Datadog, Logtail, Papertrail, ELK Stack, Grafana Loki  
* PM2 — process manager, auto-restarts on crash, cluster mode, built-in log management  
* Health check endpoint — `/health` route to verify app is running, used by load balancers and Docker  

**Full Answer:**
Centralized error handling is achieved using Express middleware: `(err, req, res, next)`.
- **Strategy:** Distinguish between *Operational* (predictable errors) and *Programmer* (unexpected bugs) errors.

**Trap Explained: The "Zombie" Process**
*"What do you do if an `uncaughtException` occurs?"*
- **The Answer:** **Exit the process.** Once an unhandled exception hits the global process, the application state is corrupted. You should perform a graceful shutdown (close DB connections) and terminate. Do not try to "resume," or you'll have a zombie process in a broken state.
  ---

  ### **Bonus Questions**

  ---

**Q31. What is `nodemon` and why is it used?** `[Fresher]`

* Development tool — automatically restarts Node.js server when file changes are detected  
* `npm install -D nodemon`  
* Usage — `nodemon app.js` instead of `node app.js`  
* `nodemon.json` — config file for ignored paths, watched extensions, restart delay  
* In `package.json` scripts — `"dev": "nodemon app.js"`  
* Node.js v18+ built-in alternative — `node --watch app.js` — no package needed  

**Full Answer:**
`nodemon` is a development-only tool that monitors your file changes and automatically restarts the process.
- **Efficiency:** It saves time by removing the need to manually kill and restart `node app.js` every time you fix a bug.
- **Modern Node:** Since Node v18.11.0, you can use the built-in `--watch` flag, which reduces your dependency count.
  ---

**Q32. What are Worker Threads in Node.js?** `[2-3 yrs]`

* `worker_threads` module — run JavaScript in parallel threads  
* Use for CPU-intensive tasks — image processing, heavy computation, encryption  
* Workers have their own V8 instance and event loop  
* Share memory via `SharedArrayBuffer` — high-performance data sharing between threads  
* Communication via `parentPort.postMessage()` and `workerData`  
* Worker threads vs `child_process.fork()`:  
  * Worker threads — share memory, lower overhead, same process  
  * Child processes — separate memory space, separate process, higher isolation  
* `cluster` module — multiple Node.js processes sharing same port for scaling HTTP servers  

**Full Answer:**
Worker threads allow for true parallelism in JavaScript.
- **Performance:** Unlike `child_process.fork()`, worker threads share memory via `SharedArrayBuffer`, making them significantly faster for data-heavy tasks.

**Trap Explained: Parallelism vs Concurrency**
*"When should I NOT use worker threads?"*
- **The Answer:** Don't use them for I/O tasks (like waiting for a database). Node's standard event loop is already perfect for that. Only use workers when your CPU is at 100% due to heavy math, image processing, or encryption.
  ---

**Q33. What is the `child_process` module in Node.js?** `[2-3 yrs]`

* Spawn separate OS processes from Node.js  
* Four methods:  
  * `exec(command, callback)` — run shell command, buffer entire output, 200KB default limit  
  * `execFile(file, args, callback)` — directly run a file, safer than exec (no shell)  
  * `spawn(command, args)` — stream output, better for large data or long-running processes  
  * `fork(modulePath)` — special spawn for Node.js scripts, built-in IPC channel between parent and child  
* Use cases — running shell scripts, calling Python/Go services, executing OS commands  
* Security — never pass user input directly to `exec` — shell injection risk  

**Full Answer:**
The `child_process` module is the bridge to the OS.
- **`spawn`**: Streams data (no memory limit).
- **`exec`**: Buffers data (has a default 1MB limit).

**Trap Explained: The `exec` Buffer Crash**
*"Why did my production log-parsing script crash?"*
- **The Reason:** You likely used `exec`, which tries to fit the entire output into a string in memory. If your logs are huge, it crashes with `ERR_CHILD_PROCESS_STDIO_MAXBUFFER`. Always use `spawn` for large output.
  ---

**Q34. What is clustering in Node.js and why is it needed?** `[2-3 yrs]`

* Node.js is single-threaded — by default uses only one CPU core  
* `cluster` module — create multiple worker processes that share the same port  
* Master process — manages workers, distributes incoming connections via round-robin  
* Worker processes — each handles actual requests independently  
* `os.cpus().length` — number of CPU cores, typically create one worker per core  
* Workers crash independently — master detects crash and restarts the worker  
* PM2 cluster mode — handles clustering automatically with `pm2 start app.js -i max`  
* Modern alternative — run multiple Docker containers behind a load balancer (preferred in cloud deployments)  

**Full Answer:**
Clustering is "Vertical Scaling." It allows you to utilize every CPU core on a single server.
- **The Pattern:** The primary process spawns workers. If a worker dies, the primary process hears the `exit` event and spawns a new one immediately.

**Follow-up: PM2 vs. Cluster Module**
Senior developers rarely write custom clustering code. Instead, we use **PM2**'s `cluster_mode`. PM2 handles the lifecycle of your workers more reliably than custom `cluster` scripts.
  ---

  ---

  ### **Advanced Industry Standard Topics**

  ---

**Q35. How does Garbage Collection (GC) work in Node.js and how do you find memory leaks?** `[Senior]`
* Node.js (V8) uses Generational Garbage Collection: Young Generation (cleaned often) and Old Generation (cleaned less).
* **Memory Leaks:** Common sources are global variables, forgotten intervals, and large closures.
* **How to detect:** Use `--inspect` and Chrome DevTools to take a **Heap Snapshot**. If "Detached DOM nodes" or certain objects keep growing without being cleared, you have a leak.

**Full Answer:**
Garbage collection is automatic, but a senior developer must understand its limits. V8 manages memory in several spaces. The "New Space" is fast but small. If an object stays alive, it moves to "Old Space."
- **The Trap:** Using an object as a cache without an expiration (LRU) policy. The cache will grow indefinitely, forcing the GC to run more often and for longer, eventually crashing the server with "JavaScript heap out of memory."

  ---

**Q36. What is a "Graceful Shutdown" and why is it mandatory for production?** `[Senior]`
* It ensures that the server finishes processing current requests before terminating the process.
* It prevents data corruption by closing Database connections properly.
* It involves listening for OS signals: `SIGTERM` and `SIGINT`.

**Full Answer:**
In a CI/CD environment, servers are restarted often. Without a graceful shutdown, users mid-request will see random "Connection Reset" errors.
- **The Pattern:** 
  1. Stop accepting new connections (`server.close()`).
  2. Wait for current requests to finish.
  3. Close database handles (MongoDB/Redis).
  4. Exit with `process.exit(0)`.

  ---

**Q37. Buffer vs. String: When should you use Buffers for high-performance I/O?** `[Senior]`
* Strings in JS are UTF-16; Buffers are raw binary data allocated outside the V8 heap.
* **The Performance Gap:** Converting a large Buffer to a String is an expensive `O(n)` CPU operation.
* **The Senior Rule:** If you are "passing data through" (e.g., reading a file and sending it to a client), **never** convert it to a string. Keep it as a Buffer to avoid GC overhead and keep the event loop fast.

**Full Answer:**
Strings have overhead because of character encoding. Buffers are just bytes. When building a streaming video app or a high-speed file uploader, always work with Buffers and Streams to keep your memory footprint low and your CPU free.

  ---

  ---

**Q38. How do you handle Secure JWT Implementation and Token Rotation in Node.js?** `[Senior]`
* **The Problem:** Storing long-lived JWTs in `localStorage` is vulnerable to XSS.
* **The Solution:** Use `httpOnly` and `Secure` cookies for Refresh Tokens.
* **Token Rotation:** Every time a Refresh Token is used, issue a **new** one and invalidate the old one.

**Full Answer:**
In a production MERN app, security is paramount.
1. **Short-lived Access Tokens:** Set to 15 minutes.
2. **Long-lived Refresh Tokens:** Stored in a database and sent via `httpOnly` cookies.
3. **Blacklisting:** If a user logs out or a leak is detected, the Refresh Token is deleted from the DB, preventing further access.
- **Senior Tip:** Implement "Refresh Token Rotation." If a stolen token is reused, the system detects the anomaly (reusing an old token) and invalidates the entire session for that user.

  ---

That's the complete **Node.js** section — **38 questions**, all clean with fixed tables.


[⬅️ Previous: Features](../../MERN_Study_Structure/02_Frontend_Development_React_N/06_Features/06_Features.md) | [🏠 Home](../../README.md) | [Next: Expressjs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/02_Expressjs/02_Expressjs.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>