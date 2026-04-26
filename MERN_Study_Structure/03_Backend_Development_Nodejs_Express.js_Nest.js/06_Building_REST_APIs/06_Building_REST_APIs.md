# Building REST APIs
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

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
## **Building REST APIs — MERN Stack Interview Kit**

---

### **1\. Routing & Controllers**

---

**Q1. How does routing work in NestJS and how is it different from Express routing?** `[Fresher]`

* NestJS routing is decorator-based — no separate route files, routes defined directly on controller methods  
* @Controller('users') — sets base path for all routes in that controller, all methods inherit this prefix  
* Method decorators define HTTP method and sub-path — @Get(), @Post(), @Put(), @Patch(), @Delete()  
* Full route \= global prefix \+ controller prefix \+ method path  
* Global prefix — app.setGlobalPrefix('api') in main.ts — prepends /api to all routes  
* Express routing comparison:  
  * Express — router.get('/users/:id', handler) in separate route file  
  * NestJS — @Get(':id') on controller method, route and handler in same place  
* Route path options:  
  * Static — @Get('profile')  
  * Parametric — @Get(':id')  
  * Wildcard — @Get('ab\*cd') matches anything between ab and cd  
  * Multiple routes — @Get(\['/profile', '/me'\]) — array of paths on same handler  
  * Optional parameter — @Get(':id?') — parameter is optional  
* @Controller can also define host binding — @Controller({ host: ':account.example.com' }) — for subdomain routing  
* Route order matters — NestJS registers routes in order they appear, more specific routes should come before wildcards  
* Versioning — NestJS supports URI, header, and media type versioning:  
  * app.enableVersioning({ type: VersioningType.URI })  
  * @Version('1') on controller or method — /v1/users  
  * @Version(\['1', '2'\]) — same handler for multiple versions

**Full Answer:**
In NestJS, routing is **Declarative**. Instead of maintaining a separate `routes.js` file and manually mapping paths to functions, you use decorators directly on the class and its methods. This ensures that the route definition and the business logic are geographically close, making the codebase much easier to navigate for large teams.

**Trap Explained: The "Specific vs Wildcard" Trap**
*"If I have a route `@Get(':id')` and another `@Get('me')`, does the order in the file matter?"*
- **The Answer:** **Yes.** Just like Express, NestJS checks routes in the order they are defined. If you put `@Get(':id')` first, the request for `/users/me` will be caught by the `:id` handler, and `me` will be treated as an ID. **Senior Rule:** Always define static routes *above* dynamic/parametric routes.

---

**Q2. How do you handle route parameters, query params, and request body in NestJS controllers?** `[Fresher]`

* Route parameters — dynamic segments in URL path:  
  * Define in route decorator — @Get(':id') or @Get(':userId/posts/:postId')  
  * Extract with @Param() decorator — @Param('id') id: string  
  * All params as object — @Param() params: Record\<string, string\>  
  * With pipe — @Param('id', ParseIntPipe) id: number — auto-converts string to number  
  * With UUID validation — @Param('id', ParseUUIDPipe) id: string — validates UUID format  
* Query parameters — key-value pairs after ? in URL:  
  * Extract with @Query() — @Query('page') page: string  
  * All query params — @Query() query: QueryParamsDto  
  * With default value — @Query('page', new DefaultValuePipe(1), ParseIntPipe) page: number  
  * ParseIntPipe on query — converts string query param to number automatically  
* Request body — JSON payload in POST/PUT/PATCH:  
  * @Body() body: CreateUserDto — full body, auto-validated if ValidationPipe enabled  
  * @Body('name') name: string — extract single field (avoid — use DTO instead)  
  * Nested body — DTO with nested class, use @ValidateNested and @Type()  
* Headers:  
  * @Headers() headers — all headers as object  
  * @Headers('authorization') auth: string — specific header  
* Combining decorators — one method can use multiple parameter decorators:  
  * @Get(':id') getUserPosts(@Param('id') id: string, @Query('page') page: string) {}  
* ParseIntPipe, ParseFloatPipe, ParseBoolPipe, ParseArrayPipe, ParseUUIDPipe, ParseEnumPipe — built-in transformation pipes for parameters

**Full Answer:**
NestJS provides specific decorators for every part of the request. The most powerful feature here is the use of **Pipes** alongside these decorators. For example, `@Param('id', ParseIntPipe)` doesn't just extract the ID; it automatically validates that it's a number and converts it from a string to a `number` type before it even hits your function body.

**Trap Explained: The "String Type" Trap**
*"In TypeScript, if I define `id: number` in my `@Param()`, will it be a number?"*
- **The Answer:** **No.** TypeScript types disappear at runtime. If you don't use a **Pipe** like `ParseIntPipe`, your `id` variable will actually be a `string` at runtime, which can cause subtle bugs in database queries (e.g., `id === 123` would be false if `id` is `"123"`).

---

**Q3. What is the @Res() decorator and when should you avoid it?** `[1-2 yrs]`

* @Res() — injects underlying HTTP response object (Express Response or Fastify Reply)  
* When you use @Res() — you take full manual control of response, NestJS framework features stop working  
* What breaks when using @Res():  
  * Interceptors — cannot transform response because NestJS no longer controls sending it  
  * Response serialization — ClassSerializerInterceptor stops working  
  * Response mapping — custom interceptors that modify return values stop working  
  * Unit testing becomes harder — must mock response object  
* When it is acceptable to use @Res():  
  * Setting custom cookies — res.cookie('token', value, options)  
  * Streaming files — res.sendFile() or piping streams  
  * Custom redirect logic with computed URL  
  * When you genuinely need low-level control  
* passthrough option — @Res({ passthrough: true }) — lets you use res for cookies or headers while still letting NestJS handle sending the response:  
  * Best of both worlds — use res.cookie() or res.setHeader() but return value normally  
  * Interceptors and serialization continue working  
  * Always prefer passthrough: true when you need to set cookies or headers  
* Correct approach for most cases — just return value from method, NestJS sends it with correct status and content type  
* @Next() — injects next function, almost never needed in NestJS, only for Express middleware compatibility

**Full Answer:**
By default, NestJS handles the response for you (returning an object results in a 200 JSON response). You should **only** use `@Res()` when you need library-specific features (like setting cookies or downloading files). Even then, you should use the `{ passthrough: true }` option so you don't lose the benefits of Nest's built-in Interceptors and Exception Filters.

**Trap Explained: The "Double Response" Error**
- **The Answer:** If you use `@Res()` without `passthrough: true`, and then also `return` a value from the method, you might get a "Headers already sent" error or simply find that your Interceptors aren't working. **Senior Rule:** If you touch the response object manually, you are responsible for calling `res.send()` or `res.json()` unless you use `passthrough`.

---

**Q4. How do you implement sub-resources and nested routing in NestJS?** `[1-2 yrs]`

* Sub-resources — resources that belong to a parent resource (/users/:userId/posts)  
* Approach 1 — include parent param in same controller:  
  * @Controller('users') with @Get(':userId/posts') method  
  * Simple but can make controller large  
* Approach 2 — separate controller with full path:  
  * @Controller('users/:userId/posts')  
  * @Get() — get all posts for user  
  * Access parent param — @Param('userId') userId: string  
  * Cleaner separation but controller name less obvious  
* Approach 3 — module-level prefix composition:  
  * Register PostsController inside UsersModule  
  * Combine prefixes logically  
* Route prefix best practices:  
  * Keep controllers focused — single resource per controller  
  * Avoid deeply nested routes beyond two levels — /users/:id/posts/:postId is fine, deeper gets complex  
  * Use query params instead of deep nesting for filtering — /posts?userId=123 instead of /users/123/posts  
* @Controller can take array of prefixes — @Controller(\['users', 'members'\]) — same controller handles both paths

**Full Answer:**
In REST API design, **Nested Routing** should be used sparingly. While NestJS allows you to do `@Controller('users/:userId/posts')`, a more scalable approach is often to keep controllers flat and use **Query Parameters** for filtering. However, if a resource truly cannot exist without its parent (e.g., a "Comment" on a "Post"), then explicit nesting in the `@Controller` decorator is the standard NestJS pattern.

**Follow-up Clarification: Global Prefix**
*"What if I want all my routes to start with `/api/v1`?"*
- **The Answer:** Don't hardcode this in every controller. Use `app.setGlobalPrefix('api/v1')` in `main.ts`. This makes it easy to change the versioning strategy later without touching every single file.

---

### **2\. Request Lifecycle in NestJS**

---

**Q5. What is the complete request lifecycle in NestJS?** `[1-2 yrs]`

* NestJS request goes through well-defined pipeline of layers before reaching handler and after leaving it  
* Complete order: Incoming HTTP Request ↓ Middleware (app.use or module middleware) ↓ Guards (@UseGuards — runs CanActivate) ↓ Interceptors (pre-handler — runs before() logic) ↓ Pipes (@UsePipes — transform and validate) ↓ Route Handler (controller method executes) ↓ Interceptors (post-handler — runs after() logic, transforms response) ↓ Exception Filters (if any error thrown at any point) ↓ HTTP Response sent to client  
* Each layer has a specific purpose and runs in strict order  
* Middleware — closest to Express middleware, runs before NestJS pipeline even starts, access to req and res, call next()  
* Guards — determine if current request is authorized to proceed, receive ExecutionContext, return boolean or throw exception  
* Interceptors (pre) — run before handler, can modify request context, start timing, add logging  
* Pipes — transform and validate incoming data (route params, query params, body), throw BadRequestException on failure  
* Handler — actual controller method with business logic  
* Interceptors (post) — run after handler returns, can transform response data, complete timing logs  
* Exception Filters — catch exceptions thrown anywhere in pipeline, format and send error response  
* Where global configurations apply — middleware in main.ts configure(), pipes/guards/filters/interceptors via useGlobalPipes/Guards/Filters/Interceptors in main.ts or APP\_PIPE/GUARD/FILTER/INTERCEPTOR tokens in AppModule

**Full Answer:**
The NestJS Request Lifecycle is the "Engine" of the framework. Understanding the order is critical for debugging. If a request is failing validation, you know it's a **Pipe** issue. If a user is getting a 403, it's likely a **Guard** issue. The most important part is that **Exception Filters** sit on the outside of everything, catching errors from any of these stages.

**Trap Explained: The "Middleware vs Guard" order**
*"Can a Guard access data added by an Express Middleware?"*
- **The Answer:** **Yes.** Since Middleware runs first, any modifications it makes to the `req` object (like adding a `req.user`) are available to the Guard. However, the reverse is **not** true—Middleware cannot see what a Guard does because the Guard hasn't run yet.

---

**Q6. What is Middleware in NestJS and how does it differ from Guards and Interceptors?** `[1-2 yrs]`

* Middleware in NestJS — equivalent to Express middleware, runs before the NestJS pipeline  
* Implements NestMiddleware interface — use(req, res, next) method  
* Applied via configure() method in module implementing NestModule interface  
* MiddlewareConsumer — configures which routes middleware applies to:  
  * consumer.apply(LoggerMiddleware).forRoutes('users')  
  * consumer.apply(LoggerMiddleware).forRoutes({ path: 'users', method: RequestMethod.GET })  
  * consumer.apply(LoggerMiddleware).forRoutes(UsersController)  
  * consumer.apply(LoggerMiddleware).exclude('auth/login').forRoutes(UsersController)  
* Functional middleware — simple function (req, res, next) \=\> {} for stateless middleware, no DI needed  
* Class middleware — implements NestMiddleware, can inject dependencies via DI  
* Key differences: Middleware vs Guards:  
  * Middleware runs before NestJS DI pipeline — no access to ExecutionContext or route metadata  
  * Guards run inside DI pipeline — have ExecutionContext, can read route metadata and custom decorators  
  * Middleware cannot easily know which handler will process request  
  * Guards know exactly which handler and class the request is targeting  
* Middleware vs Interceptors:  
  * Middleware only runs before handler — no post-processing capability  
  * Interceptors run before AND after handler — can modify both request context and response  
  * Middleware operates on raw req/res objects  
  * Interceptors operate on NestJS ExecutionContext and RxJS Observables  
* When to use middleware — request logging, body parsing for specific routes, legacy Express middleware integration, CORS handling (though helmet/cors can also be used as app.use())

**Full Answer:**
Middleware should be used for **generic, low-level** tasks that don't care about NestJS's high-level logic (like logging the raw IP address or parsing cookies). For anything that requires knowledge of the "Route" or "Role" (like Authentication/Authorization), you should always use **Guards** or **Interceptors** because they have access to the `ExecutionContext`.

**Trap Explained: The "DI in Middleware" Trap**
*"Can I inject a Service into an Express-style functional middleware?"*
- **The Answer:** **No.** If you need **Dependency Injection** (e.g., you need to inject a `DatabaseService` into your logging middleware), you must use a **Class-based Middleware** that implements `NestMiddleware`. Functional middleware is strictly for stateless logic.

---

**Q7. How do Guards work in NestJS and how do you implement authentication with them?** `[1-2 yrs]`

* Guards implement CanActivate interface — single canActivate(context: ExecutionContext) method  
* Return true — request proceeds to next stage  
* Return false — request rejected with 403 Forbidden automatically  
* Throw exception — that specific exception returned to client (401, 403, etc.)  
* Guards have access to ExecutionContext — can read route metadata, handler, class, request  
* ExecutionContext methods:  
  * context.switchToHttp().getRequest() — get underlying HTTP request  
  * context.getHandler() — get route handler method reference  
  * context.getClass() — get controller class reference  
  * context.getType() — 'http', 'ws', 'rpc' — works in HTTP, WebSocket, microservices  
* JWT Auth Guard implementation:  
  * Extract token from Authorization header — req.headers.authorization?.split(' ')\[1\]  
  * Verify with JwtService or jsonwebtoken  
  * Attach decoded user to request — req.user \= decoded  
  * Return true if valid, throw UnauthorizedException if not  
* Using @nestjs/jwt — JwtService.verify() or JwtService.verifyAsync() — returns payload or throws  
* Reading metadata in guards — use Reflector service:  
  * Reflector.getAllAndOverride(key, \[context.getHandler(), context.getClass()\])  
  * Reads metadata set by @SetMetadata() or custom decorators  
  * Pattern — if route has @Public() metadata, skip auth check  
* IS\_PUBLIC\_KEY pattern — define @Public() decorator with SetMetadata, check in guard, skip JWT verification for public routes  
* Apply guards — @UseGuards(JwtAuthGuard) on controller or method, or globally via APP\_GUARD token

**Full Answer:**
Guards are the primary way to handle **Authentication** and **Authorization** in NestJS. Unlike Middleware, they have access to the `Reflector`, which allows them to read custom metadata (like `@Roles('admin')`) from the specific route being called. This makes them incredibly dynamic—one single `AuthGuard` can behave differently for every route in your application.

**Trap Explained: The "403 vs 401" Trap**
- **The Answer:** By default, if a Guard returns `false`, NestJS throws a **403 Forbidden**. However, for authentication, you usually want a **401 Unauthorized**. **The Fix:** In your Guard, don't just return `false`; explicitly `throw new UnauthorizedException()` so the client gets the correct semantic status code.

---

**Q8. How do Interceptors work and what are common use cases?** `[2-3 yrs]`

* Interceptors implement NestInterceptor interface — intercept(context, next: CallHandler) method  
* CallHandler — has handle() method that returns Observable of response  
* RxJS-based — use pipe(), map(), tap(), catchError(), timeout() operators on Observable  
* Returning next.handle() without modification — passthrough, no change to request or response  
* Interceptor structure:  
  * Before handler — code before next.handle() call — runs before route handler  
  * next.handle() — calls the route handler  
  * pipe() on result — operators run after handler returns response  
  * tap() — side effects without modifying response (logging, metrics)  
  * map() — transform response data  
  * catchError() — catch and transform errors  
  * timeout() — throw error if handler takes too long  
* Common use cases:  
  * Response transformation — wrap all responses in consistent envelope { success: true, data: result }  
  * Logging — log method name, execution time, user, status code for every request  
  * Caching — return cached value without calling handler if cache hit  
  * Performance tracking — record start time before handler, log duration after  
  * Excluding sensitive fields — remove password fields from user responses  
  * Timeout — throw RequestTimeoutException if handler exceeds time limit  
* ClassSerializerInterceptor — uses class-transformer to serialize response, respects @Exclude() and @Expose() decorators on entity/response DTO classes  
* Apply interceptors — @UseInterceptors() on method, controller, or globally via APP\_INTERCEPTOR token

**Full Answer:**
Interceptors use **RxJS Observables** to wrap the request/response stream. This is incredibly powerful because it allows you to manipulate the data *after* the controller has finished its work but *before* the response is sent to the client. It's the standard way to implement a **Global Response Wrapper** (e.g., ensuring every successful response is wrapped in a `{ data: ... }` object).

**Trap Explained: The "Observable" Learning Curve**
*"Do I need to be an RxJS expert to use Interceptors?"*
- **The Answer:** **No**, but you must understand that if you don't return `next.handle()`, the request will **never finish**. You are essentially "blocking" the stream. Always ensure you are returning the observable, even if you are just using `.pipe(tap(...))` for side effects like logging.

---

### **3\. Request Validation using class-validator & class-transformer**

---

**Q9. What is class-validator and how does it work with NestJS?** `[Fresher]`

* class-validator — decorator-based validation library for TypeScript classes  
* Works perfectly with NestJS DTOs and ValidationPipe  
* npm install class-validator class-transformer  
* How it works:  
  * Define DTO class with validation decorators on properties  
  * ValidationPipe calls validate() from class-validator on incoming body  
  * class-transformer first converts plain JSON object to DTO class instance  
  * class-validator runs all decorators on the instance  
  * If any violation — ValidationPipe throws BadRequestException with detailed errors  
  * If valid — controller receives validated, typed DTO instance  
* Important string validators:  
  * @IsString() — must be string type  
  * @IsNotEmpty() — string must not be empty after trimming  
  * @IsEmail() — valid email format  
  * @IsUrl() — valid URL  
  * @MinLength(n) / @MaxLength(n) — string length constraints  
  * @Matches(regex) — must match regular expression  
  * @IsAlpha() / @IsAlphanumeric() — character type constraints  
  * @IsUUID() — valid UUID format  
  * @IsEnum(EnumType) — must be valid enum value  
* Number validators:  
  * @IsNumber() — must be number type  
  * @IsInt() — must be integer  
  * @Min(n) / @Max(n) — numeric range  
  * @IsPositive() / @IsNegative()  
* Boolean validators — @IsBoolean()  
* Array validators:  
  * @IsArray() — must be array  
  * @ArrayMinSize(n) / @ArrayMaxSize(n)  
  * @ArrayNotEmpty()  
  * @ArrayUnique() — no duplicate elements  
* Date validators — @IsDate() / @IsDateString()  
* Conditional validators — @ValidateIf(condition) — only validate if condition is true  
* Custom error messages — @IsEmail({}, { message: 'Please provide a valid email address' })  
* Groups — @IsString({ groups: \['create'\] }) — apply different validation for create vs update

**Full Answer:**
`class-validator` provides a declarative way to validate incoming data. By using decorators on your DTO (Data Transfer Object), you define the "Contract" that the client must follow. When combined with NestJS's `ValidationPipe`, this validation happens **before** your controller method is even called, ensuring that your business logic only ever receives clean, valid data.

**Trap Explained: The "Empty Object" Trap**
*"If a user sends an empty JSON body `{}`, will `@IsString()` catch it?"*
- **The Answer:** **No.** If a property is missing entirely, most validators (except `@IsDefined()` or `@IsNotEmpty()`) will simply ignore it. **Senior Rule:** Always use `@IsNotEmpty()` or `@IsDefined()` alongside your type validators if the field is mandatory.

---

**Q10. What is class-transformer and how does it work with class-validator?** `[1-2 yrs]`

* class-transformer — transforms plain JavaScript objects to class instances and vice versa  
* Two main functions:  
  * plainToInstance(ClassType, plainObject) — convert plain JSON to class instance with type info  
  * instanceToPlain(instance) — convert class instance to plain object (for serialization)  
* Why needed alongside class-validator:  
  * Request body arrives as plain JSON object — no class instance, no type information  
  * class-validator decorators only work on class instances  
  * class-transformer creates class instance from plain object — then class-validator can validate  
* transform: true in ValidationPipe — enables class-transformer auto-conversion  
* @Transform() decorator — custom transformation logic on a property:  
  * @Transform(({ value }) \=\> value.trim()) — trim whitespace  
  * @Transform(({ value }) \=\> value.toLowerCase()) — normalize to lowercase  
  * @Transform(({ value }) \=\> parseInt(value)) — convert string to number  
  * @Transform(({ value }) \=\> new Date(value)) — convert string to Date  
* @Type() decorator — tell class-transformer what class to use for nested objects or arrays:  
  * @Type(() \=\> AddressDto) on nested object property  
  * @Type(() \=\> Number) on array of numbers — converts each element  
  * Essential for nested DTO validation to work correctly  
* @Expose() — mark which properties to include when using excludeExtraneousValues  
* @Exclude() — exclude property from serialization (good for removing password from responses)  
* @Expose({ name: 'full\_name' }) — rename property during serialization  
* enableImplicitConversion — ValidationPipe transformOptions option, auto-converts based on TypeScript types without @Type() decorator  
* ClassSerializerInterceptor — uses instanceToPlain with class-transformer to serialize response, works with @Exclude and @Expose decorators

**Full Answer:**
`class-transformer` is the bridge between the raw JSON string sent by the client and the rich TypeScript class used by your code. It handles the "casting" of types. This is crucial because HTTP is a text-based protocol; everything arrives as a string. `class-transformer` ensures that your "Date" fields are actually `Date` objects and your "Price" fields are `numbers`.

**Trap Explained: The "Nested Object" Failure**
*"I added validation to my nested `AddressDto`, but it's not working. Why?"*
- **The Answer:** You likely forgot the **`@Type(() => AddressDto)`** decorator. Without this, `class-transformer` doesn't know that the nested object should be an instance of `AddressDto`. It leaves it as a plain JS object, and since `class-validator` only works on *instances*, the validation is skipped. Always use `@Type()` for nested objects!

---

**Q11. How do you validate nested objects and arrays in NestJS DTOs?** `[1-2 yrs]`

* Simple flat DTO — all primitives, works automatically with ValidationPipe  
* Nested object — requires special handling for deep validation:  
  * @ValidateNested() — tells class-validator to recursively validate the nested object  
  * @Type(() \=\> NestedDto) — tells class-transformer what class to instantiate for the property  
  * Both decorators required together — @ValidateNested without @Type does not work  
* Nested array of objects:  
  * @ValidateNested({ each: true }) — validate each item in array  
  * @Type(() \=\> ItemDto) — each array item transformed to ItemDto instance  
  * @IsArray() — ensure the field is actually an array  
* Optional nested object:  
  * @IsOptional() before @ValidateNested() — skips validation if property absent  
  * @ValidateNested() — validates if present  
  * @Type(() \=\> AddressDto)  
* Deeply nested — chain @ValidateNested and @Type at each level  
* Array of primitives — @IsArray() with @IsString({ each: true }) — each: true option on primitive validators  
* Union types — class-validator doesn't natively support union types, use @ValidateIf and custom validators  
* Discriminated unions — use @Type with discriminator option for polymorphic nested types  
* Common mistake — forgetting @Type() decorator — nested object stays as plain object, class-validator decorators never run on it

**Full Answer:**
Validating nested data requires the "Power Duo" of decorators: **`@ValidateNested()`** (from class-validator) and **`@Type()`** (from class-transformer). If you have an array of objects, you must also use `{ each: true }`. This tells NestJS: *"Don't just check if this is an array; go inside every element, turn it into a class instance, and run the validation rules defined inside that class."*

**Trap Explained: The "Partial Update" Trap**
*"If I use `PartialType` for nested objects, will the nested fields also become optional?"*
- **The Answer:** **No.** `PartialType` only works on the top-level properties. If your `UserDto` has a nested `AddressDto`, and you make `UpdateUserDto` a `PartialType`, the `address` field becomes optional, but if the user *does* send an address, all fields inside `AddressDto` will still be required unless you specifically create a `PartialAddressDto` as well.

---

**Q12. How do you create custom validators in NestJS?** `[2-3 yrs]`

* Sometimes built-in validators are not enough — custom business logic validation needed  
* Two approaches — custom decorator with @ValidatorConstraint, or custom pipe  
* @ValidatorConstraint approach:  
  * Implement ValidatorConstraintInterface — validate(value, args) method returns boolean  
  * validate method — contains validation logic, returns true if valid, false if invalid  
  * defaultMessage method — returns error message when validation fails  
  * @ValidatorConstraint({ name: 'isUnique', async: true }) — async: true for DB lookups  
  * Create custom decorator — @registerDecorator calling validate with the constraint  
  * Use on DTO property like any built-in decorator  
* Async custom validators — for uniqueness checks against DB:  
  * async validate(email: string) — query DB, return true if unique  
  * Inject repository or service using getFromContainer() or constructor injection in NestJS way  
  * @Injectable() on constraint class when using DI — register as provider in module  
  * useContainer(app.select(AppModule), { fallbackOnErrors: true }) in main.ts — enables DI in class-validator  
* Custom Pipe approach:  
  * Implement PipeTransform interface — transform(value, metadata) method  
  * throw BadRequestException with custom message on validation failure  
  * Return transformed value on success  
  * Apply with @UsePipes or directly on @Body() — @Body(new CustomPipe())  
  * Good for cross-field validation (comparing two fields) or complex transformation  
* Cross-field validation:  
  * class-validator runs per-field — cross-field is harder  
  * Custom @ValidatorConstraint that receives entire object  
  * Or validate in service after DTO validation passes

**Full Answer:**
Custom validators allow you to inject domain-specific logic (like "Is this username taken?") directly into the request validation layer. The standard way is using the **`@ValidatorConstraint`** interface. This keeps your controllers clean because invalid requests are rejected with a 400 error before they even touch your service methods.

**Trap Explained: The "DI in Validator" Trap**
*"Can I inject my `UsersService` into a class-validator constraint?"*
- **The Answer:** **Yes**, but it requires a special setup. You must call `useContainer(app.select(AppModule), { fallbackOnErrors: true })` in your `main.ts`. Without this, `class-validator` will use its own internal container and won't be able to resolve your NestJS dependencies, causing a "Service not found" error.

---

**Q13. What are DTOs and how do you reuse them with mapped types?** `[1-2 yrs]`

* DTO — Data Transfer Object, plain class that defines shape and validation rules for incoming data  
* Why DTOs:  
  * Explicit contract — clear definition of expected input  
  * Auto-validation with ValidationPipe  
  * TypeScript types for IDE support  
  * Documentation — swagger reads DTOs to generate API docs  
  * Security — whitelist: true strips undeclared properties  
* Without mapped types — create separate CreateUserDto and UpdateUserDto with duplicated fields  
* @nestjs/mapped-types — utility for creating DTOs based on other DTOs:  
  * PartialType(CreateUserDto) — all fields optional (for PATCH/update operations)  
  * PickType(CreateUserDto, \['email', 'password'\] as const) — only specific fields  
  * OmitType(CreateUserDto, \['role'\] as const) — all fields except specified ones  
  * IntersectionType(CreateUserDto, CreateAddressDto) — combine two DTOs  
  * Can compose — class UpdateUserDto extends OmitType(PartialType(CreateUserDto), \['id'\])  
* @nestjs/swagger versions — PartialType from @nestjs/swagger instead of @nestjs/mapped-types when using Swagger, preserves API decorator metadata  
* Response DTOs — define shape of response data:  
  * Use with ClassSerializerInterceptor and @Expose()/@Exclude() to control what is returned  
  * Different from request DTOs — response DTOs focus on what goes out, request DTOs on what comes in  
* Best practice — one DTO file per operation — create-user.dto.ts, update-user.dto.ts, query-user.dto.ts, user-response.dto.ts

**Full Answer:**
DTOs are the "Truth" of your API. Using **Mapped Types** allows you to stay **DRY** (Don't Repeat Yourself). Instead of writing a new class for an update operation, you simply `extends PartialType(CreateUserDto)`. This ensures that if you add a field to the creation DTO, it automatically exists (as optional) in the update DTO.

**Trap Explained: The "Mapped Types & Swagger" Trap**
*"Why are my fields missing from Swagger when I use `PartialType`?"*
- **The Answer:** There are two `PartialType` imports. One is from `@nestjs/mapped-types` and the other is from **`@nestjs/swagger`**. If you want your Swagger documentation to automatically detect the fields in your partial DTOs, you **must** import it from the Swagger package.

---

### **4\. Exception Handling & Custom Exceptions**

---

**Q14. How does exception handling work in NestJS?** `[Fresher]`

* NestJS has built-in global exception filter — catches all unhandled exceptions  
* Two categories of exceptions NestJS handles:  
  * HttpException and subclasses — formatted as proper HTTP error response automatically  
  * Any other exception — returned as 500 Internal Server Error  
* HttpException constructor — (response: string | object, status: number)  
  * throw new HttpException('Forbidden', HttpStatus.FORBIDDEN)  
  * throw new HttpException({ message: 'Custom error', code: 'ERR\_001' }, 403\)  
* HttpStatus enum — provides all HTTP status code constants — HttpStatus.NOT\_FOUND, HttpStatus.CREATED etc.  
* Built-in HTTP exceptions — all extend HttpException:  
  * BadRequestException — 400 — invalid input data  
  * UnauthorizedException — 401 — not authenticated  
  * ForbiddenException — 403 — authenticated but not authorized  
  * NotFoundException — 404 — resource not found  
  * MethodNotAllowedException — 405  
  * NotAcceptableException — 406  
  * RequestTimeoutException — 408  
  * ConflictException — 409 — duplicate resource  
  * GoneException — 410 — resource no longer available  
  * PayloadTooLargeException — 413  
  * UnsupportedMediaTypeException — 415  
  * UnprocessableEntityException — 422 — validation failed  
  * TooManyRequestsException — 429 — rate limit exceeded  
  * InternalServerErrorException — 500  
  * NotImplementedException — 501  
  * BadGatewayException — 502  
  * ServiceUnavailableException — 503  
  * GatewayTimeoutException — 504  
* Default error response format:  
  * statusCode — HTTP status number  
  * message — error message string or array  
  * error — HTTP status text

**Full Answer:**
NestJS handles exceptions through a global **Exception Layer**. You should never manually do `res.status(404).send(...)`. Instead, you `throw new NotFoundException()`. This is cleaner, more readable, and allows you to centralize your error logging and formatting in a single **Exception Filter**.

**Trap Explained: The "Generic Error" Trap**
*"What happens if I do `throw new Error('Something went wrong')`?"*
- **The Answer:** NestJS will catch it, but because it's not an `HttpException`, it will return a generic **500 Internal Server Error** to the client. **Senior Rule:** Always use specific semantic exceptions (like `ConflictException`) so the client knows exactly why the request failed.

---

**Q15. How do you create custom exceptions in NestJS?** `[1-2 yrs]`

* Extend HttpException for HTTP-related custom exceptions  
* Extend base Error for domain/business logic exceptions (handled by custom filter)  
* Basic custom exception — extend HttpException with preset status and message:  
  * super(message || 'User not found', HttpStatus.NOT\_FOUND) in constructor  
  * throw new UserNotFoundException() anywhere in code — consistent message  
  * throw new UserNotFoundException('User with email not found') — custom message  
* Custom exception with extra data:  
  * Add custom properties — errorCode, timestamp, details  
  * Pass structured object to super() — { message, errorCode, timestamp }  
  * Client receives structured error with extra fields for handling on frontend  
* Domain exception hierarchy — organize exceptions by domain:  
  * Base domain exception — class AppException extends HttpException  
  * User exceptions extend AppException — UserNotFoundException, UserAlreadyExistsException  
  * Auth exceptions extend AppException — InvalidCredentialsException, TokenExpiredException  
  * Payment exceptions — PaymentFailedException, InsufficientFundsException  
* Benefits of custom exceptions:  
  * Throw meaningful exceptions from service layer — NotFoundException, not generic Error  
  * Consistent error codes — frontend can handle specific codes programmatically  
  * No HTTP knowledge needed in service layer — service throws domain exceptions, filter handles HTTP mapping  
  * Better logging — catch specific exception types in filters  
  * Self-documenting code — throw new UserNotFoundException() reads clearly

**Full Answer:**
Custom exceptions allow you to create a **Domain-Specific Language** for errors. Instead of throwing a generic 404, you throw a `UserNotFoundException`. This makes your code self-documenting and allows you to attach **Custom Error Codes** (e.g., `ERR_USER_001`) that the frontend can use to show specific localized messages.

**Trap Explained: The "Response Shape" Trap**
- **The Answer:** When you create a custom exception, ensure you are passing an object to the `super()` call if you want custom fields. If you only pass a string, NestJS will wrap it in its default `{ statusCode, message, error }` shape, potentially hiding your custom fields.

---

**Q16. How do you create custom Exception Filters in NestJS?** `[1-2 yrs]`

* Exception filters — intercept exceptions, transform into formatted HTTP response  
* Implement ExceptionFilter interface — catch(exception, host: ArgumentsHost) method  
* @Catch() decorator — specify which exception type(s) to catch:  
  * @Catch(HttpException) — catch only HttpException and subclasses  
  * @Catch(NotFoundException) — catch only NotFoundException  
  * @Catch() — catch ALL exceptions (global catch-all filter)  
  * @Catch(HttpException, RpcException) — catch multiple types  
* ArgumentsHost — access to execution context, switch between HTTP/WS/RPC:  
  * host.switchToHttp().getRequest() — get request object  
  * host.switchToHttp().getResponse() — get response object  
  * host.getType() — check context type  
* HttpException filter implementation:  
  * Get status from exception.getStatus()  
  * Get response from exception.getResponse() — string or object  
  * Construct consistent error response with statusCode, timestamp, path, message  
  * Send with response.status(status).json(errorResponse)  
* Catch-all filter for unhandled errors:  
  * @Catch() with no argument — catches everything including non-HTTP errors  
  * Check if exception is HttpException — handle accordingly  
  * Otherwise return 500 with generic message — hide internal error details from client  
  * Log full error with stack trace internally  
  * Critical in production — prevents raw error details leaking to client  
* Applying filters — four levels, from narrowest to widest scope:  
  * Method level — @UseFilters(new HttpExceptionFilter()) on specific route handler  
  * Controller level — @UseFilters(new HttpExceptionFilter()) on controller class  
  * Global via main.ts — app.useGlobalFilters(new HttpExceptionFilter()) — no DI access  
  * Global via module — { provide: APP\_FILTER, useClass: HttpExceptionFilter } — DI works here  
* Prefer APP\_FILTER token over app.useGlobalFilters when filter needs injected dependencies

**Full Answer:**
Exception Filters are the "Final Guardians" of your API. They allow you to transform any error—even raw database errors or unexpected crashes—into a **Predictable JSON Format**. For a production app, you should always have a global exception filter to ensure that internal details (like SQL queries or file paths) are never leaked to the client.

**Trap Explained: The "Logging" Trap**
*"Where should I log my errors? In the service or the filter?"*
- **The Answer:** **The Filter.** Logging inside every service leads to duplicated code and missed errors. By logging inside a global Exception Filter, you are guaranteed to catch and log **100%** of the errors that occur in your request pipeline.

---

**Q17. How do you achieve a consistent error response format across a NestJS API?** `[2-3 yrs]`

* Problem — different parts of app throw different exception types with inconsistent response shapes  
  * ValidationPipe throws — { statusCode, message: string\[\], error }  
  * Manual throws — { statusCode, message: string }  
  * Unhandled errors — { statusCode: 500, message: 'Internal server error' }  
  * All look different to frontend  
* Solution — single global catch-all exception filter that formats all errors consistently  
* Consistent error response interface:  
  * success: false — always false for errors  
  * statusCode — HTTP status number  
  * message — human-readable error message  
  * errors — array of field-level errors (from ValidationPipe)  
  * errorCode — machine-readable code for frontend handling  
  * timestamp — ISO string  
  * path — request URL  
* Handling ValidationPipe errors in filter:  
  * ValidationPipe throws BadRequestException with response.message as string array  
  * Check if exception is BadRequestException with array message  
  * Map array to errors field with field names and messages  
  * Extract from exception.getResponse() which returns { message: string\[\], error, statusCode }  
* Handling domain exceptions:  
  * Custom exceptions have errorCode and structured message  
  * Extract from exception.getResponse()  
  * Spread into consistent format  
* Handling unknown errors:  
  * Not instanceof HttpException — internal error  
  * Log full error with stack trace — never lose error details internally  
  * Return generic 500 message — never expose stack trace or internal details to client  
  * NODE\_ENV check — in development can include error message, in production always generic  
* Registration — APP\_FILTER in AppModule providers with useClass pointing to global filter

**Full Answer:**
A professional API should always return a **Consistent Error Envelope**. This means whether it's a 404, a 400, or a 500, the JSON structure is the same. This allows your frontend team to write a single piece of error-handling code (like a global Axios interceptor) that can handle all API failures predictably.

**Trap Explained: The "Development vs Production" Leak**
- **The Answer:** In development, you *want* to see the error message (e.g., "Cannot read property 'id' of undefined"). In production, you **must** hide this. **The Fix:** In your exception filter, check `process.env.NODE_ENV`. If it's production, overwrite the message with a generic "Something went wrong" for all non-HTTP exceptions.

---

### **Bonus Questions (Added for Complete Coverage)**

---

**Q18. What is the difference between @Body(), @Query(), and @Param() in terms of validation?** `[Fresher]`

* @Body() — full request body, validated against DTO class by ValidationPipe automatically when transform: true set  
* @Query() — query string params, all strings by default, use ParseIntPipe/ParseBoolPipe individually or define Query DTO class  
* @Param() — route params, always strings unless pipe applied, use ParseIntPipe, ParseUUIDPipe directly  
* Validating Query DTO:  
  * Define class QueryParamsDto with class-validator decorators  
  * @IsOptional() on all fields — query params are usually optional  
  * @Type(() \=\> Number) on numeric fields — transform string to number  
  * @IsInt(), @Min(1) for page param  
  * Use @Query() queryParams: QueryParamsDto — whole object validated  
* Pipe application at different levels:  
  * Global — ValidationPipe in main.ts applies to all @Body() params  
  * Route level — @UsePipes(ValidationPipe) on method  
  * Param level — @Param('id', ParseIntPipe) — pipe on specific parameter  
  * All three approaches valid, global most common for body, param-level for individual params  
* Common validation pattern for paginated endpoints:  
  * page: @IsOptional() @Type(() \=\> Number) @IsInt() @Min(1) — default 1  
  * limit: @IsOptional() @Type(() \=\> Number) @IsInt() @Min(1) @Max(100) — default 10  
  * sortBy: @IsOptional() @IsString() @IsIn(\['createdAt', 'name', 'price'\])  
  * order: @IsOptional() @IsEnum(SortOrder) — 'asc' or 'desc'

**Full Answer:**
While they all use the same `ValidationPipe`, the implementation differs slightly. **`@Body()`** validation is usually "Implicit" (global pipe), whereas **`@Query()`** and **`@Param()`** often require "Explicit" pipes like `ParseIntPipe` because query strings are *always* strings. For complex query logic (like search/filters), it's a best practice to create a `SearchQueryDto` and use `@Query() query: SearchQueryDto`.

**Trap Explained: The "Boolean Query" Trap**
*"If I send `?active=false`, will my Query DTO see it as a boolean `false`?"*
- **The Answer:** **No.** It will be the string `"false"`. Even if you use `ParseBoolPipe`, Express/Fastify might interpret it as truthy because any non-empty string is true. **The Fix:** Use `ParseBoolPipe` explicitly or use `class-transformer`'s `@Type(() => Boolean)` and enable `transform: true` in your global pipe.

---

**Q19. How do you document API endpoints with Swagger in NestJS?** `[1-2 yrs]`

* @nestjs/swagger — official Swagger integration for NestJS  
* npm install @nestjs/swagger swagger-ui-express  
* Setup in main.ts:  
  * DocumentBuilder — fluent API for configuring OpenAPI document  
  * setTitle, setDescription, setVersion, addBearerAuth  
  * SwaggerModule.createDocument(app, config) — generates OpenAPI spec  
  * SwaggerModule.setup('api-docs', app, document) — serve Swagger UI  
* Controller and method decorators:  
  * @ApiTags('users') — group endpoints under tag in Swagger UI  
  * @ApiOperation({ summary: 'Get user by ID', description: '...' }) — describe endpoint  
  * @ApiResponse({ status: 200, description: 'Success', type: UserResponseDto }) — document response  
  * @ApiNotFoundResponse({ description: 'User not found' }) — shorthand for specific status  
  * @ApiCreatedResponse() — 201 shorthand  
  * @ApiBadRequestResponse() — 400 shorthand  
* DTO decorators — auto-generate request/response schemas:  
  * @ApiProperty({ description: 'User email', example: 'user@example.com' }) — document DTO field  
  * @ApiPropertyOptional() — optional field documentation  
  * type, enum, isArray, minimum, maximum, minLength, maxLength options  
  * @ApiHideProperty() — hide field from Swagger docs  
* Authentication in Swagger:  
  * addBearerAuth() in DocumentBuilder  
  * @ApiBearerAuth() on protected controllers or routes  
  * Authorize button in Swagger UI — enter JWT once, sent with all requests  
* Using mapped types from @nestjs/swagger — preserves @ApiProperty decorators in derived DTOs  
* Disable in production — conditional Swagger setup based on NODE\_ENV

**Full Answer:**
Swagger is **Mandatory** for any professional REST API. It serves as the bridge between the backend and the frontend. Instead of writing documentation manually, NestJS generates an interactive UI directly from your DTOs and Controller decorators. This ensures that your documentation is **always in sync** with your actual code.

**Trap Explained: The "Empty Schemas" Trap**
*"Why are my DTOs showing up as empty objects in Swagger?"*
- **The Answer:** Swagger cannot "see" your validation decorators. You **must** add the **`@ApiProperty()`** decorator to every field in your DTO that you want to appear in the documentation. **Senior Tip:** If you have many DTOs, use the `@nestjs/swagger` CLI plugin to automatically add these decorators at build time.

---

**Q20. What is the APP\_PIPE, APP\_GUARD, APP\_FILTER, APP\_INTERCEPTOR pattern?** `[2-3 yrs]`

* Problem with useGlobalPipes/Guards/Filters/Interceptors in main.ts — registered outside NestJS DI context:  
  * Cannot inject services or other providers into them  
  * No access to ConfigService, LoggerService, DatabaseService etc.  
* Solution — register global enhancers as providers in AppModule using special tokens:  
  * APP\_PIPE — register global pipe with DI support  
  * APP\_GUARD — register global guard with DI support  
  * APP\_FILTER — register global exception filter with DI support  
  * APP\_INTERCEPTOR — register global interceptor with DI support  
* Provider registration pattern:  
  * provide: APP\_GUARD (imported from @nestjs/core)  
  * useClass: JwtAuthGuard  
  * NestJS registers as global and injects it with full DI support  
  * JwtAuthGuard can now inject JwtService, ConfigService, UsersService etc.  
* Multiple global providers — add multiple entries with same token, all applied:  
  * APP\_GUARD for JwtAuthGuard and RolesGuard — both run for every request  
  * APP\_INTERCEPTOR for LoggingInterceptor and TransformResponseInterceptor  
  * Order matters — guards registered first run first  
* Order of execution for multiple global guards:  
  * Registered in providers array order — first provider runs first  
  * All must return true for request to proceed  
* Difference from useGlobal methods:  
  * useGlobalPipes — no DI, simple case only  
  * APP\_PIPE — full DI, recommended for anything that needs injected dependencies  
  * Use useGlobal only for simple stateless enhancers with no dependencies

**Full Answer:**
This is the "Senior" way to register global enhancers. While `app.useGlobalGuards()` is fine for simple tutorials, a real application almost always needs its Guards/Pipes to access the database or configuration. By using the **`APP_GUARD`** token in your `AppModule`, you allow NestJS to instantiate the guard with full access to the **Dependency Injection** system.

**Trap Explained: The "main.ts vs Module" Trap**
- **The Answer:** If you register a guard in `main.ts`, you cannot `inject` anything into its constructor. If you register it in `AppModule` using `APP_GUARD`, you can inject whatever you want. **Senior Rule:** Always prefer the `APP_` token pattern for any enhancer that isn't 100% stateless.

---

---

### **5\. Advanced API Patterns & Optimization**

---

**Q21. What are the different API Versioning strategies supported by NestJS?** `[2-3 yrs]`

* **URI Versioning:** `/v1/users` — most common, version in URL path.
* **Header Versioning:** `x-api-version: 1` — version passed in custom header.
* **Media Type Versioning:** `Accept: application/vnd.example.v1+json`.
* **Global vs Local:** Versioning can be enabled globally or per-controller/method.

**Full Answer:**
NestJS has a first-class `VersioningModule`. By calling `app.enableVersioning()`, you can choose your strategy. **URI Versioning** is the industry standard because it's the most transparent for developers and easier to cache. However, **Header Versioning** is often preferred for "cleaner" URLs in enterprise internal APIs.

**Trap Explained: The "Version 0" Trap**
*"What happens if I don't provide a version to a versioned API?"*
- **The Answer:** By default, it will return a 404. You must use the `VERSION_NEUTRAL` constant if you want a specific route to be available across all versions, or define a default version in your configuration.

---

**Q22. How do you implement Rate Limiting (Throttling) in NestJS?** `[2-3 yrs]`

* **ThrottlerModule:** The official package for rate limiting.
* **ThrottlerGuard:** A global or route-specific guard that tracks request counts.
* **Storage:** Can use in-memory (default) or Redis (recommended for production).
* **TTL & Limit:** Define how many requests are allowed within a specific time window.

**Full Answer:**
To protect your API from brute-force attacks or DDoS, we use the `@nestjs/throttler` package. We define a "Limit" (e.g., 10 requests) and a "TTL" (e.g., 60 seconds). If a user exceeds this, the `ThrottlerGuard` will automatically throw a `429 Too Many Requests` error.

**Trap Explained: The "Load Balancer IP" Trap**
*"Why is my rate limiter blocking everyone after I deployed to AWS/Nginx?"*
- **The Answer:** Your rate limiter is likely seeing the IP of the **Load Balancer**, not the client. You **must** enable `trust proxy` in your Express/Fastify instance so that NestJS can read the real client IP from the `X-Forwarded-For` header.

---

**Q23. What is the ClassSerializerInterceptor and why is it important for security?** `[2-3 yrs]`

* **Purpose:** To automatically transform class instances into plain JSON objects.
* **Decorators:** Works with `@Exclude()`, `@Expose()`, and `@Groups()`.
* **Security:** Ensures that sensitive fields (like `password` or `internalNote`) are never sent to the client.

**Full Answer:**
`ClassSerializerInterceptor` is your "Security Filter." By applying it globally, you ensure that even if you return a full `User` object from your service, the `password` field will be stripped out before it reaches the network (provided you have `@Exclude()` on that property in your DTO/Entity). This prevents accidental data leaks.

**Trap Explained: The "Plain Object" Trap**
*"I added `@Exclude()` to my DTO, but the field is still showing up. Why?"*
- **The Answer:** `ClassSerializerInterceptor` only works on **Class Instances**. If your service returns a plain JavaScript object `{ ... }` instead of `new UserDto(...)`, the interceptor will ignore it. You **must** use `class-transformer` or manually instantiate the class for the interceptor to work.

---

**Q24. How do you handle File Uploads and Streams in NestJS?** `[2-3 yrs]`

* **Multer:** NestJS uses Multer under the hood for `multipart/form-data`.
* **FileInterceptor:** The built-in interceptor to handle a single file upload.
* **StreamableFile:** A special NestJS class to handle large file downloads efficiently without loading them into RAM.

**Full Answer:**
For uploads, we use the `@FileInterceptor('file')` decorator on our controller method. For downloads, we use the `StreamableFile` class. This is superior to `res.send()` because it handles the **Node.js Stream** pipe automatically, ensuring that your server's memory usage stays low even when serving large files (like PDFs or Videos).

**Trap Explained: The "Memory Leak" Trap**
- **The Answer:** Never use `fs.readFileSync()` for file downloads in a production API. This loads the *entire* file into your server's RAM. If 100 users download a 100MB file at once, your server will crash (OOM). Always use **Streams** or `StreamableFile`.

---

**Q25. How do you optimize large JSON payloads in a REST API?** `[3+ yrs]`

* **Pagination:** Never return "all" items; use `limit` and `offset`.
* **Field Selection:** Allow clients to request only specific fields (e.g., `?fields=id,name`).
* **Compression:** Use `compression` middleware to Gzip/Brotli the JSON body.
* **DTO PickType:** Use DTOs to ensure only necessary data is serialized.

**Full Answer:**
Payload optimization is about "Data Minimalism." For large datasets, we use **Cursor-based Pagination** (better for real-time data) or **Offset-based Pagination**. Additionally, we enable Gzip compression in `main.ts` using the `compression` package, which can reduce JSON payload sizes by up to 80%.

**Trap Explained: The "Deep Nesting" Performance Trap**
- **The Answer:** Avoid returning deeply nested objects (e.g., User -> Posts -> Comments -> Likes) in a single request. This causes the "N+1 Problem" in your database and creates massive JSON payloads that slow down mobile clients. Use **Flat Responses** and provide links or IDs for related resources.

---

**Q26. What is Idempotency in REST APIs and why is it critical for reliability?** `[3+ yrs]`

* **Definition:** An operation is idempotent if performing it multiple times has the same effect as performing it once.
* **HTTP Methods:** GET, PUT, DELETE, and HEAD are idempotent by nature. POST is NOT.
* **Idempotency Key:** A unique token (UUID) sent by the client in a header (e.g., `Idempotency-Key`).
* **Implementation:** The server stores the result of the first request against the key (e.g., in Redis) and returns the same result for duplicate keys.

**Full Answer:**
Idempotency is the "Safety Net" for network failures. Imagine a mobile client makes a POST request to "Charge Credit Card," but the network drops before the client gets the 200 OK. If the client retries, the user might be charged twice. By implementing an **Idempotency Key**, the server recognizes the retry and returns the previous success response instead of creating a second charge.

**Trap Explained: The "PUT vs POST" Trap**
*"Why is PUT considered idempotent but POST is not?"*
- **The Answer:** **PUT** is used for "Replacement." If you replace a resource with the exact same data 10 times, the end state of the server is identical. **POST** is used for "Addition." If you call POST 10 times, you will create 10 new records. Senior developers distinguish their APIs by correctly choosing the method based on this principle.

---

**Q27. Explain the Richardson Maturity Model and HATEOAS.** `[3+ yrs]`

* **Level 0:** The Swamp of POX (Plain Old XML) — using HTTP just as a transport.
* **Level 1:** Resources — individual URIs for individual resources.
* **Level 2:** HTTP Verbs — using GET, POST, PUT, DELETE correctly.
* **Level 3:** HATEOAS (Hypermedia as the Engine of Application State).
* **Concept:** The API response includes links (`_links`) telling the client what they can do next.

**Full Answer:**
HATEOAS turns your API into a "Self-Discoverable" system. Instead of the frontend hardcoding URLs like `/orders/123/cancel`, the API response for an order includes a link to its own cancellation endpoint. This decouples the frontend from the backend's URL structure, allowing you to change paths without breaking clients.

**Trap Explained: The "True REST" Trap**
*"Is your API really RESTful if it doesn't use HATEOAS?"*
- **The Answer:** Technically, **No**. According to Roy Fielding (the creator of REST), an API is not truly RESTful unless it uses hypermedia. However, in the industry, "REST" is commonly used to describe Level 2 APIs. Mentioning the **Richardson Maturity Model** shows you have deep academic and practical knowledge.

---

**Q28. How do you implement Caching strategies in a NestJS REST API?** `[3+ yrs]`

* **Cache-Control Headers:** Instruct browsers/CDNs to store responses (e.g., `max-age=3600`).
* **ETags (Entity Tags):** A hash of the response body. If the data hasn't changed, the server returns `304 Not Modified`.
* **Server-Side Caching:** Using `CacheModule` (with Redis) to store expensive DB query results.
* **Cache Invalidation:** The process of clearing the cache when the underlying data is updated (e.g., `@CacheKey()` with `@CacheTTL()`).

**Full Answer:**
Caching is the most effective way to scale an API. We use **ETags** to save bandwidth (the server doesn't send the body if it hasn't changed) and **Redis** to save CPU/DB time. In NestJS, we can use the `@CacheInterceptor()` to automatically cache GET requests, significantly reducing latency for high-traffic endpoints.

**Trap Explained: The "Stale Data" Trap**
- **The Answer:** The hardest part of caching isn't storage; it's **Invalidation**. If you cache a "User Profile" for 1 hour, and the user updates their name after 5 minutes, they will see their old name for the next 55 minutes. You **must** implement a mechanism (like an Interceptor or a Hook) that clears the specific Redis key when a PUT or PATCH request is made to that resource.

---

**Q29. What is BOLA (Broken Object Level Authorization) and how do you prevent it?** `[3+ yrs]`

* **OWASP #1:** Formerly known as IDOR (Insecure Direct Object Reference).
* **Vulnerability:** A user can access another user's data by simply guessing their ID in the URL.
* **Impact:** Mass data breaches and unauthorized data access.
* **Prevention:** Always include the `userId` (from the JWT) in the database query, never rely solely on the ID provided in the URL params.

**Full Answer:**
BOLA is the most common vulnerability in modern APIs. It happens when you have a route like `/api/orders/:id` and you only check if the user is logged in, but not if they actually **own** that order. To prevent this, your service layer must always execute queries like `this.orderRepo.findOne({ where: { id, userId: req.user.id } })`.

**Trap Explained: The "Admin Bypass" Requirement**
*"How do you handle BOLA if an Admin needs to see every order?"*
- **The Answer:** Use a **Guard** or a **Logic Branch**. Your query should check: `if (user.role === 'admin') query = { id }; else query = { id, userId: user.id };`. This ensures that security is enforced for normal users while allowing administrative access.

---

**Q30. Webhooks vs. Long Polling vs. WebSockets: When to use which?** `[3+ yrs]`

* **Webhooks:** Push notifications from your server to a client's server (Async/Event-driven).
* **Long Polling:** The client keeps a connection open until the server has new data (Resource intensive).
* **WebSockets:** Full-duplex, real-time communication between client and server (TCP).
* **Use Case:** Webhooks for "Payment Success" (Stripe), WebSockets for "Chat/Trading," Long Polling for legacy browser support.

**Full Answer:**
For MERN apps, **Webhooks** are the industry standard for server-to-server communication (like receiving events from Stripe or GitHub). **WebSockets** (via Socket.io) are the choice for real-time dashboards or chat apps. The key is to choose based on who is initiating the communication and whether you need instant, two-way updates.

**Trap Explained: The "Webhook Security" Trap**
*"How do you know a Webhook is actually from Stripe and not an attacker?"*
- **The Answer:** **Signature Verification.** You must use a **Secret Key** (Webhook Signing Secret) to verify the `Stripe-Signature` header in the incoming request. If you skip this, anyone can send fake "Payment Succeeded" requests to your API and get free products.

---

That is the complete, professionalized Building REST APIs section — 30 questions with full architectural depth, ready for your MERN Interview Kit.


---

[⬅️ Previous: NestJS](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/05_NestJS/05_NestJS.md) | [🏠 Home](../../README.md) | [Next: Database ORM ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/07_Database_ORM/07_Database_ORM.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>