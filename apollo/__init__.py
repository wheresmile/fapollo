# -*- coding: utf-8 -*-
import logging

from flask import Flask, session, g

from apollo.config import config
from apollo.load_bp import load_bp
from scheduler import scheduler_start


def create_app(test_config=None):
    logging.basicConfig(level=logging.INFO)

    # flask app
    app = Flask(__name__)

    @app.before_request
    def fetch_user():
        token = session.get("token")
        if token:
            g.token = token
        else:
            g.token = None

    # global variables
    for k, v in config.FLASK_CONFIG.items():
        app.config[k] = v

    # 加载 blue_print
    load_bp(app)
    # 定时任务
    scheduler_start()

    @app.route("/api/ping")
    def ping():
        return "pong"

    return app


