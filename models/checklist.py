# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from models import Base
from models.base import BaseMixin


class ChecklistScene(Base, BaseMixin):
    __tablename__ = "checklist_scenes"

    __table_args__ = (
        {'comment': u'场景、场合、某个具体案例、过程'},
    )
    user_id = Column(Integer, index=True, nullable=False, comment="创建此场景的用户id")
    description = Column(String(256), nullable=False, comment="场景描述")


class Checklist(Base, BaseMixin):
    """
    检查列表；用户可以确认
    """

    __tablename__ = "checklists"

    __table_args__ = (
        {'comment': u'清单'},
    )

    user_id = Column(Integer, index=True, nullable=False, comment="创建此条检查项的用户id")
    scene_id = Column(Integer, index=True, nullable=False, comment="场景/场合/案例/过程的id")
    description = Column(String(256), nullable=False, comment="检查项描述")
    checked_count = Column(Integer, nullable=False, default=0, comment="被确认的个数，考虑到并发，这里只是参考值")
    last_review_id = Column(Integer, comment="最后一个评论的id，考虑到并发，这里只是一个参考值")
    position_order = Column(Integer, default=0, comment="排序的序列号")

    @classmethod
    def add(cls, session, user_id, scene_id, description):
        checklist = Checklist(
            user_id=user_id,
            scene_id=scene_id,
            description=description,
        )
        session.add(checklist)

    @classmethod
    def update(cls, session, checklist_id, description):
        checklist = cls.get_by_id(session, checklist_id)
        if checklist:
            checklist.description = description

    @classmethod
    def get_list_by_scene(cls, session, scene_id):
        checklists = session.query(Checklist).filter(
            Checklist.scene_id == scene_id,
            Checklist.deleted_at.is_(None),
        ).all()
        return checklists


