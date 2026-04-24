# Node.js

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

[⬅️ Previous: Features](../../MERN_Study_Structure/02_Frontend_Development_React_N/06_Features/06_Features.md) | [🏠 Home](../../README.md) | [Next: Expressjs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/02_Expressjs/02_Expressjs.md)
