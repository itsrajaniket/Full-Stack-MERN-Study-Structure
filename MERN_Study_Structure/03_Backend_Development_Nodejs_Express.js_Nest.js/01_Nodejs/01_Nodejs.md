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
  ---

**Q8. What is the difference between `dependencies` and `devDependencies`?** `[Fresher]`

* `dependencies` — required for application to run in production (Express, React, Mongoose)  
* `devDependencies` — only needed during development and build (nodemon, Jest, ESLint, Webpack, TypeScript)  
* `npm install --production` — installs only `dependencies`, skips `devDependencies`  
* In CI/CD and Docker production builds — set `NODE_ENV=production` to skip devDependencies  
* `peerDependencies` — library declares what version of host package it needs (e.g., React component library requiring React 18\)  
* `optionalDependencies` — install if possible, don't fail if can't install  
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
  ---

**Q11. What is the difference between `module.exports` and `exports`?** `[1-2 yrs]`

* Initially both point to the same empty object `{}`  
* `exports.fn = fn` — adds property to the shared object — works correctly  
* `module.exports = fn` — replaces the export entirely — works correctly  
* `exports = fn` — BREAKS — reassigns local variable, loses reference to `module.exports`  
* What actually gets exported is always `module.exports` — not `exports`  
* Rule of thumb — use `module.exports` when exporting a single value/class/function  
* Use `exports.x = x` when exporting multiple named things  
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
  ---

**Q21. What is the difference between reading a file synchronously vs asynchronously?** `[Fresher]`

* Sync — `fs.readFileSync(path, 'utf8')` — blocks entire event loop until done  
  * Acceptable during app startup (config loading, before server starts)  
  * Never use inside request handlers — blocks all other requests  
* Async callback — `fs.readFile(path, 'utf8', (err, data) => {})` — non-blocking  
* Async Promise — `await fs.promises.readFile(path, 'utf8')` — non-blocking, cleanest  
* Stream — `fs.createReadStream(path)` — best for large files, most memory efficient  
* Rule of thumb — sync only at startup, Promises or streams everywhere else  
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
* `cluster` module — multiple processes sharing same port for scaling HTTP servers  
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
  ---

That's the complete **Node.js** section — **34 questions**, all clean with fixed tables.


[⬅️ Previous: Features](../../MERN_Study_Structure/02_Frontend_Development_React_N/06_Features/06_Features.md) | [🏠 Home](../../README.md) | [Next: Expressjs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/02_Expressjs/02_Expressjs.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>