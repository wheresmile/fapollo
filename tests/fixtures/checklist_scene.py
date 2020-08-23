# -*- coding: utf-8 -*-
from models import ChecklistScene
from tests.fixtures.user import user_admin

scene_home_checklist = ChecklistScene(
    id=1,
    user_id=user_admin.id,
    description="首页展示的清单列表",
)

scene_2 = ChecklistScene(
    id=2,
    user_id=user_admin.id,
    description="上海置办租赁备案关键流程资料",
)