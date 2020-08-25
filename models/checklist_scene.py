# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Text

from models import Base
from models.base import BaseMixin


class ChecklistScene(Base, BaseMixin):
    __tablename__ = "checklist_scenes"

    __table_args__ = (
        {'comment': u'场景、场合、某个具体案例、过程'},
    )
    user_id = Column(Integer, index=True, nullable=False, comment="创建此场景的用户id")
    title = Column(String(256), nullable=False, comment="场景主题")
    description = Column(Text, nullable=False, comment="场景描述")
    category = Column(String(32), comment="主分类")
    item_count = Column(Integer, default=0, comment="包含的清单数目")
    priority = Column(Integer, comment="优先级")

    @classmethod
    def add(cls, session, user_id, description):
        """
        某用户添加场景
        """
        scene = ChecklistScene(
            user_id=user_id,
            description=description,
        )
        session.add(scene)
        return scene

    @classmethod
    def update(cls, session, scene_id, description):
        scene = cls.get_by_id(session, scene_id)
        if scene:
            scene.description = description

    @classmethod
    def get_scenes_ref_last_id(cls, session, last_id, limit=10):
        """
        根据最后一个 last_id （开区间）拉取接下来的场景
        :param session:
        :param last_id:
        :param limit:
        :return:
        """
        return session.query(cls).filter(
            cls.id > last_id,
        ).order_by(cls.id.asc()).limit(limit).all()


