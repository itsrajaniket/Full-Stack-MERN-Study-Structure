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

---

[⬅️ Previous: Building REST APIs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/06_Building_REST_APIs/06_Building_REST_APIs.md) | [🏠 Home](../../README.md) | [Next: Authentication Security ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/08_Authentication_Security/08_Authentication_Security.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>