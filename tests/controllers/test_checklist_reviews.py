# -*- coding: utf-8 -*-
import json
from pprint import pprint

from tests.fixtures.checklist_review import checklist_review_2


def test_checklist_reviews_all(auth):

    response = auth.get("/api/v1/checklist_reviews")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    # pprint(res_json)
    assert res_json["data"]["last_review_id"] == 1
    assert res_json["data"]["has_more_reviews"] == 0
    reviews = res_json["data"]["reviews"]
    assert len(reviews) == 2
    for review in reviews:
        assert review.get("author") is not None
        assert review.get("checklist") is not None


def test_checklist_reviews_all_with_last_review_id(auth):

    response = auth.get("/api/v1/checklist_reviews?last_review_id=2")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    # pprint(res_json)
    assert res_json["data"]["last_review_id"] == 1
    reviews = res_json["data"]["reviews"]
    assert len(reviews) == 1
    review = reviews[0]
    assert review.get("author") is not None
    assert review.get("checklist") is not None


def test_checklist_reviews_with_login_and_star(auth):
    response = auth.login(email="zhjw43@163.com", password="12345678")
    assert response.status_code == 200

    response = auth.get("/api/v1/checklist_reviews")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    pprint(res_json)
    assert res_json["data"]["last_review_id"] == 1
    reviews = res_json["data"]["reviews"]
    assert len(reviews) == 2
    assert reviews[0].get("has_stared") is 0
    assert reviews[1].get("has_stared") is 1


def test_checklist_reviews_star(auth):
    response = auth.login()
    assert response.status_code == 200
    response = auth.post("/api/v1/checklist_reviews/star", json_data=dict(
        review_id=checklist_review_2.id,
    ))
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["data"]["review_id"] == checklist_review_2.id
    assert res_json["data"]["star_count"] == 1

    # 重复提交
    response = auth.post("/api/v1/checklist_reviews/star", json_data=dict(
        review_id=checklist_review_2.id,
    ))
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["data"]["star_count"] == 1
