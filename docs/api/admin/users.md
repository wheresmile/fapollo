# 管理员-用户相关

管理员视角下，用户相关的接口。

## api

#### 获取用户列表

* `GET /api/v1/admin/users/all?page=1&size=10`
* 参数
    * page, 表示页码，默认为1
    * size，表示每页返回的个数，默认为10
* 响应

```js
{
  "code": 200,
  "msg":"",
  "data": [
    {
      "id": 1,
      "email": "zhjw43@163.com",
      "nickname": "chalvern",
      "is_admin": 1|0  // 管理员1，非管理员0
    }
  ]
}
```
 