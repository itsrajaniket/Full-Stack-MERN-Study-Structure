# Database & ORM
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] TypeORM & Prisma with NestJS
- [x] Repository Pattern
- [x] Database Migrations

## 📝 Detailed Notes

### 1. Database Integration in NestJS
NestJS provides built-in modules for popular ORMs like **TypeORM**, **Sequelize**, and **Mongoose**. Recently, **Prisma** has also become very popular.

### 2. TypeORM & Prisma
- **TypeORM**: An ORM that uses **Data Mapper** or **Active Record** patterns. It uses decorators extensively.
```typescript
@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  name: string;
}
```
- **Prisma**: A modern ORM that uses a **schema-first** approach. It generates a type-safe client based on your `schema.prisma` file.
```prisma
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
}
```

### 3. Repository Pattern
This pattern abstracts the data access logic. Instead of calling DB methods directly in your service, you use a "Repository" which handles the CRUD operations.
```typescript
@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private usersRepository: Repository<User>,
  ) {}

  findAll(): Promise<User[]> {
    return this.usersRepository.find();
  }
}
```

### 4. Database Migrations
Migrations are like version control for your database. They allow you to define changes (creating tables, adding columns) in code files that can be run on different environments (dev, staging, prod) to keep the schemas in sync.

---

## 🎓 Important Interview Questions

### Q1: What is an ORM?
ORM stands for **Object-Relational Mapping**. It is a technique that lets you query and manipulate data from a database using an object-oriented paradigm. It allows you to interact with your DB using your preferred programming language (e.g., TypeScript) instead of writing raw SQL.

### Q2: Difference between TypeORM and Prisma?
- **TypeORM**: Uses decorators on classes. More traditional. Supports multiple patterns (Active Record vs Data Mapper).
- **Prisma**: Uses a custom `.prisma` schema file. It is **auto-generated** and provides superior type-safety and IntelliSense compared to TypeORM.

### Q3: What is the "Repository Pattern"?
It is a design pattern that mediates between the domain and data mapping layers. It creates an abstraction layer between the business logic and the data source, making the code more testable and easier to switch databases if needed.

### Q4: Why are "Migrations" important?
Without migrations, you would have to manually update the database schema on every server. This is error-prone and hard to track. Migrations ensure that every developer and every server has the exact same database structure.

### Q5: Explain the "N+1 Query Problem" in ORMs.
It happens when an ORM executes one query to fetch a list of items, and then executes **N** additional queries to fetch related data for each item (e.g., fetching 10 posts and then 10 separate queries to fetch the author of each post). This can be solved using **Eager Loading** (Joins) or **Select-In** strategies.


## ❓ Questions & Doubts
- [x]

## **Database & ORM — MERN Stack Interview Kit**

---

### **1\. TypeORM & Prisma with NestJS**

---

**Q1. What is TypeORM and how does it integrate with NestJS?** `[Fresher]`

* TypeORM — ORM (Object Relational Mapper) for TypeScript and JavaScript, supports PostgreSQL, MySQL, SQLite, MongoDB and more  
* ORM — maps database tables to TypeScript classes, rows to class instances, columns to properties  
* Why ORM over raw SQL — type safety, no SQL injection risk, database agnostic, migrations, relationships handled automatically  
* @nestjs/typeorm — official NestJS integration package  
* npm install @nestjs/typeorm typeorm pg (for PostgreSQL)  
* Setup in AppModule:  
  * TypeOrmModule.forRoot() — root level DB connection config  
  * type — database type ('postgres', 'mysql', 'sqlite')  
  * host, port, username, password, database — connection details  
  * entities — array of entity classes or glob pattern  
  * synchronize: true — auto-sync schema with entities (NEVER in production — use migrations)  
  * logging — log SQL queries (useful in development)  
* TypeOrmModule.forRootAsync() — async config using ConfigService:  
  * inject: \[ConfigService\] — inject config service into factory  
  * useFactory — return config object using configService.get()  
  * Preferred over forRoot() for env-based config  
* TypeOrmModule.forFeature(\[UserEntity\]) in feature module — registers repository for that module  
* Entity — TypeScript class decorated with @Entity() representing a database table  
* Repository — auto-generated class for each entity with CRUD methods  
* DataSource — TypeORM v0.3+ main entry point, replaces Connection

**Full Answer:**
TypeORM is an Object-Relational Mapper that allows you to interact with SQL databases using TypeScript classes. In NestJS, it's integrated via the `@nestjs/typeorm` package. The core philosophy is to map **Entities** (classes) to **Tables**. The integration typically involves using `TypeOrmModule.forRoot()` in the `AppModule` for connection setup and `TypeOrmModule.forFeature()` in individual modules to inject repositories.

**Trap Explained: The `synchronize: true` Production Disaster**
*"Why should you never use `synchronize: true` in a production environment?"*
- **The Answer:** When `synchronize` is true, TypeORM automatically modifies your database schema to match your entity classes on every server restart. If you accidentally delete a property in your code, TypeORM will **DROP** that column in the database, leading to irreversible data loss. In production, you must **always** use **Migrations** to have a version-controlled, auditable trail of schema changes.


---

**Q2. What are TypeORM Entities and how do you define them?** `[Fresher]`

* Entity — class decorated with @Entity() that maps to a database table  
* @Entity('table\_name') — custom table name, defaults to class name in snake\_case  
* Column decorators:  
  * @PrimaryGeneratedColumn() — auto-increment integer primary key  
  * @PrimaryGeneratedColumn('uuid') — UUID primary key  
  * @Column() — regular column, TypeScript type inferred  
  * @Column({ type: 'varchar', length: 100, nullable: false }) — explicit options  
  * @Column({ default: true }) — default value  
  * @Column({ unique: true }) — unique constraint  
  * @Column({ select: false }) — exclude from SELECT by default (passwords)  
  * @CreateDateColumn() — auto-set on INSERT  
  * @UpdateDateColumn() — auto-set on UPDATE  
  * @DeleteDateColumn() — soft delete timestamp  
  * @VersionColumn() — auto-increment on each update (optimistic locking)  
* Relation decorators:  
  * @OneToOne(() \=\> Profile) @JoinColumn() — one-to-one, JoinColumn on owning side  
  * @OneToMany(() \=\> Post, post \=\> post.user) — one-to-many (no JoinColumn)  
  * @ManyToOne(() \=\> User, user \=\> user.posts) @JoinColumn() — many-to-one  
  * @ManyToMany(() \=\> Role) @JoinTable() — many-to-many, JoinTable on owning side  
* Relation options:  
  * eager: true — always load relation automatically  
  * cascade: true — propagate operations to related entity  
  * onDelete: 'CASCADE' — DB-level cascade delete  
  * lazy: true — load relation as Promise  
* @Index() — create database index on column or combination of columns  
* Inheritance — Single Table Inheritance with @ChildEntity() or Table Per Class

**Full Answer:**
An Entity is a class that represents a database table. You decorate the class with `@Entity()` and individual properties with decorators like `@Column()`, `@PrimaryGeneratedColumn()`, or relationship decorators like `@ManyToOne()`. These decorators provide the metadata TypeORM needs to generate SQL queries.

**Trap Explained: The "UUID vs Serial" Performance Trap**
- **The Answer:** Using `@PrimaryGeneratedColumn('uuid')` is great for distributed systems and security (prevents ID enumeration), but it can be slower for indexing in extremely large tables compared to standard `integer` IDs. A senior developer should weigh the trade-offs: use **UUIDs** for public-facing resource IDs and **Integers** for internal, high-performance joining if needed.


---

**Q3. What is Prisma and how does it differ from TypeORM?** `[1-2 yrs]`

* Prisma — next-generation ORM with schema-first approach, strong type safety, excellent developer experience  
* Schema-first — define data model in schema.prisma file, Prisma generates TypeScript client  
* npm install prisma @prisma/client  
* npx prisma init — creates prisma/schema.prisma and .env with DATABASE\_URL  
* Prisma schema — defines datasource, generator, and models:  
  * datasource db — provider and connection URL  
  * generator client — generates Prisma Client  
  * model User — fields with types, attributes, relations  
* npx prisma generate — generates fully typed Prisma Client based on schema  
* npx prisma db push — push schema to DB (development)  
* npx prisma migrate dev — create and apply migration (preferred)  
* PrismaService in NestJS — extend PrismaClient, implement OnModuleInit and OnModuleDestroy:  
  * onModuleInit — await this.$connect()  
  * onModuleDestroy — await this.$disconnect()  
  * Make PrismaService global — @Global() module or register in AppModule providers  
* Prisma Client queries — fully typed, autocomplete for all models and fields:  
  * prisma.user.findMany() — returns User\[\]  
  * prisma.user.findUnique({ where: { id } }) — returns User | null  
  * prisma.user.create({ data: createUserDto }) — returns User  
  * prisma.user.update({ where: { id }, data: updateDto }) — returns User  
  * prisma.user.delete({ where: { id } })  
  * prisma.user.count({ where: { role: 'admin' } })  
* TypeORM vs Prisma comparison:

| Feature | TypeORM | Prisma |
| ----- | ----- | ----- |
| Approach | Code-first (decorators) | Schema-first (schema.prisma) |
| Type safety | Good | Excellent — fully generated types |
| Query API | Repository \+ QueryBuilder | Prisma Client — fluent API |
| Migrations | TypeORM migrations | Prisma Migrate |
| Relations | Decorators on entity | Defined in schema |
| Raw queries | queryRunner.query() | prisma.$queryRaw |
| Learning curve | Higher | Lower |
| NestJS support | Official @nestjs/typeorm | Community module |
| Auto-completion | Partial | Excellent |

**Full Answer:**
Prisma is a modern ORM that takes a **Schema-First** approach. Unlike TypeORM, where your "Source of Truth" is spread across many TypeScript classes with decorators, Prisma uses a single `schema.prisma` file. It generates a custom **Prisma Client** that is tailored specifically to your schema, providing the best-in-class TypeScript autocompletion and type-safety in the industry.

**Trap Explained: The "Runtime vs Build-time" Difference**
*"Why is Prisma's type safety considered 'superior' to TypeORM's?"*
- **The Answer:** TypeORM relies on TypeScript's type inference and decorators, which can sometimes lead to "any" types if relations aren't handled perfectly. **Prisma generates code.** When you run `prisma generate`, it creates actual TypeScript types based on your DB schema. If you change a column name in the DB, your code will literally fail to compile until you fix the reference.


---

**Q4. How do you perform CRUD operations with TypeORM Repository in NestJS?** `[1-2 yrs]`

* Inject repository — @InjectRepository(UserEntity) private userRepo: Repository\<UserEntity\>  
* FindOptions — object passed to find methods with powerful filtering:  
  * where — filter conditions, supports operators (Equal, Like, In, Between, IsNull, Not, MoreThan, LessThan)  
  * select — specify columns to return  
  * relations — eager load specific relations  
  * order — sort results { createdAt: 'DESC' }  
  * skip and take — pagination (offset and limit)  
  * withDeleted — include soft-deleted records  
* Key Repository methods:  
  * userRepo.find(options) — find multiple records  
  * userRepo.findOne({ where: { id } }) — find single record, null if not found  
  * userRepo.findOneOrFail({ where: { id } }) — throws EntityNotFoundError if not found  
  * userRepo.save(entity) — INSERT if new, UPDATE if has id — detects automatically  
  * userRepo.create(plainObject) — create entity instance without saving  
  * userRepo.insert(data) — raw INSERT, no cascade, faster than save()  
  * userRepo.update(criteria, partialEntity) — raw UPDATE, no cascade  
  * userRepo.delete(criteria) — hard delete  
  * userRepo.softDelete(criteria) — set DeletedColumn timestamp  
  * userRepo.restore(criteria) — undo soft delete  
  * userRepo.count(options) — count matching records  
  * userRepo.exists(options) — boolean existence check  
* QueryBuilder — for complex queries:  
  * userRepo.createQueryBuilder('user')  
  * .leftJoinAndSelect('user.posts', 'post')  
  * .where('user.role \= :role', { role: 'admin' })  
  * .andWhere('post.published \= :published', { published: true })  
  * .orderBy('user.createdAt', 'DESC')  
  * .skip(0).take(10)  
  * .getManyAndCount() — returns \[results, total count\]  
* Transactions:  
  * dataSource.transaction(async manager \=\> { ... }) — all operations in one transaction  
  * manager.save(), manager.delete() inside transaction

**Full Answer:**
NestJS uses the **Repository Pattern** provided by TypeORM. You inject the repository into your service using `@InjectRepository(User)`. Common methods include `.find()` for multiple records, `.findOne()` for a single record, and `.save()` for both inserting and updating. For complex queries, you use the **QueryBuilder** which allows you to write SQL-like syntax using a fluent API.

**Trap Explained: The `save()` vs `update()` Difference**
*"When should you use `repo.save()` versus `repo.update()`?"*
- **The Answer:** `save()` is a "Heavy" operation. It first checks if the entity exists (SELECT), then performs an INSERT or UPDATE, and finally returns the full entity. `update()` is a "Light" raw SQL operation that directly updates the record without fetching it. **Senior Tip:** Use `update()` for performance-critical bulk updates, and `save()` when you need to trigger **Subscribers/Hooks** or need the updated entity returned.


---

### **2\. Repository Pattern**

---

**Q5. What is the Repository Pattern and why is it used?** `[1-2 yrs]`

* Repository Pattern — abstraction layer between business logic and data access logic  
* Service layer does not directly use TypeORM Repository or Prisma Client — uses custom repository instead  
* Benefits:  
  * Separation of concerns — business logic has no knowledge of database technology  
  * Testability — mock repository in unit tests, no real DB needed  
  * Swappable — change from TypeORM to Prisma without touching service layer  
  * Reusability — common query logic centralized in one place  
  * Readability — userRepository.findActiveAdmins() vs userRepo.find({ where: { role: 'admin', isActive: true }})  
* TypeORM built-in Repository — already follows repository pattern but exposes ORM details to service  
* Custom repository — wraps TypeORM Repository, exposes domain-specific methods:  
  * TypeORM v0.3 custom repository — @Injectable() class with @InjectRepository injected, not @EntityRepository  
  * Extend logic — add findActiveUsers(), findByEmailWithProfile(), findUsersWithPostCount() methods  
  * Hide QueryBuilder complexity — service calls clean method name, repository handles SQL  
* Repository vs Service:  
  * Repository — only data access, no business logic, no calls to other services  
  * Service — business logic, orchestrates multiple repositories or external services  
* Generic repository — base repository class with common CRUD methods, specific repositories extend it  
* In NestJS with Prisma — PrismaService IS the repository layer, but can wrap it in domain repositories for clean abstraction

**Full Answer:**
The Repository Pattern is an abstraction layer that sits between your **Business Logic (Services)** and your **Data Source (Database)**. By using repositories, your services don't need to know whether you are using TypeORM, Prisma, or even a raw SQL driver. This makes your code more modular, easier to test (via mocking), and easier to maintain.

**Trap Explained: The "Leaky Abstraction"**
- **The Answer:** A common mistake is passing TypeORM-specific objects (like `FindOptions` or `QueryBuilder`) directly from the Controller to the Service. This "leaks" the ORM implementation into your business logic. A true Repository Pattern implementation should hide these details, exposing only clean methods like `userRepository.findActiveUsers()`.


---

**Q6. How do you implement a custom repository in NestJS with TypeORM?** `[2-3 yrs]`

* TypeORM v0.3 removed @EntityRepository decorator — custom repository pattern changed  
* Current approach — @Injectable() service class with injected Repository:  
  * Inject built-in Repository with @InjectRepository(UserEntity)  
  * Add custom methods on top  
  * Register as provider in module  
  * Services inject this custom repository instead of built-in one  
* Custom repository example structure:  
  * findAllPaginated(page, limit, filters) — handles skip/take calculation, returns { data, total }  
  * findByEmailWithProfile(email) — encapsulates join logic  
  * findActiveAdmins() — encapsulates business-specific filter  
  * softDeleteById(id) — wraps soft delete with existence check  
* Benefits over using TypeORM Repository directly in service:  
  * Query logic testable in isolation  
  * Service tests mock repository — no DB dependency  
  * Changing query logic is localized to repository file  
* With Prisma — create wrapper service/repository:  
  * Inject PrismaService  
  * Expose domain-specific methods  
  * Service only calls domain methods, never prisma.user.findMany() directly  
  * If switching DB or ORM — only repository files change  
* Testing custom repository — inject mock of underlying TypeORM Repository using jest.fn() for each method, test that repository methods call correct underlying operations

**Full Answer:**
In TypeORM v0.3+, the `@EntityRepository` decorator was deprecated. The modern way to implement a custom repository in NestJS is to create a standard `@Injectable()` service and inject the base `Repository` or `DataSource` into its constructor. You then add your custom, complex query logic (like QueryBuilders) inside this service and inject it into your business services.

**Trap Explained: The "Service vs Repository" Identity Crisis**
*"Why not just put the complex SQL in the Service?"*
- **The Answer:** You *can*, but it violates the **Single Responsibility Principle (SRP)**. The Service should focus on "What" to do (business rules), while the Repository should focus on "How" to get the data (SQL/Optimization). Separating them allows you to reuse complex queries across different services without duplication.


---

### **3\. Database Migrations**

---

**Q7. What are database migrations and why are they important?** `[Fresher]`

* Database migration — version-controlled script that changes database schema in a controlled, repeatable way  
* Why migrations:  
  * Track schema changes alongside code changes in Git  
  * Reproducible — same migration runs in development, staging, production  
  * Rollback — revert schema changes if deployment fails  
  * Team collaboration — everyone applies same schema changes in correct order  
  * Production safety — never use synchronize: true in production, it can DROP columns with data  
* synchronize: true danger — TypeORM auto-syncs schema, can drop columns that exist in DB but removed from entity, irreversible data loss  
* Migration workflow:  
  * Developer changes entity  
  * Generate migration — compares current DB schema vs entity definitions  
  * Review generated SQL — verify it is correct  
  * Commit migration file with code changes  
  * Run migrations in CI/CD before deploying new code  
* Migration table — TypeORM and Prisma maintain migrations table in DB — tracks which migrations have run

**Full Answer:**
Migrations are **Version Control for your Database**. They are code files that describe a transformation (e.g., "Add email column to Users table"). By running these scripts in order, you ensure that every developer's local DB and every production server have the exact same structure.

**Trap Explained: The "Manual DB Change" Trap**
- **The Answer:** Never make changes to your production database schema manually via a GUI like pgAdmin or DBeaver. If you do, your code's Migrations will be out of sync, and the next time a migration runs, it might fail or create a conflict. **Senior Rule:** If it's not in a migration file, it doesn't exist in the database.


---

**Q8. How do you create and run migrations with TypeORM in NestJS?** `[1-2 yrs]`

* TypeORM CLI configuration — separate datasource file for CLI use:  
  * data-source.ts — exports DataSource instance with all entity and migration paths  
  * CLI needs to know where entities and migrations are  
* package.json scripts:  
  * typeorm:generate — npx typeorm-ts-node-esm migration:generate src/migrations/MigrationName \-d src/data-source.ts  
  * typeorm:run — npx typeorm-ts-node-esm migration:run \-d src/data-source.ts  
  * typeorm:revert — npx typeorm-ts-node-esm migration:revert \-d src/data-source.ts  
  * typeorm:create — create empty migration file to write manually  
* Migration file structure:  
  * up(queryRunner) — changes to apply (add column, create table, create index)  
  * down(queryRunner) — how to revert the up changes (drop column, drop table)  
  * Always implement down — enables rollback  
* Running migrations in production:  
  * migrationsRun: true in TypeOrmModule config — auto-run pending migrations on startup  
  * Or run explicitly in deployment script before starting app  
  * Never run generate in production — only run pre-generated migrations  
* Common migration operations:  
  * queryRunner.addColumn(table, new TableColumn({...}))  
  * queryRunner.dropColumn(table, columnName)  
  * queryRunner.createIndex(table, new TableIndex({...}))  
  * queryRunner.createForeignKey(table, new TableForeignKey({...}))  
  * queryRunner.query('ALTER TABLE ...') — raw SQL when needed

**Full Answer:**
With TypeORM, you typically use the CLI to `generate` a migration by comparing your entities to your current DB schema. This creates a file with an `up()` method (to apply the change) and a `down()` method (to revert it). You then use `migration:run` to apply these changes to the database.

**Trap Explained: The "Empty Migration" Mystery**
*"Why did TypeORM generate an empty migration even though I changed my entity?"*
- **The Answer:** This usually happens if the CLI can't correctly find your entities or your database connection. Always ensure your `DataSource` configuration is correctly pointing to the compiled `.js` files (or `.ts` with `ts-node`) and that all entities are listed in the `entities` array.


---

**Q9. How do Prisma migrations work?** `[1-2 yrs]`

* Prisma Migrate — migration system built into Prisma CLI, generates SQL migration files  
* Migration workflow:  
  * Edit schema.prisma — add/change/remove models or fields  
  * npx prisma migrate dev \--name migration\_name — generates SQL migration file, applies it to dev DB, regenerates Prisma Client  
  * Review prisma/migrations/timestamp\_name/migration.sql — actual SQL to be applied  
  * Commit migration files with code changes  
  * npx prisma migrate deploy — apply pending migrations in production (no generates, no client update)  
* Migration files — plain SQL, human-readable, version controlled, never edit manually after applying  
* prisma/migrations folder — each migration is folder with timestamp\_name containing migration.sql  
* Prisma shadow database — temporary DB Prisma creates during migrate dev to detect schema drift (requires extra DB in dev)  
* Schema drift — when DB schema and migration history are out of sync (manual DB changes)  
* npx prisma migrate status — shows which migrations are applied vs pending  
* npx prisma migrate reset — drops DB, recreates, runs all migrations, runs seed (DEVELOPMENT ONLY)  
* Baseline existing DB — for adding Prisma to existing project:  
  * npx prisma migrate diff — generate migration from existing DB  
  * npx prisma migrate resolve \--applied migration\_name — mark as already applied  
* Prisma vs TypeORM migrations:  
  * Prisma generates plain SQL — easier to review and understand  
  * TypeORM generates TypeScript with queryRunner API — more programmatic but verbose  
  * Prisma migrate dev is simpler — one command does everything  
  * Both require committing migration files and running deploy in production

**Full Answer:**
Prisma Migrate uses the `schema.prisma` file as the source of truth. When you run `prisma migrate dev`, Prisma compares your schema to the database, generates a **Plain SQL** file, and applies it. This is simpler than TypeORM because you can read and edit the raw SQL directly before it's finalized.

**Trap Explained: The "Reset" Trap**
*"Why did Prisma ask to 'Reset' my database when I ran a migration?"*
- **The Answer:** If you make a manual change to the database that conflicts with the migration history, Prisma detects "Drift." In development, it often asks to reset (delete all data) to ensure the schema is clean. **Senior Rule:** In production, **never** use `migrate dev`. Always use `prisma migrate deploy`, which only applies the SQL files without checking for drift or regenerating the client.


---

**Q10. How do you handle Database Transactions in NestJS?** `[2-3 yrs]`

* **ACID Properties:** Atomicity, Consistency, Isolation, Durability.
* **TypeORM Transaction:** Use `dataSource.transaction()` or the `@Transaction()` decorator (deprecated in favor of QueryRunner).
* **Prisma Transaction:** Use `prisma.$transaction([query1, query2])` for sequential or interactive transactions.
* **Use Case:** Transferring money between accounts — both the debit and credit must succeed, or both must fail.

**Full Answer:**
Transactions ensure that a series of database operations are treated as a single unit of work. In NestJS, the most robust way is to use the **QueryRunner** in TypeORM. You manually `startTransaction()`, `commitTransaction()`, and `rollbackTransaction()` inside a `try-catch` block. This gives you absolute control over the execution flow and is much safer than decorators for complex business logic.

**Trap Explained: The "External API" Transaction Trap**
*"Should you put an external API call (like sending an Email) inside a DB transaction?"*
- **The Answer:** **No.** Transactions only protect database state. If your DB commit fails but your Email was already sent, you have an inconsistent system. **Senior Rule:** Always perform side effects (emails, file uploads) *after* the transaction has successfully committed.

---

**Q11. What is the difference between Optimistic and Pessimistic Locking?** `[3+ yrs]`

* **Optimistic Locking:** Assumes conflicts are rare. Uses a `version` column. If the version has changed since you read it, the update fails.
* **Pessimistic Locking:** Assumes conflicts are likely. Locks the row (`SELECT ... FOR UPDATE`) so no one else can read/write until you are done.
* **Implementation:** TypeORM has `@VersionColumn()` for optimistic and `setLock('pessimistic_write')` for pessimistic.

**Full Answer:**
Optimistic locking is preferred for most web apps because it doesn't hold DB connections open. You simply check if the `version` matches. Pessimistic locking is for high-concurrency, high-stakes operations (like a flash sale with limited stock) where you cannot afford a "first-come, last-served" collision.

**Trap Explained: The "Deadlock" Trap**
- **The Answer:** Pessimistic locking can lead to **Deadlocks** where Transaction A waits for Transaction B, and Transaction B waits for Transaction A. To prevent this, always acquire locks in a consistent order and keep transactions as short as possible.

---

**Q12. How do you optimize database performance with Indexing?** `[3+ yrs]`

* **B-Tree Index:** The default for most columns (equality and range queries).
* **Composite Index:** An index on multiple columns (e.g., `firstName` and `lastName`).
* **GIN Index:** Used for searching inside JSONB or arrays in PostgreSQL.
* **Trade-off:** Indexes speed up SELECTs but slow down INSERTs/UPDATEs because the index must be updated too.

**Full Answer:**
Indexing is the first line of defense against slow queries. You should index columns used in `WHERE`, `JOIN`, and `ORDER BY` clauses. A common senior-level strategy is the **Covering Index**, where the index itself contains all the data needed for the query, allowing the DB to skip reading the actual table entirely.

**Trap Explained: The "Over-Indexing" Trap**
- **The Answer:** Adding an index to every single column is a disaster. It bloats your database size and significantly degrades write performance. Only index columns that are actually used in your query patterns. Use `EXPLAIN ANALYZE` in SQL to see if your index is actually being used.

---

**Q13. What is Connection Pooling and why is it necessary?** `[2-3 yrs]`

* **The Problem:** Opening a new database connection for every single HTTP request is extremely expensive and slow.
* **The Solution:** A "Pool" of pre-opened connections that are reused by different requests.
* **Configuration:** Managed via `max` and `min` settings in your ORM config.

**Full Answer:**
Connection pooling is what allows a Node.js app to handle thousands of concurrent users. Instead of the overhead of a handshake for every request, the app "borrows" a connection from the pool and "returns" it when finished. In a microservices environment, you must carefully manage pool sizes to ensure you don't exhaust the database's maximum allowed connections.

**Trap Explained: The "Connection Leak"**
- **The Answer:** If you use a raw `queryRunner` or a manual client and forget to `release()` it, you have a **Connection Leak**. Eventually, your pool will empty, and your app will hang indefinitely, waiting for a connection that will never come. Always use `finally { queryRunner.release() }`.

---

**Q14. How do you implement Soft Deletes and Auditing in an ORM?** `[2-3 yrs]`

* **Soft Delete:** Adding a `deletedAt` timestamp instead of deleting the row. The row stays in the DB but is filtered out of queries.
* **Auditing:** Tracking `createdBy`, `updatedBy`, and `updatedAt`.
* **Subscribers/Hooks:** Code that runs automatically before/after a DB operation.

**Full Answer:**
Soft deletes are critical for data recovery and compliance. TypeORM supports this natively with `@DeleteDateColumn()` and the `.softDelete()` method. For auditing, we use **Subscribers**. For example, a `UserSubscriber` can automatically set the `updatedBy` field to the current user's ID before any update is saved.

**Trap Explained: The "Unique Constraint" Conflict**
*"If I soft-delete a user with email 'test@test.com', can I create a new user with that same email?"*
- **The Answer:** **No**, if you have a unique constraint on email. The DB still sees the old row. **The Fix:** You must either include the `deletedAt` column in your unique index (PostgreSQL partial index) or use a "Trash" table for deleted records.

---

That is the complete, professionalized Database & ORM section — 14 questions with full architectural depth, ready for your MERN Interview Kit.


---

[⬅️ Previous: Building REST APIs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/06_Building_REST_APIs/06_Building_REST_APIs.md) | [🏠 Home](../../README.md) | [Next: Authentication Security ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/08_Authentication_Security/08_Authentication_Security.md)


---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>