# 格言


## api

#### 获取今日格言（单条）

* `GET /api/v1/motto`
* 参数无
* 响应

```js
{
  "code": 200,
  "msg":"",
  "data": [
    {
      "details": "今天做点什么有意义的事情？",
      "source": "见周边"
    }
  ]
}
```