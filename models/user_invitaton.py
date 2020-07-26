# -*- coding: utf-8 -*-
import uuid
from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Boolean, DateTime, Integer,
)

from models.base import (
    Base,
    BaseMixin,
)


class UserInvitation(Base, BaseMixin):
    __tablename__ = "user_invitations"

    __table_args__ = (
        {'comment': u'用户邀请码'},
    )
    user_id = Column(Integer, index=True, comment="码拥有者的id")
    code = Column(String(64), unique=True, nullable=False, comment="邀请码")
    invited_user_id = Column(Integer, index=True, nullable=True, comment="被邀请者的id")
    is_used = Column(Boolean, nullable=False, default=False, comment="是否使用")
    used_time = Column(DateTime, nullable=True, comment="使用的时间")

    @classmethod
    def add(cls, session, user_id):
        user_invitation = UserInvitation(
            user_id=user_id,
            code=str(uuid.uuid4())
        )
        session.add(user_invitation)
        session.commit()
        return user_invitation

    @classmethod
    def get_by_code(cls, session, code):
        return session.query(cls).filter(
            cls.code == code,
            cls.deleted_at.is_(None),
        ).first()

    @classmethod
    def get_all_code_of_user(cls, session, user_id):
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.deleted_at.is_(None),
        ).all()

    @classmethod
    def count_of_user(cls, session, user_id):
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.deleted_at.is_(None),
        ).count()

    def used_by_user(self, invited_user_id):
        self.invited_user_id = invited_user_id,
        self.is_used = True
        self.used_time = datetime.now()
