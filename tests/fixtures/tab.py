# -*- coding: utf-8 -*-
from models import Tab

home_tab = Tab(
    id=1,
    display_name="首页",
    slug="/",
    location=Tab.LOCATION_HOME,
)