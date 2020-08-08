# -*- coding: utf-8 -*-
from models.checklist import Checklist, ChecklistScene
from tests.fixtures.checklist_scene import scene_home_checklist
from tests.fixtures.user import user_admin


checklist_1 = Checklist(
    id=1,
    scene_id=scene_home_checklist.id,
    user_id=user_admin.id,
    description="这是第一个清单，关于诗与远方",
    last_review_id=1,
    position_order=1,
    checked_count=1,
)

checklist_2 = Checklist(
    id=2,
    scene_id=scene_home_checklist.id,
    user_id=user_admin.id,
    description="这是第二个清单，关于生活",
    last_review_id=2,
    position_order=2,
    checked_count=1,
)

checklist_3 = Checklist(
    id=3,
    scene_id=scene_home_checklist.id,
    user_id=user_admin.id,
    description="这是第三个清单，关于生活",
    position_order=3,
)

