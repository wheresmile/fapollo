# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from scheduler import scheduler


@scheduler.scheduled_job("cron", day_of_week="0-6")
def hello():
    print("hello: {}".format(datetime.now()))
    logging.info("hello: {}".format(datetime.now()))

