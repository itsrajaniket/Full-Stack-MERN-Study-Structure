import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

new_content = """### Q4. What are HTTP status codes and what are the most important ones?

---

#### ✅ The Core Answer
Status codes are 3-digit numbers sent by the server to tell the client if a request was successful or if there was an error.
*   **2xx**: Success (e.g., 200 OK, 201 Created).
*   **3xx**: Redirection.
*   **4xx**: Client Error (e.g., 400 Bad Request, 404 Not Found).
*   **5xx**: Server Error (e.g., 500 Internal Server Error).

---

#### 🔑 Key Technical Terms Used
*   **Standardization:** Using the same codes so every developer knows what happened.
*   **Response Header:** Where the status code is stored.

---

#### 📖 Detailed Explanation
Think of **Hand Signals** in sports.
*   **Thumbs Up (200)**: "Good job, I got it!"
*   **Pointing Somewhere Else (301)**: "The ball is over there now!"
*   **Stop Sign (403)**: "You aren't allowed to do that!"
*   **Shrugging Shoulders (500)**: "I messed up, I don't know what to do!"

---

#### 🧠 One Line to Remember
Status codes are short "system messages" that tell the frontend exactly what happened on the server.

---

### Q5. What is the difference between 200, 201, and 204 status codes?

---

#### ✅ The Core Answer
All three mean **Success**, but in different ways:
*   **200 OK**: The request was successful and data is being sent back (e.g., after a GET).
*   **201 Created**: The request was successful and a **new resource** was created (e.g., after a POST).
*   **204 No Content**: The request was successful, but there is **no data** to send back (e.g., after a DELETE).

---

#### 🔑 Key Technical Terms Used
*   **Resource Creation:** Adding something new to the database.
*   **Empty Body:** When a response has headers but no actual content.

---

#### 📖 Detailed Explanation
Imagine **Shopping Online**.
*   **200 OK**: You click "View Order" and you see your list of items.
*   **201 Created**: You click "Place Order" and the screen says "Order #123 generated successfully."
*   **204 No Content**: You click "Cancel Order" and the order is deleted. The screen just shows a checkmark. There's no "Order" left to show you, so the body is empty.

---

#### 🧠 One Line to Remember
200 is "Got it," 201 is "Created it," and 204 is "Deleted it/Done."

---

### Q6. What is the difference between 400, 401, 403, and 404 status codes?

---

#### ✅ The Core Answer
These are **Client Errors** (The user did something wrong):
*   **400 Bad Request**: You sent bad data (e.g., missing an email in signup).
*   **401 Unauthorized**: I don't know who you are. **(Please Login)**.
*   **403 Forbidden**: I know who you are, but you aren't allowed here. **(No Permission)**.
*   **404 Not Found**: This URL or item doesn't exist.

---

#### 🔑 Key Technical Terms Used
*   **Authentication (401):** Checking "Who are you?"
*   **Authorization (403):** Checking "What can you do?"

---

#### 📖 Detailed Explanation
Imagine a **VIP Party**.
*   **400**: You tried to enter wearing **No Shoes**. You broke the dress code rules.
*   **401**: You don't have an **Invitation**. You need to show your ID first.
*   **403**: You showed your ID, but your name is **Not on the VIP List**. You are a regular guest trying to enter the private lounge.
*   **404**: You are looking for the party at the **Wrong Address**. There is no party here!

---

#### 🧠 One Line to Remember
400 is "Bad Data," 401 is "Login First," 403 is "No Access," and 404 is "Missing."

---

### Q7. What are REST API best practices for naming endpoints?

---

#### ✅ The Core Answer
1. Use **Nouns**, not Verbs (e.g., /users, not /getUsers).
2. Use **Plural** nouns (e.g., /products).
3. Use **Hierarchical** paths (e.g., /users/123/orders).
4. Use **Hyphens** for readability (e.g., /latest-news).
5. Keep everything **Lowercase**.

---

#### 🔑 Key Technical Terms Used
*   **Endpoint:** The URL where an API is accessed.
*   **Kebab-case:** Writing-like-this using hyphens.

---

#### 📖 Detailed Explanation
Think of a **Filing System** in an office.
*   **Bad Naming**: A drawer labeled "GoGetFiles" or "IWantToReadThis."
*   **Good Naming**: A drawer labeled **"Invoices"**. Inside that drawer, you have folders for years **"2023"**, and inside those, specific files **"Inv-101"**.
The URL /invoices/2023/101 makes sense to everyone. It describes **what** is there, not **what to do** with it.

---

#### 🧠 One Line to Remember
Endpoints should be simple, plural nouns like /users that describe the data.

---

### Q8. What is statelessness in REST and why is it important?

---

#### ✅ The Core Answer
Statelessness means the server **does not remember anything** about the client between requests. Every single request must include all the data needed to process it (like a JWT token for auth). This is important because it makes the server much easier to **Scale**—if you have 10 servers, the client can talk to any of them and get the same result without the servers needing to share session data.

---

#### 🔑 Key Technical Terms Used
*   **Client State:** Data stored on the user's phone/browser.
*   **Server State:** Data stored in the server's memory (Avoided in REST).

---

#### 📖 Detailed Explanation
Imagine a **Drive-Thru vs. A Sit-down Restaurant**.
*   **Stateful (Sit-down)**: You sit at a table. The waiter remembers you. You can say "I'll have another one of those" and he knows what you mean because he has the "State" of your table.
*   **Stateless (Drive-Thru)**: Every time you pull up to the speaker, you must say your **Full Order**. Even if you just drove around the building, the worker doesn't remember you. This is "Stateless."
Because it's stateless, the Drive-Thru can handle 100 cars a minute much more easily than a sit-down restaurant.

---

#### 🧠 One Line to Remember
Statelessness means the server treats every request as brand new, making it faster and easier to scale.

---

### Q9. What is API versioning and what are the different strategies?

---

#### ✅ The Core Answer
API versioning is the process of managing changes to an API without breaking existing apps that use it.
Strategies:
1. **URL Versioning**: Putting the version in the path (e.g., api/v1/users). **(Most Common)**.
2. **Header Versioning**: Using a custom header (e.g., X-API-Version: 2).
3. **Query Versioning**: Using a parameter (e.g., /users?v=2).

---

#### 🔑 Key Technical Terms Used
*   **Backward Compatibility:** Ensuring old versions of an app still work with the new server.
*   **Breaking Change:** A change that stops old apps from working (e.g., deleting a field).

---

#### 📖 Detailed Explanation
Imagine a **Phone Charger**.
*   **v1**: The old fat charger (Micro-USB).
*   **v2**: The new fast charger (USB-C).
If a company suddenly stopped making the old chargers, millions of people with old phones would be angry.
In software, we keep both versions running. The old phone uses the v1 endpoint, and the new phone uses the v2 endpoint. Eventually, after many years, we might retire v1, but only after giving everyone a long time to upgrade.

---

#### 🧠 One Line to Remember
Versioning ensures that when you upgrade your server, you don't break older versions of your app.

---

### Q10. What is the difference between REST and GraphQL?

---

#### ✅ The Core Answer
*   **REST**: You have many endpoints (URLs) for different data. The server decides what data to send you. You often get "Over-fetching" (too much data) or "Under-fetching" (not enough).
*   **GraphQL**: You have **one single endpoint**. The client sends a "Query" telling the server **exactly** which fields it needs. You get exactly what you ask for, and nothing more.

---

#### 🔑 Key Technical Terms Used
*   **Over-fetching:** Getting 50 fields when you only needed 2.
*   **Single Endpoint:** GraphQL usually lives at just /graphql.

---

#### 📖 Detailed Explanation
Imagine **Ordering Food**.
*   **REST**: It's like a **Set Menu**. If you order "Breakfast," you get Eggs, Toast, and Coffee. Even if you hate coffee, it's on the plate. If you also wanted a cookie, you have to place a separate order (another API call).
*   **GraphQL**: It's like a **Custom Buffet**. You walk up with a plate and say "I want exactly 2 eggs and 1 piece of toast." You get exactly that. No coffee, no waste, and you got everything in one trip.

---

#### 💻 Comparison Table
| Feature | REST | GraphQL |
| :--- | :--- | :--- |
| **Endpoints** | Many (e.g., /users, /posts) | One (e.g., /graphql) |
| **Data Control** | Server decides | Client decides |
| **Performance** | Can be slow (Over-fetching) | Very efficient |

---

#### 🧠 One Line to Remember
REST uses many fixed URLs; GraphQL uses one URL and lets you ask for exactly what you need.

---

## 🍃 Module 10: MongoDB & Mongoose

### Q1. What is MongoDB and how is it different from a relational database?

---

#### ✅ The Core Answer
MongoDB is a **NoSQL, document-oriented database**. Unlike relational databases (SQL) that use tables and rows, MongoDB stores data in **flexible, JSON-like documents** (BSON). It is "Schema-less," meaning you can store different fields in documents within the same collection, allowing for faster development and easier horizontal scaling.

---

#### 🔑 Key Technical Terms Used
*   **NoSQL:** A database that does not use the traditional table/row/SQL model.
*   **Document-Oriented:** Data is stored as individual objects (documents) instead of rows.
*   **Horizontal Scaling:** Adding more servers to handle load, rather than just making one server bigger.

---

#### 📖 Detailed Explanation
Imagine a **Filing Cabinet**.
*   **SQL (Relational)**: This is like a **Strict Ledger Book**. Every page must have exactly 5 columns. If you want to add a "Phone Number" for one person, you have to redraw the *entire* book for everyone.
*   **MongoDB (NoSQL)**: This is like a **Folder of Sheets**. Each person has their own sheet. One sheet might have a Name and Age; another might have a Name and 10 Phone Numbers. You just drop the sheets into the folder.

---

#### 🧠 One Line to Remember
MongoDB is a flexible database that stores data in JSON-like documents instead of rigid tables.

---
"""

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(new_content)

print("Rest of Module 9 and start of Module 10 appended.")
