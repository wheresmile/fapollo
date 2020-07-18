# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, DateTime

from models import Base
from models.base import BaseMixin


class KvConfig(Base, BaseMixin):
    KEY_HOME_CHECKLIST_SCENE_ID = "home_checklist_scene_id"  # 首页展示的清单场景id

    __tablename__ = "kv_configs"
    __table_args__ = (
        {'comment': u'key-value配置项'},
    )

    key = Column(String(64), unique=True, nullable=False, comment="键值")
    value = Column(String(512), comment="具体的值")

    @classmethod
    def add_or_update(cls, session, key, value):
        kv_config = cls.find_by_key(session, key)
        if kv_config:
            kv_config.value = value
        else:
            kv_config = KvConfig(
                key=key,
                value=value,
            )
            session.add(kv_config)

    @classmethod
    def get_value_of_key(cls, session, key):
        kv_config = session.query(cls).filter(
            cls.key == key,
        ).first()
        if kv_config:
            return kv_config.value

