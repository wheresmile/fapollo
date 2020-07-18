# -*- coding: utf-8 -*-
import json


def test_register(client):
    response = client.post(
        '/api/v1/auth/register',
        json={"nickname": "zhjw43", "email": "chalvern@163.com", "password": "12345678"}
    )
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["msg"] == "注册成功"


def test_register_invalid_email(client):
    response = client.post(
        '/api/v1/auth/register',
        json={"nickname": "zhjw43", "email": "chalvern@163com", "password": "12345"}
    )
    assert response.status_code == 500


def test_login(client, auth):
    assert client.get('/api/v1/auth/login').status_code == 405
    response = auth.login(email='zhjw43@163.com', password='12345678')
    res_json = json.loads(response.get_data(as_text=True))
    assert res_json["msg"] == "登录成功"
    assert res_json["data"]["token"] == "123456"


def test_logout(auth):
    response = auth.login(email='zhjw43@163.com', password='12345678')
    assert response.status_code == 200
    response = auth.logout()
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["msg"] == "注销成功"
    # 注销后 token 会变化
    response = auth.logout()
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["msg"] == "未登录"


def test_logout_before_login(auth):
    response = auth.logout()
    assert response.status_code == 200
    assert json.loads(response.get_data(as_text=True))["msg"] == "未登录"