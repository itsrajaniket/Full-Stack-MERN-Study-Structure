# Advanced Topics
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] WebSockets with NestJS (Gateway)
- [x] Microservices Architecture in NestJS
- [x] Caching with Redis
- [x] Task Scheduling (Cron Jobs)
- [x] Testing with Jest

## 📝 Detailed Notes

### 1. WebSockets with NestJS (Gateways)
NestJS uses the term **Gateways** to describe components that handle WebSocket connections. It supports both `socket.io` and `ws`.
```typescript
@WebSocketGateway()
export class ChatGateway {
  @SubscribeMessage('message')
  handleMessage(client: any, payload: any): string {
    return 'Hello world!';
  }

  // Namespaces & Rooms
  @SubscribeMessage('joinRoom')
  handleJoinRoom(client: any, room: string) {
    client.join(room);
  }
}
```

### 6. Docker for Backend
Containerization ensures your backend runs the same everywhere.
```dockerfile
# Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5000
CMD ["npm", "start"]
```

### 2. Microservices Architecture
NestJS provides a built-in `Microservice` module that supports various transport layers like **TCP**, **Redis**, **RabbitMQ**, and **Kafka**.
- **Request-Response**: Like HTTP but over a different protocol.
- **Event-Based**: Fire-and-forget messaging.

### 3. Caching with Redis
Caching significantly improves performance by reducing DB load. NestJS has a `CacheModule` that can be configured to use `redis-store`.
```typescript
@UseInterceptors(CacheInterceptor)
@Get()
findAll() { ... }
```

### 4. Task Scheduling (Cron Jobs)
Useful for background tasks like sending weekly emails or cleaning up temporary files. Use `@nestjs/schedule`.
```typescript
@Cron(CronExpression.EVERY_MINUTE)
handleCron() {
  this.logger.debug('Called every minute');
}
```

### 5. Advanced Testing with Jest
- **Unit Testing**: Testing individual classes/methods with mocks.
- **E2E Testing**: Testing the entire application flow using `Supertest`.

---

## 🎓 Important Interview Questions

### Q1: What is a "Gateway" in NestJS?
A Gateway is a class annotated with `@WebSocketGateway()` that handles real-time communication using WebSockets. It allows you to use decorators like `@SubscribeMessage()` to listen for specific events from clients.

### Q2: How do Microservices communicate in NestJS?
They use a **Proxy** to communicate. You define a `ClientProxy` in your app that sends messages to the microservice via a transport layer like TCP or RabbitMQ. You can use `send()` for request-response or `emit()` for events.

### Q3: What is "Redis" and why is it used for caching?
Redis is an **In-Memory** data store, which means it is much faster than traditional disk-based databases like MongoDB or PostgreSQL. It is used for caching frequently accessed data, session storage, and as a message broker.

### Q4: Explain "Cron Jobs" and provide a use case.
Cron Jobs are scheduled tasks that run at specific intervals. A common use case in a MERN app would be a task that runs every night at 2:00 AM to delete expired user sessions or to generate daily sales reports.

### Q5: What is the difference between Unit Testing and E2E Testing?
- **Unit Testing**: Tests a single unit of code (like a Service method) in isolation by mocking its dependencies. It's fast and focused.
- **E2E Testing**: Tests the full request-response cycle by starting the actual server and hitting endpoints with `Supertest`. It ensures all components work together correctly.


## ❓ Questions & Doubts
- [x]
## **Advanced NestJS Topics — MERN Stack Interview Kit**

---

### **1\. WebSockets with NestJS (Gateway)**

---

**Q1. What is a NestJS Gateway and how does it work?** `[1-2 yrs]`

* Gateway — NestJS component for handling WebSocket connections, equivalent to a controller but for WebSockets  
* Built on Socket.io or native WebSocket (ws package) depending on adapter  
* @WebSocketGateway() decorator — marks class as a gateway, optionally takes port and options:  
  * @WebSocketGateway(3001) — separate port from HTTP  
  * @WebSocketGateway({ namespace: '/chat' }) — Socket.io namespace  
  * @WebSocketGateway({ cors: { origin: '\*' } }) — CORS for WebSocket  
* @WebSocketServer() — inject Socket.io Server instance — io object for broadcasting  
* @SubscribeMessage('eventName') — handle incoming event from client, equivalent to socket.on()  
* @MessageBody() — extract message payload, like @Body() for HTTP  
* @ConnectedSocket() — inject the individual socket that sent the message  
* Return value from handler — automatically emitted back to sender as acknowledgement  
* Lifecycle hooks:  
  * handleConnection(client, ...args) — called when client connects  
  * handleDisconnect(client) — called when client disconnects  
  * Implement OnGatewayConnection and OnGatewayDisconnect interfaces  
* Emitting from gateway:  
  * client.emit('event', data) — emit to specific client  
  * this.server.emit('event', data) — broadcast to all  
  * this.server.to('room').emit('event', data) — emit to room  
  * client.join('room') — add client to room  
* Gateway is a provider — can inject services, repositories, other providers via constructor DI  
* Gateways run in same process as HTTP server — share all providers and modules

---

**Q2. How do you authenticate WebSocket connections in NestJS?** `[2-3 yrs]`

* WebSocket connections need authentication same as HTTP endpoints  
* Two approaches — middleware level or guard level  
* Socket.io auth option — client sends token in auth object on connect:  
  * socket \= io(url, { auth: { token: 'Bearer jwt...' } })  
  * Server accesses via client.handshake.auth.token  
* NestJS WsGuard — implement CanActivate for WebSocket context:  
  * context.switchToWs().getClient() — get socket client  
  * context.switchToWs().getData() — get message data  
  * Extract token from client.handshake.auth or client.handshake.headers.authorization  
  * Verify JWT and attach user to client.data.user  
  * Apply with @UseGuards(WsJwtGuard) on gateway class or specific handlers  
* IoAdapter approach — validate token during connection handshake, reject before connection established:  
  * Custom IoAdapter extending SocketIoAdapter  
  * Override createIOServer — add use() middleware to Socket.io server  
  * Middleware verifies token, calls next(new Error()) if invalid  
  * Client never completes connection if token invalid  
* Storing user on socket — client.data.user \= decodedUser — available in all handlers for that client  
* Room-based authorization — verify user has access to room before joining:  
  * Check in handleConnection or in @SubscribeMessage handler before client.join()

---

### **2\. Microservices Architecture in NestJS**

---

**Q3. What are Microservices in NestJS and what transport layers are supported?** `[2-3 yrs]`

* Microservices — architectural style where application is split into small, independent services communicating over network  
* NestJS has first-class microservices support via @nestjs/microservices package  
* Communication patterns:  
  * Request-Response — one service sends message, waits for reply (synchronous)  
  * Event-based — one service emits event, others react (asynchronous, fire and forget)  
* Supported transport layers:  
  * TCP — built-in, simple, good for internal communication  
  * Redis — pub/sub based, good for event broadcasting  
  * NATS — lightweight messaging system, good for microservices  
  * RabbitMQ — feature-rich message broker, durable queues, dead letter exchanges  
  * Kafka — high-throughput distributed streaming, good for event sourcing  
  * gRPC — Google's RPC framework, uses Protocol Buffers, fast binary serialization  
  * MQTT — lightweight, good for IoT  
* Creating a microservice — NestFactory.createMicroservice() instead of NestFactory.create()  
* Hybrid app — both HTTP server and microservice in same app — NestFactory.create() then app.connectMicroservice()  
* @MessagePattern('pattern') — handle request-response messages, return value sent back  
* @EventPattern('event') — handle fire-and-forget events, no return value expected  
* ClientProxy — inject to send messages from one service to another:  
  * client.send('pattern', data) — request-response, returns Observable  
  * client.emit('event', data) — fire-and-forget event

---

**Q4. What is the difference between Monolith and Microservices architecture?** `[2-3 yrs]`

* Monolith — entire application deployed as single unit, all features in one codebase and process  
* Microservices — application split into independent services, each deployed separately

| Aspect | Monolith | Microservices |
| ----- | ----- | ----- |
| Deployment | Single unit | Independent per service |
| Scaling | Scale entire app | Scale individual services |
| Development | Simpler initially | Complex but independent |
| Team size | Small to medium | Large teams, per service |
| Data | Single shared DB | Database per service |
| Communication | In-process calls | Network calls (latency) |
| Failure | One failure can bring down app | Isolated failures |
| Testing | Easier end-to-end | Complex distributed testing |
| Tech stack | Single stack | Each service can differ |

* When to use microservices — large teams, different scaling needs per feature, independent deployment requirements, high traffic specific features  
* When NOT to use microservices — small team, early stage product, simple domain, network overhead matters  
* NestJS in practice — start as modular monolith, migrate to microservices when genuinely needed  
* Modular monolith — NestJS modules provide good separation, can be extracted to services later

---

### **3\. Caching with Redis in NestJS**

---

**Q5. How do you implement caching in NestJS with Redis?** `[1-2 yrs]`

* @nestjs/cache-manager — official caching module  
* npm install @nestjs/cache-manager cache-manager cache-manager-redis-yet  
* CacheModule.registerAsync() in AppModule:  
  * isGlobal: true — available everywhere  
  * useFactory with ConfigService for Redis URL  
  * store: redisStore — use Redis as backing store  
  * ttl — default time-to-live in milliseconds  
* Two ways to use caching: Automatic caching with @CacheInterceptor:  
  * @UseInterceptors(CacheInterceptor) on controller or method  
  * Automatically caches GET request responses  
  * Cache key \= request URL by default  
  * @CacheTTL(30000) — override TTL per route  
  * @CacheKey('custom-key') — custom cache key  
  * Does not work for non-GET or user-specific data without customization  
* Manual caching with Cache Manager:  
  * @Inject(CACHE\_MANAGER) private cacheManager: Cache  
  * await cacheManager.set('key', value, ttl)  
  * await cacheManager.get\<Type\>('key')  
  * await cacheManager.del('key')  
  * Full control over keys, TTL, and when to cache  
* Cache invalidation — delete keys on create/update/delete operations:  
  * After creating a post — del('posts:all')  
  * After updating user — del('user:' \+ id)  
  * Pattern deletion — scan for keys matching pattern, delete all (use with caution on large datasets)  
* Cache key strategy — namespace with resource type and ID — users:all, users:123, posts:page:1:limit:10

---

### **4\. Task Scheduling (Cron Jobs)**

---

**Q6. How do you implement task scheduling in NestJS?** `[1-2 yrs]`

* @nestjs/schedule — official scheduling module built on node-cron  
* npm install @nestjs/schedule  
* ScheduleModule.forRoot() in AppModule imports — initializes scheduler  
* Three types of scheduled tasks: Cron jobs — run on schedule defined by cron expression:  
  * @Cron(CronExpression.EVERY\_HOUR) — predefined expressions  
  * @Cron('0 0 \* \* \*') — custom cron string — midnight daily  
  * @Cron('0 9 \* \* MON-FRI') — weekdays at 9am  
  * CronExpression enum — EVERY\_SECOND, EVERY\_MINUTE, EVERY\_HOUR, EVERY\_DAY\_AT\_MIDNIGHT etc.  
  * @Cron(CronExpression.EVERY\_DAY\_AT\_MIDNIGHT, { name: 'cleanup', timeZone: 'Asia/Kolkata' })  
  * name option — allows dynamic control via SchedulerRegistry  
* Intervals — run repeatedly every N milliseconds:  
  * @Interval(10000) — run every 10 seconds  
  * @Interval('health-check', 30000\) — named interval  
* Timeouts — run once after N milliseconds:  
  * @Timeout(5000) — run once 5 seconds after app starts  
  * @Timeout('startup-task', 3000\) — named timeout  
* Cron expressions — five or six parts: second(optional) minute hour day-of-month month day-of-week  
* SchedulerRegistry — dynamically manage scheduled tasks:  
  * getCronJob('name') — get cron job reference  
  * job.stop() — pause cron job  
  * job.start() — resume cron job  
  * deleteCronJob('name') — remove scheduled job  
  * addCronJob('name', job) — dynamically add new job at runtime  
* Scheduled tasks in NestJS are providers — inject any service, repository, mailer, or other provider  
* Dynamic cron from DB — load schedule config on startup, register via SchedulerRegistry  
* Distributed scheduling concern — if multiple instances running, all execute cron — use Redis lock or dedicated scheduler instance to prevent duplicate runs

---

**Q7. What are common use cases for task scheduling in a MERN backend?** `[1-2 yrs]`

* Database cleanup tasks:  
  * Delete expired OTPs, verification tokens, password reset tokens  
  * Purge soft-deleted records after retention period  
  * Clean up incomplete/abandoned uploads  
  * Archive old records to cold storage table  
* Notification and communication:  
  * Send daily digest emails to users  
  * Send reminder notifications for upcoming events  
  * Weekly report generation and email  
  * Push notification for inactivity reminders  
* Data synchronization:  
  * Sync data from external APIs on schedule — exchange rates, weather, inventory  
  * Aggregate analytics data hourly  
  * Recalculate search rankings or recommendation scores  
* Cache management:  
  * Warm up cache before peak hours  
  * Clear stale cache entries  
  * Pre-generate expensive reports  
* Health and maintenance:  
  * Database connection pool health checks  
  * Disk space monitoring alerts  
  * Dead letter queue processing — retry failed jobs  
  * Session cleanup — remove expired sessions from Redis

---

### **5\. Testing with Jest in NestJS**

---

**Q8. How do you write unit tests for NestJS services?** `[1-2 yrs]`

* NestJS generates spec files alongside source files — users.service.spec.ts  
* Test module — Testing.createTestingModule() — NestJS-aware testing utility:  
  * providers array — list service and its mocked dependencies  
  * compile() — builds test module  
  * get(ServiceClass) — retrieve instance from test module  
* Mocking dependencies — replace real providers with mocks:  
  * useValue with jest.fn() mocked methods — most common  
  * Jest auto-mock — jest.createMockFromModule() — auto-mock all methods  
  * MockFactory pattern — function returning object with all methods as jest.fn()  
* Mock pattern for repository:  
  * mockUserRepository — object with find, findOne, save, delete as jest.fn()  
  * { provide: getRepositoryToken(UserEntity), useValue: mockUserRepository }  
* Test structure:  
  * describe('UsersService') — outer group  
  * beforeEach — create fresh testing module, reset mocks  
  * describe('findOne') — inner group per method  
  * it('should return user when found') — specific scenario  
  * it('should throw NotFoundException when not found')  
* Assertion patterns:  
  * expect(result).toEqual(expectedUser) — deep equality  
  * expect(mockRepo.findOne).toHaveBeenCalledWith({ where: { id } }) — verify called correctly  
  * await expect(service.findOne('bad-id')).rejects.toThrow(NotFoundException)  
* Coverage — npx jest \--coverage — generates HTML report showing untested lines  
* Focus on testing business logic in services — edge cases, error paths, computed values

---

**Q9. How do you write end-to-end (e2e) tests in NestJS?** `[2-3 yrs]`

* E2E tests — test entire HTTP request pipeline including middleware, guards, pipes, controllers, services  
* NestJS generates test/app.e2e-spec.ts by default  
* Setup — create full NestJS app in beforeAll, close in afterAll:  
  * Testing.createTestingModule with AppModule — real module, not mocked  
  * app.init() — boots the full application  
  * supertest request(app.getHttpServer()) — make real HTTP requests  
* Database for e2e — use separate test DB:  
  * Set TEST\_DATABASE\_URL in environment  
  * Override database module in test — TypeOrmModule with test connection  
  * Or use sqlite in-memory for speed  
  * Run migrations before tests — programmatically or in global setup  
  * Seed test data in beforeEach, clean in afterEach  
* Authentication in e2e:  
  * Make real login request — POST /auth/login — get JWT  
  * Attach to subsequent requests — .set('Authorization', Bearer token)  
  * Or generate test JWT directly with JwtService.sign()  
* Test scenarios:  
  * Happy path — valid input, expected response, correct status code  
  * Validation errors — invalid body, expect 400 with error details  
  * Auth errors — no token, expect 401; wrong role, expect 403  
  * Not found — non-existent ID, expect 404  
  * Conflict — duplicate email, expect 409  
* jest.config.js — separate config for e2e — different testMatch pattern, longer timeout  
* Global setup and teardown — jest globalSetup/globalTeardown for DB connection management  
* E2E tests run slower — run separately from unit tests in CI, unit tests on every push, e2e on PR or before deploy

---

---

[⬅️ Previous: Authentication Security](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/08_Authentication_Security/08_Authentication_Security.md) | [🏠 Home](../../README.md) | [Next: MongoDB ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/01_MongoDB/01_MongoDB.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>