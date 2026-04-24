# Authentication & Authorization

## 📚 Curriculum Checklist
- [x] [JWT Authentication](https://jwt.io/introduction/) (jsonwebtoken)
- [x] OAuth & Google/Facebook Login (Passport.js)
- [x] Role-Based Access Control (RBAC)
- [x] Session & Cookie Management

## 📝 Detailed Notes

### 1. Authentication vs Authorization
- **Authentication**: Verifying **who** a user is (e.g., Login).
- **Authorization**: Verifying **what** a user is allowed to do (e.g., Admin vs. User roles).

### 2. JWT (JSON Web Tokens)
JWT is a stateless way to handle authentication.
- **Header**: Contains the algorithm and token type.
- **Payload**: Contains the claims (user ID, username).
- **Signature**: Used to verify the sender and ensure the message wasn't changed.
```javascript
const jwt = require('jsonwebtoken');
const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: '1d' });
```

### 3. Cookies & Sessions
- **Sessions**: Data is stored on the **server** (in memory or Redis). A `sessionID` is sent to the client as a cookie.
- **Cookies**: Small pieces of data stored in the **browser**. Can be `HttpOnly` (prevents JS access/XSS) and `Secure` (HTTPS only).

### 4. OAuth & Passport.js
Passport is a popular middleware for Node.js that simplifies authentication.
- **Strategies**: `passport-local` (email/pass), `passport-google-oauth20` (Google login).
- **Process**: User clicks "Login with Google" → redirected to Google → Google returns a code → Code exchanged for Profile/Token → Passport creates/finds the user.

### 5. Role-Based Access Control (RBAC)
Creating middleware to check user roles before granting access.
```javascript
const authorize = (roles = []) => {
    return (req, res, next) => {
        if (!roles.includes(req.user.role)) {
            return res.status(403).json({ message: 'Forbidden' });
        }
        next();
    };
};
// Usage: app.get('/admin', authenticate, authorize(['admin']), (req, res) => { ... })
```

---

## 🎓 Important Interview Questions

### Q1: What is the difference between `LocalStorage` and `HttpOnly Cookies` for storing JWTs?
- **LocalStorage**: Vulnerable to **XSS** attacks. Any script on the page can read the token.
- **HttpOnly Cookies**: Secure from XSS because JS cannot access them. However, they are vulnerable to **CSRF** (Cross-Site Request Forgery).

### Q2: How do you handle "Token Revocation" in JWT?
Since JWTs are stateless, you can't easily revoke them. Solutions include:
1. Short expiration times (e.g., 15 mins) + Refresh Tokens.
2. A "Blacklist" in Redis to store revoked tokens until they expire.
3. Checking a `tokenVersion` field in the DB on every request (makes it stateful).

### Q3: What is "Salting" a password?
Salting is adding random data to a password before hashing it. This ensures that two users with the same password have different hashes, preventing "Rainbow Table" attacks. Use `bcrypt` for this:
```javascript
const salt = await bcrypt.genSalt(10);
const hashed = await bcrypt.hash(password, salt);
```

### Q4: Explain the OAuth 2.0 flow.
1. **User Authorization**: User grants access.
2. **Authorization Code**: App receives a code.
3. **Token Exchange**: App exchanges code for an Access Token.
4. **API Access**: App uses token to fetch user data.

### Q5: What is a "Refresh Token"?
A refresh token is a long-lived token used to get new access tokens when they expire. This allows the user to stay logged in without re-entering credentials frequently, while keeping the access token's lifespan short for security.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Expressjs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/02_Expressjs/02_Expressjs.md) | [🏠 Home](../../README.md) | [Next: Advanced Expressjs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/04_Advanced_Expressjs/04_Advanced_Expressjs.md)
