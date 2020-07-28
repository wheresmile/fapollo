# -*- coding: utf-8 -*-
from models.checklist import Checklist, ChecklistScene
from tests.fixtures.user import user_admin


scene_home_checklist = ChecklistScene(
    id=1,
    user_id=user_admin.id,
    description="首页展示的清单列表",
)


checklist_1 = Checklist(
    id=1,
    scene_id=scene_home_checklist.id,
    user_id=user_admin.id,
    description="这是第一个清单，关于诗与远方",
    last_review_id=1,
)

checklist_2 = Checklist(
    id=2,
    scene_id=scene_home_checklist.id,
    user_id=user_admin.id,
    description="这是第二个清单，关于生活",
    last_review_id=2,
)


