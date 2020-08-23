# 清单打卡相关接口

## api

#### 拉取所有的打卡记录

* `GET /api/v1/checklist_reviews?last_review_id=1`
* 参数，登录态可选
    * last_review_id, 最后拉取的 review_id，默认为 2<<32（降序）
* 响应（每次返回10个）
```js
{
  "code": 200,
  "msg":"",
  "data": {
    "has_more_reviews": 1 | 0,  // 是否有更多的记录
    "last_review_id": 拉取的最后一个 review_id
    "reviews":[
      {
        "author": {
          "id":1,
          "nickname": "Jing维"
        },
        "checklist":{
          "id":1,
          "description": "学习"
        }
        "review_id": 1,
        "created_at": "2020-08-15 13:11:22",
        "review_mood": "阅读MySQL文档第一章",
        "star_count": 0,  // 点赞数
        "has_stared": 1|0,  // 登陆状态下如果当前用户已点赞返回1，其他情况返回0
      }
    ]
  }
}
```


#### 给某个打卡点赞

* `POST /api/v1/checklist_reviews`
* 参数，登录态可选
```js
{
    "review_id": 1
}
```

* 响应
```js
{
  "code": 200,
  "msg":"",
  "data":{
    "review_id": 1,
    "star_count": 1,  // 总共点赞数
    "has_stared": 1|0,  // 登陆状态下如果当前用户已点赞返回1，其他情况返回0
  }
}
```
