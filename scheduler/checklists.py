# -*- coding: utf-8 -*-
from models import Checklist, get_session
from scheduler import scheduler


@scheduler.scheduled_job("cron", minute=0, hour=0)
def checklists_reset_checked_count():
    scene_id = 1
    with get_session() as s:
        Checklist.reset_all_checked_count(s, scene_id)

