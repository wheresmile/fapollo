# -*- coding: utf-8 -*-
import json


def test_get_home_tabs(client):
    response = client.get('/api/v1/home/tabs')
    assert response.status_code == 200

    res_json = json.loads(response.get_data(as_text=True))
    assert type(res_json["data"]) is list
    assert res_json["data"][0]["display_name"] == "首页"


def test_get_home_tabs(client):
    response = client.get('/api/v1/home/checklists')
    assert response.status_code == 200

    res_json = json.loads(response.get_data(as_text=True))
    data = res_json["data"]
    assert type(data) is list
    assert len(data) == 2
    assert data[0]["checked_count"] == 0
    assert data[0]["last_review"]["author_nickname"] == "chalvern"

