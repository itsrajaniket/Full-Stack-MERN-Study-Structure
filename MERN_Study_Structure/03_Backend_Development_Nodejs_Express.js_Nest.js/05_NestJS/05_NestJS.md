# NestJS (Enterprise Backend Development)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] NestJS Fundamentals
- [x] Introduction to NestJS & Architecture
- [x] Controllers, Modules, and Providers
- [x] Dependency Injection in NestJS
- [x] Configuration Management

## 📝 Detailed Notes

### 1. Introduction to NestJS
NestJS is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications. It is built with and fully supports **TypeScript** and uses **Express** (by default) or Fastify under the hood. It follows an **opinionated** architecture inspired by Angular.

### 2. NestJS Architecture
- **Modules**: Used to organize the code. Every Nest app has at least one root module.
- **Controllers**: Responsible for handling incoming **requests** and returning responses to the client.
- **Providers (Services)**: Used to handle complex **business logic**. Can be "injected" into controllers.

### 3. Dependency Injection (DI)
Instead of manually creating objects, NestJS manages them for you. You define a class with `@Injectable()` and pass it into the constructor of another class.
```typescript
@Injectable()
export class UsersService { ... }

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}
}
```

### 4. DTOs (Data Transfer Objects)
Used to define the shape of the data being sent over the network. Combined with `class-validator`, they provide powerful runtime validation.
```typescript
export class CreateUserDto {
  @IsString()
  name: string;

  @IsEmail()
  email: string;
}
```

### 5. Pipes, Guards, and Interceptors
- **Pipes**: Used for **validation** and **transformation** (e.g., parsing a string ID into a number).
- **Guards**: Used for **authentication** and **authorization** (checking if a user is logged in).
- **Interceptors**: Used to transform the response or log execution time.

---

## 🎓 Important Interview Questions

### Q1: Why use NestJS over plain Express?
NestJS provides a **standardized architecture**, making it much easier for large teams to maintain the codebase. It has built-in support for TypeScript, Dependency Injection, and powerful tools for validation, error handling, and testing that you would otherwise have to set up manually in Express.

### Q2: What is "Dependency Injection"?
It is a design pattern where a class receives its dependencies from an external source (the NestJS container) rather than creating them itself. This makes code more modular, easier to test, and loosely coupled.

### Q3: What is the purpose of the `@Module()` decorator?
It provides metadata that Nest uses to organize the application structure. It defines which controllers belong to the module, which providers are available, and which other modules are imported.

### Q4: Explain the difference between a Controller and a Service.
- **Controller**: The entry point. It handles HTTP routing, extracts parameters from the request, and returns the final response. It should be "thin".
- **Service**: The brain. It contains the actual business logic, database queries, and integration with third-party APIs.

### Q5: What are "DTOs" and why are they important?
DTOs define the contract for the data being sent in a request. They ensure that the data matches the expected format before it ever reaches your service logic, preventing runtime errors and improving security.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Advanced Expressjs](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/04_Advanced_Expressjs/04_Advanced_Expressjs.md) | [🏠 Home](../../README.md) | [Next: Building REST APIs ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/06_Building_REST_APIs/06_Building_REST_APIs.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>