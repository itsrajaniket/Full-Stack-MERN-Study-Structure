import os

file_path = r"c:\Users\ANIKET\Desktop\MERN QNA\MERN_Interview_Study_Kit.md"

new_content = """### Q2. What is the difference between a document and a collection in MongoDB?

---

#### ✅ The Core Answer
*   **Document**: The basic unit of data in MongoDB (equivalent to a **Row** in SQL). It is a set of key-value pairs.
*   **Collection**: A group of MongoDB documents (equivalent to a **Table** in SQL). A collection lives inside a database.

---

#### 🔑 Key Technical Terms Used
*   **Key-Value Pair:** Data stored as '"name": "Aniket"'.
*   **BSON:** The binary format MongoDB uses to store documents.

---

#### 📖 Detailed Explanation
Think of a **College Library**.
*   **The Database**: The Library building.
*   **A Collection**: A **Bookshelf** (e.g., the "Computer Science" shelf).
*   **A Document**: An **Individual Book** on that shelf.
Each book has its own info, but they are all grouped together on the shelf because they are related.

---

#### 🧠 One Line to Remember
A document is a single data entry; a collection is a group of those entries.

---

### Q3. What is BSON and how is it different from JSON?

---

#### ✅ The Core Answer
BSON stands for **Binary JSON**. While JSON is a text-based format that humans can read easily, BSON is a **binary representation** of that data. MongoDB uses BSON because it is faster for the computer to search and parse, and it supports more data types like **Dates and Binary data** that regular JSON cannot handle.

---

#### 🔑 Key Technical Terms Used
*   **Serialization:** Converting an object into a format that can be stored or transmitted.
*   **Parsing:** Reading data and turning it back into a usable object.

---

#### 📖 Detailed Explanation
Imagine **Writing a Letter vs. Sending a Zip File**.
*   **JSON**: Like a hand-written letter. Anyone can read it, but it takes up more space and is slower to process.
*   **BSON**: Like a compressed zip file. A human can't read it directly, but a computer can "unzip" and read it much faster, and you can include things inside the zip (like photos/Dates) that are hard to represent in a plain letter.

---

#### 🧠 One Line to Remember
BSON is a faster, more powerful binary version of JSON used by MongoDB internally.

---

### Q4. What is the difference between insertOne and insertMany?

---

#### ✅ The Core Answer
*   **insertOne()**: Adds a **single document** to a collection. Returns the `_id` of the new document.
*   **insertMany()**: Adds an **array of documents** in a single request. It is much more efficient than calling `insertOne` multiple times because it reduces the number of trips to the server.

---

#### 🔑 Key Technical Terms Used
*   **Network Overhead:** The time wasted sending many small messages instead of one big one.
*   **Atomicity:** In `insertMany`, if one document fails, you can choose if the others should still be saved.

---

#### 📖 Detailed Explanation
Think of **Carrying Groceries**.
*   **insertOne**: You take one bag from the car to the kitchen, then go back for the next bag. It takes a lot of time and walking.
*   **insertMany**: You put all 10 bags in a **cart** and push them all to the kitchen at once. One trip, much faster.

---

#### 🧠 One Line to Remember
insertOne is for one item; insertMany is for adding a list of items quickly.

---

### Q5. What is the difference between find and findOne?

---

#### ✅ The Core Answer
*   **find()**: Returns a **Cursor** (a pointer to a list) of all documents that match the query. If nothing is found, it returns an empty list.
*   **findOne()**: Returns the **very first** document that matches the query. It returns a single object or `null` if nothing is found.

---

#### 🔑 Key Technical Terms Used
*   **Cursor:** A way to iterate through large amounts of data without loading everything into memory at once.
*   **Query Criteria:** The filter you use (e.g., '{ "age": 25 }').

---

#### 📖 Detailed Explanation
Imagine searching for a **Blue Pen** in a drawer.
*   **find**: You take out **every blue pen** you can find and put them in a pile on the desk.
*   **findOne**: You reach in, grab the **first blue pen** your hand touches, and stop immediately. You don't care if there are 10 more pens in there.

---

#### 🧠 One Line to Remember
find gives you a list of all matches; findOne gives you only the first match.

---

### Q6. What are update operators like $set, $unset, $inc, $push, and $pull?

---

#### ✅ The Core Answer
Update operators are special keywords used to modify specific parts of a document without replacing the whole thing:
*   **$set**: Sets the value of a field.
*   **$unset**: Removes a field.
*   **$inc**: Increases a number (e.g., increments views by 1).
*   **$push**: Adds an item to an array.
*   **$pull**: Removes an item from an array.

---

#### 🔑 Key Technical Terms Used
*   **Atomic Update:** An update that happens in one step, ensuring data doesn't get corrupted.
*   **Modifier:** Another name for these operators.

---

#### 📖 Detailed Explanation
Think of an **Employee File**.
*   **$set**: Updating their **Address**.
*   **$inc**: Giving them a **Salary Raise** (Add 5000 to the current value).
*   **$push**: Adding a **New Certificate** to their list of achievements.
Without these, you would have to download the whole file, change it in JavaScript, and upload the whole thing back, which is slow and risky.

---

#### 🧠 One Line to Remember
Update operators allow you to change specific fields in a document quickly and safely.

---

### Q7. What is the difference between updateOne, updateMany, and replaceOne?

---

#### ✅ The Core Answer
*   **updateOne()**: Updates the **first** document that matches the filter.
*   **updateMany()**: Updates **all** documents that match the filter (e.g., update "status" to "inactive" for all old users).
*   **replaceOne()**: Deletes the old document and puts a **completely new document** in its place (keeping the same `_id`). It does not use update operators like `$set`.

---

#### 🔑 Key Technical Terms Used
*   **Filter:** The "Where" clause (e.g., '{ "isAdmin": true }').
*   **Overwriting:** What happens in `replaceOne` if you aren't careful.

---

#### 📖 Detailed Explanation
Imagine **Renovating a House**.
*   **updateOne**: You paint the **Front Door** of the first house on the street.
*   **updateMany**: You paint the **Front Doors** of every house on the street.
*   **replaceOne**: You **Tear down the house** and build a brand new one on the same plot of land.

---

#### 🧠 One Line to Remember
updateOne fixes one item; updateMany fixes a group; replaceOne swaps the whole item for a new one.

---

### Q8. What is the upsert option in MongoDB?

---

#### ✅ The Core Answer
**Upsert** is a combination of **Update + Insert**. If you set `upsert: true` in an update command:
1. If a document matches your filter, it **Updates** it.
2. If **no** document matches, it **Inserts** a brand new document using the data you provided.

---

#### 🔑 Key Technical Terms Used
*   **Conditional Logic:** The database makes a decision ("Does it exist?") for you.
*   **Idempotency:** You can run the same command many times without creating duplicates.

---

#### 📖 Detailed Explanation
Think of **Attendance in a Class**.
The teacher has a list of students.
*   **With Upsert**: The teacher calls a name. If the student is there, she marks "Present" (Update). If the student's name isn't on the list, she **adds their name** to the bottom and then marks "Present" (Insert).
It ensures that by the end of the day, that student is on the list no matter what.

---

#### 🧠 One Line to Remember
Upsert updates a document if it exists, or creates it if it doesn't.

---

### Q9. What is the ObjectId in MongoDB?

---

#### ✅ The Core Answer
An `ObjectId` is a **unique 12-byte identifier** automatically generated by MongoDB for every document (stored in the `_id` field). It is designed to be unique across different machines and time. It consists of a **Timestamp**, a Machine ID, a Process ID, and a random counter.

---

#### 🔑 Key Technical Terms Used
*   **Primary Key:** The unique ID used to find a specific document.
*   **Hexadecimal:** The 24-character string representation (e.g., '507f1f77...').

---

#### 📖 Detailed Explanation
Imagine a **Global Tracking Number** for a package.
Even if 10 different people in 10 different cities ship a package at the exact same second, the tracking numbers will be different because they include the **City Code** (Machine ID) and a **Random Serial Number**.
Because the ID starts with a **Timestamp**, documents are naturally sorted by the time they were created!

---

#### 🧠 One Line to Remember
`ObjectId` is a unique, time-stamped "fingerprint" for every document in MongoDB.

---

### Q10. What is the difference between embedded documents and referenced documents?

---

#### ✅ The Core Answer
*   **Embedded (Denormalized)**: Related data is stored **inside** the parent document (e.g., an array of addresses inside a User).
*   **Referenced (Normalized)**: Only an **ID** is stored in the parent document, and the actual data lives in a different collection. You use `populate()` to link them.

---

#### 🔑 Key Technical Terms Used
*   **Normalization:** Splitting data into many small tables/collections.
*   **Data Consistency:** The risk that if you change an address in one place, it doesn't update everywhere (a problem in Embedded).

---

#### 📖 Detailed Explanation
*   **Embedded**: Like your **Passport**. Your name, photo, and stamps are all inside one book. When you show the book, everything is there.
*   **Referenced**: Like a **Library Card**. The card doesn't have the books inside it; it just has an **ID**. To see the books, the librarian has to look up that ID in a different system.

---

#### 🧠 One Line to Remember
Embed for data that always goes together; Reference for data that is shared or very large.

---
"""

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(new_content)

print("MongoDB Module Part 1 appended.")
