# -*- coding: utf-8 -*-
from flask import (
    Blueprint, session, g,
)
from marshmallow import Schema, fields, validate

from controllers.utils import (
    json_required,
    succeed,
    failed, login_required,
)
from models import (
    get_session,
    User, UserInvitation,
)

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


@auth_bp.route("login", methods=["POST"])
@json_required
def login():
    json_dict = g.json_dict
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
@login_required()
def logout():
    # 更新 token，即让所有的终端下线
    session.clear()
    s = g.mysql_session
    user = g.user
    user.reset_token(s)
    return succeed(msg="注销成功")


class SignUpSchema(Schema):
    """
    用来校验 auth 传入的字段
    """
    nickname = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(validate=validate.Length(min=8))
    invitation_code = fields.Str(required=True)


signup_schema = SignUpSchema()


@auth_bp.route("register", methods=["POST"])
@json_required
def register():
    json_dict = g.json_dict
    json_dict = signup_schema.load(json_dict)
    email = json_dict["email"]
    nickname = json_dict["nickname"]
    password = json_dict["password"]
    invitation_code = json_dict["invitation_code"]

    with get_session() as s:
        invitation = UserInvitation.get_by_code(s, invitation_code)
        if invitation is None or invitation.is_used:
            return failed(msg="邀请码无效")
        user = User.register(s, nickname, email, password)
        # 邀请码置位
        invitation.used_by_user(user.id)

        return succeed(msg="注册成功")
