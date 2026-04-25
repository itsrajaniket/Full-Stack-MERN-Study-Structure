# Advanced Express.js
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] File Uploading (Multer, Cloudinary, AWS S3)
- [x] Rate Limiting & Security Best Practices (Helmet, CORS)
- [x] Caching (Redis)
- [x] WebSockets (Socket.io)
- [x] API Documentation (Swagger, Postman)
- [x] Testing (Jest, Supertest, Mocha)

## 📝 Detailed Notes

### 1. File Uploading (Multer & Cloudinary)
Express doesn't handle `multipart/form-data` out of the box. Use **Multer**.
- **Multer**: Middleware for uploading files.
- **Cloudinary/S3**: Storing files on a cloud provider is better than storing on the server's local disk.
```javascript
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });
app.post('/profile', upload.single('avatar'), (req, res) => {
    // req.file is the `avatar` file
});
```

### 2. Rate Limiting & Security
- **Rate Limiting**: Prevent Brute Force/DDoS attacks. Use `express-rate-limit`.
- **Helmet**: Secures your app by setting various HTTP headers.
- **CORS**: Cross-Origin Resource Sharing. Restricted by default for security.

### 3. Caching with Redis
Redis is an in-memory data structure store. Use it to cache database queries or expensive calculations.
```javascript
const redis = require('redis');
const client = redis.createClient();
// Check cache before querying DB
const cachedData = await client.get('users');
if (cachedData) return JSON.parse(cachedData);
```

### 4. WebSockets (Socket.io)
Real-time, bi-directional communication between client and server.
```javascript
const io = require('socket.io')(server);
io.on('connection', (socket) => {
    socket.on('chat message', (msg) => {
        io.emit('chat message', msg);
    });
});
```

### 5. API Documentation (Swagger)
Provides an interactive UI for your API. Defined via JSDoc or YAML files.

### 6. Testing (Jest & Supertest)
```javascript
const request = require('supertest');
const app = require('./app');

describe('GET /users', () => {
    it('responds with json', async () => {
        const response = await request(app).get('/users');
        expect(response.statusCode).toBe(200);
        expect(response.body).toBeInstanceOf(Array);
    });
});
```

### 7. API Versioning
Always version your APIs to avoid breaking changes for frontend clients.
- `app.use('/api/v1', v1Routes);`
- `app.use('/api/v2', v2Routes);`

### 8. Pagination, Filtering, and Sorting
Crucial for performance in real-world apps.
```javascript
// Example logic:
const page = Number(req.query.page) || 1;
const limit = Number(req.query.limit) || 10;
const skip = (page - 1) * limit;

const products = await Product.find(query).limit(limit).skip(skip).sort(req.query.sort);
```

---

## 🎓 Important Interview Questions

### Q1: Why should you avoid storing uploaded files on your own server's disk?
1. **Scalability**: If you have multiple server instances (e.g., behind a load balancer), a file uploaded to Server A won't be accessible on Server B.
2. **Storage**: Servers usually have limited disk space.
3. **Data Loss**: If the server crashes or is redeployed, local files might be lost. **Use S3 or Cloudinary** for persistent storage.

### Q2: What is the difference between WebSockets and HTTP?
- **HTTP**: Unidirectional (Client → Server). Stateless. Connection closes after each request.
- **WebSockets**: Bi-directional (Full-duplex). Persistent connection. Low latency. Best for chat, notifications, live sports scores.

### Q3: Explain "Rate Limiting" and why it's important.
Rate limiting is a strategy for limiting network traffic. It puts a cap on how many times someone can repeat an action within a certain timeframe (e.g., "Max 5 login attempts per minute"). It protects against DDoS attacks and brute-force password cracking.

### Q4: What is a "Race Condition" in Node.js?
A situation where the outcome depends on the timing or sequence of async operations. For example, two async requests incrementing a counter in a database at the same time might both read the same initial value and overwrite each other's updates.

### Q5: How do you document your Express APIs professionally?
Using **Swagger (OpenAPI)**. It allows other developers to see all your endpoints, the required request body/headers, and expected response codes without reading your source code.


## ❓ Questions & Doubts
- [x]

---

[⬅️ Previous: Authentication Authorization](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/03_Authentication_Authorization/03_Authentication_Authorization.md) | [🏠 Home](../../README.md) | [Next: NestJS ➡️](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/05_NestJS/05_NestJS.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>