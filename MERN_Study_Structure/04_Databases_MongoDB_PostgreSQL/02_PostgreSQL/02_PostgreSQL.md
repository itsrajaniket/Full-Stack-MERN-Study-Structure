# PostgreSQL (Relational Database)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Introduction to SQL & PostgreSQL
- [x] [PostgreSQL](https://www.postgresql.org/docs/) Installation & Setup
- [x] Data Types in PostgreSQL (INT, VARCHAR, TEXT, JSON, etc.)
- [x] Connecting PostgreSQL with Node.js (pg, Prisma, TypeORM)

## 📝 Detailed Notes

### 1. Introduction to SQL & PostgreSQL
PostgreSQL (Postgres) is an **Open-Source Relational Database Management System (RDBMS)**. It uses **SQL (Structured Query Language)** for defining and manipulating data.
- **Tables & Rows**: Data is stored in tables with a fixed schema.
- **ACID Compliance**: Postgres is strictly ACID compliant (Atomicity, Consistency, Isolation, Durability), making it ideal for financial data.

### 2. Data Types
- **INT / SERIAL**: Numbers and auto-incrementing IDs.
- **VARCHAR(n) / TEXT**: Short strings and long text.
- **BOOLEAN**: True/False.
- **TIMESTAMP**: Date and time.
- **JSON / JSONB**: Postgres supports JSON natively. `JSONB` is the binary version which is faster to query and supports indexing.

### 3. Connecting to Node.js
- **pg**: The low-level driver for Postgres.
- **Prisma / TypeORM**: High-level ORMs that provide type-safety and easier query syntax.

### 4. Basic Table Creation
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎓 Important Interview Questions

### Q1: What makes PostgreSQL "Advanced" compared to MySQL?
Postgres is known for its **extensibility**, support for advanced data types (like arrays and JSONB), and strict adherence to SQL standards. It also handles complex analytical queries and high-concurrency write operations better than MySQL in many scenarios.

### Q2: What is "ACID" in databases?
- **Atomicity**: All operations in a transaction succeed, or none do.
- **Consistency**: The database remains in a valid state after a transaction.
- **Isolation**: Concurrent transactions don't interfere with each other.
- **Durability**: Once a transaction is committed, it remains even after a system failure.

### Q3: What is the difference between `JSON` and `JSONB` in Postgres?
- **JSON**: Stores an exact copy of the input text. Fast to insert, but slow to query as it needs to be parsed every time.
- **JSONB**: Stores data in a decomposed binary format. Slightly slower to insert, but **much faster to query** and supports indexing.

### Q4: Explain the purpose of a "Primary Key" and a "Foreign Key".
- **Primary Key**: A unique identifier for every row in a table.
- **Foreign Key**: A column that creates a link between data in two tables, ensuring **Referential Integrity**.

### Q5: What is a "Unique Constraint"?
A rule that ensures all values in a column (or a set of columns) are distinct from each other (e.g., Email addresses in a User table).


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: MongoDB](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/01_MongoDB/01_MongoDB.md) | [🏠 Home](../../README.md) | [Next: CRUD Operations ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/03_CRUD_Operations/03_CRUD_Operations.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>