# -*- coding: utf-8 -*-
from flask import Blueprint, g

from controllers.utils import succeed, login_required
from models import get_session, User

user_bp = Blueprint("user", __name__, url_prefix="/api/v1/user/info")


@user_bp.route("", methods=["GET"])
@login_required()
def user_info():
    s = g.mysql_session
    user = g.user
    response = dict(
        nickname=user.nickname,
        email=user.email,
        is_admin=1 if user.admin else 0,
    )
    return succeed(data=response)
