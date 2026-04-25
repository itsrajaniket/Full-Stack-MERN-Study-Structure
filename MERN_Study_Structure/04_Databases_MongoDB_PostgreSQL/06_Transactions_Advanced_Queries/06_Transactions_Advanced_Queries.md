# Transactions & Advanced Queries
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] ACID Properties
- [x] Transactions (BEGIN, COMMIT, ROLLBACK)
- [x] Common Table Expressions (CTEs)
- [x] Window Functions (ROW_NUMBER(), RANK(), DENSE_RANK(), etc.)

## 📝 Detailed Notes

### 1. Transactions (ACID)
A transaction is a single unit of work. If a transaction is successful, all of the data modifications made during the transaction are committed.
- **BEGIN**: Starts a transaction.
- **COMMIT**: Saves the changes.
- **ROLLBACK**: Undoes the changes if an error occurs.
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### 2. Common Table Expressions (CTEs)
A CTE is a temporary result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement. It makes complex queries more readable.
```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) AS total_sales
    FROM orders
    GROUP BY region
)
SELECT * FROM regional_sales WHERE total_sales > 10000;
```

### 3. Window Functions
Window functions perform a calculation across a set of table rows that are somehow related to the current row.
- **ROW_NUMBER()**: Assigns a unique number to each row.
- **RANK()**: Assigns a rank to each row (with gaps).
- **DENSE_RANK()**: Assigns a rank to each row (without gaps).
```sql
SELECT name, salary, 
       RANK() OVER (ORDER BY salary DESC) as salary_rank
FROM employees;
```

---

## 🎓 Important Interview Questions

### Q1: What are the ACID properties in a database?
- **Atomicity**: All or nothing.
- **Consistency**: Database goes from one valid state to another.
- **Isolation**: Transactions don't see each other's intermediate states.
- **Durability**: Committed data is permanent.

### Q2: What is the benefit of using a CTE?
1. **Readability**: It breaks down large queries into smaller, named blocks.
2. **Recursion**: CTEs can be recursive, which is useful for querying hierarchical data like organizational charts or bill of materials.

### Q3: Difference between `RANK()` and `DENSE_RANK()`?
- `RANK()`: If two rows have the same value, they get the same rank, and the next rank is skipped (e.g., 1, 2, 2, 4).
- `DENSE_RANK()`: If two rows have the same value, they get the same rank, and the next rank is **not** skipped (e.g., 1, 2, 2, 3).

### Q4: What is a "Deadlock"?
A deadlock happens when two or more transactions are waiting for each other to release locks on resources. Database engines usually detect this and abort one of the transactions.

### Q5: Explain the `OVER()` clause in Window Functions.
The `OVER()` clause defines the "window" or set of rows the function should operate on. It can contain `PARTITION BY` (to group rows) and `ORDER BY` (to sort rows within the window).


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Indexes Performance Optimization](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/05_Indexes_Performance_Optimization/05_Indexes_Performance_Optimization.md) | [🏠 Home](../../README.md) | [Next: PostgreSQL Advanced Topics ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/07_PostgreSQL_Advanced_Topics/07_PostgreSQL_Advanced_Topics.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>