# -*- coding: utf-8 -*-
import logging
import glob
import importlib

from flask import Blueprint


def load_bp(app, path="controllers/**/*.py"):
    """
    加载 Blueprint
    :param app: flask app
    :param path:
    :return:
    """
    for file_path in glob.glob(path, recursive=True):
        module_name = file_path.split(".")[0].replace("/", ".")
        try:
            module = importlib.import_module(module_name)

            if "__init__" in file_path:
                continue

            if hasattr(module, "_DO_NOT_LOAD_BP"):
                logging.warning("ignore module %s because of attribute _DO_NOT_LOAD_BP settled", module_name)
                continue

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, Blueprint):
                    logging.info("register %s to flask", attr_name)
                    app.register_blueprint(attr)
        except AttributeError:
            logging.error("failed to load module %s", module_name)
