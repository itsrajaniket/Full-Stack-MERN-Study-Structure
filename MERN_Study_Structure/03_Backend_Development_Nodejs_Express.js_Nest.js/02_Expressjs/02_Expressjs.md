# Express.js
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Setting Up an Express Server
- [x] Middleware (Built-in, Third-party, Custom)
- [x] Routing & Route Parameters
- [x] Request and Response Objects
- [x] Error Handling in Express
- [x] RESTful APIs & CRUD Operations
- [x] Creating RESTful API Endpoints
- [x] Handling Query Parameters & Request Body (Express.json, URL Encoded)
- [x] HTTP Status Codes & Response Handling

## 📝 Detailed Notes

### 1. Setting Up an Express Server
Express is a minimal and flexible Node.js web application framework.
```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

### 2. Middleware
Middleware functions have access to the `req`, `res`, and `next` functions.
- **Built-in**: `express.json()`, `express.static()`.
- **Custom**: 
```javascript
app.use((req, res, next) => {
    console.log(`${req.method} request to ${req.url}`);
    next(); // Pass to next middleware
});
```
- **Third-party**: `cors`, `helmet`, `morgan`.

### 3. Routing & Parameters
- **Route Params**: `app.get('/users/:id', (req, res) => { const id = req.params.id; })`
- **Query Params**: `app.get('/search', (req, res) => { const query = req.query.q; })`

### 4. Request and Response
- **req**: `req.body`, `req.params`, `req.query`, `req.headers`.
- **res**: `res.send()`, `res.json()`, `res.status(404).json({ error: 'Not Found' })`, `res.redirect()`.

### 5. Error Handling (The Professional Way)
Don't just use `res.status(500)`. Create a centralized error handler.
```javascript
// utils/ErrorHandler.js
class ErrorHandler extends Error {
  constructor(message, statusCode) {
    super(message);
    this.statusCode = statusCode;
    Error.captureStackTrace(this, this.constructor);
  }
}

// middleware/error.js
module.exports = (err, req, res, next) => {
  err.statusCode = err.statusCode || 500;
  err.message = err.message || "Internal Server Error";
  res.status(err.statusCode).json({ success: false, message: err.message });
};
```

### 6. Express Router (Modular Architecture)
For large apps, don't put everything in `app.js`.
```javascript
// routes/userRoutes.js
const express = require('express');
const router = express.Router();
router.route('/register').post(registerUser);

// app.js
app.use('/api/v1', require('./routes/userRoutes'));
```

### 6. HTTP Status Codes
- **200**: OK
- **201**: Created
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

---

## 🎓 Important Interview Questions

### Q1: What is Middleware in Express?
Middleware is a function that sits between the request and the response. It can execute code, modify the request/response objects, end the request-response cycle, or call the next middleware in the stack using `next()`.

**Full Answer:**
Middleware functions are the backbone of Express. They have access to the `req` and `res` objects and the `next` function in the application's request-response cycle.
- **Types:** Application-level, Router-level, Error-handling, Built-in, and Third-party.
- **Capabilities:** They can perform tasks like logging, authentication, data validation, and body parsing.
- **Flow:** A middleware must either end the request-response cycle (e.g., `res.send()`) or call `next()` to pass control to the next function.

**Trap Explained: The "Hanging Request"**
Interviewers will ask: *"What happens if you forget to call `next()` in a middleware?"*
- **The Answer:** The request will **hang** forever. The browser will show a loading spinner until it eventually times out. Control never reaches your route handler, and the server never sends a response.

---

### Q2: What is the difference between `app.use()` and `app.get()`?
- `app.use()`: Mounts the middleware for **all** HTTP methods on the specified path (or all paths if no path is given).
- `app.get()`: Mounts the middleware only for **GET** requests on the specified path.

**Full Answer:**
`app.use()` is generally used for global middleware like logging (`morgan`), security (`helmet`), or body parsing (`express.json`). It doesn't care about the HTTP verb (GET, POST, etc.).
`app.get()`, `app.post()`, etc., are specific route handlers.

**Trap Explained: Order of Execution**
*"If I put a global `app.use()` after my `app.get()` route, will it run for that route?"*
- **The Answer:** **No.** Express matches and executes middleware and routes in the exact order they are defined. Once a response is sent, the cycle ends.

---

### Q3: How do you handle 404 errors in Express?
Since Express executes middleware in order, you can place a middleware function at the very end of your routes that sends a 404 response.
```javascript
app.use((req, res) => {
    res.status(404).send('Page Not Found');
});
```

**Full Answer:**
In Express, 404 is not an "error" in the traditional sense; it's simply the result of the request not matching any defined route. By placing a catch-all middleware at the bottom of your file (after all routes), you can catch these "orphaned" requests.

**Follow-up: Why not put it at the top?**
If you put your 404 handler at the top of the file, it will match **every** request and send a 404 before your actual routes ever get a chance to run.

---

### Q4: What is the purpose of `express.json()` middleware?
It parses incoming requests with JSON payloads and makes the data available in `req.body`. Without it, `req.body` will be `undefined`.

**Full Answer:**
Before Express 4.16.0, we had to install a separate package called `body-parser`. Now, it's built directly into Express. It is essential for POST and PUT requests where data is sent in the body.

**Trap Explained: The "Undefined Body"**
*"I am sending data from Postman, but `req.body` is empty. Why?"*
- **The Answer:** This is usually caused by a missing `app.use(express.json())` or the client failing to set the `Content-Type: application/json` header. If the header is missing, Express won't know it needs to parse the body.

---

### Q5: How do you implement "CORS" in Express?
By using the `cors` third-party middleware. It allows your backend to accept requests from different origins (e.g., your React frontend on port 3000 calling your API on port 5000).
```javascript
const cors = require('cors');
app.use(cors());
```

**Full Answer:**
CORS (Cross-Origin Resource Sharing) is a security feature implemented by browsers. By default, a browser won't let a script on `localhost:3000` call an API on `localhost:5000` unless the server explicitly allows it. The `cors` middleware adds the necessary `Access-Control-Allow-Origin` headers to the response.

---

### Q6: What is the difference between `res.send()`, `res.json()`, and `res.end()`?
* `res.send()`: Sends a response of various types (String, Object, Buffer). Sets `Content-Type` automatically.
* `res.json()`: Converts the object to a JSON string and sets the `Content-Type` to `application/json`.
* `res.end()`: Ends the response process without sending any data.

**Full Answer:**
For a MERN developer building APIs, `res.json()` is the standard choice as it explicitly signals to the frontend that it is receiving JSON data. `res.send()` is more flexible but less explicit.

---

### Q7: Why does Error-Handling middleware have 4 arguments?
* Standard middleware: `(req, res, next)`
* Error middleware: `(err, req, res, next)`

**Full Answer:**
Express distinguishes error-handling middleware by the number of arguments (arity). When you provide 4 arguments, Express knows this is the "final destination" for errors. Any time you call `next(err)` in your app, Express skips all normal middleware and jumps straight to the first middleware it finds with 4 arguments.

**Trap Explained: Arity**
*"If I remove the `next` argument from my error handler, will it still work?"*
- **The Answer:** **No.** Express uses function "arity" (the number of arguments) to identify a middleware. If you only provide 3 arguments, Express treats it as a normal middleware and will not pass the `err` object to it.

---

### Q8: What are Route Parameters vs. Query Parameters?
* Route Params: `/users/:id` -> `req.params.id` (Used for specific resources).
* Query Params: `/users?role=admin` -> `req.query.role` (Used for filtering/sorting).

**Full Answer:**
Route parameters are part of the URL path and are essential for identifying a resource. Query parameters are optional and are typically used for pagination, searching, or filtering lists.

---

### Q9: What is `next()` and `next('route')`?
* `next()`: Moves to the next middleware in the current stack.
* `next('route')`: Skips the rest of the middleware functions in the current router stack and moves to the next route.

**Full Answer:**
`next()` is used to pass control within the same route handler or middleware chain. `next('route')` is a specialized command used when you have multiple route handlers for the same URL path. It tells Express to stop executing the current route stack and jump to the *next* route that matches the same path.

**Trap Explained: Only for `app.METHOD()`**
Note that `next('route')` only works in middleware functions that were loaded by using the `app.METHOD()` or `router.METHOD()` functions. It will not work inside an `app.use()`.

---

### Q10: How do you serve static files in Express?
* Using the built-in `express.static()` middleware.
* Example: `app.use(express.static('public'))`.

**Full Answer:**
This allows you to serve CSS, images, and client-side JavaScript files directly. For production MERN apps, the "public" or "build" folder of the React app is often served this way.


### Q11: What is the purpose of `express.Router`?
* It allows you to create modular, mountable route handlers.
* A Router instance is a complete middleware and routing system; it is often referred to as a "mini-app."

**Full Answer:**
In a small app, you might put all routes in `app.js`. But in a production MERN app, you use `express.Router()` to split your code into files like `userRoutes.js`, `productRoutes.js`, etc. This makes the code maintainable and easier to test.

---

### Q12: How do you handle file uploads in Express?
* Express doesn't have built-in support for `multipart/form-data`.
* We use the **Multer** middleware.

**Trap Explained: The Memory Trap**
*"Should I store uploaded files in the database?"*
- **The Answer:** **No.** Storing large files (images/videos) in MongoDB/SQL will significantly slow down your queries. The professional way is to use Multer to upload to a folder or, even better, to a cloud service like **AWS S3** or **Cloudinary**, and only store the **URL** in the database.

---

### Q13: What is "Helmet" and why should you use it?
* Helmet is a collection of 15 smaller middleware functions that set HTTP response headers.
* Example: `app.use(helmet())`.

**Full Answer:**
In a production environment, your server is constantly scanned for vulnerabilities. Helmet mitigates these risks by setting headers that:
- Prevent Clickjacking (`X-Frame-Options`).
- Prevent MIME-type sniffing (`X-Content-Type-Options`).
- Force HTTPS (`Strict-Transport-Security`).
- Disable the `X-Powered-By` header (so attackers don't know you're using Express).

---

### Q14: What is the difference between `res.redirect()` and `res.render()`?
* `res.redirect()`: Sends a 302 status code to the browser, telling it to go to a new URL.
* `res.render()`: Compiles a template (like EJS or Pug) and sends the resulting HTML string to the client.

**Full Answer:**
In a modern MERN stack, we rarely use `res.render()` because React handles the UI. Instead, we use `res.json()` to send data, and the React frontend handles the navigation. However, `res.redirect()` is still useful for OAuth flows or legacy server-side logic.

---

### Q15: How do you implement Rate Limiting in Express?
* Using the `express-rate-limit` middleware.
* Example: `app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 100 }))`.

**Full Answer:**
Rate limiting is essential for production APIs to prevent Brute-force attacks and Denial of Service (DoS) by limiting the number of requests a single IP can make within a certain timeframe.

---

### Q16: What is the significance of the `app.set('trust proxy', 1)` setting?
* It tells Express that the app is behind a proxy (like Nginx, Heroku, or AWS ELB).
* It allows Express to trust the `X-Forwarded-For` header to get the real client IP.

**Full Answer:**
If you don't enable this, Express will think the proxy is the client, which can break features like Rate Limiting or Session management that rely on identifying individual users by their IP.

---

### Q17: How do you handle asynchronous errors in Express?
* In Express 4, you must wrap async code in `try/catch` and call `next(err)`.
* In Express 5, unhandled promise rejections are automatically passed to the error handler.

**Full Answer:**
A common senior-level pattern is to use an `asyncHandler` wrapper to avoid writing `try/catch` in every single route:
```javascript
const asyncHandler = fn => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};
```

---

### Q18: What is "Validation" in Express and how is it done?
* Ensuring the incoming data (body, params, query) meets specific rules.
* Common library: **express-validator**.

**Full Answer:**
Never trust user input. Validation prevents bad data from reaching your database and protects against NoSQL injection. `express-validator` allows you to define rules like `.isEmail()` or `.isLength({ min: 5 })` directly in your route definition.

---

### Q19: What is the "Clean Architecture" for an Express project?
* **Routes**: Handle URL mapping.
* **Controllers**: Handle business logic and response sending.
* **Models**: Handle database interactions.
* **Middleware**: Handle cross-cutting concerns like Auth or Validation.

**Full Answer:**
Separating these concerns makes the project scalable. If you need to change your database from MongoDB to Postgres, you only change the Models, leaving the Controllers and Routes untouched.

---

### Q20: How do you handle environment variables in Express?
* Using the `dotenv` package.
* Loading with `require('dotenv').config()`.

**Full Answer:**
Secrets like API keys, database URLs, and JWT secrets should never be hardcoded. They should stay in a `.env` file that is ignored by Git, ensuring security across different environments (Dev, Staging, Prod).


### Q21: How do you prevent NoSQL Injection and XSS in Express?
* NoSQL Injection: Use `mongo-sanitize` to strip `$` and `.` from user input.
* XSS (Cross-Site Scripting): Use `xss-clean` or `helmet` to sanitize input and set security headers.

**Full Answer:**
Security is a non-negotiable for Senior roles. You must sanitize all incoming data. For NoSQL, this means preventing users from sending objects like `{"$gt": ""}` in a password field. For XSS, it means ensuring that user-submitted scripts are not executed in other users' browsers.

---

### Q22: How do you optimize Express response performance?
* **Compression**: Use the `compression` middleware (Gzip/Brotli).
* **Minification**: Minify HTML/CSS/JS if serving static files.

**Full Answer:**
Enabling Gzip compression can reduce the size of your JSON responses by up to 70%, significantly improving the speed of your MERN app for users with slow connections. 
Example: `const compression = require('compression'); app.use(compression());`

---

### Q23: What is the "Service Layer" pattern and why use it?
* It separates Business Logic from Controller logic.
* **Controller**: Handles `req`, `res`, and status codes.
* **Service**: Handles database calls, calculations, and 3rd-party APIs.

**Full Answer:**
In a large project, your controllers will get bloated if they handle everything. By moving the logic to a Service layer, you make your code "DRY" (Don't Repeat Yourself). This also makes unit testing much easier because you can test the Service functions without needing to mock `req` and `res`.

---

### Q24: How do you perform Unit and Integration testing in Express?
* Libraries: **Jest** (Test Runner) and **Supertest** (HTTP assertions).

**Full Answer:**
Supertest allows you to simulate HTTP requests to your Express app without actually starting the server on a port. This is vital for CI/CD pipelines to ensure that a change in one route doesn't break another.

---

### Q25: How do you handle a "Graceful Shutdown" in Express?
* Listening for `SIGTERM` and `SIGINT` signals.
* Stopping the server from accepting new connections before exiting.

**Full Answer:**
When your app is restarting (during deployment), you don't want to kill active requests. The pattern is to stop the server from accepting new traffic, wait for existing requests to finish, and then close the database connections before exiting.
```javascript
const server = app.listen(3000);
process.on('SIGTERM', () => {
  server.close(() => {
    console.log('HTTP server closed');
    mongoose.connection.close(false, () => {
      process.exit(0);
    });
  });
});
```

---

  ### **Advanced Industry Standard Topics Added**
  * **Security:** NoSQL Injection, XSS Prevention.
  * **Performance:** Gzip Compression, ETag Caching.
  * **Architecture:** Service Layer Pattern, Modular Routing.
  * **Testing:** Integration testing with Supertest.
  * **DevOps:** Graceful Shutdown, Health Checks.

  ---

## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Nodejs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/01_Nodejs/01_Nodejs.md) | [🏠 Home](../../README.md) | [Next: Authentication Authorization ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/03_Authentication_Authorization/03_Authentication_Authorization.md)

---

  <div align="center">
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>