# Authentication & Security
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

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

## **Authentication & Security — MERN Stack Interview Kit**

---

* Note — JWT, RBAC, bcrypt, CORS, Helmet, Rate Limiting covered in depth in previous Authentication section — this section covers NestJS-specific implementation patterns only

---

**Q1. How do you implement JWT authentication in NestJS with Passport.js?** `[1-2 yrs]`

* npm install @nestjs/passport @nestjs/jwt passport passport-jwt  
* JwtModule.registerAsync() in AuthModule — inject ConfigService for secret and expiry  
* JwtStrategy — extends PassportStrategy(Strategy from passport-jwt):  
  * constructor — super() with jwtFromRequest and secretOrKey options  
  * validate(payload) — called after JWT verified, return value attached to req.user  
  * jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken() — extract from Bearer header  
* JwtAuthGuard — extends AuthGuard('jwt') from @nestjs/passport:  
  * Passport handles extraction, verification, and calling validate automatically  
  * Override canActivate for public route skipping — check IS\_PUBLIC\_KEY metadata  
  * Override handleRequest to customize error thrown on invalid token  
* @Public() decorator pattern — routes that skip JWT:  
  * @SetMetadata(IS\_PUBLIC\_KEY, true) custom decorator  
  * JwtAuthGuard checks Reflector for IS\_PUBLIC\_KEY — if true, skip verification  
  * Cleaner than applying guard to every protected route individually  
* Register JwtAuthGuard globally — APP\_GUARD in AppModule — all routes protected by default  
* Add @Public() to login, register, and any public endpoints  
* req.user — populated by validate() return value, access in controllers with @Req() or custom @CurrentUser() decorator  
* Refresh token implementation — separate RefreshTokenStrategy with different secret, endpoint to exchange refresh token for new access token

**Full Answer:**
Implementing JWT in NestJS is a multi-step process involving the `JwtModule` and `PassportModule`. The core logic lives in a **Strategy** class where you define how the token is extracted (usually from the Bearer header) and verified. The `validate()` method is crucial; whatever it returns is automatically attached to the `req.user` object by Nest.

**Trap Explained: The "Secret" Leak**
- **The Answer:** Never hardcode your `JWT_SECRET`. Always use `ConfigService` and `JwtModule.registerAsync()` to ensure the secret is loaded from environment variables.
- **Code Example:**
```typescript
// WRONG: Hardcoded
JwtModule.register({ secret: 'my-secret' })

// RIGHT: Dynamic
JwtModule.registerAsync({
  inject: [ConfigService],
  useFactory: (config: ConfigService) => ({
    secret: config.get('JWT_SECRET'),
  }),
})
```

---

**Q2. How do you implement RBAC in NestJS?** `[1-2 yrs]`

* Already covered in detail — NestJS-specific implementation:  
* Roles enum — define in shared constants — USER, ADMIN, MODERATOR  
* @Roles(...roles) decorator — @SetMetadata(ROLES\_KEY, roles) shorthand custom decorator  
* RolesGuard — implements CanActivate, inject Reflector:  
  * Read required roles from metadata — reflector.getAllAndOverride(ROLES\_KEY, \[handler, class\])  
  * If no roles metadata — allow access (guard is permissive by default)  
  * Check req.user.role against required roles array  
  * Return true if user has required role, throw ForbiddenException if not  
* Register both JwtAuthGuard and RolesGuard as APP\_GUARD — authentication runs first, authorization second  
* Usage on routes — @Roles(Role.ADMIN) @Get('admin-only') — clean and readable  
* Permission-based alternative — @Permissions('delete:users') for more granular control  
* Store role in JWT payload — avoids DB lookup on every request for role check  
* For dynamic roles — fetch user from DB in validate() and attach full user with current role

**Full Answer:**
RBAC in NestJS relies on **Reflect Metadata**. You "tag" your routes with roles using a custom `@Roles()` decorator. Then, a global `RolesGuard` uses the `Reflector` service to "read" those tags and compare them against the `role` stored in the user's JWT.

**Trap Explained: The "Global Guard" Order**
*"Does the RolesGuard run before the JwtAuthGuard?"*
- **The Answer:** If registered as `APP_GUARD`, they run in the order they are listed in the `providers` array. However, `RolesGuard` **must** run after `JwtAuthGuard` because it needs the `req.user` object populated by the JWT check. If `req.user` is undefined, your roles check will crash or fail.

---

**Q3. How do you hash passwords with bcrypt in NestJS?** `[Fresher]`

* Already covered thoroughly — NestJS implementation pattern:  
* npm install bcrypt @types/bcrypt  
* In AuthService or dedicated HashingService:  
  * hashPassword(password: string) — bcrypt.hash(password, 10\) — async, returns Promise\<string\>  
  * comparePassword(plain, hashed) — bcrypt.compare(plain, hashed) — returns Promise\<boolean\>  
* Never hash in controller — always in service layer  
* Call hashPassword in register() before User.create()  
* Call comparePassword in login() before issuing JWT  
* @Column({ select: false }) on password in entity — never returned in queries unless explicitly selected  
* When select: false — use queryBuilder with addSelect or find with select option when password is needed for comparison

**Full Answer:**
Password hashing is a non-negotiable security requirement. In NestJS, we typically wrap `bcrypt` in a `HashingService`. We use a **Salt rounds** value of 10-12 to ensure the hash is computationally expensive enough to resist brute-force attacks but fast enough for a good user experience.

**Trap Explained: The "Async" Requirement**
*"Can I use `bcrypt.hashSync` instead?"*
- **The Answer:** **NO.** `hashSync` blocks the Node.js Event Loop. While it's calculating a hash (which takes ~100ms), your entire server is "frozen" and cannot handle any other requests. Always use the async `bcrypt.hash()` method.

---

**Q4. What are security best practices specific to NestJS apps?** `[2-3 yrs]`

* Helmet — app.use(helmet()) in main.ts — already covered, same as Express  
* CORS — app.enableCors({ origin, methods, credentials }) in main.ts — NestJS built-in  
* Rate limiting — @nestjs/throttler package — NestJS-native rate limiting:  
  * npm install @nestjs/throttler  
  * ThrottlerModule.forRoot(\[{ ttl: 60000, limit: 10 }\]) in AppModule imports  
  * APP\_GUARD with ThrottlerGuard — applies globally  
  * @Throttle({ default: { limit: 5, ttl: 60000 } }) — override per route  
  * @SkipThrottle() — disable for specific routes  
  * ThrottlerModule.forRootAsync() — use ConfigService for values  
* Validation globally — app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true })) — strips and rejects extra fields  
* express-mongo-sanitize — prevent NoSQL injection — app.use(mongoSanitize())  
* @nestjs/config with Joi validation — fail fast on missing env vars at startup  
* Hide stack traces in production — custom exception filter returns generic message when NODE\_ENV is production  
* Sensitive fields — @Exclude() with ClassSerializerInterceptor on response DTOs — never leak password, tokens

**Full Answer:**
A secure NestJS app uses layers of defense. We use **Helmet** for HTTP headers, **Throttler** for rate limiting, and **ValidationPipe** to prevent "Mass Assignment" attacks. Additionally, we use the `ClassSerializerInterceptor` to ensure that even if a developer accidentally returns a User object, the password field is automatically stripped out before reaching the client.

**Trap Explained: The "Whitelisting" Security Hole**
- **The Answer:** By default, `ValidationPipe` ignores unknown fields. If an attacker sends `{"role": "admin"}` in a profile update, and you don't have `whitelist: true`, that field might reach your database. Always set `whitelist: true` AND `forbidNonWhitelisted: true` to throw an error when extra fields are detected.

---

### **Missing Value: Advanced Industry Topics**

**Q5. How do you implement distributed Rate Limiting in a NestJS Microservices environment?** `[Senior]`

* Standard `ThrottlerModule` uses in-memory storage (local to one instance).  
* **The Problem:** If you have 5 instances of your API, each instance has its own counter, allowing an attacker to make 5x the intended requests.  
* **The Solution:** Use `throttler-storage-redis`.  
* **Implementation:** Configure the Throttler to use a Redis connection so all instances share the same request count per IP.

**Full Answer:**
In production, we never use in-memory throttling. We use a **Shared Storage** (usually Redis). This ensures that if a user is limited to 100 requests per minute, they can't bypass this by hitting different instances of our server behind a Load Balancer.

---

**Q6. What is "Double Submit Cookie" and how does it protect against CSRF?** `[Senior]`

* **The Problem:** JWTs stored in `httpOnly` cookies are vulnerable to CSRF.  
* **The Solution:** The server generates a random CSRF token and sends it as a **non-httpOnly** cookie. The frontend reads this cookie and sends the value in a custom header (e.g., `X-XSRF-TOKEN`) with every request.  
* **The Validation:** The server compares the cookie value with the header value. An attacker on a different site can't read the cookie (Same-Origin Policy), so they can't send the matching header.

**Full Answer:**
Double Submit Cookie is a stateless way to prevent CSRF. Because an attacker's site (`evil.com`) can't read cookies from your site (`myapp.com`), they can't "Double Submit" the token. This is the standard protection used by Angular and many React-based enterprise frameworks.

---

**Q7. How do you prevent NoSQL Injection in MERN/NestJS beyond simple sanitization?** `[Senior]`

* Sanitization (removing `$`) is good but not enough.  
* **The Senior Approach:** Use **Strict Schema Validation**.  
* In NestJS, we use **DTOs** with `class-validator`. If we define a field as `@IsString()`, and an attacker sends an object `{"$gt": ""}`, the `ValidationPipe` will reject the request before it ever touches Mongoose.

**Full Answer:**
While `mongo-sanitize` is a great safety net, the primary defense should be your **Type System**. By enforcing that an `email` field must be a string and nothing else, you eliminate the possibility of an attacker injecting a MongoDB operator object into your queries.

---

**Q8. What is "Token Rotation" and why is it mandatory for Refresh Tokens?** `[Senior]`

* **The Attack:** If a long-lived Refresh Token is stolen, the attacker can stay logged in indefinitely.  
* **The Solution:** Every time a Refresh Token is used to get a new Access Token, the server **invalidates** the old Refresh Token and issues a **new** one.  
* **Detection:** If the server sees an "Old" (already used) Refresh Token being used again, it's a sign of a breach. The server then invalidates **all** tokens for that user, forcing a re-login.

**Full Answer:**
Token Rotation is the "Kill Switch" for stolen credentials. It limits the window of opportunity for an attacker and provides a mechanism to detect and stop a session hijacking attempt in real-time.

---

**Q9. How do you implement "Least Privilege" using Scopes/Permissions in NestJS?** `[Senior]`

* Roles (Admin/User) are often too broad.  
* **The Pattern:** Use **Permissions (Scopes)** like `read:users`, `write:posts`, `delete:logs`.  
* **Implementation:** Add a `permissions` array to your JWT. Create a `@Permissions()` decorator and a `PermissionsGuard` that checks for specific strings rather than broad roles.

**Full Answer:**
"Least Privilege" means giving a user the absolute minimum access they need. Instead of checking if a user is an `admin`, we check if they have the `user:delete` permission. This allows for much more flexible security where you can create custom roles (e.g., "Support Agent" who can read but not delete).

---

That is the complete, professionalized Authentication & Security section — 9 questions with full senior-level depth, ready for your MERN Interview Kit.

---

[⬅️ Previous: Database ORM](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/07_Database_ORM/07_Database_ORM.md) | [🏠 Home](../../README.md) | [Next: Advanced Topics ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/09_Advanced_Topics/09_Advanced_Topics.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>