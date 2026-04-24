# CRUD Operations:

## 📚 Curriculum Checklist
- [x] SELECT, INSERT, UPDATE, DELETE
- [x] Filtering Data (WHERE, LIKE, IN, BETWEEN)
- [x] Sorting & Limiting (ORDER BY, LIMIT, OFFSET)

## 📝 Detailed Notes

### 1. CREATE (INSERT)
Used to add new rows to a table.
```sql
INSERT INTO users (username, email) VALUES ('aniket', 'aniket@example.com');
```

### 2. READ (SELECT)
Used to retrieve data.
- **Select All**: `SELECT * FROM users;`
- **Select Specific Columns**: `SELECT username, email FROM users;`
- **Filtering**: `SELECT * FROM users WHERE age > 18;`

### 3. UPDATE
Used to modify existing data. **Always use a WHERE clause** to avoid updating all rows.
```sql
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
```

### 4. DELETE
Used to remove rows. **Always use a WHERE clause**.
```sql
DELETE FROM users WHERE id = 1;
```

### 5. UPSERT (INSERT ... ON CONFLICT)
A combination of INSERT and UPDATE. If the row exists (based on a unique constraint), update it; otherwise, insert.
```sql
INSERT INTO users (id, username) VALUES (1, 'aniket')
ON CONFLICT (id) DO UPDATE SET username = EXCLUDED.username;
```

### 5. Filtering Data (WHERE, LIKE, IN)
- **Exact Match**: `WHERE name = 'John'`
- **Pattern Match**: `WHERE name LIKE 'J%'` (Names starting with J)
- **List Match**: `WHERE role IN ('Admin', 'Editor')`
- **Range Match**: `WHERE age BETWEEN 20 AND 30`

### 6. Sorting & Limiting
- **Sorting**: `SELECT * FROM users ORDER BY created_at DESC;`
- **Limiting**: `SELECT * FROM users LIMIT 10 OFFSET 20;` (Skip first 20, show next 10)

---

## 🎓 Important Interview Questions

### Q1: What is the difference between `DELETE` and `TRUNCATE`?
- **DELETE**: A DML command. It can have a `WHERE` clause. It deletes rows one by one and logs each deletion. It is slower but can be rolled back.
- **TRUNCATE**: A DDL command. It removes all rows from a table. It is much faster because it deallocates the data pages instead of deleting rows. It cannot be rolled back in some databases and doesn't trigger "On Delete" triggers.

### Q2: What does the `LIKE` operator do in SQL?
It is used in a `WHERE` clause to search for a specified pattern in a column.
- `%`: Represents zero, one, or multiple characters.
- `_`: Represents a single character.

### Q3: How do you implement "Pagination" in SQL?
Using `LIMIT` (how many items per page) and `OFFSET` (how many items to skip).
`SELECT * FROM products LIMIT 10 OFFSET (page_number - 1) * 10;`

### Q4: Explain the difference between `WHERE` and `HAVING`.
- **WHERE**: Used to filter rows **before** any groupings are made.
- **HAVING**: Used to filter groups **after** the `GROUP BY` clause has been applied.

### Q5: What is a "Null" value in SQL?
`NULL` represents a missing or unknown value. It is not the same as zero or an empty string. You check for it using `IS NULL` or `IS NOT NULL`.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: PostgreSQL](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/02_PostgreSQL/02_PostgreSQL.md) | [🏠 Home](../../README.md) | [Next: Types of Joins ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/04_Types_of_Joins/04_Types_of_Joins.md)
