# -*- coding: utf-8 -*-
from flask import Blueprint, request

from controllers.utils import succeed
from models import get_session, User
from models.checklist import Checklist
from models.checklist_review import ChecklistReview
from models.kv_config import KvConfig

checklist_bp = Blueprint("checklist", __name__, url_prefix="/api/v1/checklist")


@checklist_bp.route("home", methods=["GET"])
def get_home_checklists():
    """
    获取首页的清单列表
    :return:
    """
    with get_session() as s:
        raw_scene_id = KvConfig.get_value_of_key(s, KvConfig.KEY_HOME_CHECKLIST_SCENE_ID)
        checklists_res = []
        if raw_scene_id:
            checklists = Checklist.get_list_by_scene(s, int(raw_scene_id))
            review_ids = [x.last_review_id for x in checklists]
            reviews = ChecklistReview.get_by_id_list(s, review_ids)
            reviews_id_map = {x.id: x for x in reviews}
            # 评论的用户信息
            review_user_ids = [x.user_id for x in reviews]
            review_users = User.get_by_id_list(s, review_user_ids)
            review_users_id_map = {x.id: x for x in review_users}
            for checklist in checklists:
                single_checklist_info = dict(
                    id=checklist.id,
                    description=checklist.description,
                    checked_count=checklist.checked_count,
                )
                review = reviews_id_map.get(checklist.last_review_id)
                # 设置最后一个评论以及对应评论的作者信息
                if review:
                    review_user = review_users_id_map.get(review.user_id)
                    last_review = dict(
                        description=review.detail,
                    )
                    if review_user:
                        last_review["author_nickname"] = review_user.nickname
                    single_checklist_info["last_review"] = last_review

                checklists_res.append(single_checklist_info)

        return succeed(data=checklists_res)

