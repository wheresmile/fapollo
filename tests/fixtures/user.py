# -*- coding: utf-8 -*-
from models import User


user_admin = User(
    id=1,
    nickname="chalvern",
    email="zhjw43@163.com",
    password="$2b$12$xxYfYcTKsCsGpnd94Gjg.utYVO7umre1ioBI96uRt7opyF18DJZtu",  # 12345678
    verified=True,
    token="123456",
    admin=True,
)

user_common = User(
    id=2,
    nickname="jingwei",
    email="wheresmile@163.com",
    password="$2b$12$xxYfYcTKsCsGpnd94Gjg.utYVO7umre1ioBI96uRt7opyF18DJZtu",  # 12345678
    verified=True,
    token="1234567",
    admin=False,
)

