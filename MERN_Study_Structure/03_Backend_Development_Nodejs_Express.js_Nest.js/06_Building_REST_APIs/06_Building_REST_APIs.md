# Building REST APIs

## 📚 Curriculum Checklist
- [x] Routing & Controllers
- [x] Request Lifecycle in NestJS
- [x] Request Validation using class-validator & class-transformer
- [x] Exception Handling & Custom Exceptions

## 📝 Detailed Notes

### 1. Routing & Controllers in NestJS
Controllers are responsible for handling incoming requests. You use decorators to define routes.
```typescript
@Controller('items')
export class ItemsController {
  @Get() // GET /items
  findAll() { return []; }

  @Post() // POST /items
  create(@Body() dto: CreateDto) { return 'Created'; }

  @Get(':id') // GET /items/1
  findOne(@Param('id') id: string) { return `Item ${id}`; }
}
```

### 2. Request Lifecycle in NestJS
Understanding the order of execution is crucial:
1. **Incoming Request**
2. **Middleware**
3. **Guards** (Auth check)
4. **Interceptors** (Pre-processing)
5. **Pipes** (Validation/Transformation)
6. **Controller** (Business logic starts)
7. **Service** (DB calls)
8. **Interceptors** (Post-processing)
9. **Exception Filters** (If an error occurs)
10. **Outgoing Response**

### 3. Request Validation
NestJS uses `class-validator` and `class-transformer` to validate incoming data at runtime.
```typescript
// main.ts
app.useGlobalPipes(new ValidationPipe({
  whitelist: true, // Strips non-allowed properties
  forbidNonWhitelisted: true, // Throws error if non-allowed props found
}));
```

### 4. Exception Handling
NestJS has a built-in **Global Exception Filter** that handles all unhandled exceptions.
- **Custom Exceptions**:
```typescript
throw new HttpException('Forbidden', HttpStatus.FORBIDDEN);
// Or specialized ones:
throw new NotFoundException('User not found');
```

---

## 🎓 Important Interview Questions

### Q1: What is the "Request Lifecycle" in NestJS?
It is the sequence of steps a request goes through before a response is sent. Key stages include Middleware → Guards → Interceptors → Pipes → Controller → Service. Understanding this helps you decide where to put logic (e.g., Auth in Guards, Validation in Pipes).

### Q2: How do you handle validation in NestJS?
By using `ValidationPipe` globally or locally, and defining `DTOs` (Data Transfer Objects) with decorators from `class-validator` like `@IsString()`, `@IsEmail()`, etc.

### Q3: What is the benefit of using a `Global Exception Filter`?
It ensures that your API always returns a consistent error format (e.g., `{ statusCode: 400, message: '...', error: 'Bad Request' }`) regardless of where the error occurred in the code, improving the developer experience for frontend consumers.

### Q4: Explain the `@Body()`, `@Param()`, and `@Query()` decorators.
- `@Body()`: Accesses the request body.
- `@Param()`: Accesses URL parameters (e.g., `id` in `/users/:id`).
- `@Query()`: Accesses URL query strings (e.g., `page` in `/users?page=1`).

### Q5: What is "Dependency Injection" in the context of a Controller?
Controllers don't create their own services. Instead, they "ask" for them in the constructor. NestJS identifies the required service and provides an instance of it. This makes the controller easier to test because you can mock the service.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: NestJS](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/05_NestJS/05_NestJS.md) | [🏠 Home](../../README.md) | [Next: Database ORM ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/07_Database_ORM/07_Database_ORM.md)
