# Types of Joins:

## 📚 Curriculum Checklist
- [ ] INNER JOIN
- [ ] LEFT JOIN, RIGHT JOIN
- [ ] FULL JOIN
- [ ] Foreign Keys & Constraints
- [ ] One-to-One, One-to-Many, Many-to-Many Relationships

## 📝 Detailed Notes

### 1. What is a JOIN?
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.

### 2. Types of Joins
- **INNER JOIN**: Returns records that have matching values in both tables.
- **LEFT (OUTER) JOIN**: Returns all records from the left table, and the matched records from the right table. If no match, the result is NULL on the right side.
- **RIGHT (OUTER) JOIN**: Returns all records from the right table, and the matched records from the left table.
- **FULL (OUTER) JOIN**: Returns all records when there is a match in either left or right table.

```sql
-- Example: Get all users and their posts
SELECT users.username, posts.title
FROM users
INNER JOIN posts ON users.id = posts.user_id;
```

### 3. Relationships in SQL
- **One-to-One**: A row in Table A is linked to only one row in Table B (e.g., User and UserProfile).
- **One-to-Many**: A row in Table A can be linked to multiple rows in Table B (e.g., User and Posts).
- **Many-to-Many**: Rows in Table A can be linked to multiple rows in Table B and vice-versa. Requires a **Junction Table** (e.g., Students and Courses).

### 4. Constraints
- **NOT NULL**: Cannot have a NULL value.
- **UNIQUE**: All values must be different.
- **PRIMARY KEY**: Uniquely identifies each row.
- **FOREIGN KEY**: Prevents actions that would destroy links between tables.
- **CHECK**: Ensures the value satisfies a specific condition.

---

## 🎓 Important Interview Questions

### Q1: What is the difference between `INNER JOIN` and `LEFT JOIN`?
- **INNER JOIN** only returns rows where there is a match in **both** tables.
- **LEFT JOIN** returns **all** rows from the left table, even if there are no matches in the right table (right side columns will be NULL).

### Q2: How do you implement a Many-to-Many relationship?
By creating a third table, often called a **Junction Table** or **Join Table**, which contains the Foreign Keys of both related tables.
*Example: `student_courses` table with `student_id` and `course_id`.*

### Q3: What is a "Self-Join"?
A self-join is a regular join, but the table is joined with itself. This is useful for hierarchical data, such as an `employees` table where an `employee_id` is linked to a `manager_id` in the same table.

### Q4: Explain the `ON` vs `USING` clause in Joins.
- **ON**: Used to specify the join condition when the column names are different (e.g., `ON a.id = b.user_id`).
- **USING**: A shorthand used when the column names are identical in both tables (e.g., `USING (user_id)`).

### Q5: What is a "Cross Join"?
A Cross Join returns the Cartesian product of the two tables—it combines every row of the first table with every row of the second table. It does not require a join condition.


## ❓ Questions & Doubts
- [ ]

---

[⬅️ Previous: CRUD Operations](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/03_CRUD_Operations/03_CRUD_Operations.md) | [🏠 Home](../../README.md) | [Next: Indexes Performance Optimization ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/05_Indexes_Performance_Optimization/05_Indexes_Performance_Optimization.md)