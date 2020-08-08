# -*- coding: utf-8 -*-
from models import get_session, Checklist
from tests.fixtures.checklist import checklist_1


def test_reset_all_checked_count(client):
    assert checklist_1.checked_count != 0
    assert checklist_1.last_review_id != 0

    with get_session() as s:
        Checklist.reset_all_checked_count(s, checklist_1.scene_id)
    with get_session() as s:
        checklist_1_after = Checklist.get_by_id(s, checklist_1.id)
        assert checklist_1_after.checked_count == 0
        assert checklist_1_after.last_review_id == 0
