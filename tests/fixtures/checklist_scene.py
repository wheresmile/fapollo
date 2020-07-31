# -*- coding: utf-8 -*-
from models import ChecklistScene
from tests.fixtures.user import user_admin

scene_home_checklist = ChecklistScene(
    id=1,
    user_id=user_admin.id,
    description="首页展示的清单列表",
)