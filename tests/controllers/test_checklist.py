# -*- coding: utf-8 -*-
import json


def test_get_home_tabs(client):
    response = client.get('/api/v1/checklist/home')
    assert response.status_code == 200

    res_json = json.loads(response.get_data(as_text=True))
    data = res_json["data"]
    assert type(data) is list
    assert len(data) == 2
    assert data[0]["checked_count"] == 0
    assert data[0]["last_review"]["author_nickname"] == "chalvern"




