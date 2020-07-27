# -*- coding: utf-8 -*-
import json


def test_add_user_invitation(client, auth):
    response = auth.login(email='zhjw43@163.com', password='12345678')
    assert response.status_code == 200

    response = client.post("/api/v1/user/invitation/add", json=None)
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["code"] == 200
    assert res_json["data"]["is_used"] == 0
    assert res_json["data"].get("code") is not None


def test_get_all_user_invitations(client, auth):
    response = auth.login(email='zhjw43@163.com', password='12345678')
    assert response.status_code == 200

    response = client.get("/api/v1/user/invitation/all")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["code"] == 200
    response_data = res_json["data"]
    assert type(response_data) is list
    assert len(response_data) == 2
