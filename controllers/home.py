# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
)

from controllers.utils import succeed, login_required
from models import (
    get_session,
    Tab, KvConfig, Checklist, ChecklistReview, User,
)

home_bp = Blueprint("home", __name__, url_prefix="/api/v1/home")


@home_bp.route("tabs", methods=["GET"])
def get_tabs_of_home():
    with get_session() as s:
        tabs = Tab.get_by_location(s, Tab.LOCATION_HOME)
        res = []
        for tab in tabs:
            res.append(dict(
                id=tab.id,
                display_name=tab.display_name,
                slug=tab.slug,
            ))
        return succeed(data=res)


@home_bp.route("checklists", methods=["GET"])
@login_required(required=False)
def get_home_checklists(token):
    """
    获取首页的清单列表
    :return:
    """
    with get_session() as s:
        raw_scene_id = KvConfig.get_value_of_key(s, KvConfig.KEY_HOME_CHECKLIST_SCENE_ID)
        checklists_res = []
        if raw_scene_id is None:
            return succeed(data=checklists_res)

        checklists = Checklist.get_list_by_scene(s, int(raw_scene_id))
        # 检索每个检查项全平台最后一次提交
        review_ids = [x.last_review_id for x in checklists]
        reviews = ChecklistReview.get_by_id_list(s, review_ids)
        reviews_id_map = {x.id: x for x in reviews}
        # 评论的用户信息
        review_user_ids = [x.user_id for x in reviews]
        review_users = User.get_by_id_list(s, review_user_ids)
        review_users_id_map = {x.id: x for x in review_users}

        # 检索自己是否打卡的相关信息
        my_reviews_id_map = {}
        if token:
            user = User.get_by_token(s, token)
            my_reviews = ChecklistReview.get_today_list_of_user(s, user.id)
            my_reviews_id_map = {x.checklist_id: x for x in my_reviews}

        for checklist in checklists:
            single_checklist_info = dict(
                id=checklist.id,
                description=checklist.description,
                checked_count=checklist.checked_count,
                checked=0,
            )
            if my_reviews_id_map.get(checklist.id):
                single_checklist_info["checked"] = 1
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
