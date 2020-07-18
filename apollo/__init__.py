# -*- coding: utf-8 -*-
import logging

from flask import Flask, session, g

from apollo.config import config
from apollo.load_bp import load_bp


def create_app(test_config=None):
    logging.basicConfig(level=logging.INFO)

    # flask app
    app = Flask(__name__)

    @app.before_request
    def fetch_user():
        token = session.get("token")
        if token:
            from models import get_session
            with get_session() as s:
                from models import User
                user = User.get_by_token(s, token=token)
            g.user = user
        else:
            g.user = None

    # global variables
    for k, v in config.FLASK_CONFIG.items():
        app.config[k] = v

    # 加载 blue_print
    load_bp(app)

    @app.route("/ping")
    def ping():
        return "pong"

    return app


