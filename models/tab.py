# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, String

from models import Base
from models.base import BaseMixin


class Tab(Base, BaseMixin):
    """
    标签以及其跳转
    """
    LOCATION_HOME = "home"  # 主页场景

    __tablename__ = "tabs"

    __table_args__ = (
        {'comment': u'标签及其跳转配置'},
    )

    display_name = Column(String(256), nullable=False, comment="标签展示名")
    slug = Column(String(256), nullable=False, comment="标签跳转路径")
    location = Column(String(256), nullable=False, comment="标签位置")

    @classmethod
    def register(cls, session, display_name, slug, location):
        tab = Tab(
            display_name=display_name,
            slug=slug,
            location=location,
        )
        return tab

    @classmethod
    def update(cls, session, tab_id, display_name, slug):
        tab = cls.get_by_id(session, tab_id)
        tab.display_name = display_name
        tab.slug = slug
        return tab

    @classmethod
    def get_by_location(cls, session, location):
        return session.query(cls).filter(
            cls.location == location,
            cls.deleted_at.is_(None),
        ).all()

    @classmethod
    def get_by_id(cls, session, tab_id):
        return session.query(cls).filter(
            cls.id == tab_id,
        ).first()
