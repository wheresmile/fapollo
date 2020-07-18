# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, String, Integer

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
    priority = Column(Integer, nullable=False, comment="权重，用来标识展示顺序")
    location = Column(String(256), nullable=False, comment="标签位置")

    @classmethod
    def add(cls, session, display_name, slug, location, priority):
        tab = Tab(
            display_name=display_name,
            slug=slug,
            location=location,
            priority=priority,
        )
        session.add(tab)
        return tab

    @classmethod
    def update(cls, session, tab_id, display_name, slug, priority):
        tab = cls.get_by_id(session, tab_id)
        tab.display_name = display_name
        tab.slug = slug
        tab.priority = priority
        return tab

    @classmethod
    def get_by_location(cls, session, location):
        return session.query(cls).filter(
            cls.location == location,
            cls.deleted_at.is_(None),
        ).order_by(cls.priority).all()

    @classmethod
    def get_by_id(cls, session, tab_id):
        return session.query(cls).filter(
            cls.id == tab_id,
        ).first()
