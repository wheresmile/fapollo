# -*- coding: utf-8 -*-
import json


def test_admin_get_user_list(client, auth):
    response = auth.login(email='zhjw43@163.com', password='12345678')
    assert response.status_code == 200

    response = client.get("/api/v1/admin/users/all")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["code"] == 200
    response_data = res_json["data"]
    assert type(response_data) is list
    assert len(response_data) == 2


def test_not_admin_get_user_list(client, auth):
    response = auth.login(email='wheresmile@163.com', password='12345678')
    assert response.status_code == 200

    response = client.get("/api/v1/admin/users/all")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["code"] == 400
    assert res_json["msg"] == "需要管理员身份"

