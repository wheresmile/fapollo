# -*- coding: utf-8 -*-
from urllib import request

from flask import (
    Blueprint,
)

from controllers.utils import succeed, login_required, json_required
from models import (
    get_session, Checklist, ChecklistReview, User,
)

checklist_reviews_bp = Blueprint("checklist_reviews", __name__, url_prefix="/api/v1/checklist_reviews")


@checklist_reviews_bp.route("", methods=["GET"])
def fetch_all():
    """
    根据传入的 last_review_id 进行抽取，固定每次抽取 fetch_size 个
    :return:
    """
    last_id = request.args.get("last_review_id", 2 >> 31)
    fetch_size = 20
    with get_session() as s:
        ChecklistReview
    return succeed(data={})
