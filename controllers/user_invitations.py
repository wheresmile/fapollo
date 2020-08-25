# -*- coding: utf-8 -*-

from flask import Blueprint, g

from controllers.utils import succeed, login_required, failed
from models import get_session, User
from models.user_invitaton import UserInvitation

user_invitation_bp = Blueprint("user_invitation", __name__, url_prefix="/api/v1/user/invitation")


@user_invitation_bp.route("add", methods=["POST"])
@login_required()
def add():
    s = g.mysql_session
    user = g.user
    user_invitation_count = UserInvitation.count_of_user(s, user.id)
    if user_invitation_count >= 10:
        return failed(code=402, msg="邀请码个数已超上限")
    user_invitation_code = UserInvitation.add(s, user.id)
    return succeed(msg="已成功生成",
                   data=dict(
                       code=user_invitation_code.code,
                       is_used=0,
                   ))


@user_invitation_bp.route("all", methods=["GET"])
@login_required()
def get_all_of():
    s = g.mysql_session
    user = g.user
    invitation_codes = UserInvitation.get_all_code_of_user(s, user.id)
    res = []
    for invitation_code in invitation_codes:
        res.append(dict(
            code=invitation_code.code,
            is_used=(1 if invitation_code.is_used else 0),
        ))
    return succeed(data=res)



