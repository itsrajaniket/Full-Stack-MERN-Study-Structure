# Authentication & Security

## 📚 Curriculum Checklist
- [x] [JWT Authentication](https://jwt.io/introduction/) with Passport.js
- [x] Role-Based Access Control (RBAC)
- [x] Hashing Passwords (bcrypt)
- [x] Security Best Practices (CORS, Helmet, Rate Limiting)

## 📝 Detailed Notes

### 1. JWT Authentication in NestJS
NestJS provides a `@nestjs/jwt` package to handle token creation and verification.
```typescript
@Injectable()
export class AuthService {
  constructor(private jwtService: JwtService) {}

  async login(user: any) {
    const payload = { username: user.username, sub: user.userId };
    return { access_token: this.jwtService.sign(payload) };
  }
}
```

### 2. Passport.js Integration
NestJS uses Passport strategies via `@nestjs/passport`. You define a class that extends `PassportStrategy`.
- **Local Strategy**: For username/password login.
- **JWT Strategy**: For protecting routes with a Bearer token.

### 3. Guards for RBAC (Role-Based Access Control)
You can create a custom `RolesGuard` that checks the user's roles from the JWT payload against a required role defined by a decorator.
```typescript
@SetMetadata('roles', ['admin'])
@UseGuards(JwtAuthGuard, RolesGuard)
@Get()
findAll() { ... }
```

### 4. Hashing Passwords (bcrypt)
Never store passwords in plain text. Use `bcrypt` to hash them before saving to the DB and use `bcrypt.compare` during login.

### 5. Security Middleware
- **Helmet**: Adds security headers to prevent common attacks like Clickjacking or XSS.
- **CORS**: Defines which domains are allowed to access your API.
- **Rate Limiting**: Throttles the number of requests a single client can make.
```typescript
// main.ts
app.use(helmet());
app.enableCors();
```

### 6. NoSQL Injection & Data Sanitization
Attackers can send malicious queries in `req.body` (e.g., `{"$gt": ""}`). Use `mongo-sanitize` to remove any keys starting with `$`.
```javascript
const sanitize = require('mongo-sanitize');
const cleanBody = sanitize(req.body);
```
Also, use **express-validator** or **Zod** to ensure inputs match expected types (string, email, etc.).

---

## 🎓 Important Interview Questions

### Q1: What is a "Guard" in NestJS?
A Guard is a class annotated with `@Injectable()` that implements the `CanActivate` interface. Guards determine whether a given request will be handled by the route handler or not based on certain conditions (like authentication or roles).

### Q2: How do you handle JWT expiration in NestJS?
You configure the `expiresIn` property in the `JwtModule` options. When a token expires, the `JwtAuthGuard` will automatically throw a `401 Unauthorized` exception.

### Q3: What is "Bcrypt" and why is it used?
Bcrypt is a library used to hash passwords. It incorporates a **Salt** and is **Computationally Expensive** (slow), which makes it very resistant to brute-force and rainbow table attacks.

### Q4: Explain "CORS" and how to enable it in NestJS.
CORS (Cross-Origin Resource Sharing) is a security feature that blocks web pages from making requests to a different domain than the one that served the web page. In NestJS, you enable it using `app.enableCors()` in your `main.ts` file.

### Q5: What is "Helmet" and why should you use it?
Helmet is a collection of 14 smaller middleware functions that set HTTP response headers. These headers help secure your app by protecting against well-known web vulnerabilities like cross-site scripting (XSS), sniffing, and clickjacking.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Database ORM](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/07_Database_ORM/07_Database_ORM.md) | [🏠 Home](../../README.md) | [Next: Advanced Topics ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/09_Advanced_Topics/09_Advanced_Topics.md)
