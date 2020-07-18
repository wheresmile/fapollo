# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
)

from controllers.utils import succeed
from models import (
    get_session,
    Tab,
)

tab_bp = Blueprint("tab", __name__, url_prefix="/api/v1/tab")


@tab_bp.route("home", methods=["GET"])
def get_tabs_of_home():
    with get_session() as s:
        tabs = Tab.get_by_location(s, Tab.LOCATION_HOME)
        res = []
        for tab in tabs:
            res.append(dict(
                id=tab.id,
                display_name=tab.display_name,
                slug=tab.slug,
            ))
        return succeed(data=res)
