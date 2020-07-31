# -*- coding: utf-8 -*-
import functools

from flask import (
    jsonify,
    request, g,
)

from models import get_session, User


def response(code, msg, data):
    r = {
        "code": code,  # 业务code
        "msg": msg,  # 提示消息
        "data": data or {},
    }
    return jsonify(r)


def succeed(code=200, msg="", data=None):
    return response(code, msg, data)


def failed(code=400, msg="", data=None):
    return response(code, msg, data)


def json_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        json_dict = request.get_json()
        if not json_dict:
            return failed(msg="参数非法")

        return func(json_dict, *args, **kwargs)
    return wrapper


def login_required(required=True):
    def _login_required(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = g.token
            if token is None and required:
                return failed(msg="未登录")
            return func(token, *args, **kwargs)
        return wrapper
    return _login_required


def login_optioned(func):
    """
    登陆是可选的情况
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = g.token
        return func(token, *args, **kwargs)

    return wrapper


def admin_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = g.token
        if token is None:
            return failed(msg="未登录")
        with get_session() as s:
            user = User.get_by_token(s, token)
            if not user.admin:
                return failed(msg="需要管理员身份")
            return func(user, *args, **kwargs)

    return wrapper