# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from models import Base
from models.base import BaseMixin


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
    def add(cls, session, user_id, scene_id, description, position_order=1):
        checklist = Checklist(
            user_id=user_id,
            scene_id=scene_id,
            description=description,
            position_order=position_order,
        )
        session.add(checklist)

    @classmethod
    def update(cls, session, checklist_id, description, position_order):
        checklist = cls.get_by_id(session, checklist_id)
        if checklist:
            checklist.description = description
            checklist.position_order = position_order

    @classmethod
    def get_list_by_scene(cls, session, scene_id):
        checklists = session.query(Checklist).filter(
            Checklist.scene_id == scene_id,
            Checklist.deleted_at.is_(None),
        ).order_by(Checklist.position_order.asc()).all()
        return checklists

    @classmethod
    def reset_all_checked_count(cls, session, scene_id):
        session.query(Checklist).filter(
            cls.scene_id == scene_id,
        ).update({Checklist.checked_count: 0, Checklist.last_review_id: 0},
                 synchronize_session=False)

    def update_order(self, position_order):
        self.position_order = position_order

