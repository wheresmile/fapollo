# 用户相关接口

## api

#### 获取当前用户信息

* `GET /api/v1/user/info`
* 参数无，需要登录态
* 响应

```js
{
  "code": 200,
  "msg":"",
  "data": [
    {
      "email": "zhjw43@163.com",
      "nickname": "chalvern",
      "is_admin": 1|0  // 管理员1，非管理员0
    }
  ]
}
```
 
#### 添加邀请码

* `POST /api/v1/user/invitation/add`
* 参数无，需要登录态
* 响应

```js 
{
  "code": 200,
  "msg":"已成功生成",
  "data":{
    "code": "invitation_code",
    "is_used": 0
  }
}
```

#### 获取当前用户邀请码列表

* `GET /api/v1/user/invitation/all`
* 参数无，需登录态
* 响应

```js
{
  "code": 200,
  "msg":"已成功生成",
  "data":[
    {
      "code": "invitation_code",
      "is_used": 1|0
    }
  ]
}
```
 