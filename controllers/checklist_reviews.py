# -*- coding: utf-8 -*-
from flask import (
    Blueprint, request,
)

from controllers.utils import succeed, login_required, json_required
from models import (
    get_session, Checklist, ChecklistReview, User, ChecklistReviewStar,
)

checklist_reviews_bp = Blueprint("checklist_reviews", __name__, url_prefix="/api/v1/checklist_reviews")

REVIEW_ID_LIMITATION = 2 << 32  # 最大的ID


@checklist_reviews_bp.route("", methods=["GET"])
@login_required(required=False)
def fetch_all(token):
    """
    根据传入的 last_review_id 进行抽取，固定每次抽取 fetch_size 个
    :return:
    """
    last_id = request.args.get("last_review_id", REVIEW_ID_LIMITATION)
    fetch_size = 20
    with get_session() as s:
        reviews = ChecklistReview.get_reviews_ref_last_review_id(s, last_id, fetch_size)
        # 发布阅评的用户信息
        user_ids = [x.user_id for x in reviews]
        users = User.get_by_id_list(s, user_ids)
        users_id_map = {x.id: x for x in users}
        # 每个阅评对应的检查项
        checklist_ids = [x.checklist_id for x in reviews]
        checklists = Checklist.get_by_id_list(s, checklist_ids)
        checklists_id_map = {x.id: x for x in checklists}

        # 点赞
        review_star_map = {}
        if token:
            user = User.get_by_token(s, token)
            review_ids = [x.id for x in reviews]
            review_stars = ChecklistReviewStar.get_reviews_star_of_user(s, user.id, review_ids)
            review_star_map = {x.review_id: x for x in review_stars}

        reviews_json = []
        for review in reviews:
            review_json = dict(
                review_id=review.id,
                review_mood=review.detail,
                star_count=review.star_count,
                created_at=review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                has_stared=0,
            )
            # 组装用户信息，如果不存在用户信息，说明数据不完整，不做记录
            review_author = users_id_map.get(review.user_id)
            if review_author is None:
                continue
            review_json["author"] = review_author.get_base_info()

            # 组装检查项信息
            checklist = checklists_id_map.get(review.checklist_id)
            if checklist is None:
                continue
            review_json["checklist"] = dict(
                id=checklist.id,
                description=checklist.description,
            )

            # 拼点赞信息
            review_star = review_star_map.get(review.id)
            if review_star:
                review_json["has_stared"] = 1

            reviews_json.append(review_json)

        last_review_id = reviews[-1].id if reviews else -1

        return succeed(data=dict(
            reviews=reviews_json,
            last_review_id=last_review_id,
        ))


@checklist_reviews_bp.route("star", methods=["POST"])
@login_required()
@json_required
def star(json_dict, token):
    review_id = json_dict["review_id"]
    with get_session() as s:
        user = User.get_by_token(s, token)
        review = ChecklistReview.get_by_id(s, review_id)
        is_add_success = ChecklistReviewStar.add_star(s, user.id, review.id)
        if is_add_success:
            review = ChecklistReview.add_star_count(s, review.id, 1)
        return succeed(data=dict(
            review_id=review_id,
            star_count=review.star_count,
        ))
