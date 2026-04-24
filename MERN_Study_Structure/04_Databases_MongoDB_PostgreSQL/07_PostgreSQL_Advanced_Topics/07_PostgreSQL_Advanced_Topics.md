# PostgreSQL Advanced Topics

## 📚 Curriculum Checklist
- [x] Stored Procedures & Functions
- [x] Triggers & Event Listeners
- [x] Full-Text Search in PostgreSQL
- [x] JSON & JSONB Data Handling
- [x] [PostgreSQL](https://www.postgresql.org/docs/) with Prisma ORM / TypeORM

## 📝 Detailed Notes

### 1. Stored Procedures & Functions
- **Functions**: Usually return a value and are used in SELECT statements.
- **Procedures**: Used for complex operations, can handle transactions (COMMIT/ROLLBACK), and don't necessarily return a value.
```sql
CREATE OR REPLACE FUNCTION get_user_count() RETURNS integer AS $$
BEGIN
    RETURN (SELECT COUNT(*) FROM users);
END;
$$ LANGUAGE plpgsql;
```

### 2. Triggers
Triggers are functions that automatically run when an event (INSERT, UPDATE, DELETE) occurs on a table.
- **Use case**: Automatically updating a `last_modified` timestamp.

### 3. Full-Text Search (FTS)
Postgres has built-in support for searching natural language documents.
- **tsvector**: The document type optimized for search.
- **tsquery**: The search query.
```sql
SELECT title FROM posts WHERE to_tsvector(body) @@ to_tsquery('postgres & database');
```

### 4. Views & Materialized Views
- **View**: A virtual table based on the result-set of an SQL statement. It doesn't store data.
- **Materialized View**: Stores the result-set physically. Useful for complex, slow-running queries that don't need real-time data (needs to be refreshed manually).
```sql
CREATE MATERIALIZED VIEW sales_summary AS 
SELECT category, SUM(amount) FROM sales GROUP BY category;

REFRESH MATERIALIZED VIEW sales_summary;
```

### 4. JSON & JSONB handling
You can query into JSON columns using the `->` and `->>` operators.
```sql
SELECT data->>'name' FROM profiles WHERE data @> '{"city": "Mumbai"}';
```

---

## 🎓 Important Interview Questions

### Q1: What is a "Trigger" and when would you use one?
A trigger is a set of actions that run automatically when a specified database event occurs. Use cases include logging changes, enforcing complex business rules, or maintaining summary tables (e.g., updating a `total_sales` count in a `category` table whenever an `order` is placed).

### Q2: What is the difference between a Function and a Stored Procedure?
- **Function**: Must return a value. Can be used in a SELECT statement. Cannot manage transactions (no COMMIT/ROLLBACK).
- **Procedure**: Doesn't have to return a value. Can manage transactions. Is called using the `CALL` statement.

### Q3: Why use Full-Text Search in Postgres instead of a simple `LIKE %query%`?
1. **Performance**: FTS uses specialized indexes (`GIN` or `GiST`).
2. **Relevance**: FTS can rank results based on how well they match.
3. **Features**: FTS handles stemming (searching for "running" finds "run"), stop words, and complex boolean queries.

### Q4: What is the `JSONB` index type?
You can create a **GIN (Generalized Inverted Index)** on a JSONB column to make searching within the JSON structure extremely fast.

### Q5: How do you handle "Concurrency Control" in Postgres?
Postgres uses **MVCC (Multi-Version Concurrency Control)**. Instead of locking the database for every change, it keeps multiple versions of a row. Readers don't block writers, and writers don't block readers.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Transactions Advanced Queries](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/06_Transactions_Advanced_Queries/06_Transactions_Advanced_Queries.md) | [🏠 Home](../../README.md) | `🏁 End`
