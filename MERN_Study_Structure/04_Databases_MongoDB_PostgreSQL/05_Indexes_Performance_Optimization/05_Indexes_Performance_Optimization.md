# Indexes & Performance Optimization

## 📚 Curriculum Checklist
- [x] Creating Indexes (CREATE INDEX)
- [x] Understanding Query Execution Plans (EXPLAIN ANALYZE)
- [x] Normalization vs. Denormalization

## 📝 Detailed Notes

### 1. Indexing (CREATE INDEX)
Indexes are used to speed up the retrieval of data from a database.
- **B-Tree Index**: The default and most common index type in Postgres.
- **Unique Index**: Ensures all values in the indexed column are unique.
```sql
CREATE INDEX idx_user_email ON users(email);
```

### 2. Query Execution Plans (EXPLAIN ANALYZE)
The `EXPLAIN` command shows the execution plan that the PostgreSQL planner generates for the supplied statement. `ANALYZE` actually executes the query and shows real timing.
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@test.com';
```
Look for:
- **Seq Scan**: Sequential scan (Slow for large tables).
- **Index Scan**: Using an index (Fast).

### 3. Normalization vs. Denormalization
- **Normalization**: The process of organizing data to reduce redundancy (e.g., 1NF, 2NF, 3NF). Good for write-heavy apps.
- **Denormalization**: The process of adding redundant data to speed up reads (e.g., storing `post_count` in the `users` table). Good for read-heavy apps.

### 4. Database Caching
Using tools like **Redis** to store frequently accessed data in memory to avoid hitting the database.

---

## 🎓 Important Interview Questions

### Q1: When should you NOT create an index?
1. On very small tables (Seq scan is faster).
2. On columns with low cardinality (e.g., a "Gender" column with only 2 values).
3. On columns that are frequently updated (Index updates add overhead to writes).

### Q2: What is the difference between `EXPLAIN` and `EXPLAIN ANALYZE`?
- `EXPLAIN` only shows the **estimated** plan without running the query.
- `EXPLAIN ANALYZE` **runs** the query and shows the actual execution time and rows processed.

### Q3: Explain "Third Normal Form" (3NF).
A table is in 3NF if:
1. It is in 2NF.
2. It has no **transitive dependencies** (i.e., non-key columns should depend only on the primary key, not on other non-key columns).

### Q4: What is "Database Sharding"?
Sharding is a method for distributing a single dataset across multiple databases, which can then be stored on multiple nodes. This is a form of horizontal scaling.

### Q5: What is a "Composite Index"?
An index created on multiple columns. The order of columns matters; a composite index on `(last_name, first_name)` can speed up queries on `last_name` alone or `last_name` + `first_name`, but NOT on `first_name` alone.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Types of Joins](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/04_Types_of_Joins/04_Types_of_Joins.md) | [🏠 Home](../../README.md) | [Next: Transactions Advanced Queries ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/06_Transactions_Advanced_Queries/06_Transactions_Advanced_Queries.md)
