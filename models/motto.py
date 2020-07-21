# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer

from models import Base
from models.base import BaseMixin


class Motto(Base, BaseMixin):
    __tablename__ = "mottoes"

    __table_args__ = (
        {'comment': u'格言'},
    )
    user_id = Column(Integer, index=True, nullable=False, comment="创建用户的id")
    details = Column(String(512), nullable=False, comment="场景描述")
    source = Column(String(64), nullable=True, comment="发布者自填的作者或出处")

    @classmethod
    def add(cls, session, user_id, details, source):
        motto = Motto(
            user_id=user_id,
            details=details,
            source=source,
        )
        session.add(motto)

    @classmethod
    def get_last(cls, session):
        return session.query(cls).order_by(cls.id.desc()).first()
