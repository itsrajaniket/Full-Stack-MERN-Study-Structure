# Authentication & Authorization
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

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


## **Authentication & Authorization — MERN Stack Interview Kit**

---

### **1\. OAuth & Google/Facebook Login (Passport.js)**

---

**Q1. What is the difference between Authentication and Authorization?** `[Fresher]`

* Authentication — verifying WHO you are (identity) — login process  
* Authorization — verifying WHAT you are allowed to do (permissions) — access control  
* Authentication always comes before authorization  
* Example — logging into a system is authentication, accessing admin panel is authorization  
* Common confusion — 401 Unauthorized actually means unauthenticated (not logged in), 403 Forbidden means unauthorized (logged in but no permission)  
* In MERN apps — JWT handles authentication, RBAC handles authorization

**Full Answer:**
In a production environment, this distinction is critical for debugging. 
- **Authentication (AuthN):** Is the user who they say they are? (Passport, JWT, OAuth).
- **Authorization (AuthZ):** Does this authenticated user have the right to delete this resource? (RBAC, Scopes, ABAC).

**Trap Explained: The 401 vs 403 Mix-up**
Interviewers love to ask: *"If a user is logged in but tries to access a page they don't have permission for, what status code do you return?"*
- **The Answer:** **403 Forbidden.** Many beginners return 401. 401 (Unauthorized) actually means the server doesn't know who you are. 403 (Forbidden) means the server knows you but says "No."

---

**Q2. What is JWT (JSON Web Token) and how does it work?** `[Fresher]`

* JWT — compact, URL-safe token format for securely transmitting information between parties  
* Stateless — server does not store session, token contains all needed info  
* Structure — three Base64URL-encoded parts separated by dots: Header.Payload.Signature  
* Header — algorithm used and token type, example: { "alg": "HS256", "typ": "JWT" }  
* Payload — claims (data) about the user, example: { "userId": "123", "role": "admin", "iat": 1234567890, "exp": 1234567890 }  
* Signature — HMAC of encoded header \+ payload using secret key — verifies token was not tampered  
* How it works:  
  * User logs in with credentials  
  * Server verifies credentials, creates JWT signed with secret key  
  * Server sends JWT to client  
  * Client stores JWT (localStorage or HttpOnly cookie)  
  * Client sends JWT in every request (Authorization: Bearer token header)  
  * Server verifies signature on every request, extracts user info from payload  
  * No database lookup needed to verify token — stateless  
* Standard claims in payload:  
  * iat — issued at (timestamp)  
  * exp — expiration time (timestamp)  
  * sub — subject (user ID)  
  * iss — issuer  
  * aud — audience  
* JWT is signed, NOT encrypted — payload is Base64 encoded, anyone can decode it  
* Never put sensitive data in JWT payload (passwords, credit card numbers)  
* jsonwebtoken package — most used Node.js JWT library  
  * jwt.sign(payload, secret, options) — create token  
  * jwt.verify(token, secret) — verify and decode token  
  * jwt.decode(token) — decode without verifying (unsafe, for debugging only)

**Full Answer:**
JWTs allow for **Stateless Authentication**. This means the server doesn't need to keep a list of "who is logged in" in memory or a database (like sessions do). The server simply trusts the token if the signature matches its secret key.

**Trap Explained: "Is JWT Encrypted?"**
- **The Answer:** **No.** By default, a JWT is only **signed**. Anyone can take your JWT, go to `jwt.io`, and read your `userId` or `email`. Never store passwords or sensitive data in the payload. If you need encryption, you would need a **JWE** (JSON Web Encryption), which is rarely used in standard MERN apps.

---

**Q3. What is the difference between Access Token and Refresh Token?** `[1-2 yrs]`

* Access Token — short-lived JWT used to authenticate API requests (15 mins to 1 hour)  
* Refresh Token — long-lived token used only to get new access tokens (7 days to 30 days)  
* Why two tokens — short-lived access token limits damage if stolen, refresh token allows staying logged in without re-entering credentials  
* Flow:  
  * Login → server issues both access token and refresh token  
  * Client uses access token for API calls  
  * Access token expires → client sends refresh token to /auth/refresh endpoint  
  * Server verifies refresh token → issues new access token  
  * Refresh token expires or is revoked → user must log in again  
* Refresh token storage — should be in HttpOnly cookie (not localStorage — XSS safe)  
* Access token storage — memory (React state) is safest, localStorage is common but XSS risk  
* Refresh token rotation — issue new refresh token each time it is used, invalidate old one  
* Refresh token revocation — store in DB or Redis, check on each use (adds statefulness)  
* Token blacklisting — store invalidated tokens in Redis until expiry for logout functionality

**Full Answer:**
This dual-token system balances **security and user experience**. If an access token is stolen, it only works for a few minutes. If a refresh token is stolen, we can detect it via **Rotation** (if the old one is used again, we know an attack happened) and revoke it in the database.

**Trap Explained: The "Stateless" Myth**
*"If JWT is stateless, how do you log a user out or block a stolen token?"*
- **The Answer:** This is where JWT becomes "hybrid." To truly log someone out before the token expires, you **must** maintain a blacklist in Redis or check a `validToken` version in your database. This adds a small amount of state, but only for security checks.

---

**Q4. How do you implement JWT authentication in a MERN app?** `[1-2 yrs]`

* Install — npm install jsonwebtoken bcryptjs  
* Password hashing — never store plain text passwords, use bcryptjs  
  * bcrypt.hash(password, saltRounds) — hash password before saving  
  * bcrypt.compare(plainPassword, hashedPassword) — verify on login  
  * saltRounds — cost factor, 10-12 is recommended for production  
* Registration flow:  
  * Receive email and password from request body  
  * Check if user already exists  
  * Hash password with bcrypt  
  * Save user to database  
  * Return success (do not auto-login or return token — debated)  
* Login flow:  
  * Receive email and password  
  * Find user by email  
  * Compare password with bcrypt.compare  
  * If valid — sign JWT with user ID and role as payload  
  * Set expiry — jwt.sign(payload, secret, { expiresIn: '15m' })  
  * Send token to client  
* Auth middleware:  
  * Extract token from Authorization header — split "Bearer token"  
  * jwt.verify(token, secret) — throws if invalid or expired  
  * Attach decoded user to req.user  
  * Call next() to continue  
* Protect routes — use auth middleware on all protected routes

**Full Answer:**
Implementing this correctly requires strict environment variable management. Always ensure `JWT_SECRET` is complex and unique. In the middleware, always check if the token exists before trying to verify it to avoid `null` errors.

**Trap Explained: The "Bcrypt Timing" Trap**
*"Why is bcrypt better than just using a simple SHA256 hash?"*
- **The Answer:** Bcrypt includes a **Salt** (to prevent rainbow table attacks) and a **Cost Factor** (to make it slow). If it takes 100ms to check one password, a hacker can only try 10 passwords a second, making brute-force attacks impossible.

---

**Q5. What is OAuth 2.0 and how does it work?** `[1-2 yrs]`

* OAuth 2.0 — authorization framework that allows third-party apps to access user data without sharing passwords  
* Enables "Login with Google", "Login with Facebook", "Login with GitHub"  
* Key roles:  
  * Resource Owner — the user  
  * Client — your application (MERN app)  
  * Authorization Server — Google/Facebook/GitHub (issues tokens)  
  * Resource Server — API that holds user data (Google APIs, etc.)  
* Authorization Code Flow (most secure, for server-side apps):  
  * User clicks "Login with Google"  
  * App redirects user to Google's authorization URL with client\_id, redirect\_uri, scope  
  * User authenticates with Google and grants permissions  
  * Google redirects back to your app with a short-lived authorization code  
  * Your server exchanges code for access token (server-to-server, secret not exposed)  
  * Server uses access token to fetch user profile from Google  
  * Server creates or finds user in your DB, issues your own JWT  
* PKCE (Proof Key for Code Exchange) — extension for public clients (SPAs, mobile)  
* Scopes — permissions requested from provider (profile, email, etc.)  
* State parameter — random string to prevent CSRF during OAuth flow  
* OAuth 2.0 is for authorization (access to resources), OpenID Connect (OIDC) adds authentication layer on top

**Full Answer:**
OAuth is often confused with Authentication. OAuth is strictly for **access**. OpenID Connect (OIDC) was built on top of OAuth 2.0 to provide the identity layer (the `id_token`). Most MERN apps use the **Authorization Code Flow** because it keeps the Access Token on the backend, away from the browser's view.

**Trap Explained: The "Implicit Flow"**
- **The Answer:** The "Implicit Flow" (where the token is sent directly in the URL hash) is now **deprecated** and considered insecure. Senior interviewers will look for you to mention the **Authorization Code Flow with PKCE** as the modern standard.

---

**Q6. What is Passport.js and how does it work?** `[1-2 yrs]`

* Passport.js — authentication middleware for Node.js, supports 500+ strategies  
* Strategy pattern — each authentication method is a separate strategy (local, Google, Facebook, JWT, GitHub)  
* Core packages:  
  * passport — core package  
  * passport-local — username/password authentication  
  * passport-google-oauth20 — Google OAuth 2.0  
  * passport-facebook — Facebook OAuth  
  * passport-jwt — JWT authentication  
* How Passport works:  
  * Configure strategy with credentials and verify callback  
  * Use passport.initialize() middleware  
  * Use passport.session() if using sessions (not needed for JWT)  
  * Use passport.authenticate('strategy') as route middleware  
* passport.serializeUser() — what to store in session (user ID)  
* passport.deserializeUser() — fetch user from DB using stored ID  
* Verify callback — called after strategy authenticates user, you decide if user is valid:  
  * done(null, user) — success, attach user to req.user  
  * done(null, false) — authentication failed  
  * done(err) — error occurred  
* Google OAuth 20 strategy setup:  
  * clientID and clientSecret from Google Cloud Console  
  * callbackURL — must match registered redirect URI exactly  
  * Verify callback receives accessToken, refreshToken, profile, done  
  * profile.emails\[0\].value — user's email from Google  
  * Create or find user in DB based on Google ID or email

**Full Answer:**
Passport.js abstracts the complexity of multiple login methods. Its power lies in the `req.user` object it creates. Once authenticated, any subsequent route has access to the user's data.

**Trap Explained: Serialize vs Deserialize**
- **The Answer:** **Serialization** happens once upon login (to save the ID to the session). **Deserialization** happens on *every* request (to fetch the full user object from the DB using that ID). In a JWT-based app, we usually skip these two functions entirely.

---

**Q7. What is the difference between Passport.js Local Strategy and JWT Strategy?** `[2-3 yrs]`

* Local Strategy — handles username/password login, typically combined with sessions or issues JWT on success  
* JWT Strategy — validates JWT token on each protected request, stateless  
* Local Strategy flow:  
  * Client sends username and password  
  * Passport calls verify callback with credentials  
  * You check DB and bcrypt.compare password  
  * done(null, user) if valid  
* JWT Strategy flow:  
  * Client sends JWT in Authorization header  
  * Passport extracts and verifies token  
  * done(null, user) with decoded payload  
  * No DB call needed (unless checking revocation)  
* Using passport-jwt options:  
  * jwtFromRequest — how to extract token (fromAuthHeaderAsBearerToken is most common)  
  * secretOrKey — same secret used to sign tokens  
* When to use Passport vs manual JWT — Passport adds structure and reusability, manual is simpler for small apps  
* In modern MERN apps — many teams skip Passport for JWT and implement manually, use Passport mainly for OAuth strategies

**Full Answer:**
The **Local Strategy** is for the "Entry Point" (the login route). The **JWT Strategy** is for the "Protected Routes" (everything else). Combining them creates a complete security flow.

**Trap Explained: The `done()` function**
*"What is the difference between `done(null, false)` and `done(err)`?"*
- **The Answer:** `done(err)` means a **server error** happened (like the DB is down). `done(null, false)` means the server is fine, but the **credentials were wrong**. Mixing these up will result in poor error handling for the user.

---

### **2\. Role-Based Access Control (RBAC)**

---

**Q8. What is Role-Based Access Control (RBAC)?** `[Fresher]`

* RBAC — access control mechanism where permissions are assigned to roles, and roles are assigned to users  
* Instead of assigning permissions directly to users, you assign roles  
* Core concepts:  
  * Users — the authenticated principals  
  * Roles — named groups of permissions (admin, user, moderator, editor)  
  * Permissions — specific actions allowed (read:users, write:posts, delete:comments)  
  * Resources — what is being protected (routes, data, features)  
* Example roles in a MERN app:  
  * admin — full access to everything  
  * moderator — can manage content but not users  
  * user — can only access own data  
  * guest — read-only public access  
* RBAC vs ABAC (Attribute-Based Access Control):  
  * RBAC — based on roles assigned to user  
  * ABAC — based on attributes of user, resource, and environment (more granular, more complex)  
* Why RBAC — simpler to manage, scalable, easy to audit who has access to what

**Full Answer:**
RBAC is the industry standard for most SaaS applications. By grouping permissions into roles, you avoid the nightmare of updating 10,000 individual users when a permission changes.

**Trap Explained: The "Role Bloat"**
*"What happens when an Admin needs to be an Editor for just one specific project?"*
- **The Answer:** This is the limit of RBAC. In advanced systems, we use **ACLs (Access Control Lists)** or **ABAC** to handle these edge cases. Mentioning this shows you understand the limitations of basic roles.

---

**Q9. How do you implement RBAC in an Express.js application?** `[1-2 yrs]`

* Store role in JWT payload and in user DB document  
* Role field in user model — role: { type: String, enum: \['user', 'admin', 'moderator'\], default: 'user' }  
* Auth middleware — verifies JWT, attaches req.user with role  
* Authorization middleware — checks role after auth: Basic role check middleware:  
  * Create requireRole(role) factory function  
  * Check req.user.role against required role  
  * Return 403 if insufficient role  
  * Call next() if authorized  
* Multiple roles middleware:  
  * Create requireAnyRole(...roles) middleware  
  * Use roles.includes(req.user.role) check  
  * Same 403 and next() pattern  
* Route protection order — auth middleware first, then role middleware:  
  * router.delete('/users/:id', protect, requireRole('admin'), deleteUser)  
* Permission-based approach (more granular than role-based):  
  * Store permissions array in user model or derive from role  
  * Middleware checks if required permission is in user's permissions array  
  * More flexible — users can have custom permissions beyond their role  
* Ownership check — user can only modify their own resources:  
  * Check req.user.id \=== resource.userId.toString()  
  * Admin bypass — allow admins to modify any resource

**Full Answer:**
Implementing RBAC is all about **Middleware Composition**. You chain your `authenticate` middleware first, followed by your `authorize` middleware. This ensures that only known users are checked for permissions.

**Trap Explained: The "Admin Bypass"**
*"How do you ensure an Admin can delete any post, but a User can only delete their own?"*
- **The Answer:** Your ownership middleware should always have a **priority check**:
```javascript
if (req.user.role === 'admin') return next();
if (req.user.id === resource.authorId) return next();
return res.status(403).json({ message: "Not authorized" });
```
This is a very common senior-level coding interview task.

---

**Q10. What are common security mistakes in RBAC implementation?** `[2-3 yrs]`

* Only checking role on frontend — never trust frontend, always enforce on backend  
* Not checking ownership — user A can modify user B's data if only role check is done  
* Role stored only in JWT without DB validation — if role changes in DB, old JWT still has old role  
* Horizontal privilege escalation — user accessing another user's resource (same role, different user)  
* Vertical privilege escalation — user gaining higher role permissions  
* Mass assignment vulnerability — allowing role field to be set via req.body without restriction  
* Fix — never include role in fields that can be updated via regular update endpoint, only via admin endpoint  
* Not revoking tokens when role changes — JWT is stateless, role change doesn't reflect until token expiry  
* Fix — short access token expiry plus check role from DB on sensitive operations  
* Insecure direct object reference (IDOR) — exposing sequential IDs that can be enumerated  
* Fix — use MongoDB ObjectIDs (non-sequential) or UUID, always verify ownership

**Full Answer:**
Security is layered. Even if your RBAC is perfect, a **Mass Assignment** vulnerability (where a user sends `{"role": "admin"}` in their profile update JSON) can destroy your system. Always use "Allow-lists" for fields users can update.

**Trap Explained: The IDOR Attack**
- **The Answer:** Insecure Direct Object Reference (IDOR) happens when you allow a user to fetch `/api/orders/101` and they simply change it to `/api/orders/102` to see someone else's order. **The Fix:** Your controller must always include the owner in the query: `Order.findOne({ _id: id, userId: req.user.id })`.

---

### **3\. Session & Cookie Management**

---

**Q11. What is session-based authentication and how does it work?** `[Fresher]`

* Traditional authentication mechanism — server stores session data  
* Flow:  
  * User logs in with credentials  
  * Server creates session object in memory or DB with session ID  
  * Server sends session ID to client in a cookie (Set-Cookie header)  
  * Browser automatically sends cookie with every request to same domain  
  * Server looks up session ID, retrieves session data, identifies user  
  * On logout — server destroys session, client clears cookie  
* Session storage options:  
  * In-memory — default, fast but lost on server restart, not scalable across multiple servers  
  * Database — MongoDB, PostgreSQL — persistent, survives restarts  
  * Redis — in-memory store, fast like memory but persistent and shared across server instances  
* express-session package — session middleware for Express  
  * secret — used to sign the session ID cookie  
  * resave — force session to be saved even if unmodified (usually false)  
  * saveUninitialized — save new empty sessions (usually false for GDPR compliance)  
  * store — where to store session data (MemoryStore, MongoStore, RedisStore)  
  * cookie.secure — true in production (HTTPS only)  
  * cookie.httpOnly — true — prevent JS access to cookie  
  * cookie.maxAge — session expiry in milliseconds

**Full Answer:**
Sessions were the bedrock of the web for decades. The server holds the "truth" and the client only holds a "key" (the Session ID). In modern MERN apps, we still use sessions when we need **Opaque Tokens** (tokens that mean nothing if stolen) or when we need to instantly kill a user's access server-side.

**Trap Explained: The "Sticky Session" Problem**
*"If you use In-Memory sessions, what happens when you have two servers?"*
- **The Answer:** Authentication will fail half the time because Server A doesn't know about the session created on Server B. **The Fix:** Use a shared session store like **Redis** (Connect-Redis) to allow any server to validate any session.

---

**Q12. What is the difference between session-based and JWT-based authentication?** `[1-2 yrs]`

* Statefulness:  
  * Session — stateful, server stores session data, must look up on every request  
  * JWT — stateless, server stores nothing, token contains all info  
* Scalability:  
  * Session — harder to scale horizontally (multiple servers need shared session store like Redis)  
  * JWT — easily scales horizontally, any server can verify token with shared secret  
* Storage:  
  * Session — session ID in cookie (small), data on server  
  * JWT — entire token in cookie or localStorage (larger)  
* Revocation:  
  * Session — easy, just delete session from store  
  * JWT — hard, token valid until expiry unless blacklisted in Redis  
* Performance:  
  * Session — DB/Redis lookup on every request  
  * JWT — just cryptographic verification, no DB lookup  
* Security:  
  * Session with HttpOnly cookie — immune to XSS for session ID  
  * JWT in localStorage — vulnerable to XSS  
  * JWT in HttpOnly cookie — same XSS protection as session, but CSRF risk  
* When to use sessions — traditional server-rendered apps, when you need instant revocation  
* When to use JWT — REST APIs, microservices, mobile apps, stateless requirements  
* In MERN — JWT is more common due to React frontend and REST API architecture

**Full Answer:**
This is the most common architectural question. **JWT** is preferred for modern SPAs because it works seamlessly with mobile apps and cross-domain APIs. **Sessions** are preferred for banking or highly sensitive apps where you need to be able to "Kill Switch" a user instantly.

**Trap Explained: The "JWT is smaller" Myth**
- **The Answer:** Actually, **Sessions are smaller**. A Session Cookie is just a tiny ID (32 chars). A JWT can be huge because it contains user data, roles, and metadata. If your JWT gets too big, it can actually slow down your network requests!

---

**Q13. What are cookies and what are their security attributes?** `[1-2 yrs]`

* Cookies — small key-value data stored in browser, automatically sent with HTTP requests to matching domain  
* Set by server via Set-Cookie response header  
* Read by client via document.cookie (unless HttpOnly)  
* Cookie attributes:  
  * HttpOnly — cookie not accessible via JavaScript, protects against XSS stealing cookies  
  * Secure — cookie only sent over HTTPS connections, never HTTP  
  * SameSite — controls cross-site request behavior:  
    * Strict — cookie never sent with cross-site requests (most secure, may break OAuth flows)  
    * Lax — cookie sent with top-level navigation GET requests from other sites (default in modern browsers)  
    * None — sent with all cross-site requests (requires Secure flag), needed for third-party integrations  
  * Domain — which domain the cookie is valid for  
  * Path — which URL path the cookie is sent to (default /)  
  * Max-Age — expiry in seconds from now  
  * Expires — specific expiry date/time  
  * Session cookie — no Max-Age or Expires, deleted when browser closes  
  * Persistent cookie — has Max-Age or Expires, survives browser restart  
* Best practice for auth cookies:  
  * HttpOnly: true — prevent JS access  
  * Secure: true — HTTPS only  
  * SameSite: 'strict' or 'lax' — prevent CSRF  
  * Short Max-Age — limit exposure window

**Full Answer:**
In a production MERN app, you should **never** send a plain cookie. Always use `HttpOnly` and `Secure`. `SameSite: 'Lax'` is the best balance for most apps, while `'Strict'` is the safest but can cause issues if users follow a link to your site from an email or social media.

**Trap Explained: The "LocalStorage vs Cookie" Debate**
- **The Answer:** If you store a JWT in **LocalStorage**, it is vulnerable to **XSS** (any script can read it). If you store it in an **HttpOnly Cookie**, it is immune to XSS but vulnerable to **CSRF**. Most senior developers prefer the Cookie approach because CSRF is easier to defend against (using SameSite).

---

**Q14. What is CSRF (Cross-Site Request Forgery) and how do you prevent it?** `[2-3 yrs]`

* CSRF — attack where malicious website tricks authenticated user's browser into making unwanted requests to your API  
* Why it works — browser automatically sends cookies with every request, including cross-site ones  
* Example attack:  
  * User logged into bank.com with session cookie  
  * User visits evil.com which has hidden form that posts to bank.com/transfer  
  * Browser sends bank.com cookie with the forged request  
  * Bank processes transfer thinking it's legitimate  
* Prevention methods:  
  * SameSite cookie attribute — SameSite=Strict or Lax prevents cookie being sent on cross-site requests — simplest fix  
  * CSRF tokens — server generates random token, client must include in every state-changing request  
    * csurf package for Express (deprecated, use csrf-csrf instead)  
    * Token stored in cookie, must be included in request header — attacker cannot read it due to same-origin policy  
  * Double Submit Cookie pattern — send same random value in both cookie and request header  
  * Checking Origin/Referer headers — verify request comes from expected origin  
* JWT in Authorization header — not vulnerable to CSRF because browser does not auto-send custom headers (only cookies are auto-sent)  
* CSRF vs XSS:  
  * XSS — attacker runs code in YOUR site's context  
  * CSRF — attacker tricks YOUR browser into making requests to another site  
  * HttpOnly prevents XSS from stealing cookies but does not prevent CSRF

**Full Answer:**
CSRF is essentially **Identity Theft** for a single request. The browser is too "helpful" and sends your login cookie to sites it shouldn't. By using the `Authorization: Bearer <token>` header instead of cookies, you eliminate this risk because that header must be added manually by your JavaScript code.

**Trap Explained: "Is GET vulnerable to CSRF?"**
- **The Answer:** **No**, provided your GET routes are "Pure" (they don't change data). CSRF attacks typically target POST, PUT, and DELETE. If you have a GET route that deletes a user (e.g., `/user/delete?id=1`), you are highly vulnerable!

---

**Q15. What is XSS (Cross-Site Scripting) and how does it relate to authentication?** `[2-3 yrs]`

* XSS — attacker injects malicious JavaScript into your web page that executes in other users' browsers  
* Three types:  
  * Stored XSS — malicious script saved in DB (comments, user profiles), served to all visitors  
  * Reflected XSS — malicious script in URL parameter, reflected in response  
  * DOM-based XSS — client-side script writes attacker-controlled data to DOM  
* Impact on authentication — attacker can steal tokens from localStorage, session data, make authenticated API calls  
* Prevention:  
  * Sanitize all user input before storing — never trust client data  
  * Escape output when rendering user data in HTML  
  * Content Security Policy (CSP) header — restrict what scripts can execute on your page  
  * HttpOnly cookies — JWT or session cookie cannot be read by injected scripts  
  * Use helmet CSP — app.use(helmet.contentSecurityPolicy({ directives: {...} }))  
  * DOMPurify — sanitize HTML on client side before rendering  
  * In React — JSX auto-escapes values, use dangerouslySetInnerHTML carefully  
* Why localStorage is risky for JWT — any XSS can read localStorage, HttpOnly cookie cannot be read by scripts

**Full Answer:**
XSS is the #1 vulnerability in modern web apps. Even if you use React (which escapes strings by default), an attacker can use things like `javascript:alert(1)` in an `href` attribute. Always use **DOMPurify** on the frontend and **Helmet** on the backend to provide layers of defense.

**Trap Explained: The "React is safe" Trap**
*"Since React escapes HTML, we don't need to worry about XSS, right?"*
- **The Answer:** **Wrong.** React only escapes string content. It does NOT protect against:
1. `dangerouslySetInnerHTML`
2. Malicious URLs in `<a>` or `<iframe>` tags.
3. Server-side rendering (SSR) if not handled carefully.
Mentioning these three things proves you are a senior-level developer.

---

**Q16. How do you implement logout properly in a MERN app?** `[1-2 yrs]`

* JWT logout challenges — JWT is stateless, server cannot invalidate it directly  
* Client-side logout — delete token from localStorage or clear cookie — simplest but token still valid until expiry  
* Server-side JWT invalidation options:  
  * Token blacklist in Redis — store invalidated token JTI (JWT ID) until expiry, check on every request  
  * Short access token expiry — limit damage window (15 minutes)  
  * Refresh token revocation — delete refresh token from DB, user cannot get new access tokens  
* Cookie-based logout:  
  * Server clears cookie by setting same cookie with expired Max-Age or Expires in past  
  * res.clearCookie('token') in Express  
* Session-based logout:  
  * req.session.destroy() — destroys session on server  
  * Clear session cookie on client  
* Logout from all devices — invalidate all refresh tokens for user in DB (delete all records with userId)  
* Best practice in MERN:  
  * Short-lived access token (15 min) in memory  
  * Refresh token in HttpOnly cookie  
  * On logout — revoke refresh token in DB, clear cookie, remove access token from memory

**Full Answer:**
Proper logout isn't just about clearing the UI. You must **Revoke** the ability to get new tokens. By deleting the Refresh Token from your database, the user's current session is effectively "dead" as soon as the 15-minute access token expires.

**Trap Explained: The "Delete Cookie" Illusion**
*"If I delete the cookie from the browser, is the user logged out?"*
- **The Answer:** Not technically. If an attacker stole that cookie 1 minute ago, they are **still logged in** until the token actually expires on the server. This is why **Refresh Token Revocation** is mandatory for secure apps.

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q17. What is bcrypt and why is it used for password hashing?** `[Fresher]`

* bcrypt — adaptive password hashing algorithm designed for security  
* Why not MD5/SHA256 — they are fast (bad for passwords), bcrypt is deliberately slow  
* Salt — random data added to password before hashing, prevents rainbow table attacks  
* bcrypt auto-generates and stores salt within the hash — no need to store separately  
* Cost factor (saltRounds) — controls how slow hashing is, doubles computation per increment  
  * saltRounds of 10 — \~100ms per hash (good balance)  
  * saltRounds of 12 — \~400ms per hash (more secure, slightly slower)  
* bcrypt.hash(password, 10\) — async, always use async version in Express to avoid blocking  
* bcrypt.compare(plain, hashed) — returns boolean, timing-safe comparison (prevents timing attacks)  
* Never store plain text passwords — even in logs  
* Never compare passwords with \=== — use bcrypt.compare always  
* Argon2 — newer, more secure alternative to bcrypt (winner of Password Hashing Competition)

**Full Answer:**
Bcrypt is "adaptive," meaning as computers get faster, you can simply increase the `saltRounds` to keep it secure. This makes it future-proof.

**Trap Explained: The "Blocking the Event Loop" Trap**
- **The Answer:** Bcrypt is computationally heavy. If you use the synchronous version (`bcrypt.hashSync`), your entire Node.js server will **STOP** for 100ms-400ms while it calculates. **Always use the async version** (`await bcrypt.hash`) to keep the Event Loop free.

---

**Q18. What is the difference between hashing and encryption?** `[1-2 yrs]`

* Hashing — one-way transformation, cannot be reversed, fixed-length output  
  * Use for passwords — you never need original, just verify with same hash  
  * Algorithms — bcrypt, Argon2, SHA-256 (not for passwords — too fast)  
* Encryption — two-way transformation, can be decrypted with key, variable length output  
  * Use for sensitive data you need to retrieve — payment info, personal data  
  * Algorithms — AES-256 (symmetric), RSA (asymmetric)  
* Encoding — not security-related, just format transformation (Base64, URL encoding) — easily reversible  
* In MERN:  
  * Passwords — hash with bcrypt (hashing)  
  * JWT payload — Base64 encoded (encoding), signature is HMAC (hashing)  
  * Sensitive user data — encrypt with AES (encryption)  
  * API communication — TLS/HTTPS (encryption)

**Full Answer:**
Understanding the "direction" of data is key. **Hashing is a one-way street.** Once hashed, you can never get the password back. **Encryption is a two-way street.** You can lock it and unlock it using a key.

**Trap Explained: The "Base64 is Encrypted" Trap**
- **The Answer:** Many beginners think Base64 (used in JWTs) is encryption. It is **NOT**. It is just a different way of writing text (Encoding). Anyone can decode Base64 in 1 second without a key.

---

**Q19. What is the difference between symmetric and asymmetric JWT signing?** `[2-3 yrs]`

* Symmetric signing — HS256 algorithm — single secret key used to both sign and verify  
  * Simple, fast, same key on all services  
  * Risk — any service with the key can also forge tokens  
  * Use when — single server or trusted internal services  
* Asymmetric signing — RS256 or ES256 algorithm — private key signs, public key verifies  
  * Private key kept secret on auth server only  
  * Public key distributed to all services that need to verify tokens  
  * Services can verify but cannot forge tokens  
  * Use when — microservices, third-party verification, multiple independent services  
* In MERN:  
  * Single Express backend — HS256 is sufficient and simpler  
  * Microservices or third-party token verification — RS256 preferred  
* JWT\_SECRET env var — for HS256, must be long random string (32+ characters)  
* Key rotation — periodically change signing keys, use kid (key ID) header to identify which key

**Full Answer:**
In a **Microservices** architecture, you don't want every microservice to have the "Master Key." With **Asymmetric (RS256)**, the Authentication Service has the Private Key (to sign), and all other services have the Public Key (to verify). This is much more secure.

**Trap Explained: The "Secret vs Key"**
- **The Answer:** For HS256, your "secret" is just a string in an `.env` file. For RS256, you need a `.pem` file (a certificate). Senior developers will often ask how you manage these files securely (e.g., AWS Secrets Manager, Vault).

---

**Q20. What is two-factor authentication (2FA) and how would you implement it?** `[2-3 yrs]`

* 2FA — requires two forms of verification — something you know (password) \+ something you have (phone)  
* Common 2FA methods:  
  * TOTP (Time-based One-Time Password) — Google Authenticator, Authy  
  * SMS OTP — one-time code via SMS (less secure — SIM swapping attacks)  
  * Email OTP — code sent to email  
  * Hardware keys — YubiKey (most secure)  
* TOTP implementation with speakeasy package:  
  * Generate secret for user — speakeasy.generateSecret()  
  * Show QR code to user using qrcode package — user scans with authenticator app  
  * Save encrypted secret to user's DB record  
  * On login — after password verified, prompt for TOTP code  
  * Verify code — speakeasy.totp.verify({ secret, token, encoding: 'base32' })  
  * Issue JWT only after both factors verified  
* Backup codes — generate 8-10 single-use codes at setup, store hashed in DB  
* 2FA in MERN flow:  
  * Login → password correct → if 2FA enabled → return temp token → frontend shows OTP form → verify OTP → issue full JWT

**Full Answer:**
Implementing 2FA is about **Multi-Stage Authentication**. You don't give the user their final JWT until the second factor is verified. Instead, you give them a "Partial Token" that only allows access to the `/verify-2fa` route.

**Trap Explained: The "SMS is enough" Trap**
- **The Answer:** SMS is the least secure form of 2FA because of **SIM Swapping** attacks. For a high-security MERN app, always recommend **TOTP (Authenticator Apps)** as the primary method.

---

---

### **4\. Advanced Security & Architecture**

---

**Q21. What is SSO (Single Sign-On) and how does it differ from standard OAuth?** `[3+ yrs]`

* **SSO:** A session/user authentication service that permits a user to use one set of login credentials to access multiple applications.
* **Standard OAuth:** Primarily used for delegated access (letting an app act on your behalf).
* **OIDC (OpenID Connect):** The identity layer on top of OAuth 2.0 that actually handles SSO.
* **SAML (Security Assertion Markup Language):** An older, XML-based SSO standard used heavily in Enterprise/Corporate environments.

**Full Answer:**
SSO is about **Identity Consolidation**. Instead of every app having its own user database, they all trust a central **Identity Provider (IdP)** like Okta, Auth0, or Azure AD. This is critical for large companies where an employee needs to access Jira, Slack, and Zoom with one click.

**Trap Explained: "Is OAuth SSO?"**
- **The Answer:** Strictly speaking, **No**. OAuth is for *Authorization*. However, **OpenID Connect (OIDC)**, which is built on OAuth, is the standard for modern SSO. If an interviewer asks this, clarifying that OIDC is the "Identity Layer" shows high-level expertise.

---

**Q22. How do you protect a MERN app against Brute-Force and DoS attacks?** `[2-3 yrs]`

* **Rate Limiting:** Limit the number of requests a single IP can make in a time window.
* **`express-rate-limit`:** Standard middleware to limit requests.
* **`rate-limit-mongo` / `rate-limit-redis`:** Distributed rate limiting for multi-server setups.
* **Login Throttling:** Incrementally increase wait time after failed login attempts.
* **CAPTCHA:** Google reCAPTCHA or Cloudflare Turnstile for high-risk routes (Login/Signup).

**Full Answer:**
Protection must be implemented at multiple layers. 
1. **Network Layer:** Cloudflare/WAF to block known malicious IPs.
2. **App Layer:** Middleware like `express-rate-limit` to prevent scripted attacks on `/login`.
3. **Database Layer:** Locking a user account after 5 failed attempts (Account Lockout Policy).

**Trap Explained: The "Distributed Rate Limit" Trap**
*"If you use `express-rate-limit` in memory, does it work for 3 servers?"*
- **The Answer:** **No.** Each server will have its own counter. An attacker can hit all 3 servers and get 3x the limit. **The Fix:** Use a **Redis-backed** rate limiter so all servers share the same count.

---

**Q23. What are critical Security Headers every MERN app should have?** `[2-3 yrs]`

* **Helmet.js:** A collection of 15 smaller middleware functions that set security-related HTTP headers.
* **CSP (Content Security Policy):** Prevents XSS by restricting where scripts can be loaded from.
* **HSTS (HTTP Strict Transport Security):** Forces browsers to only use HTTPS.
* **X-Frame-Options:** Prevents **Clickjacking** by disallowing your site to be put in an `<iframe>`.
* **X-Content-Type-Options:** Prevents browsers from "guessing" the MIME type of a file (MIME sniffing).

**Full Answer:**
Using `app.use(helmet())` is the bare minimum. A senior developer should also configure a custom **CSP**. For example, `script-src 'self' https://apis.google.com` tells the browser only to run scripts from your domain and Google.

**Trap Explained: The "Clickjacking" Attack**
- **The Answer:** Clickjacking is when an attacker puts your site in an invisible iframe over their own site. When a user thinks they are clicking a "Play Game" button on the attacker's site, they are actually clicking "Delete Account" on your site. **The Fix:** `X-Frame-Options: DENY`.

---

**Q24. How do you handle Multi-Tenant Authentication in MERN?** `[3+ yrs]`

* **Definition:** A single instance of an app serving multiple customers (tenants), like Slack or Shopify.
* **Isolation Levels:**
    1. **Database-per-tenant:** Most secure, most expensive.
    2. **Schema-per-tenant:** Good balance.
    3. **Shared Database (Row-level isolation):** Most common, uses a `tenantId` field on every table.
* **Auth Flow:** User logs in → JWT includes `tenantId` → Middleware ensures user only sees data for that `tenantId`.

**Full Answer:**
Multi-tenancy requires **Identity Scoping**. When a user logs in, their JWT doesn't just say "who" they are, but "where" they belong. Your database queries should **always** include the `tenantId` to prevent data leakage between customers.

**Trap Explained: The "Cross-Tenant Leakage"**
- **The Answer:** This is the biggest risk in multi-tenancy. If you forget to add `tenantId` to one `findOne` query, Customer A might see Customer B's data. **The Fix:** Use a Mongoose plugin or a Global Middleware that automatically appends the `tenantId` to every query filter.

---

**Q25. What is Passwordless Authentication (Magic Links/WebAuthn)?** `[3+ yrs]`

* **Magic Links:** User enters email → Server sends a signed, short-lived link → User clicks and is logged in.
* **WebAuthn / Passkeys:** Uses hardware (TouchID, FaceID, YubiKey) to authenticate without passwords.
* **Benefits:** Higher security (no passwords to steal), better UX (no passwords to remember).

**Full Answer:**
Passwordless is the future. **Magic Links** are great for onboarding, but **Passkeys (WebAuthn)** are the gold standard because they use public-key cryptography and are immune to phishing. In MERN, you can use libraries like `SimpleWebAuthn` to implement this.

**Trap Explained: "Are Magic Links safer than passwords?"**
- **The Answer:** **Yes and No.** They are safer because there is no password to leak in a DB breach. However, they are only as safe as the user's **Email Account**. If the email is compromised, the app is compromised.

---

That's the complete, professionalized Authentication & Authorization section — 25 questions with full subtopic depth, ready for your MERN Interview Kit.


---

[⬅️ Previous: Expressjs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/02_Expressjs/02_Expressjs.md) | [🏠 Home](../../README.md) | [Next: Advanced Expressjs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/04_Advanced_Expressjs/04_Advanced_Expressjs.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>