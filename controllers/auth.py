# -*- coding: utf-8 -*-
from flask import (
    Blueprint, session,
)
from marshmallow import Schema, fields, validate

from controllers.utils import (
    json_required,
    succeed,
    failed, login_required,
)
from models import (
    get_session,
    User,
)

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


class AuthSchema(Schema):
    """
    用来校验 auth 传入的字段
    """
    nickname = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(validate=validate.Length(min=8))


auth_schema = AuthSchema()


@auth_bp.route("login", methods=["POST"])
@json_required
def login(json_dict):
    email = json_dict["email"]
    password = json_dict["password"]

    with get_session() as s:
        user = User.get_by_email(s, email)
        if not user:
            return failed(msg="邮箱或密码不对=_=")

        user = User.login(s, email, password)
        if not user:
            return failed(msg="邮箱或密码不对。。")
        session["token"] = user.token
        return succeed(msg="登录成功", data={"token": user.token})


@auth_bp.route("logout", methods=["POST"])
@login_required
def logout(user):
    session.clear()
    # 更新 token，即让所有的终端下线
    with get_session() as s:
        user.reset_token(s)
    return succeed(msg="注销成功")


@auth_bp.route("register", methods=["POST"])
@json_required
def register(json_dict):
    json_dict = auth_schema.load(json_dict)
    email = json_dict["email"]
    nickname = json_dict["nickname"]
    password = json_dict["password"]
    if len(password) < 8:
        return failed(msg="密码至少8位")

    with get_session() as s:
        user = User.register(s, nickname, email, password)
        return succeed(msg="注册成功", data={"token": user.token})
