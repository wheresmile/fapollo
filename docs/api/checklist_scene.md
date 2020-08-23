# 清单场景相关接口


## api

#### 获取每日清单场景列表

* `GET /api/v1/checklist_scene/all?last_scene_id=0`
* 参数
    * last_scene_id, 最后拉取的 scene_id，默认为 0
* 响应(每次返回10个)
```js
{
  "code": 200,
  "msg":"",
  "data": {
    "last_id": 1,
    "has_more": 1 | 0,
    "scenes": [
      {
        "id": 1,
        "description": "置办租赁备案关键流程资料",
        "item_count": 10  // 清单数目
      }
    ]
  }
```


#### 获取特定场景的清单列表

* `GET /api/v1/checklist_scene/checklists?scene_id=1`
* 参数
    * scene_id, 场景id
* 响应
```js
{
  "code": 200,
  "msg":"",
  "data": [
    {
      "id": 1,
      "description": "学习",
      "checked_count": 1,  // 历史有多少次今日打卡
      "checked": 1|0,  // 如果用户登录，1表示已打卡；用户未登录时一直返回0
    }
  ]
}
```