# -*- coding: utf-8 -*-
import json
from pprint import pprint


def test_checklist_reviews_all(auth):

    response = auth.get("/api/v1/checklist_reviews")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    # pprint(res_json)
    assert res_json["data"]["last_review_id"] == 1
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


