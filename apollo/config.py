# -*- coding: utf-8 -*-
import os


class Config:
    def __init__(self):
        # self.SQLALCHEMY_DB_URI = os.getenv("SQLALCHEMY_DB_URI", "sqlite:///instance/tools.db")
        self.SQLALCHEMY_DB_URI = os.getenv("SQLALCHEMY_DB_URI", "mysql+pymysql://root:123456@localhost/fapollo?charset=utf8mb4")
        self.SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO") == "True"
        self.DEBUG = os.getenv("DEBUG") == "True"

        # 配置，一般是全局变量
        self.FLASK_CONFIG = {
            "SECRET_KEY": os.getenv("FLASK_SECRET_KEY", "dev"),
            "SITE_NAME": os.getenv("SITE_NAME", "清单"),
        }


config = Config()
