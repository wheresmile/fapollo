# -*- coding: utf-8 -*-
import json


def test_get_home_tabs(client):
    response = client.get('/api/v1/tab/home')
    assert response.status_code == 200

    res_json = json.loads(response.get_data(as_text=True))
    assert type(res_json["data"]) is list
    assert res_json["data"][0]["display_name"] == "首页"



