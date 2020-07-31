# -*- coding: utf-8 -*-
import json

from tests.fixtures.checklist import checklist_1


def test_add_review_to_checklist(auth):
    response = auth.login()
    assert response.status_code == 200

    mood_1 = "哈哈😸，又坚持了一天"
    response = auth.post("/api/v1/checklists/review", json_data=dict(
        checklist_id=checklist_1.id,
        mood=mood_1,
    ))
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["data"]["review_id"] is not None
    assert res_json["data"]["mood"] == mood_1

    old_review_id = res_json["data"]["review_id"]

    # 如果已经存在过，则更新
    mood_2 = "再坚持一天"
    response = auth.post("/api/v1/checklists/review", json_data=dict(
        checklist_id=checklist_1.id,
        mood=mood_2,
    ))
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    new_review_id = res_json["data"]["review_id"]
    assert old_review_id == new_review_id
    assert res_json["data"]["mood"] == mood_2

