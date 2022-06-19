# 몽고DB 구축방법

[몽고DB사이트](https://www.mongodb.com/)

## 몽고DB의 CRUD

1. C
- db.users.insertOne({name : "hyeon2", email:"hyeon2@gmail.com"})

2. R
- db.users.find()

3. U
- db.users.updateOne({_id : ObjectId("62af16e4d8a633f4b1842236")},{$set: {email: "dong@gmail.com"}}) 

4. D
- db.users.deleteOne({_id : ObjectId("62af16e4d8a633f4b1842236")})
