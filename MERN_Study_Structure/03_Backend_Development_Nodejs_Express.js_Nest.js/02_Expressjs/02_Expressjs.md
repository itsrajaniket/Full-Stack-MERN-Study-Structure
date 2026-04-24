# Express.js

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

### Q2: What is the difference between `app.use()` and `app.get()`?
- `app.use()`: Mounts the middleware for **all** HTTP methods on the specified path (or all paths if no path is given).
- `app.get()`: Mounts the middleware only for **GET** requests on the specified path.

### Q3: How do you handle 404 errors in Express?
Since Express executes middleware in order, you can place a middleware function at the very end of your routes that sends a 404 response.
```javascript
app.use((req, res) => {
    res.status(404).send('Page Not Found');
});
```

### Q4: What is the purpose of `express.json()` middleware?
It parses incoming requests with JSON payloads and makes the data available in `req.body`. Without it, `req.body` will be `undefined`.

### Q5: How do you implement "CORS" in Express?
By using the `cors` third-party middleware. It allows your backend to accept requests from different origins (e.g., your React frontend on port 3000 calling your API on port 5000).
```javascript
const cors = require('cors');
app.use(cors());
```


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Nodejs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/01_Nodejs/01_Nodejs.md) | [🏠 Home](../../README.md) | [Next: Authentication Authorization ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/03_Authentication_Authorization/03_Authentication_Authorization.md)
