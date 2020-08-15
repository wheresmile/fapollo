# 标签相关接口

## api

#### 拉取首页的标签


* `GET /api/v1/home/tabs`
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
      "display_name": "今日清单",
      "slug": "checklist"
    }
  ]
}
```