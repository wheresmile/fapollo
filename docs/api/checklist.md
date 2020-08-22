# 清单相关接口

与清单有关的接口

## api

#### 获取每日清单列表

* `GET /api/v1/home/checklists`
* 参数无，登录态可选
* 响应
```js
{
  "code": 200,
  "msg":"",
  "data": [
    {
      "id": 1,
      "description": "学习",
      "checked_count": 1,  // 今日有多少人今日打卡
      "checked": 1|0,  // 如果用户登录，1表示已打卡；用户未登录时一直返回0
      "last_review": {  // 用户自己今日打卡信息，可能为空
        "author_nickname": "jing维", 
        "description": "MySQL文档第一章"
      }
    }
  ]
}
```

#### 打卡今日清单中某个清单

* `POST /api/v1/checklists/review`
* 参数
```js
{
  "checklist_id": 1,  // 打卡清单的id
  "mood": "打卡内容"
}
```
* 响应

```js
{
  "code": 200,
  "msg":"",
  "data": {
    "checklist": {
      "id": 1,
      "checked_count": 2  // 已打卡次数
    }
    "is_new": 1 | 0,  // 当前清单是否是当日首次打卡
    "review_id": 1,  // 打卡对应记录的 id
    "mood": "打卡内容"
  }
}
```