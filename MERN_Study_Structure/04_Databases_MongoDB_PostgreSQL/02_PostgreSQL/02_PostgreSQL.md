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

## **PostgreSQL (Relational Database) — MERN Stack Interview Kit**

---

### **1\. Introduction to SQL & PostgreSQL**

---

**Q1. What is PostgreSQL and why is it used?** `[Fresher]`

* PostgreSQL — open-source, object-relational database management system (ORDBMS)  
* Developed at University of California Berkeley in 1986, one of the oldest and most reliable RDBMS  
* Known as Postgres — pronounced "post-gres-Q-L"  
* Fully ACID compliant — Atomicity, Consistency, Isolation, Durability guaranteed  
* Why PostgreSQL over other SQL databases:  
  * Fully open-source — no licensing costs unlike Oracle or SQL Server  
  * Standards compliant — closely follows SQL standard  
  * Extensible — custom data types, functions, operators, index types  
  * Advanced features — JSON support, full-text search, geospatial (PostGIS), arrays, ranges  
  * Better performance for complex queries than MySQL in many cases  
  * Strong community — active development, frequent releases  
  * Excellent support for concurrent reads and writes — MVCC  
* PostgreSQL vs MySQL:  
  * PostgreSQL — more feature-rich, better standards compliance, better for complex queries and analytics  
  * MySQL — simpler, widely used in web hosting, slightly faster for simple reads historically  
  * Both excellent choices — PostgreSQL preferred for complex applications, financial systems, geospatial  
* PostgreSQL in MERN context:  
  * Replaces MongoDB when relational data model is better suited  
  * Used with NestJS \+ TypeORM or Prisma  
  * Perfect for structured data with complex relationships  
  * Used when strong ACID guarantees required — financial, healthcare, e-commerce  
* Current stable version — PostgreSQL 16 (as of 2024\)  
* Popular managed services — AWS RDS, Google Cloud SQL, Supabase, Neon, Railway, Render

---

**Q2. What are the core SQL concepts every developer must know?** `[Fresher]`

* Database — container for all objects (tables, views, functions, sequences)  
* Schema — namespace within database, default is public, used to organize tables  
* Table — structured set of data in rows and columns  
* Row — single record in a table  
* Column — field with specific data type and constraints  
* Primary Key — unique identifier for each row, not null, automatically indexed  
* Foreign Key — column referencing primary key in another table, enforces referential integrity  
* Index — data structure speeding up data retrieval at cost of write performance  
* View — virtual table based on SELECT query, no data stored  
* Sequence — auto-incrementing number generator, used for primary keys  
* Constraint types:  
  * PRIMARY KEY — uniqueness \+ not null  
  * UNIQUE — no duplicate values, nulls allowed  
  * NOT NULL — value must be provided  
  * CHECK — custom condition must be true  
  * FOREIGN KEY — referential integrity between tables  
  * DEFAULT — value used when none provided  
* SQL command categories:  
  * DDL — Data Definition Language — CREATE, ALTER, DROP, TRUNCATE  
  * DML — Data Manipulation Language — SELECT, INSERT, UPDATE, DELETE  
  * DCL — Data Control Language — GRANT, REVOKE  
  * TCL — Transaction Control Language — BEGIN, COMMIT, ROLLBACK, SAVEPOINT  
* ACID properties in PostgreSQL:  
  * Atomicity — transaction is all or nothing  
  * Consistency — data always valid, constraints never violated  
  * Isolation — concurrent transactions behave as if sequential  
  * Durability — committed data survives system failures (WAL — Write-Ahead Log)

---

**Q3. What are the most important SQL queries every developer must know?** `[Fresher]`

* SELECT basics:  
  * SELECT \* FROM users — all columns, all rows  
  * SELECT id, name, email FROM users — specific columns  
  * SELECT DISTINCT role FROM users — unique values only  
  * SELECT name AS full\_name FROM users — column alias  
  * SELECT COUNT(\*), AVG(age), SUM(amount), MIN(price), MAX(price) FROM table — aggregate functions  
* Filtering with WHERE:  
  * WHERE age \> 18 AND active \= true  
  * WHERE role IN ('admin', 'moderator')  
  * WHERE name LIKE 'John%' — starts with John, case-sensitive  
  * WHERE name ILIKE '%john%' — contains john, case-insensitive (PostgreSQL specific)  
  * WHERE email IS NULL / IS NOT NULL  
  * WHERE age BETWEEN 18 AND 65  
  * WHERE created\_at \> NOW() \- INTERVAL '30 days'  
* Sorting and limiting:  
  * ORDER BY created\_at DESC, name ASC  
  * LIMIT 10 OFFSET 20 — pagination (page 3 with 10 per page)  
* Joins:  
  * INNER JOIN — only matching rows from both tables  
  * LEFT JOIN — all rows from left, matching from right, NULL if no match  
  * RIGHT JOIN — all rows from right, matching from left  
  * FULL OUTER JOIN — all rows from both, NULL where no match  
  * CROSS JOIN — cartesian product, every combination  
  * Self JOIN — join table with itself (hierarchy, manager-employee)  
* Grouping:  
  * GROUP BY department — group rows by department  
  * HAVING COUNT(\*) \> 5 — filter after grouping (WHERE filters before grouping)  
  * SELECT department, COUNT(*), AVG(salary) FROM employees GROUP BY department HAVING COUNT(*) \> 5  
* Subqueries:  
  * WHERE id IN (SELECT user\_id FROM orders WHERE total \> 1000\)  
  * SELECT *, (SELECT COUNT(*) FROM orders WHERE orders.user\_id \= users.id) AS order\_count FROM users  
  * FROM (SELECT ...) AS subquery — derived table  
* CTEs (Common Table Expressions):  
  * WITH active\_users AS (SELECT \* FROM users WHERE active \= true) SELECT \* FROM active\_users  
  * Recursive CTE — for tree structures, hierarchies  
  * Multiple CTEs — WITH cte1 AS (...), cte2 AS (...) SELECT ...  
* Window functions:  
  * ROW\_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC)  
  * RANK(), DENSE\_RANK(), NTILE()  
  * LAG(salary) OVER (...) — access previous row value  
  * LEAD(salary) OVER (...) — access next row value  
  * SUM(amount) OVER (PARTITION BY user\_id ORDER BY date) — running total

---

**Q4. What are database normalization and the normal forms?** `[1-2 yrs]`

* Normalization — process of organizing tables to reduce data redundancy and improve data integrity  
* Denormalization — intentionally introducing redundancy for query performance  
* First Normal Form (1NF):  
  * Each column contains atomic (indivisible) values  
  * No repeating groups or arrays in columns  
  * Each row uniquely identified by primary key  
  * Violation — storing phone1, phone2, phone3 as separate columns or comma-separated in one column  
  * Fix — separate phones table with user\_id foreign key  
* Second Normal Form (2NF):  
  * Must be in 1NF  
  * Every non-key attribute fully depends on entire primary key (no partial dependency)  
  * Relevant when table has composite primary key  
  * Violation — order\_items table with (order\_id, product\_id) as PK but product\_name depends only on product\_id  
  * Fix — separate products table, reference by product\_id  
* Third Normal Form (3NF):  
  * Must be in 2NF  
  * No transitive dependencies — non-key columns must depend only on primary key, not other non-key columns  
  * Violation — storing city and zip\_code in users table when city can be derived from zip\_code  
  * Fix — separate zip\_codes table with city information  
* Boyce-Codd Normal Form (BCNF) — stricter 3NF for edge cases with multiple candidate keys  
* When to denormalize:  
  * Read-heavy workloads where joins are too slow  
  * Reporting and analytics tables  
  * Caching frequently joined data  
  * Document stores like MongoDB are denormalized by design  
* Practical approach — normalize to 3NF, then selectively denormalize based on performance requirements

---

**Q5. How do transactions work in PostgreSQL?** `[1-2 yrs]`

* Transaction — unit of work that is atomic, either all succeeds or all rolled back  
* BEGIN — start transaction explicitly  
* COMMIT — save all changes permanently  
* ROLLBACK — undo all changes since BEGIN  
* Autocommit — PostgreSQL wraps each statement in implicit transaction if no explicit BEGIN  
* Savepoints — partial rollback within transaction:  
  * SAVEPOINT savepoint\_name — mark point in transaction  
  * ROLLBACK TO SAVEPOINT name — undo back to savepoint without aborting entire transaction  
  * RELEASE SAVEPOINT name — remove savepoint  
* Isolation levels — control how transactions see changes made by concurrent transactions:  
  * READ UNCOMMITTED — can read dirty (uncommitted) data — PostgreSQL treats same as READ COMMITTED  
  * READ COMMITTED — default in PostgreSQL — only see committed data, but different SELECT in same transaction may see different data if others commit in between  
  * REPEATABLE READ — same SELECT always returns same data within transaction, prevents non-repeatable reads  
  * SERIALIZABLE — strongest isolation, transactions appear to run one after another, prevents all anomalies  
* Concurrency problems:  
  * Dirty read — reading uncommitted data from another transaction  
  * Non-repeatable read — same row returns different values in same transaction  
  * Phantom read — new rows appear in repeated range query within same transaction  
  * Lost update — two transactions read same row, both modify, one overwrites the other  
* SET TRANSACTION ISOLATION LEVEL SERIALIZABLE — set isolation for current transaction  
* Advisory locks — application-level locks for custom concurrency control  
* Row-level locking:  
  * SELECT ... FOR UPDATE — lock rows for update, other transactions wait  
  * SELECT ... FOR SHARE — allow others to also share lock but not update  
  * SELECT ... FOR UPDATE SKIP LOCKED — skip locked rows, useful for job queues

---

### **2\. Data Types in PostgreSQL**

---

**Q6. What are the data types available in PostgreSQL?** `[Fresher]`

* Numeric types:  
  * SMALLINT — 2 bytes, \-32768 to 32767  
  * INTEGER / INT — 4 bytes, \-2 billion to 2 billion  
  * BIGINT — 8 bytes, very large integers  
  * SERIAL / BIGSERIAL — auto-incrementing integer (shorthand for sequence \+ default)  
  * DECIMAL(precision, scale) / NUMERIC — exact decimal, use for money — no floating point errors  
  * REAL — 4 byte floating point, imprecise  
  * DOUBLE PRECISION / FLOAT8 — 8 byte floating point, imprecise  
  * MONEY — currency with locale-aware formatting (less portable, prefer NUMERIC)  
* String types:  
  * CHAR(n) — fixed length, padded with spaces  
  * VARCHAR(n) — variable length up to n characters  
  * TEXT — unlimited variable length string — no performance difference from VARCHAR in PostgreSQL  
  * PostgreSQL recommendation — use TEXT for unlimited strings, VARCHAR(n) only when length must be enforced  
* Boolean — BOOLEAN — true, false, null — accepts 'true', 'false', 'yes', 'no', '1', '0'  
* Date and time:  
  * DATE — date only, no time — YYYY-MM-DD  
  * TIME — time only, no date  
  * TIMESTAMP — date and time, no timezone  
  * TIMESTAMPTZ — date and time WITH timezone (stores UTC, displays in session timezone) — always prefer over TIMESTAMP  
  * INTERVAL — time duration — INTERVAL '2 hours 30 minutes'  
  * NOW() — current timestamp with timezone  
  * CURRENT\_DATE, CURRENT\_TIME, CURRENT\_TIMESTAMP  
* UUID — Universally Unique Identifier, 128-bit, excellent for distributed systems:  
  * gen\_random\_uuid() — generate UUID v4 (requires pgcrypto or built-in in v13+)  
  * Better than SERIAL for distributed systems — no coordination needed  
  * Slightly larger index than integer  
* JSON types — PostgreSQL-specific, very powerful:  
  * JSON — stores JSON as text, validates on insert, preserves whitespace and key order  
  * JSONB — stores JSON as binary, more efficient, supports indexes, does NOT preserve order  
  * Always prefer JSONB over JSON — better performance, indexing support  
  * JSONB operators — \-\>\> for text extraction, \-\> for JSON extraction, @\> contains, ? key exists  
  * GIN index on JSONB — index any key within JSONB column  
* Array types — PostgreSQL supports arrays of any type:  
  * INTEGER\[\], TEXT\[\], VARCHAR(50)\[\]  
  * ANY, ALL operators — WHERE 'admin' \= ANY(roles)  
  * array\_append, array\_remove, unnest functions  
  * GIN index for array containment queries  
* Network address types — INET (IP address), CIDR (network), MACADDR  
* Geometric types — POINT, LINE, BOX, POLYGON, CIRCLE — for simple geometric calculations  
* Range types — INT4RANGE, TSRANGE, DATERANGE — represent ranges of values, check overlap  
* Enumerated types — CREATE TYPE mood AS ENUM ('happy', 'sad', 'neutral') — custom fixed set of values  
* BYTEA — binary data storage  
* PostgreSQL-specific best practices:  
  * Use TIMESTAMPTZ not TIMESTAMP — timezone awareness prevents bugs  
  * Use TEXT not VARCHAR unless length constraint needed  
  * Use NUMERIC not FLOAT for financial calculations  
  * Use UUID for distributed primary keys  
  * Use JSONB for flexible semi-structured data

---

**Q7. What is the difference between JSON and JSONB in PostgreSQL?** `[1-2 yrs]`

* Both store JSON data but internally very different  
* JSON:  
  * Stores exact text representation of input JSON  
  * Preserves whitespace and duplicate keys  
  * Faster to insert — no processing on write  
  * Slower to query — must parse text on every read  
  * No index support except on whole column  
* JSONB:  
  * Stores JSON in decomposed binary format  
  * Does not preserve whitespace or key order  
  * Removes duplicate keys — last value wins  
  * Slightly slower to insert — parsing on write  
  * Much faster to query — binary format, no reparsing  
  * Supports GIN indexes — index individual keys and values within JSONB  
  * Supports full range of JSON operators and functions  
* JSONB operators:  
  * \-\> — get field as JSON — '{"name": "John"}' \-\> 'name' returns "John" (JSON)  
  * \-\>\> — get field as text — returns John (text, no quotes)  
  * \#\> — get nested value by path — data \#\> '{address,city}'  
  * \#\>\> — get nested value as text  
  * @\> — contains — '{"a":1}' @\> '{"a":1}' returns true  
  * \<@ — is contained by  
  * ? — key exists — data ? 'email'  
  * ?| — any of keys exist  
  * ?& — all keys exist  
  * || — concatenate JSONB objects  
    * — delete key from JSONB  
* GIN index on JSONB:  
  * CREATE INDEX idx\_data\_gin ON users USING GIN (data)  
  * Supports @\>, ?, ?|, ?& operators efficiently  
  * jsonb\_path\_ops operator class — smaller index, only supports @\>  
* When to use JSONB vs relational columns:  
  * JSONB — dynamic/unknown attributes, metadata, configuration, event data  
  * Relational columns — frequently queried, sorted, joined fields  
  * Hybrid approach — store core fields as columns, extras in JSONB

---

**Q8. What are PostgreSQL-specific features that go beyond standard SQL?** `[2-3 yrs]`

* Full-text search — built-in, no Elasticsearch needed for basic use:  
  * tsvector — text search vector, preprocessed searchable format  
  * tsquery — search query with & (and), | (or), \! (not) operators  
  * to\_tsvector('english', text) — convert text to searchable vector  
  * to\_tsquery('english', 'search & term') — create search query  
  * @@ operator — match tsvector against tsquery  
  * GIN index on tsvector — fast full-text search  
  * ts\_rank() — relevance ranking function  
  * ts\_headline() — highlight matching terms in results  
* Array operations:  
  * ANY / ALL — WHERE 5 \= ANY(ARRAY\[1,2,5,10\])  
  * unnest() — expand array to rows, like $unwind in MongoDB  
  * array\_agg() — aggregate rows into array — equivalent to $push in MongoDB  
  * ARRAY\[...\] — array constructor  
* Window functions — powerful analytics without GROUP BY losing row detail  
* LATERAL JOIN — allows subquery to reference columns from preceding tables  
* DISTINCT ON — SELECT DISTINCT ON (user\_id) \* FROM orders ORDER BY user\_id, created\_at DESC — get latest order per user  
* Upsert — INSERT ... ON CONFLICT:  
  * ON CONFLICT (email) DO NOTHING — ignore if duplicate  
  * ON CONFLICT (email) DO UPDATE SET updated\_at \= NOW() — update on conflict  
  * More powerful than MongoDB upsert — specify exact conflict column and action  
* Materialized views — cached query result stored as physical table:  
  * CREATE MATERIALIZED VIEW monthly\_sales AS SELECT ...  
  * REFRESH MATERIALIZED VIEW monthly\_sales — update cached data  
  * Good for expensive reports that don't need real-time data  
* Table partitioning — split large table into smaller physical pieces:  
  * RANGE partitioning — by date range  
  * LIST partitioning — by specific values  
  * HASH partitioning — by hash of column  
* Generated columns — column computed from other columns, stored automatically:  
  * full\_name GENERATED ALWAYS AS (first\_name || ' ' || last\_name) STORED  
* Foreign Data Wrappers — query external data sources as if local tables (CSV, MongoDB, other Postgres)  
* Logical replication — replicate specific tables, not entire cluster  
* Table inheritance — child tables inherit parent columns and constraints

---

### **3\. Connecting PostgreSQL with Node.js**

---

**Q9. What is the `pg` package and how do you use it to connect PostgreSQL?** `[Fresher]`

* pg — node-postgres, official PostgreSQL client for Node.js  
* Low-level driver — gives raw SQL access, no ORM abstraction  
* npm install pg  
* Two ways to use pg — single Client or Pool  
* Single Client:  
  * const client \= new Client({ connectionString })  
  * await client.connect()  
  * const result \= await client.query('SELECT \* FROM users WHERE id \= $1', \[userId\])  
  * result.rows — array of row objects  
  * result.rowCount — number of rows affected  
  * await client.end() — close connection  
  * Use for scripts, migrations, one-off operations  
* Connection Pool (recommended for web apps):  
  * const pool \= new Pool({ connectionString, max: 20 })  
  * const result \= await pool.query('SELECT ...', \[params\])  
  * Pool manages multiple connections, reuses them across requests  
  * No need to connect/disconnect manually — pool handles lifecycle  
  * max — maximum pool size, default 10  
  * idleTimeoutMillis — close idle connections after timeout  
  * connectionTimeoutMillis — throw error if can't get connection within timeout  
* Parameterized queries — always use $1, $2, $3 placeholders:  
  * pool.query('SELECT \* FROM users WHERE email \= $1 AND active \= $2', \[email, true\])  
  * Prevents SQL injection — parameters never interpolated into query string  
  * Never use string template literals to build queries with user input  
* Transaction with pg:  
  * const client \= await pool.connect() — get dedicated client from pool  
  * try — client.query('BEGIN'), operations, client.query('COMMIT')  
  * catch — client.query('ROLLBACK')  
  * finally — client.release() — return client to pool  
* pg vs Mongoose — pg gives raw SQL control, Mongoose gives document abstraction  
* When to use raw pg — complex queries that ORMs can't express, maximum performance, full SQL control

---

**Q10. How do you use Prisma with PostgreSQL in a Node.js or NestJS application?** `[1-2 yrs]`

* Prisma — already covered in NestJS section, here focusing on PostgreSQL-specific patterns  
* prisma/schema.prisma for PostgreSQL:  
  * datasource db — provider: "postgresql", url from env DATABASE\_URL  
  * DATABASE\_URL format — postgresql://user:password@host:port/dbname?schema=public  
* PostgreSQL-specific Prisma schema features:  
  * @db.Text — map to TEXT type instead of VARCHAR  
  * @db.Timestamptz — map to TIMESTAMPTZ  
  * @db.JsonB — map to JSONB type — ALWAYS use for JSON fields in PostgreSQL  
  * @db.Uuid — map to UUID type  
  * @default(dbgenerated("gen\_random\_uuid()")) — use PostgreSQL UUID generation  
  * @default(autoincrement()) — SERIAL/BIGSERIAL  
  * Enum types — define in schema, maps to PostgreSQL enum  
* Prisma Migrate with PostgreSQL:  
  * npx prisma migrate dev — creates SQL migration file using PostgreSQL syntax  
  * Generated SQL uses PostgreSQL-specific types and syntax  
  * npx prisma migrate deploy — run in production/CI  
  * npx prisma db pull — introspect existing PostgreSQL DB and generate schema  
* Prisma Client PostgreSQL queries:  
  * All standard CRUD — same as MongoDB section  
  * JSON field queries — prisma.user.findMany({ where: { metadata: { path: \['city'\], equals: 'Mumbai' } } })  
  * Array field queries — not native Prisma type but via raw queries  
  * Full-text search — prisma.$queryRaw for complex PostgreSQL-specific queries  
* Raw queries with Prisma:  
  * prisma.$queryRaw\`SELECT \* FROM users WHERE name ILIKE ${'%' \+ search \+ '%'}\` — tagged template, safe  
  * prisma.$executeRaw — for INSERT/UPDATE/DELETE raw SQL  
  * Prisma.$queryRawUnsafe — avoid, SQL injection risk  
* Connection pooling — Prisma uses its own connection pool, configure pool\_timeout and connection\_limit in DATABASE\_URL

---

**Q11. How do you use TypeORM with PostgreSQL in NestJS?** `[1-2 yrs]`

* TypeORM — already covered in NestJS section, focusing on PostgreSQL-specific usage  
* npm install @nestjs/typeorm typeorm pg  
* TypeOrmModule.forRoot configuration for PostgreSQL:  
  * type: 'postgres'  
  * host, port (5432 default), username, password, database  
  * ssl: { rejectUnauthorized: false } — required for hosted PostgreSQL (Atlas, Railway, Render, Supabase)  
  * ssl: true — for strict SSL verification in production  
  * synchronize: false — NEVER true in production  
  * logging: true — log SQL queries in development  
  * migrationsRun: true — auto-run migrations on startup  
* PostgreSQL-specific TypeORM column types:  
  * @Column('text') — TEXT type  
  * @Column('timestamptz') — TIMESTAMPTZ — always prefer over timestamp  
  * @Column('jsonb') — JSONB — always prefer over json  
  * @Column('uuid') @PrimaryGeneratedColumn('uuid') — UUID  
  * @Column('decimal', { precision: 10, scale: 2 }) — NUMERIC for money  
  * @Column('enum', { enum: UserRole, default: UserRole.USER }) — PostgreSQL ENUM  
  * @Column('simple-array') — stores array as comma-separated text — avoid, use separate table  
  * @Column('int', { array: true }) — native PostgreSQL array column  
* PostgreSQL-specific indexes in TypeORM:  
  * @Index({ unique: true }) — unique index  
  * @Index({ where: 'active \= true' }) — partial index  
  * Full-text search index — requires raw migration SQL  
* Upsert with TypeORM:  
  * userRepo.upsert(data, { conflictPaths: \['email'\] }) — INSERT ... ON CONFLICT  
  * conflictPaths — columns that define uniqueness conflict  
* Raw PostgreSQL query with TypeORM:  
  * dataSource.query('SELECT \* FROM users WHERE name ILIKE $1', \['%' \+ search \+ '%'\])  
  * queryRunner.query() inside transactions  
  * Always use $1 placeholders — never string concatenation

---

**Q12. What is the difference between Prisma, TypeORM, and raw pg for PostgreSQL?** `[2-3 yrs]`

* Choosing the right tool depends on project needs, team preferences, and complexity

| Aspect | raw pg | TypeORM | Prisma |
| ----- | ----- | ----- | ----- |
| Abstraction | None — raw SQL | Medium — decorators \+ QueryBuilder | High — schema-first, generated client |
| Type safety | Manual | Good with TypeScript | Excellent — fully generated types |
| SQL control | Full — write any SQL | Good — QueryBuilder for complex | Limited — raw for complex queries |
| Schema definition | SQL files | TypeScript entity classes | schema.prisma file |
| Migrations | Manual SQL | TypeORM CLI | Prisma Migrate — best DX |
| Learning curve | SQL knowledge needed | Medium | Low — intuitive API |
| Performance | Fastest — no overhead | Good | Good — slight overhead |
| Complex queries | Best — full SQL | QueryBuilder is powerful | Limited without $queryRaw |
| Auto-completion | None | Partial | Excellent |
| Community | Stable | Large | Fast growing |
| NestJS integration | Manual | Official @nestjs/typeorm | Community module |

* When to use raw pg:  
  * Performance-critical paths  
  * Complex analytical queries that ORMs cannot express  
  * Database-heavy applications where SQL expertise is strength  
  * Microservices that need minimal dependencies  
* When to use TypeORM:  
  * NestJS projects using official integration  
  * Teams comfortable with decorator-based approach  
  * Projects needing advanced QueryBuilder for complex queries  
  * Multiple database types in same project  
* When to use Prisma:  
  * New projects where developer experience is priority  
  * Teams who prefer schema-first approach  
  * TypeScript projects needing maximum type safety  
  * When migration tooling and DX matters  
* Recommendation for MERN/PERN stack — Prisma for new NestJS \+ PostgreSQL projects, TypeORM for teams already familiar with it

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q13. What are indexes in PostgreSQL and what types are available?** `[1-2 yrs]`

* Index — separate data structure that speeds up SELECT at cost of INSERT/UPDATE/DELETE performance and storage  
* CREATE INDEX idx\_users\_email ON users(email) — basic index  
* CREATE UNIQUE INDEX — enforce uniqueness and speed up lookups  
* DROP INDEX idx\_name — remove index  
* REINDEX — rebuild corrupted or bloated index  
* PostgreSQL index types:  
  * B-Tree (default) — balanced tree, good for equality and range queries, ORDER BY, most common  
  * Hash — only equality comparisons, faster than B-Tree for equality only  
  * GIN (Generalized Inverted Index) — for composite values like arrays, JSONB, full-text search — multiple values per row  
  * GiST (Generalized Search Tree) — geometric, range, full-text search  
  * SP-GiST — space-partitioned GiST, for non-balanced structures  
  * BRIN (Block Range Index) — very small, for naturally ordered large tables like timestamps, approximate  
* Partial index — index only rows matching condition:  
  * CREATE INDEX idx\_active\_users ON users(email) WHERE active \= true  
  * Smaller index, faster, only queries matching condition benefit  
* Covering index — include extra columns in index for covered queries:  
  * CREATE INDEX idx\_email ON users(email) INCLUDE (name, role)  
  * Query SELECT name, role FROM users WHERE email \= '...' — no table access needed  
* Expression index — index on expression result:  
  * CREATE INDEX idx\_lower\_email ON users(LOWER(email))  
  * WHERE LOWER(email) \= 'john@example.com' — uses index  
* Multicolumn index — same as compound index in MongoDB:  
  * CREATE INDEX idx\_last\_first ON users(last\_name, first\_name)  
  * Column order matters — left-prefix rule same as MongoDB  
* EXPLAIN ANALYZE — show query execution plan with actual timing:  
  * Seq Scan — full table scan, no index used  
  * Index Scan — using index  
  * Index Only Scan — covered index, no heap access  
  * Bitmap Index Scan — for multiple conditions, combines index results

---

**Q14. What are PostgreSQL views and when should you use them?** `[1-2 yrs]`

* View — named saved SELECT query, acts as virtual table  
* CREATE VIEW active\_users AS SELECT \* FROM users WHERE active \= true AND deleted\_at IS NULL  
* Query view like a table — SELECT \* FROM active\_users WHERE role \= 'admin'  
* Benefits:  
  * Simplify complex queries — hide JOIN complexity behind simple view name  
  * Security — expose only specific columns, hide sensitive data  
  * Consistency — business logic defined once in view, not duplicated in every query  
  * Abstraction — change underlying table structure without changing all queries  
* Views do NOT store data — query executed every time view is queried  
* Updatable views — simple views on single table without DISTINCT/GROUP BY can be updated  
* Materialized views — store query result physically:  
  * CREATE MATERIALIZED VIEW monthly\_report AS SELECT ...  
  * REFRESH MATERIALIZED VIEW monthly\_report — update data  
  * REFRESH MATERIALIZED VIEW CONCURRENTLY — refresh without locking reads  
  * Great for expensive aggregations, reports, denormalized read models  
  * Can create indexes on materialized view  
  * Trade-off — data can be stale between refreshes  
* WITH CHECK OPTION — prevent updates through view that would make row invisible to view

---

**Q15. What is connection pooling and why is it important in PostgreSQL?** `[2-3 yrs]`

* PostgreSQL creates new OS process per connection — expensive, \~5MB RAM per connection  
* Connection limit — PostgreSQL default max\_connections is 100  
* Without pooling — each API request opens new connection, max\_connections exceeded quickly  
* Connection pool — maintain set of pre-opened connections, reuse across requests  
* Application-level pooling — pg Pool, Prisma pool, TypeORM pool — pool within single process  
* Problem — multiple Node.js processes (PM2 cluster, multiple containers) each have own pool — total connections multiply  
* PgBouncer — dedicated connection pooler, sits between app and PostgreSQL:  
  * All app processes connect to PgBouncer instead of PostgreSQL directly  
  * PgBouncer maintains small pool of real PostgreSQL connections  
  * Thousands of app connections map to small pool of DB connections  
  * Three modes:  
    * Session mode — client gets connection for entire session, similar to no pooler  
    * Transaction mode — client gets connection only during transaction, best for stateless APIs  
    * Statement mode — connection returned after each statement, cannot use transactions  
* Neon Serverless — built-in connection pooling via HTTP for serverless environments  
* Supabase — uses PgBouncer built-in  
* Connection pool sizing — rule of thumb: num\_connections \= (num\_cpu\_cores \* 2\) \+ effective\_spindle\_count  
* Pool configuration options in pg:  
  * max — maximum connections in pool  
  * min — minimum connections to maintain  
  * idleTimeoutMillis — close idle connections after timeout  
  * connectionTimeoutMillis — error if connection not available within timeout  
  * maxUses — close connection after N uses (prevents long-lived connection issues)

---

That is the complete PostgreSQL section — 15 questions with full subtopic depth, ready to merge into your MERN Interview Kit.
---

[⬅️ Previous: MongoDB](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/01_MongoDB/01_MongoDB.md) | [🏠 Home](../../README.md) | [Next: CRUD Operations ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/03_CRUD_Operations/03_CRUD_Operations.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>