# -*- coding: utf-8 -*-
import glob
import importlib
import logging
from datetime import datetime

from models import Base


def save_fixtures(session, path="tests/fixtures/**/*.py"):
    """
    保存 fixtures 到库中
    """
    model_names_set = set()
    for file_path in glob.glob(path, recursive=True):
        module_name = file_path.split(".")[0].replace("/", ".")
        try:
            module = importlib.import_module(module_name)

            if "__init__" in file_path:
                continue

            if hasattr(module, "_DO_NOT_SAVE"):
                logging.warning("ignore module %s because of attribute _DO_NOT_SAVE settled", module_name)
                continue

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, Base):
                    if attr_name in model_names_set:
                        continue
                    model_names_set.add(attr_name)  # 去重
                    # 创建一个新的对象
                    attr_tmp = attr.__class__(**{c.name: getattr(attr, c.name) for c in attr.__table__.columns})
                    logging.info("add %s to database", attr_name)
                    session.add(attr_tmp)
        except AttributeError:
            logging.error("failed to load module %s", module_name)
