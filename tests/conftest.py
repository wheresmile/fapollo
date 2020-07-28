# -*- coding: utf-8 -*-
import logging
import os

import sys

from tests.fixtures import save_fixtures

sys.path.insert(0, os.path.dirname(__file__) + "/../")  # noqa

from models import Base, engine, get_session

import pytest

from apollo import create_app


def logging_config():
    stdout_handler = logging.StreamHandler(sys.stderr)
    log = logging.getLogger()
    log.addHandler(stdout_handler)


@pytest.fixture
def app():
    logging_config()
    Base.metadata.create_all(engine)
    with get_session() as session:
        save_fixtures(session)
    app = create_app()
    yield app
    Base.metadata.drop_all(engine)


@pytest.fixture
def client(app):
    return app.test_client()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, email='zhjw43@163.com', password='12345678'):
        return self._client.post(
            '/api/v1/auth/login',
            json={"email": email, "password": password}
        )

    def logout(self):
        return self._client.post('/api/v1/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
