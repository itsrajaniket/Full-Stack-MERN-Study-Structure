# MongoDB (NoSQL Database)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Introduction to NoSQL & MongoDB
- [x] [MongoDB](https://www.mongodb.com/docs/manual/) Installation & Setup
- [x] JSON & BSON Basics
- [x] Connecting MongoDB with Node.js (Mongoose/NestJS TypeORM)
- [x] Creating Databases & Collections
- [x] Insert Operations: insertOne(), insertMany()
- [x] Read Operations: find(), findOne(), Query Operators ($eq, $gt, $lt, $in, $regex, etc.)
- [x] Update Operations: updateOne(), updateMany(), $set, $push, $pull
- [x] Delete Operations: deleteOne(), deleteMany()
- [x] Indexing (createIndex())
- [x] Compound Indexes
- [x] Aggregation Framework ($match, $group, $lookup, $sort, $project)
- [x] Relationships in MongoDB
- [x] One-to-One, One-to-Many, Many-to-Many
- [x] Embedding vs. Referencing ($lookup for Joins)
- [x] Transactions in MongoDB
- [x] Schema Validation
- [x] [MongoDB](https://www.mongodb.com/docs/manual/) Atlas (Cloud Database)
- [x] Replication & Sharding (Basic Understanding)
- [x] Security Best Practices

## 📝 Detailed Notes

### 1. Introduction to NoSQL & MongoDB
MongoDB is a **Document-oriented NoSQL database**. Unlike relational databases (SQL) that use tables and rows, MongoDB uses **Collections** and **Documents**.
- **JSON & BSON**: MongoDB stores data in BSON (Binary JSON) format, which supports more data types (like `Date` and `BinData`) than standard JSON.

### 2. Mongoose (Node.js ODM)
Mongoose provides a straight-forward, schema-based solution to model your application data.
```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true },
  age: Number
});
const User = mongoose.model('User', userSchema);
```

### 3. CRUD Operations
- **Create**: `db.collection.insertOne({ name: "Aniket" })`
- **Read**: `db.collection.find({ age: { $gt: 18 } })`
- **Update**: `db.collection.updateOne({ _id: id }, { $set: { active: true } })`
- **Delete**: `db.collection.deleteOne({ _id: id })`

### 4. Indexing for Performance
Indexes support the efficient execution of queries in MongoDB. Without indexes, MongoDB must perform a **collection scan**.
- **Single Field**: `db.collection.createIndex({ name: 1 })`
- **Compound**: `db.collection.createIndex({ status: 1, date: -1 })`

### 5. Aggregation Framework
The aggregation framework is a powerful tool for data analysis, similar to SQL's `GROUP BY` and `JOIN`.
```javascript
db.orders.aggregate([
  { $match: { status: "A" } },
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);
```

### 6. Relationships: Embedding vs. Referencing
- **Embedding**: Storing related data in a single document (Faster reads, restricted size).
- **Referencing**: Storing data in separate collections and linking them via `_id` (Flexible, but requires `$lookup` for joins).

---

## 🎓 Important Interview Questions

### Q1: Difference between SQL and NoSQL?
- **SQL**: Relational, fixed schema, table-based, vertically scalable, ACID compliant.
- **NoSQL**: Non-relational, dynamic schema, document-based, horizontally scalable, follows BASE (Basically Available, Soft state, Eventual consistency).

### Q2: What is the "Aggregation Pipeline"?
It is a framework for data transformation. It consists of multiple stages (like `$match`, `$group`, `$sort`) where the output of one stage serves as the input to the next.

### 6. MongoDB Change Streams
Change streams allow applications to access real-time data changes without the complexity and risk of tailing the oplog.
```javascript
const collection = db.collection('orders');
const changeStream = collection.watch();
changeStream.on('change', next => {
  console.log(next); // Trigger real-time notification
});
```

### 7. Capped Collections
Fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order (useful for logging).

### Q3: When should you use "Embedding" over "Referencing"?
- **Use Embedding**: When the data is frequently read together and the child data doesn't grow indefinitely (e.g., Address of a User).
- **Use Referencing**: When the data is large, shared across documents, or updated frequently (e.g., Authors of a Book).

### Q4: What is an "Index" and why is it important?
An index is a special data structure that stores a small portion of the collection's data set in a traversable form. It drastically improves query performance by allowing MongoDB to find documents without scanning every single one.

### Q5: What are "Transactions" in MongoDB?
Starting from version 4.0, MongoDB supports multi-document ACID transactions. They allow you to ensure that multiple operations either all succeed or all fail together, which is crucial for financial or sensitive data.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Advanced Topics](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/09_Advanced_Topics/09_Advanced_Topics.md) | [🏠 Home](../../README.md) | [Next: PostgreSQL ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/02_PostgreSQL/02_PostgreSQL.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>