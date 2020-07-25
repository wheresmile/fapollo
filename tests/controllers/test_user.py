# -*- coding: utf-8 -*-
import json


def test_get_user_info(client, auth):
    response = auth.login(email='zhjw43@163.com', password='12345678')
    assert response.status_code == 200

    response = client.get("/api/v1/user/info")
    assert response.status_code == 200
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["code"] == 200
    assert res_json["data"]["email"] == "zhjw43@163.com"

