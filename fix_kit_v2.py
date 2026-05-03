import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

# 1. Read the file up to line 6890
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

clean_lines = lines[:6890]

# 2. Define the new content
new_content = """#### ✅ The Core Answer
You serve static files (like Images, CSS, or plain HTML) using the built-in **express.static()** middleware. You point it to a folder (usually named public), and Express makes every file inside that folder accessible via a URL.

---

#### 🔑 Key Technical Terms Used
*   **Static Asset:** A file that doesn't change (Images, CSS, JS files).
*   **__dirname:** A Node.js variable that gives the absolute path of the current folder.

---

#### 📖 Detailed Explanation
Imagine a **Restaurant**.
*   **Dynamic Routes**: These are the **Kitchen**. A chef has to actually cook a meal specifically for you.
*   **Static Files**: This is a **Vending Machine** in the lobby. The snacks (Images/CSS) are already made. You just put in the money (The URL), and the machine drops the item instantly. The chef doesn't need to do any work.
express.static turns a folder into that vending machine.

---

#### 💻 Code Example
```javascript
const path = require('path');

// Serve files from the "public" folder
app.use(express.static(path.join(__dirname, 'public')));

// Now you can visit: http://localhost:3000/images/logo.png
```

---

#### 🧠 One Line to Remember
Use app.use(express.static('public')) to make images and CSS files available to the public.

---

### Q15. What is the MVC pattern and how do you implement it in Express.js?

---

#### ✅ The Core Answer
MVC stands for **Model-View-Controller**. It is a design pattern used to organize code into three distinct parts:
1.  **Model**: Handles the **Database** logic (Mongoose schemas).
2.  **View**: Handles the **UI/Frontend** (React or Template Engines).
3.  **Controller**: The **"Brain"** that connects the Model and View (Route logic).
In Express, you implement this by creating separate folders: /models, /controllers, and /routes.

---

#### 🔑 Key Technical Terms Used
*   **Separation of Concerns:** Giving every part of your code a specific job so it's not messy.
*   **Business Logic:** The actual rules and math of your app (kept in Controllers).

---

#### 📖 Detailed Explanation
Think of a **Professional Restaurant**.
*   **The Model (The Pantry)**: This is where the food is stored. It doesn't know how to cook; it just holds the ingredients.
*   **The View (The Customer's Table)**: This is where the final product is shown. The customer doesn't see the pantry or the chef; they just see the plate.
*   **The Controller (The Chef)**: He is the middle-man. He takes an order (The Request), gets ingredients (The Model), and sends back a plate (The View).

---

#### 💻 Folder Structure Example
*   `app.js` (Main entry)
*   `/routes/userRoutes.js` (URLs)
*   `/controllers/userController.js` (Brain/Logic)
*   `/models/userModel.js` (Database Schema)

---

#### 🧠 One Line to Remember
MVC splits your code into Database (Model), Logic (Controller), and UI (View) for better organization.

---

---

## 🌐 Module 9: REST API Design

### Q1. What is a REST API and what does REST stand for?

---

#### ✅ The Core Answer
REST stands for **Representational State Transfer**. It is an architectural style for designing networked applications. A REST API is a way for two computer systems to communicate over HTTP using standard methods like GET, POST, PUT, and DELETE. It is **Stateless**, meaning the server does not store any session information about the client.

---

#### 🔑 Key Technical Terms Used
*   **Architectural Style:** A set of rules or patterns for building software.
*   **Stateless:** Each request from the client must contain all the information needed to understand and process it.
*   **Resources:** The data or services provided by the API (e.g., Users, Products).

---

#### 📖 Detailed Explanation
Imagine a **Vending Machine**.
1. **The Interface**: You see buttons for different snacks (The Endpoints).
2. **The Request**: You press a button and put in money (HTTP Method + Data).
3. **The Response**: The machine drops your snack (JSON Data).
4. **Statelessness**: The vending machine doesn't care who you are or what you bought 5 minutes ago. Every time you walk up to it, it treats you as a brand-new customer. All it needs is the current button press and the money.

---

#### 🧠 One Line to Remember
REST is a standard set of rules for how computers talk to each other using simple HTTP commands.

---

### Q2. What are HTTP methods and how are they used in REST APIs?

---

#### ✅ The Core Answer
HTTP methods (also called Verbs) tell the server what action to perform on a resource.
*   **GET**: Read data.
*   **POST**: Create new data.
*   **PUT**: Update/Replace existing data.
*   **PATCH**: Partially update data.
*   **DELETE**: Remove data.

---

#### 🔑 Key Technical Terms Used
*   **Idempotent:** An action that, if performed multiple times, always produces the same result (GET, PUT, DELETE).
*   **Safe Methods:** Methods that do not change any data on the server (GET).

---

#### 📖 Detailed Explanation
Think of a **Facebook Post**.
*   **GET**: You are **Reading** the post. (Safe - doesn't change anything).
*   **POST**: You are **Creating** a new post. (Every time you click 'Post', a new one appears).
*   **PUT**: You are **Replacing** the whole post with a new version.
*   **PATCH**: You are just **Editing a Typo** in the post. You only send the corrected word, not the whole post.
*   **DELETE**: You are **Removing** the post.

---

#### 🧠 One Line to Remember
HTTP methods are verbs like GET and POST that define the action a user wants to take.

---

### Q3. What is the difference between PUT and PATCH?

---

#### ✅ The Core Answer
*   **PUT**: Used for **Full Updates**. You must send the entire object. If you leave a field out, it might be deleted or set to null on the server.
*   **PATCH**: Used for **Partial Updates**. You only send the specific fields you want to change. It is more efficient for small edits.

---

#### 🔑 Key Technical Terms Used
*   **Payload:** The data you send in the body of the request.
*   **Partial Update:** Changing only a piece of the data.

---
"""

# 3. Write back the clean lines + the new content
with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)
    f.write(new_content)

print("File truncated and Module 8/9 restored.")
