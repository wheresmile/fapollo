# -*- coding: utf-8 -*-
import functools
import logging

from flask import (
    jsonify,
    request, g,
)

from models import get_session, User


def response(code, msg, data):
    r = {
        "code": code,  # 业务code
        "msg": msg,  # 提示消息
        "data": {} if data is None else data,
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
        g.json_dict = json_dict
        return func(*args, **kwargs)
    return wrapper


def login_required(required=True, admin_required=False):
    def _login_required(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            token = g.token
            with get_session() as s:
                user = User.get_by_token(s, token)
                if user is None:
                    if required or admin_required:
                        return failed(code=401, msg="未登录")
                else:
                    if admin_required and (not user.admin):
                        return failed(code=403, msg="需要管理员身份")
                    logging.info(f"用户user_id={user.id} 调用了模块 {func.__module__} 中的 {func.__name__} 方法。")

                g.mysql_session = s
                g.user = user
                return func(*args, **kwargs)
        return wrapper
    return _login_required
