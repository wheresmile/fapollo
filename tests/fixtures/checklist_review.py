# -*- coding: utf-8 -*-
from models import ChecklistReview
from tests.fixtures.checklist import checklist_1, checklist_2
from tests.fixtures.user import user_admin

checklist_review_1 = ChecklistReview(
    id=1,
    user_id=user_admin.id,
    checklist_id=checklist_1.id,
    detail="第一个评论",
    star_count=1,
)

checklist_review_2 = ChecklistReview(
    id=2,
    user_id=user_admin.id,
    checklist_id=checklist_2.id,
    detail="第二个评论",
    star_count=0,
)

