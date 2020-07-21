# -*- coding: utf-8 -*-

from flask import Blueprint

from controllers.utils import succeed
from models import get_session, User
from models.checklist import Checklist
from models.checklist_review import ChecklistReview
from models.kv_config import KvConfig
from models.motto import Motto

motto_bp = Blueprint("motto", __name__, url_prefix="/api/v1/motto")


@motto_bp.route("", methods=["GET"])
def get_motto():
    data = dict(
        details="今天可以做点什么有意义的事情？",
        source="见周边",
    )
    with get_session() as s:
        motto_kv = KvConfig.get_value_of_key(session=s, key=KvConfig.KEY_MOTTO_ID)
        if motto_kv is None:
            motto = Motto.get_last(session=s)
        else:
            motto = Motto.get_by_id(s, int(motto_kv.value))
        if motto:
            data["details"] = motto.details
            data["source"] = motto.source
        return succeed(data=data)

