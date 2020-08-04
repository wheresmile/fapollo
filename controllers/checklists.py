# -*- coding: utf-8 -*-

from flask import (
    Blueprint,
)

from controllers.utils import succeed, login_required, json_required
from models import (
    get_session, Checklist, ChecklistReview, User,
)

checklists_bp = Blueprint("checklists", __name__, url_prefix="/api/v1/checklists")


@checklists_bp.route("review", methods=["POST"])
@login_required()
@json_required
def add_review(json_dict, token):
    with get_session() as s:
        user = User.get_by_token(s, token)
        checklist = Checklist.get_by_id(s, json_dict["checklist_id"])
        review = ChecklistReview.add_or_update(s, user.id, checklist.id, json_dict.get("mood", "打卡"))
        checklist.last_review_id = review.id
        s.commit()
        return succeed(data=dict(
            review_id=review.id,
            mood=review.detail,
        ))
