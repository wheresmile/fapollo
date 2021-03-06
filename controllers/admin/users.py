# -*- coding: utf-8 -*-
from flask import (
    Blueprint, request, g,
)

from controllers.utils import succeed, login_required
from models import (
    User,
)

admin_users_bp = Blueprint("admin_users", __name__, url_prefix="/api/v1/admin/users")


@admin_users_bp.route("all", methods=["GET"])
@login_required(admin_required=True)
def get_all():
    mysql_session = g.mysql_session
    page_no = request.args.get("page", 1)
    page_size = request.args.get("size", 10)
    page_size = min(page_size, 100)
    offset = (page_no - 1) * page_size
    users = User.get_list(mysql_session, offset=offset, limit=page_size)
    data = []
    for user in users:
        data.append(dict(
            id=user.id,
            nickname=user.nickname,
            email=user.email,
            is_admin=(1 if user.admin else 0),
        ))
    return succeed(data=data)
