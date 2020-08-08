# -*- coding: utf-8 -*-
import glob
import importlib
import logging
from apscheduler.schedulers.gevent import GeventScheduler

scheduler = GeventScheduler()


def _load_scheduler(path="scheduler/**/*.py"):
    """ 动态加载 path 下的所有 scheduler """

    for file_path in glob.glob(path, recursive=True):
        module_name = file_path.split(".")[0].replace("/", ".")
        try:
            if "__init__" in file_path:
                continue
            importlib.import_module(module_name)
        except AttributeError:
            logging.error("failed to load scheduler %s", module_name)


def scheduler_start():
    _load_scheduler()
    scheduler.start()
