import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

new_content = """### Q2. What is JWT and what does it stand for?

---

#### ✅ The Core Answer
JWT stands for **JSON Web Token**. It is a compact, URL-safe way of securely transmitting information between a client and a server as a JSON object. In MERN apps, JWT is used to keep users logged in. After a user logs in, the server sends them a JWT, and the client sends that token back with every future request to prove they are authenticated.

---

#### 🔑 Key Technical Terms Used
*   **Compact:** Small enough to be sent in a URL or an HTTP header.
*   **Digital Signature:** A piece of the token that proves it hasn't been tampered with.

---

#### 📖 Detailed Explanation
Imagine a **Concert Wristband**.
1. **Login**: You buy a ticket at the box office (Login).
2. **Token**: The box office gives you a **Wristband** (JWT).
3. **Usage**: For the rest of the night, you don't need to show your ticket again. You just show your wristband to the security guards at the gate. They can see the wristband is real because it has a special holographic stamp (Signature).
4. **Stateless**: The security guard doesn't need to call the box office to check if you are on a list; he just looks at the wristband on your arm.

---

#### 🧠 One Line to Remember
JWT is a secure "digital wristband" that proves a user is logged in without the server needing to remember them.

---

### Q3. What are the three parts of a JWT token?

---

#### ✅ The Core Answer
A JWT consists of three parts separated by dots (`.`):
1.  **Header**: Contains metadata about the token (e.g., the algorithm used like HS256).
2.  **Payload**: Contains the actual data (claims) like user ID or name. **(Warning: This part is NOT encrypted, only encoded!)**
3.  **Signature**: Created by taking the header, payload, and a secret key, and hashing them together. This ensures the token hasn't been changed.

---

#### 🔑 Key Technical Terms Used
*   **Base64Url Encoding:** The way the JSON is turned into a string. It is easy to reverse!
*   **Hashing Algorithm:** The math used to create the signature.

---

#### 📖 Detailed Explanation
Think of a **Postcard**.
1. **Header**: The **Stamp and Postmark**. It tells the post office how to handle the mail.
2. **Payload**: The **Message** written on the back. Anyone can read it if they see the postcard, so you shouldn't write your bank password there.
3. **Signature**: The **Wax Seal** on an old letter. If the seal is broken, you know someone tried to change the message.

---

#### 🧠 One Line to Remember
A JWT has a Header (Type), a Payload (Data), and a Signature (Security).

---

### Q4. How do you generate and verify a JWT in Node.js?

---

#### ✅ The Core Answer
In Node.js, we use the `jsonwebtoken` library:
*   **Generate**: Use `jwt.sign(payload, secretKey, options)`. The payload is usually the User ID.
*   **Verify**: Use `jwt.verify(token, secretKey)`. If the token is valid, it returns the decoded payload; if not, it throws an error.

---

#### 💻 Code Example
```javascript
const jwt = require('jsonwebtoken');

// 1. Generate (Login)
const token = jwt.sign({ id: user._id }, 'mySecretKey', { expiresIn: '1h' });

// 2. Verify (Middleware)
try {
  const decoded = jwt.verify(token, 'mySecretKey');
  console.log(decoded.id);
} catch (err) {
  console.log("Invalid Token");
}
```

---

#### 🧠 One Line to Remember
Use `jwt.sign()` to create a token and `jwt.verify()` to check if it's real.

---

### Q5. What is the difference between access tokens and refresh tokens?

---

#### ✅ The Core Answer
*   **Access Token**: A short-lived token (e.g., 15 minutes) used to access protected routes. If stolen, it expires quickly, limiting the damage.
*   **Refresh Token**: A long-lived token (e.g., 7 days) used only to get a **new** access token when the old one expires. It is usually stored more securely (like an httpOnly cookie) and can be revoked by the server if needed.

---

#### 📖 Detailed Explanation
Imagine a **Hotel Key Card**.
*   **Access Token**: The **Key Card** itself. It lets you into your room. It only works for a short time.
*   **Refresh Token**: The **ID/Passport** you showed at the front desk. You don't walk around the hotel with your passport in your hand, you keep it in the safe. When your key card stops working, you go back to the desk, show your passport, and they give you a new card.

---

#### 🧠 One Line to Remember
Access tokens are for daily use; Refresh tokens are for getting new access tokens.

---

### Q6. Where should you store JWT tokens on the client side?

---

#### ✅ The Core Answer
There are two common places:
1.  **LocalStorage**: Easy to use, but vulnerable to **XSS attacks** (a malicious script can steal the token).
2.  **HttpOnly Cookies**: More secure because JavaScript cannot access them. This prevents tokens from being stolen by malicious scripts, protecting you from XSS. **(Recommended for production)**.

---

#### 🔑 Key Technical Terms Used
*   **XSS (Cross-Site Scripting):** When an attacker injects a script into your website.
*   **HttpOnly:** A cookie flag that makes it "invisible" to JavaScript code.

---

#### 🧠 One Line to Remember
LocalStorage is easy but risky; httpOnly Cookies are much more secure for storing tokens.

---

### Q7. What are the security risks of storing JWT in localStorage vs httpOnly cookies?

---

#### ✅ The Core Answer
*   **LocalStorage (XSS Risk)**: If an attacker manages to run ANY script on your page (like a bad npm package or an unescaped comment), they can run `localStorage.getItem('token')` and steal your user's identity instantly.
*   **HttpOnly Cookies (CSRF Risk)**: While safe from scripts (XSS), cookies are vulnerable to **CSRF** (Cross-Site Request Forgery). However, CSRF can be easily prevented using "SameSite" cookie flags or CSRF tokens.

---

#### 📖 Detailed Explanation
*   **LocalStorage**: Like keeping your house key **under the doormat**. It's easy for you, but anyone who knows where to look can grab it.
*   **HttpOnly Cookies**: Like keeping your key in a **Bank Vault**. You can't even see it, but when you show up at the bank (The server), the vault opens for you automatically.

---

#### 🧠 One Line to Remember
LocalStorage is vulnerable to script theft (XSS); Cookies are safer but need protection against fake requests (CSRF).

---

### Q8. What is token expiry and why is it important?

---

#### ✅ The Core Answer
Token expiry is a timestamp inside the JWT (the `exp` claim) that tells the server when the token should stop working. It is critical for security because it ensures that even if a token is stolen, the attacker can only use it for a **limited time**. Without expiry, a stolen token could give an attacker access to a user's account forever.

---

#### 🧠 One Line to Remember
Expiry puts an "expiration date" on a user's login session to keep things safe.

---

### Q9. How do you protect routes in an Express API using JWT middleware?

---

#### ✅ The Core Answer
You create a **Middleware function** that:
1.  Reads the token from the `Authorization` header (e.g., `Bearer <token>`).
2.  Checks if the token exists.
3.  Uses `jwt.verify()` to validate it.
4.  If valid, it attaches the user data to `req.user` and calls `next()`.
5.  If invalid, it sends a **401 Unauthorized** error.

---

#### 💻 Code Example
```javascript
const protect = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ msg: "No token!" });

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(401).json({ msg: "Token is not valid" });
  }
};
```

---

#### 🧠 One Line to Remember
A middleware checks for a valid token before letting the request reach the "brain" of your app.

---

### Q10. What is password hashing and why should you never store plain text passwords?

---

#### ✅ The Core Answer
Password hashing is the process of turning a password into a scrambled string of characters (a hash) using a one-way mathematical function. You **never** store plain text because if your database is hacked, the attacker will have every user's password. With hashing, the attacker only sees scrambled text that is nearly impossible to turn back into the original password.

---

#### 🔑 Key Technical Terms Used
*   **One-way function:** A function that is easy to scramble but impossible to unscramble.
*   **Rainbow Table:** A list of pre-calculated hashes that hackers use to "guess" passwords.

---

#### 🧠 One Line to Remember
Never store real passwords; only store their scrambled "hashes" for security.

---

### Q11. What is bcrypt and how does it work?

---

#### ✅ The Core Answer
`bcrypt` is a library used to securely hash passwords. It works by:
1.  **Salting**: Adding random characters to the password before hashing so even two identical passwords have different hashes.
2.  **Cost Factor (Rounds)**: Intentionally making the hashing process slow. This makes "Brute Force" attacks (guessing millions of passwords) too slow for hackers to succeed.

---

#### 💻 Code Example
```javascript
// Hashing (Signup)
const salt = await bcrypt.genSalt(10);
const hashedPassword = await bcrypt.hash(password, salt);

// Comparing (Login)
const isMatch = await bcrypt.compare(enteredPassword, hashedPassword);
```

---

#### 🧠 One Line to Remember
`bcrypt` uses "salts" and "slow hashing" to make passwords impossible for hackers to guess.

---

### Q12. What is the difference between hashing and encryption?

---

#### ✅ The Core Answer
*   **Hashing**: A **one-way** process. Once you hash data, you cannot "unhash" it to get the original back. It is used for passwords.
*   **Encryption**: A **two-way** process. You scramble data with a key, and you can unscramble it (decrypt) later using that same key. It is used for sending private messages or sensitive data that needs to be read later.

---

#### 📖 Detailed Explanation
*   **Hashing**: Like making a **Fruit Smoothie**. You can't turn the smoothie back into an apple and a banana. You can only make another smoothie and see if it tastes the same.
*   **Encryption**: Like putting a letter in a **Locked Box**. If you have the key, you can open the box and read the original letter exactly as it was.

---

#### 🧠 One Line to Remember
Hashing is for things you don't need to read back (passwords); Encryption is for things you do (messages).

---

### Q13. What is role-based access control and how do you implement it?

---

#### ✅ The Core Answer
**RBAC** means giving users different permissions based on their "Role" (e.g., User, Admin, Moderator). In Express, you implement this by creating a middleware that checks the `req.user.role` after the JWT has been verified. If the user's role doesn't match the required role, you send a **403 Forbidden** error.

---

#### 💻 Code Example
```javascript
const authorize = (roles) => {
  return (req, res, next) => {
    if (!roles.includes(req.user.role)) {
      return res.status(403).json({ msg: "Access Denied" });
    }
    next();
  };
};

// Usage: Only admins can delete products
app.delete('/product/:id', protect, authorize(['admin']), deleteProduct);
```

---

#### 🧠 One Line to Remember
RBAC checks the user's "Job Title" before letting them perform sensitive actions.

---

### Q14. What is OAuth 2.0 and what problem does it solve?

---

#### ✅ The Core Answer
OAuth 2.0 is a protocol that allows a website to access a user's data from another service (like Google or Facebook) **without the user sharing their password**. It solves the problem of "Trust." Instead of giving your Google password to a random app, you give Google permission to send that app a temporary "Access Token."

---

#### 📖 Detailed Explanation
Imagine a **Valet Key** for a car.
When you give your car to a valet, you don't give him your main key (which can open the trunk and glovebox). You give him a **Valet Key** that can *only* start the car and drive it a short distance.
OAuth is that valet key. It lets an app "drive" your Google account without giving it the "keys" to your whole digital life.

---

#### 🧠 One Line to Remember
OAuth lets you log in using Google/Facebook without sharing your password with the website.

---

### Q15. What is the difference between session-based and token-based authentication?

---

#### ✅ The Core Answer
*   **Session-based**: The server stores user data in its **Memory** or a database and gives the client a "Session ID" in a cookie. The server must "remember" every user.
*   **Token-based (JWT)**: The server sends a **signed token** to the client. The client stores it. The server doesn't "remember" anything; it just checks the signature every time the client sends the token back.

---

#### 💻 Comparison Table
| Feature | Session-based | Token-based (JWT) |
| :--- | :--- | :--- |
| **Storage** | Server-side (Memory/DB) | Client-side (Cookie/Local) |
| **Scalability** | Hard (Servers must sync) | Easy (Servers are stateless) |
| **Best For** | Traditional Web Apps | Modern Mobile & SPA Apps |

---

#### 🧠 One Line to Remember
Sessions make the server remember you; Tokens make you carry your own ID.

---

## 🛠️ Module 12: Git & Version Control

### Q1. What is the difference between Git and GitHub?

---

#### ✅ The Core Answer
*   **Git**: Is a **Local Tool**. It is software installed on your computer that tracks changes in your code (version control).
*   **GitHub**: Is a **Cloud Platform**. It is a website where you store your Git projects (repositories) so you can share them and collaborate with others.
Think of Git as the "Camera" and GitHub as "Instagram."

---

#### 🧠 One Line to Remember
Git is the tool you use to track code; GitHub is the place where you store and share it.

---
"""

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(new_content)

print("Rest of Module 11 and start of Module 12 appended.")
