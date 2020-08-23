# -*- coding: utf-8 -*-

from flask import (
    Blueprint, request,
)

from controllers.utils import succeed, login_required, json_required, admin_required
from models import (
    get_session, ChecklistScene, Checklist, ChecklistReview, User,
)

checklist_scene_bp = Blueprint("checklist_scene", __name__, url_prefix="/api/v1/checklist_scene")
SCENE_ID_LIMITATION = 2 << 32  # 最大的ID


@checklist_scene_bp.route("all", methods=["GET"])
def fetch_all():
    """
    按照 id 正序给出
    :return:
    """
    last_id = request.args.get("last_scene_id", 0)
    fetch_size = 10
    with get_session() as s:
        scenes = ChecklistScene.get_scenes_ref_last_id(s, last_id=last_id, limit=fetch_size)
        has_more = fetch_size == len(scenes)
        scenes_json = []
        for scene in scenes:
            scene_json = dict(
                id=scene.id,
                description=scene.description,
                item_count=scene.item_count,
            )
            scenes_json.append(scene_json)

        last_id = scenes[-1].id if scenes else SCENE_ID_LIMITATION
        return succeed(data=dict(
            scenes=scenes_json,
            last_id=last_id,
            has_more=(1 if has_more else 0),
        ))


@checklist_scene_bp.route("add", methods=["POST"])
@json_required
@admin_required
def add_scene(mysql_session, admin, json_dict):
    """
    增加场景，暂时限定只管理员有权限
    """
    description = json_dict["description"]
    scene = ChecklistScene.add(mysql_session, admin.id, description)
    mysql_session.commit()
    return succeed(data=dict(
        id=scene.id,
        description=scene.description,
        item_count=scene.item_count,
    ))


@checklist_scene_bp.route("checklists", methods=["GET"])
@login_required(required=False)
def get_checklists_of_scene(token):
    """
    获取某个场景的清单列表
    :return:
    """
    raw_scene_id = request.args.get("scene_id")
    checklists_res = []
    if raw_scene_id is None:
        return succeed(code=400, msg="非法的场景ID")

    with get_session() as s:
        checklists = Checklist.get_list_by_scene(s, int(raw_scene_id))

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

            checklists_res.append(single_checklist_info)

        return succeed(data=checklists_res)