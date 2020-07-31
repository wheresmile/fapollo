# -*- coding: utf-8 -*-
import datetime


def now():
    return datetime.datetime.now()


def beginning_of_day(dt):
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return dt


def ending_of_day(dt):
    dt = dt.replace(hour=23, minute=59, second=59, microsecond=999999)
    return dt


def beginning_and_end_of_today():
    current_time = now()
    return beginning_of_day(current_time), ending_of_day(current_time)
