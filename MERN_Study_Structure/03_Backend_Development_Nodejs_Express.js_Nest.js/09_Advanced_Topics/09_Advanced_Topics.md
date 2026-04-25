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

---

[⬅️ Previous: Authentication Security](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/08_Authentication_Security/08_Authentication_Security.md) | [🏠 Home](../../README.md) | [Next: MongoDB ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/01_MongoDB/01_MongoDB.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>