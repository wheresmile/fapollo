[toc]

# 账户相关接口

## api

#### 注册

* `POST /api/v1/auth/register`
* 参数
```json
{
  "nickname": "Jing维", 
  "email": "zhjw43@163.com",
  "password": "password", 
  "invitation_code": "from_other_user"
}
```
* 响应

```
// 正常
{
  "code": 200,
  "msg":"注册成功",
  "data": {}
}
```

#### 登录

* `POST /api/v1/auth/login`
* 参数
```json
{
  "email": "your_email",
  "password": "your_password"
}
```
* 响应

```js
{
  "code": 200,
  "msg":"",
  "data":{
    "token": "user_token",  // 目前未使用
  }
}
```

#### 登出（注销登录）

* `POST /api/v1/auth/logout`
* 参数无，需要登录态
* 响应

```js
{
  "code": 200,
  "msg":"注销成功",
  "data": {}
}
```

