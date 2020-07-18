# -*- coding: utf-8 -*-


def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert b"pong" in response.data

