# -*- coding: utf-8 -*-
from models import ChecklistReview
from tests.fixtures.user import user_admin

checklist_review_1 = ChecklistReview(
    user_id=user_admin.id,
    checklist_id=1,
    detail="第一个评论",
)

checklist_review_2 = ChecklistReview(
    user_id=user_admin.id,
    checklist_id=2,
    detail="第二个评论",
)