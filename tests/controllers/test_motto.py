# -*- coding: utf-8 -*-
import json


def test_get_home_tabs(client):
    response = client.get('/api/v1/motto')
    assert response.status_code == 200

    res_json = json.loads(response.get_data(as_text=True))
    data = res_json["data"]
    assert data["details"] == "今天可以做点什么有意义的事情？"
    assert data["source"] == "见周边"