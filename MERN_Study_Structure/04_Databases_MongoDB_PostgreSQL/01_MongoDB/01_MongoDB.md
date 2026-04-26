# MongoDB (NoSQL Database)
> ✍️ **Author:** [Aniket Raj](https://github.com/itsrajaniket) | 📅 **Updated:** April 2025
---

## 📚 Curriculum Checklist
- [x] Introduction to NoSQL & MongoDB
- [x] [MongoDB](https://www.mongodb.com/docs/manual/) Installation & Setup
- [x] JSON & BSON Basics
- [x] Connecting MongoDB with Node.js (Mongoose/NestJS TypeORM)
- [x] Creating Databases & Collections
- [x] Insert Operations: insertOne(), insertMany()
- [x] Read Operations: find(), findOne(), Query Operators ($eq, $gt, $lt, $in, $regex, etc.)
- [x] Update Operations: updateOne(), updateMany(), $set, $push, $pull
- [x] Delete Operations: deleteOne(), deleteMany()
- [x] Indexing (createIndex())
- [x] Compound Indexes
- [x] Aggregation Framework ($match, $group, $lookup, $sort, $project)
- [x] Relationships in MongoDB
- [x] One-to-One, One-to-Many, Many-to-Many
- [x] Embedding vs. Referencing ($lookup for Joins)
- [x] Transactions in MongoDB
- [x] Schema Validation
- [x] [MongoDB](https://www.mongodb.com/docs/manual/) Atlas (Cloud Database)
- [x] Replication & Sharding (Basic Understanding)
- [x] Security Best Practices

## 📝 Detailed Notes

### 1. Introduction to NoSQL & MongoDB
MongoDB is a **Document-oriented NoSQL database**. Unlike relational databases (SQL) that use tables and rows, MongoDB uses **Collections** and **Documents**.
- **JSON & BSON**: MongoDB stores data in BSON (Binary JSON) format, which supports more data types (like `Date` and `BinData`) than standard JSON.

### 2. Mongoose (Node.js ODM)
Mongoose provides a straight-forward, schema-based solution to model your application data.
```javascript
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, unique: true },
  age: Number
});
const User = mongoose.model('User', userSchema);
```

### 3. CRUD Operations
- **Create**: `db.collection.insertOne({ name: "Aniket" })`
- **Read**: `db.collection.find({ age: { $gt: 18 } })`
- **Update**: `db.collection.updateOne({ _id: id }, { $set: { active: true } })`
- **Delete**: `db.collection.deleteOne({ _id: id })`

### 4. Indexing for Performance
Indexes support the efficient execution of queries in MongoDB. Without indexes, MongoDB must perform a **collection scan**.
- **Single Field**: `db.collection.createIndex({ name: 1 })`
- **Compound**: `db.collection.createIndex({ status: 1, date: -1 })`

### 5. Aggregation Framework
The aggregation framework is a powerful tool for data analysis, similar to SQL's `GROUP BY` and `JOIN`.
```javascript
db.orders.aggregate([
  { $match: { status: "A" } },
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);
```

### 6. Relationships: Embedding vs. Referencing
- **Embedding**: Storing related data in a single document (Faster reads, restricted size).
- **Referencing**: Storing data in separate collections and linking them via `_id` (Flexible, but requires `$lookup` for joins).

---

## 🎓 Important Interview Questions

### Q1: Difference between SQL and NoSQL?
- **SQL**: Relational, fixed schema, table-based, vertically scalable, ACID compliant.
- **NoSQL**: Non-relational, dynamic schema, document-based, horizontally scalable, follows BASE (Basically Available, Soft state, Eventual consistency).

### Q2: What is the "Aggregation Pipeline"?
It is a framework for data transformation. It consists of multiple stages (like `$match`, `$group`, `$sort`) where the output of one stage serves as the input to the next.

### 6. MongoDB Change Streams
Change streams allow applications to access real-time data changes without the complexity and risk of tailing the oplog.
```javascript
const collection = db.collection('orders');
const changeStream = collection.watch();
changeStream.on('change', next => {
  console.log(next); // Trigger real-time notification
});
```

### 7. Capped Collections
Fixed-size collections that support high-throughput operations that insert and retrieve documents based on insertion order (useful for logging).

### Q3: When should you use "Embedding" over "Referencing"?
- **Use Embedding**: When the data is frequently read together and the child data doesn't grow indefinitely (e.g., Address of a User).
- **Use Referencing**: When the data is large, shared across documents, or updated frequently (e.g., Authors of a Book).

### Q4: What is an "Index" and why is it important?
An index is a special data structure that stores a small portion of the collection's data set in a traversable form. It drastically improves query performance by allowing MongoDB to find documents without scanning every single one.

### Q5: What are "Transactions" in MongoDB?
Starting from version 4.0, MongoDB supports multi-document ACID transactions. They allow you to ensure that multiple operations either all succeed or all fail together, which is crucial for financial or sensitive data.


## ❓ Questions & Doubts
- [x]
## **MongoDB (NoSQL Database) — MERN Stack Interview Kit**

---

### **1\. Introduction to NoSQL & MongoDB**

---

**Q1. What is NoSQL and how is it different from SQL databases?** `[Fresher]`

* NoSQL — "Not Only SQL" — category of databases that store data in formats other than relational tables  
* SQL databases — relational, fixed schema, tables with rows and columns, ACID compliant by default  
* NoSQL databases — flexible schema, various data models, designed for scale and flexibility  
* Four types of NoSQL databases:  
  * Document stores — MongoDB, CouchDB — store JSON-like documents  
  * Key-Value stores — Redis, DynamoDB — simple key to value mapping  
  * Column-family stores — Cassandra, HBase — column-oriented storage  
  * Graph databases — Neo4j, Amazon Neptune — nodes and edges for relationships  
* SQL vs NoSQL comparison:

| Aspect | SQL | NoSQL (MongoDB) |
| ----- | ----- | ----- |
| Schema | Fixed, predefined | Flexible, dynamic |
| Data model | Tables, rows, columns | Documents, collections |
| Joins | Native, easy | Manual via $lookup |
| ACID | Full by default | Eventual or per-operation |
| Scaling | Vertical (scale up) | Horizontal (scale out) |
| Query language | SQL standard | MongoDB Query Language |
| Relationships | Foreign keys, joins | Embedding or referencing |
| Best for | Structured, relational data | Flexible, hierarchical data |

* When to choose MongoDB:  
  * Flexible or evolving schema — startup, MVP, frequent schema changes  
  * Hierarchical data that maps naturally to documents  
  * High write throughput and horizontal scaling needed  
  * Geospatial data, real-time analytics, content management  
* When to choose SQL:  
  * Complex relationships with many joins  
  * Strong ACID transaction requirements  
  * Financial data, strict data integrity needs  
  * Reporting and complex queries across many entities

---

**Q2. What is MongoDB and what are its core concepts?** `[Fresher]`

* MongoDB — open-source, document-oriented NoSQL database developed by MongoDB Inc.  
* Stores data as BSON documents — Binary JSON format  
* Core concepts:  
  * Database — top-level container, equivalent to SQL database  
  * Collection — group of documents, equivalent to SQL table but schema-less  
  * Document — individual record, equivalent to SQL row, stored as BSON  
  * Field — key-value pair inside document, equivalent to SQL column  
  * \_id — unique identifier for every document, auto-generated ObjectId if not provided  
* Key features:  
  * Schema-less — each document in collection can have different fields  
  * Rich query language — filter, sort, project, aggregate  
  * Indexing — support for single, compound, text, geospatial, TTL indexes  
  * Aggregation Framework — powerful data processing pipeline  
  * Replication — replica sets for high availability  
  * Sharding — horizontal scaling across multiple servers  
  * Transactions — multi-document ACID transactions (v4.0+)  
  * Atlas — managed cloud database service  
* ObjectId — 12-byte unique identifier:  
  * 4 bytes — Unix timestamp  
  * 5 bytes — random value unique to machine and process  
  * 3 bytes — incrementing counter  
  * Sortable by creation time — ObjectId.getTimestamp()  
* MongoDB versions — current stable is v7.x, Atlas always offers latest

---

### **2\. JSON & BSON Basics**

---

**Q3. What is BSON and how is it different from JSON?** `[Fresher]`

* JSON — JavaScript Object Notation, text-based, human-readable data interchange format  
* BSON — Binary JSON, MongoDB's binary-encoded serialization format for documents  
* Why BSON over JSON:  
  * Efficient traversal — BSON documents contain length prefixes, can skip over fields quickly  
  * More data types — JSON has limited types, BSON adds Date, Binary, ObjectId, Decimal128, Int32, Int64, Regex, Timestamp  
  * Smaller size for numeric data — JSON stores numbers as strings, BSON uses binary encoding  
  * Faster to encode/decode — binary format is faster to parse than text parsing  
* Data types in BSON not in JSON:  
  * Date — native date object with millisecond precision  
  * ObjectId — 12-byte unique identifier  
  * Int32 / Int64 — explicit integer types  
  * Decimal128 — high-precision decimal for financial data  
  * Binary — raw binary data  
  * Regular Expression — stored with flags  
  * Timestamp — internal MongoDB type for replication  
  * Null vs Undefined — both supported  
* JSON in MongoDB — drivers convert JSON to BSON when writing, BSON to JSON when reading  
* Extended JSON — MongoDB's JSON representation of BSON types for cases where standard JSON used:  
  * ObjectId represented as { "$oid": "..." }  
  * Date as { "$date": "..." }  
  * Used in mongodump/mongorestore and Atlas Data API

---

### **3\. Connecting MongoDB with Node.js**

---

**Q4. How do you connect MongoDB to a Node.js application using Mongoose?** `[Fresher]`

* Mongoose — ODM (Object Document Mapper) for MongoDB and Node.js  
* ODM vs ORM — ODM works with documents and collections instead of tables and rows  
* npm install mongoose  
* Connection:  
  * mongoose.connect(MONGODB\_URI) — returns Promise  
  * Connection string format — mongodb://username:password@host:port/database  
  * Atlas format — mongodb+srv://username:password@cluster.mongodb.net/database  
* Connection options — useNewUrlParser and useUnifiedTopology deprecated in v6+, not needed  
* Connection events:  
  * mongoose.connection.on('connected', handler)  
  * mongoose.connection.on('error', handler)  
  * mongoose.connection.on('disconnected', handler)  
* Best practice — connect once at app startup, Mongoose maintains connection pool  
* Connection pooling — Mongoose maintains pool of connections, default maxPoolSize is 5, increase for high-traffic apps  
* Mongoose in Express — connect before app.listen(), handle connection error to prevent app starting without DB  
* Schema — defines structure and validation rules for documents in a collection  
* Model — compiled version of Schema, provides interface to MongoDB collection  
* Schema definition:  
  * type — String, Number, Boolean, Date, ObjectId, Array, Mixed, Map  
  * required — validation  
  * default — default value or function  
  * unique — unique index  
  * index — create index  
  * validate — custom validator  
  * enum — allowed values  
  * min/max — numeric constraints  
  * minlength/maxlength — string constraints  
  * trim, lowercase, uppercase — string transforms  
* mongoose.model('User', userSchema) — creates model, uses 'users' collection by default (pluralized, lowercase)

---

**Q5. How do you connect MongoDB in a NestJS application?** `[1-2 yrs]`

* Two options — @nestjs/mongoose (Mongoose-based) or TypeORM with MongoDB support  
* @nestjs/mongoose — most common for MongoDB in NestJS:  
  * npm install @nestjs/mongoose mongoose  
  * MongooseModule.forRoot(uri) in AppModule imports  
  * MongooseModule.forRootAsync() — use ConfigService for URI  
  * MongooseModule.forFeature(\[{ name: User.name, schema: UserSchema }\]) in feature module  
* Defining Schema in NestJS:  
  * @Schema() decorator on class — equivalent to new Schema()  
  * @Prop() decorator on properties — equivalent to schema field definition  
  * @Prop({ required: true, unique: true }) — pass options  
  * @Prop({ type: mongoose.Schema.Types.ObjectId, ref: 'User' }) — reference  
  * SchemaFactory.createForClass(User) — generates Mongoose schema from class  
  * export type UserDocument \= HydratedDocument\<User\> — TypeScript type for document  
* Injecting Model in Service:  
  * @InjectModel(User.name) private userModel: Model\<UserDocument\>  
  * Use model exactly like Mongoose model — find, create, updateOne etc.  
* Mongoose middleware in NestJS — add pre/post hooks on schema before creating:  
  * UserSchema.pre('save', function(next) {...}) — hash password before save  
  * UserSchema.post('find', ...) — transform results  
* Virtual properties — computed fields not stored in DB:  
  * @Prop({ virtual: true }) or defined on schema directly  
  * toJSON: { virtuals: true } — include virtuals in JSON output

---

### **4\. CRUD Operations**

---

**Q6. How do Insert operations work in MongoDB?** `[Fresher]`

* insertOne(document) — insert single document, returns insertedId  
* insertMany(documents\[\]) — insert array of documents, returns insertedIds array  
* \_id auto-generated as ObjectId if not provided  
* insertMany options:  
  * ordered: true (default) — stop on first error, documents before error are inserted  
  * ordered: false — continue on error, insert all valid documents, report errors at end  
* Mongoose equivalents:  
  * new Model(data).save() — creates document instance and saves, triggers middleware and validation  
  * Model.create(data) — shortcut for new \+ save, can accept array  
  * Model.insertMany(array) — bypass some Mongoose validation for performance, raw bulk insert  
* save() vs create() vs insertMany():  
  * save() — full Mongoose middleware pipeline, validation, virtuals, pre/post hooks  
  * create() — same as save() but convenience method  
  * insertMany() — faster, bypasses validators and middleware by default  
* Document validation — Mongoose validates before save() unless { validateBeforeSave: false }  
* Timestamps — { timestamps: true } in schema options — auto-adds createdAt and updatedAt  
* Upsert — insertOne or updateOne with upsert:true — insert if not found, update if found

---

**Q7. How do Read operations work in MongoDB?** `[Fresher]`

* find(filter, projection) — returns cursor of matching documents  
* findOne(filter, projection) — returns first matching document or null  
* MongoDB shell — db.collection.find() returns cursor, iterate with .toArray() or .forEach()  
* Mongoose — find() returns Query, await to get array, findOne() returns single document  
* Filter operators — comparison:  
  * $eq — { field: value } or { field: { $eq: value } } — equal  
  * $ne — not equal  
  * $gt — greater than  
  * $gte — greater than or equal  
  * $lt — less than  
  * $lte — less than or equal  
  * $in — { field: { $in: \[val1, val2\] } } — value in array  
  * $nin — value not in array  
* Logical operators:  
  * $and — { $and: \[{ age: { $gt: 18 } }, { active: true }\] }  
  * $or — { $or: \[{ role: 'admin' }, { role: 'moderator' }\] }  
  * $nor — none of conditions true  
  * $not — negates expression  
* Element operators:  
  * $exists — { field: { $exists: true } } — field exists in document  
  * $type — check field BSON type  
* Array operators:  
  * $all — array contains all specified values  
  * $elemMatch — { tags: { $elemMatch: { $gt: 5 } } } — at least one element matches  
  * $size — { tags: { $size: 3 } } — array has exact size  
* Text search — $text: { $search: 'keyword' } — requires text index  
* $regex — { name: { $regex: 'john', $options: 'i' } } — case-insensitive pattern match  
* Projection — second argument to find, 1 to include field, 0 to exclude:  
  * { name: 1, email: 1, \_id: 0 } — include name and email, exclude \_id  
  * Cannot mix include and exclude except for \_id  
* Cursor methods — chained on find():  
  * .sort({ createdAt: \-1 }) — sort descending  
  * .skip(20).limit(10) — pagination  
  * .count() / .countDocuments() — count results  
  * .select('name email') — Mongoose projection shorthand  
  * .lean() — return plain JS objects instead of Mongoose documents (faster, no methods)  
  * .populate('userId') — replace ObjectId reference with actual document

---

**Q8. How do Update operations work in MongoDB?** `[Fresher]`

* updateOne(filter, update, options) — update first matching document  
* updateMany(filter, update, options) — update all matching documents  
* replaceOne(filter, replacement) — completely replace document (not just fields)  
* Update operators:  
  * $set — { $set: { name: 'John', age: 30 } } — set specific fields, does not affect other fields  
  * $unset — { $unset: { tempField: '' } } — remove a field  
  * $inc — { $inc: { views: 1, score: \-5 } } — increment/decrement numeric field  
  * $mul — multiply numeric field  
  * $rename — rename a field  
  * $min / $max — update only if new value is less/greater than current  
  * $currentDate — set field to current date  
* Array update operators:  
  * $push — { $push: { tags: 'nodejs' } } — add element to array  
  * $push with $each — { $push: { tags: { $each: \['node', 'js'\] } } } — add multiple  
  * $push with $sort — sort array after push  
  * $push with $slice — limit array size after push  
  * $pull — { $pull: { tags: 'nodejs' } } — remove matching elements from array  
  * $pullAll — remove all matching values  
  * $addToSet — add element only if not already present (no duplicates)  
  * $pop — remove first (-1) or last (1) element  
  * $ positional operator — update first matching array element  
  * $\[\] — update all array elements  
  * $\[identifier\] — update filtered array elements with arrayFilters  
* Options:  
  * upsert: true — create document if no match found  
  * multi: true — for older driver, use updateMany instead  
* Mongoose methods:  
  * Model.findByIdAndUpdate(id, update, { new: true }) — returns updated document (new: true) or original (default)  
  * Model.findOneAndUpdate(filter, update, options)  
  * Model.updateOne / updateMany — same as native driver  
  * runValidators: true option — run schema validators on update (not run by default)

---

**Q9. How do Delete operations work in MongoDB?** `[Fresher]`

* deleteOne(filter) — delete first matching document, returns deletedCount  
* deleteMany(filter) — delete all matching documents, returns deletedCount  
* deleteMany({}) — delete ALL documents in collection (dangerous — no confirmation)  
* Mongoose equivalents:  
  * Model.deleteOne(filter)  
  * Model.deleteMany(filter)  
  * Model.findByIdAndDelete(id) — find, delete, return deleted document  
  * Model.findOneAndDelete(filter) — find, delete, return deleted document  
* Soft delete vs hard delete:  
  * Hard delete — document permanently removed from DB  
  * Soft delete — set deletedAt timestamp or isDeleted boolean, filter out in queries  
  * Why soft delete — audit trail, accidental deletion recovery, GDPR compliance (can fully delete later)  
* Soft delete in Mongoose — mongoose-delete plugin or manual implementation:  
  * Add deletedAt: Date field to schema  
  * Override all find methods to add { deletedAt: { $exists: false } } automatically  
  * restore() method to unset deletedAt  
* Drop collection — db.collection.drop() — removes entire collection and its indexes  
* Cascade delete — MongoDB has no built-in cascade, must handle manually in application:  
  * Delete user → also delete all their posts, comments, sessions in service layer  
  * Mongoose middleware — pre('deleteOne') hook to cascade related deletions

---

### **5\. Indexing**

---

**Q10. What are indexes in MongoDB and why are they important?** `[1-2 yrs]`

* Index — special data structure that stores small portion of collection data in easy-to-traverse form  
* Without index — MongoDB does collection scan (COLLSCAN) — examines every document  
* With index — MongoDB does index scan (IXSCAN) — examines only relevant documents  
* Performance impact — queries on large collections 100x-1000x faster with proper indexes  
* Default index — \_id field is always indexed automatically  
* Creating indexes:  
  * db.collection.createIndex({ field: 1 }) — ascending (1) or descending (-1)  
  * mongoose schema — { field: { type: String, index: true } }  
  * mongoose schema — { timestamps: true } creates index on createdAt/updatedAt  
  * Model.createIndexes() — sync schema indexes to MongoDB  
* Index types:  
  * Single field — most common, one field  
  * Compound — multiple fields, covered below  
  * Multikey — automatically created when indexing array field, one entry per array element  
  * Text — full-text search, tokenizes strings  
  * Geospatial — 2dsphere for GPS coordinates, $near, $geoWithin queries  
  * Hashed — hash of field value, only equality queries, good for sharding key  
  * TTL — Time To Live, automatically delete documents after specified time:  
    * createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 })  
    * Great for sessions, OTPs, temporary data  
    * MongoDB background thread removes expired documents every 60 seconds  
  * Wildcard — { '$\*\*': 1 } — index all fields or specific nested paths  
* Index options:  
  * unique: true — enforce uniqueness constraint  
  * sparse: true — only index documents where field exists  
  * background: true — legacy, now all indexes build in background  
  * partialFilterExpression — index only documents matching condition  
  * collation — language-specific string comparison rules  
* Explain plan — db.collection.find(query).explain('executionStats') — analyze query performance:  
  * COLLSCAN — no index used, slow  
  * IXSCAN — index used, fast  
  * totalDocsExamined vs nReturned — ratio shows index effectiveness

---

**Q11. What are Compound Indexes and how do they work?** `[1-2 yrs]`

* Compound index — index on multiple fields in specified order  
* createIndex({ lastName: 1, firstName: 1, age: \-1 })  
* Index prefix rule — compound index can serve queries on:  
  * { lastName } — uses index  
  * { lastName, firstName } — uses index  
  * { lastName, firstName, age } — uses index  
  * { firstName } alone — does NOT use index (not a prefix)  
  * { age } alone — does NOT use index  
* Sort optimization — compound index can satisfy sort operations:  
  * Index on { status: 1, createdAt: \-1 } — serves query with same sort  
  * Sort direction must match index direction or be completely reversed  
* Covered query — query fully satisfied by index without examining documents:  
  * All queried fields AND all projected fields are in the index  
  * Most efficient possible query — no document fetch needed  
* Index selectivity — high selectivity means few documents match — better index efficiency:  
  * email field — high selectivity, unique per user  
  * status field — low selectivity if only 3 values  
  * Put high selectivity fields first in compound index for best performance  
* ESR rule for compound index order — Equality, Sort, Range:  
  * Fields used in equality conditions first  
  * Fields used in sort second  
  * Fields used in range conditions last  
* Index intersection — MongoDB can sometimes use two separate indexes together, but compound index usually more efficient  
* Too many indexes — each index costs write performance and storage — only create indexes you actually need  
* Unused indexes — db.collection.aggregate(\[{$indexStats:{}}\]) — identify never-used indexes and drop them

---

### **6\. Aggregation Framework**

---

**Q12. What is the MongoDB Aggregation Framework?** `[1-2 yrs]`

* Aggregation pipeline — sequence of stages that process documents and transform them  
* Documents flow through pipeline, each stage transforms the stream  
* More powerful than find() — can group, reshape, join, calculate, filter across multiple steps  
* db.collection.aggregate(\[stage1, stage2, stage3\])  
* Key stages:  
  * $match — filter documents, like find() filter, should be first stage for performance (uses indexes)  
  * $project — reshape documents, include/exclude/add/rename fields  
  * $group — group documents by expression, calculate aggregates  
  * $sort — sort documents by field  
  * $limit — limit number of documents  
  * $skip — skip number of documents (for pagination with $limit)  
  * $lookup — left outer join with another collection  
  * $unwind — deconstruct array field, one document per array element  
  * $addFields — add new fields without removing existing ones  
  * $replaceRoot — replace entire document with a subdocument  
  * $count — count documents in pipeline  
  * $facet — run multiple sub-pipelines in parallel  
  * $bucket / $bucketAuto — categorize documents into buckets  
  * $out — write pipeline results to a collection  
  * $merge — merge pipeline results into existing collection

---

**Q13. How does $match and $group work in aggregation?** `[1-2 yrs]`

* $match — filter stage, reduces document count early in pipeline:  
  * { $match: { status: 'active', age: { $gte: 18 } } }  
  * Use $match as first stage whenever possible — uses indexes, reduces documents for subsequent stages  
  * After $group — filter on aggregated values with second $match  
  * Equivalent to SQL WHERE clause  
* $group — group documents by expression, calculate aggregated values:  
  * \_id — required, defines grouping key — what to group by  
  * \_id: '$department' — group by department field  
  * \_id: null — group all documents into one (for collection-wide aggregation)  
  * \_id: { year: { year:′year: ' year:′createdAt' }, month: { month:′month: ' month:′createdAt' } } — compound grouping key  
  * Accumulator operators:  
    * sum — { $sum: ' amount' } — sum values, { $sum: 1 } — count documents  
    * $avg — calculate average  
    * $min / $max — minimum/maximum value in group  
    * $first / $last — first/last value in group (after sort)  
    * $push — collect values into array  
    * $addToSet — collect unique values into array  
    * $count — count documents in group (v5.0+)  
* Practical example — sales report:  
  * $match — only completed orders  
  * $group — by product category, sum total revenue, count orders  
  * $sort — by total revenue descending  
  * $limit — top 10 categories  
  * Equivalent to SQL — SELECT category, SUM(amount), COUNT(\*) FROM orders WHERE status='completed' GROUP BY category ORDER BY SUM(amount) DESC LIMIT 10

---

**Q14. How does $lookup work for joining collections?** `[1-2 yrs]`

* $lookup — performs left outer join between collections  
* Basic $lookup:  
  * from — the collection to join with  
  * localField — field from input documents  
  * foreignField — field in joined collection to match against  
  * as — name for output array field containing joined documents  
  * Result — array field added to each document with matching documents from joined collection  
  * Empty array if no matches (left outer join behavior)  
* Uncorrelated $lookup with pipeline (more powerful):  
  * from — collection to join  
  * let — define variables from local document for use in pipeline  
  * pipeline — run aggregation pipeline on joined collection with $$variable references  
  * as — output array field name  
  * More flexible — allows complex join conditions, additional filtering, shaping joined documents  
* $unwind after $lookup:  
  * $lookup always returns array  
  * { unwind:′unwind: ' unwind:′joinedField' } — flatten array, one document per joined element  
  * { unwind: { path: ' joinedField', preserveNullAndEmptyArrays: true } } — keep documents with no match  
* Multiple $lookup stages — chain to join more than two collections  
* Performance considerations:  
  * $lookup is expensive — avoid in hot paths if possible  
  * $match before $lookup to reduce documents being joined  
  * Index foreignField — MongoDB uses index on joined collection  
  * Consider embedding for frequently joined data  
* $lookup vs application-level joins:  
  * $lookup — single round trip to DB, more efficient for large datasets  
  * Mongoose populate() — multiple queries to DB, simpler code, better for small datasets

---

**Q15. How does $project work in aggregation?** `[1-2 yrs]`

* $project — reshape documents in pipeline, include/exclude/transform fields  
* Include field — { $project: { name: 1, email: 1 } }  
* Exclude field — { $project: { password: 0, \_\_v: 0 } }  
* Rename field — { project: { fullName: ' name' } }  
* Add computed field:  
  * String operations — $concat, $toUpper, $toLower, $substr, $trim  
  * Math operations — $add, $subtract, $multiply, $divide, $mod, $abs, $round  
  * Date operations — $year, $month, $dayOfMonth, $hour, $dateToString  
  * Conditional — $cond: { if: condition, then: value, else: otherValue }  
  * $ifNull — provide fallback if field is null  
  * $type — return BSON type of field  
* Array operations in $project:  
  * $size — length of array  
  * $arrayElemAt — element at index  
  * $slice — extract subset of array  
  * $filter — filter array elements  
  * $map — transform each array element  
  * $reduce — reduce array to single value  
* $addFields vs $project:  
  * $project — must explicitly include all fields you want to keep  
  * $addFields — adds/overwrites fields, keeps all existing fields  
  * Use $addFields when adding computed fields without wanting to list all existing fields

---

### **7\. Relationships in MongoDB**

---

**Q16. What are the different ways to model relationships in MongoDB?** `[1-2 yrs]`

* Two fundamental approaches — embedding and referencing  
* No foreign keys or joins at DB level — relationships handled by application or $lookup  
* Embedding (denormalization):  
  * Store related data as subdocument or array within parent document  
  * Single document contains all related data  
  * Example — user document with embedded address object, embedded preferences object  
  * Pros — single query fetches all data, atomic updates on single document, no joins  
  * Cons — document size limit (16MB), duplication if embedded data shared, updating embedded data in many parents is difficult  
* Referencing (normalization):  
  * Store ObjectId of related document in field  
  * Example — post document with authorId field pointing to users collection  
  * Pros — no duplication, independent document updates, no size concerns  
  * Cons — multiple queries or $lookup needed, not atomic across documents  
* One-to-One:  
  * Embed if always accessed together — user and user profile  
  * Reference if one side is large or independently accessed  
  * Example — user embeds contactInfo subdocument  
* One-to-Many:  
  * Embed if "many" is small and bounded — blog post with comments (embed if few comments)  
  * Reference if "many" is large or unbounded — user has thousands of orders (reference)  
  * Example — order has array of embedded line items (bounded), user has array of orderIds (reference)  
* Many-to-Many:  
  * Array of references in one or both sides  
  * Example — student has courseIds array, course has studentIds array  
  * Or separate junction-like approach — enrollment document with studentId and courseId  
  * $lookup to join them in queries  
* Rule of thumb for embedding vs referencing:  
  * Embed — data always accessed together, one-to-one or one-to-few, data doesn't change often  
  * Reference — large or unbounded arrays, data accessed independently, many-to-many, frequently updated shared data

---

**Q17. How does Mongoose populate work for referenced documents?** `[1-2 yrs]`

* populate() — Mongoose feature that replaces ObjectId reference with actual document from referenced collection  
* Not a MongoDB feature — Mongoose makes separate query under the hood  
* Single reference — await Post.findById(id).populate('author') — replaces author ObjectId with full User document  
* Multiple populates — .populate('author').populate('category') or .populate(\['author', 'category'\])  
* Nested populate — .populate({ path: 'author', populate: { path: 'profile' } }) — populate author then author's profile  
* Select fields during populate — .populate({ path: 'author', select: 'name email \-\_id' }) — only fetch specific fields  
* Match condition in populate — .populate({ path: 'comments', match: { approved: true } }) — filter populated documents  
* Options — sort, limit, skip within populate  
* Virtual populate — populate without storing reference array in document:  
  * Schema virtual — ref, localField, foreignField — same as $lookup concept  
  * { virtuals: true } in toJSON/toObject options — include virtuals in output  
  * Useful when you don't want to store array of IDs but still want populate to work  
* populate() vs $lookup:  
  * populate() — multiple queries (N+1 risk for arrays), simpler code, works with Mongoose documents  
  * $lookup — single aggregation query, more efficient for large datasets, returns plain objects  
  * For fetching single document with references — populate() is fine  
  * For list queries or analytics — prefer $lookup in aggregation pipeline

---

### **8\. Transactions in MongoDB**

---

**Q18. What are MongoDB transactions and when should you use them?** `[2-3 yrs]`

* MongoDB transactions — ACID guarantees across multiple documents and collections (v4.0+)  
* ACID:  
  * Atomicity — all operations succeed or all fail, no partial updates  
  * Consistency — DB moves from one valid state to another  
  * Isolation — concurrent transactions don't interfere  
  * Durability — committed transactions survive failures  
* Before transactions — each document operation was atomic, multi-document wasn't  
* Requirement — transactions require replica set (even single node replica set) or sharded cluster  
* Session-based — transactions attached to a ClientSession  
* When to use transactions:  
  * Transfer money between accounts — debit one, credit another atomically  
  * Create order and decrement inventory simultaneously  
  * Register user and create their profile in one atomic operation  
  * Any operation touching multiple documents that must all succeed or all fail  
* When NOT to use transactions — single document operations are already atomic, transactions have performance overhead  
* Transaction in Mongoose:  
  * Start session — const session \= await mongoose.startSession()  
  * session.startTransaction()  
  * Pass session to all operations — User.create(\[doc\], { session })  
  * session.commitTransaction() on success  
  * session.abortTransaction() on error  
  * session.endSession() in finally block — always clean up  
* withTransaction() helper — handles commit, abort, and retry automatically:  
  * session.withTransaction(async () \=\> { ...operations... })  
  * Retries on transient errors automatically  
  * More reliable than manual try/catch approach  
* Transaction limitations:  
  * 60 second time limit by default  
  * Maximum 1000 document modifications per transaction  
  * Higher latency than non-transactional operations  
  * Avoid long-running transactions

---

### **9\. Schema Validation**

---

**Q19. How does schema validation work in MongoDB?** `[1-2 yrs]`

* MongoDB native schema validation — JSON Schema validation rules on collections  
* Two approaches — MongoDB-level validation and Mongoose-level validation  
* MongoDB-level validation (validator option on collection):  
  * db.createCollection('users', { validator: { $jsonSchema: { ... } } })  
  * Enforced at DB level — any driver, any language must comply  
  * validationLevel — strict (default, all inserts/updates) or moderate (existing docs not checked on update)  
  * validationAction — error (reject invalid, default) or warn (allow but log)  
  * JSON Schema operators — bsonType, required, properties, minimum, maximum, minLength, enum, pattern  
* Mongoose-level validation (most common in MERN):  
  * Defined in schema — required, min, max, enum, match, validate  
  * Runs before save() — returns ValidationError if fails  
  * Does NOT run on updateOne/updateMany by default — must pass { runValidators: true }  
  * Custom validator function — validate: { validator: function(v) { return ... }, message: '...' }  
  * Async validators — validator function returns Promise  
  * Cross-field validation — validate at schema level or in pre-save hook  
* When to use each:  
  * Mongoose validation — application layer, good for MERN apps using Mongoose, rich error messages  
  * MongoDB native validation — DB layer, language-agnostic, last line of defense  
  * Best practice — use both — Mongoose for rich UX error messages, MongoDB for data integrity guarantee  
* Validation error handling in Express — catch ValidationError from Mongoose, return 400 with field-level errors  
* @nestjs/mongoose — validation decorators on schema classes work same way

---

### **10\. MongoDB Atlas**

---

**Q20. What is MongoDB Atlas and what are its key features?** `[Fresher]`

* MongoDB Atlas — MongoDB's fully managed cloud database service  
* Available on AWS, Google Cloud, and Azure  
* Free tier — M0 cluster, 512MB storage, shared resources, good for development and learning  
* Key features:  
  * Automated backups — continuous backup with point-in-time recovery  
  * Auto-scaling — scale storage and compute automatically  
  * Global clusters — distribute data across multiple regions  
  * Atlas Search — full-text search built on Lucene, no Elasticsearch needed  
  * Atlas Data API — RESTful HTTP API to access data without drivers  
  * Atlas App Services — serverless functions, triggers, sync for mobile  
  * Atlas Charts — built-in data visualization  
  * Performance Advisor — recommends indexes based on query patterns  
  * Real-time Performance Panel — monitor operations, connections, opcounters  
  * Database Auditing — log all database activity for compliance  
* Connection from Node.js:  
  * Get connection string from Atlas dashboard — Connect button on cluster  
  * Replace password and database name in connection string  
  * Add IP to access list — 0.0.0.0/0 for development, specific IPs for production  
  * Network peering — connect from AWS/GCP/Azure without public internet  
* Atlas in MERN production:  
  * Store MONGODB\_URI in environment variables — never hardcode  
  * Enable IP access list — restrict to server IP in production  
  * Create dedicated DB user with minimum required permissions  
  * Enable encryption at rest and in transit  
  * Set up alerts for connection count, storage usage, query performance

---

### **11\. Replication & Sharding**

---

**Q21. What is a Replica Set in MongoDB?** `[2-3 yrs]`

* Replica set — group of MongoDB servers that maintain same dataset for high availability  
* Minimum recommended — 3 nodes (1 primary \+ 2 secondaries)  
* Primary node — receives all write operations, one primary at a time  
* Secondary nodes — replicate primary's oplog, maintain copy of data, serve read operations if configured  
* Oplog (operations log) — special capped collection recording all write operations in order  
* Automatic failover — if primary becomes unavailable, secondaries elect new primary (takes \~10 seconds)  
* Read preference — controls where reads go:  
  * primary — all reads from primary (default, strong consistency)  
  * primaryPreferred — primary if available, secondary fallback  
  * secondary — all reads from secondaries (eventual consistency, stale reads possible)  
  * nearest — lowest network latency node  
* Write concern — controls acknowledgment for write operations:  
  * w: 1 — acknowledge from primary only (default)  
  * w: majority — acknowledge from majority of nodes (safer)  
  * w: 0 — fire and forget  
* Read concern — controls data isolation level for reads  
* Atlas automatically sets up replica set — all Atlas clusters are replica sets  
* Why replica sets matter for developers:  
  * Transactions require replica set  
  * Change streams require replica set — real-time change notifications  
  * High availability — app keeps running if one node fails

---

**Q22. What is Sharding in MongoDB?** `[2-3 yrs]`

* Sharding — horizontal scaling by distributing data across multiple servers (shards)  
* Each shard is a replica set — stores subset of total data  
* When to shard — data too large for single server, write throughput exceeds single server capacity  
* Components:  
  * Shards — each stores portion of data, replica sets  
  * mongos — query router, directs queries to correct shard(s)  
  * Config servers — store cluster metadata and shard key mappings  
* Shard key — field(s) used to distribute documents across shards  
  * Chosen carefully — wrong shard key causes hot spots or scatter-gather queries  
  * Good shard key — high cardinality (many unique values), even distribution, frequently used in queries  
  * Bad shard key — low cardinality (boolean), monotonically increasing (ObjectId alone — all inserts hit one shard)  
* Chunk — range of shard key values, MongoDB balances chunks across shards  
* Targeted query — query includes shard key, mongos routes to specific shard — efficient  
* Scatter-gather query — query does not include shard key, mongos must query ALL shards — expensive  
* Sharding strategies:  
  * Range sharding — documents with similar shard key values on same shard — good for range queries, bad for monotonic keys  
  * Hash sharding — hash of shard key distributes evenly — prevents hot spots, bad for range queries  
  * Zone sharding — assign shard key ranges to specific shards — good for geo-distribution  
* Atlas sharding — available on M30+ clusters, configured via Atlas UI

---

### **12\. Security Best Practices**

---

**Q23. What are MongoDB security best practices?** `[2-3 yrs]`

* Authentication — always enable, disabled by default in local MongoDB:  
  * Create admin user first, then enable \--auth flag  
  * Atlas always requires authentication  
  * Use strong passwords — generate random 32+ character passwords  
  * Connection string includes credentials — store in env vars, never commit  
* Authorization — Role-Based Access Control (RBAC):  
  * Built-in roles — read, readWrite, dbAdmin, userAdmin, clusterAdmin  
  * Principle of least privilege — app user should have only readWrite on app database, not admin  
  * Create separate users per application — not one shared admin user  
  * Read-only user for analytics and reporting  
* Network security:  
  * Bind to specific IP — \--bind\_ip 127.0.0.1 for local only  
  * Atlas IP Access List — whitelist specific IPs, not 0.0.0.0/0 in production  
  * VPC peering / Private Link — connect without public internet in production  
  * Disable direct internet access to MongoDB port (27017)  
  * Firewall rules — only allow app servers to connect to MongoDB  
* Encryption:  
  * TLS/SSL — encrypt data in transit, always enabled in Atlas  
  * Encryption at rest — Atlas encrypted storage, or MongoDB KMIP for self-hosted  
  * Field-level encryption — encrypt specific sensitive fields (credit cards, SSN) before storing  
* Injection prevention:  
  * NoSQL injection — user input used directly in queries can manipulate query operators  
  * express-mongo-sanitize — removes $ and . from req.body, req.query  
  * Validate all query input — use Mongoose validators or class-validator in NestJS  
  * Use parameterized queries — Mongoose query builders are safe, avoid string concatenation  
* Auditing and monitoring:  
  * Enable audit logging — track all DB operations, changes to users and roles  
  * Atlas alerting — set up alerts for unusual activity  
  * Monitor failed authentication attempts  
  * Regularly rotate credentials  
  * Use Atlas database access history  
* Backups:  
  * Atlas automated backups — enable on all production clusters  
  * Test restore process regularly — backup is useless if restore fails  
  * Retention policy — keep backups for compliance requirements

---

That is the complete MongoDB section — 23 questions with full subtopic depth, ready to merge into your MERN Interview Kit.
---

[⬅️ Previous: Advanced Topics](../../MERN_Study_Structure/03_Backend_Development_Nodejs_E/09_Advanced_Topics/09_Advanced_Topics.md) | [🏠 Home](../../README.md) | [Next: PostgreSQL ➡️](../../MERN_Study_Structure/04_Databases_MongoDB_PostgreSQL/02_PostgreSQL/02_PostgreSQL.md)

---
<div align='center'>
  <img src='https://img.shields.io/badge/Curriculum_Designed_By-Aniket_Raj-007ACC?style=for-the-badge&logo=github&logoColor=white' />
</div>