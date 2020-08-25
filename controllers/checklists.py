# -*- coding: utf-8 -*-

from flask import (
    Blueprint, g,
)

from controllers.utils import succeed, login_required, json_required
from models import (
    get_session, Checklist, ChecklistReview, User,
)

checklists_bp = Blueprint("checklists", __name__, url_prefix="/api/v1/checklists")


@checklists_bp.route("review", methods=["POST"])
@login_required()
@json_required
def add_review():
    json_dict=g.json_dict
    s = g.mysql_session
    user = g.user
    checklist = Checklist.get_by_id(s, json_dict["checklist_id"])
    is_new, review = ChecklistReview.add_or_update(s, user.id, checklist.id, json_dict.get("mood", "打卡"))
    s.commit()
    if is_new:  # 下面的更新存在并发问题
        checklist.checked_count += 1
        checklist.last_review_id = review.id
    return succeed(data=dict(
        checklist=dict(
            id=checklist.id,
            checked_count=checklist.checked_count,
        ),
        is_new=(1 if is_new else 0),
        review_id=review.id,
        mood=review.detail,
    ))
