# -*- coding: utf-8 -*-
from models import ChecklistReviewStar
from tests.fixtures.user import user_admin
from tests.fixtures.checklist_review import checklist_review_1

checklist_review_star_1 = ChecklistReviewStar(
    id=1,
    user_id=user_admin.id,
    review_id=checklist_review_1.id,
    on=True,
)