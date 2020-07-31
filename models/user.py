# -*- coding: utf-8 -*-
import uuid
import bcrypt

from sqlalchemy import (
    Column,
    String,
    Boolean,
)

from models.base import (
    Base,
    BaseMixin,
)


class User(Base, BaseMixin):
    __tablename__ = "users"

    __table_args__ = (
        {'comment': u'用户表'},
    )

    nickname = Column(String(256), nullable=False, comment="昵称")
    email = Column(String(128), nullable=False, unique=True, comment="邮箱")
    password = Column(String(128), nullable=False, comment="加密后的密码")
    verified = Column(Boolean, nullable=False, default=False, comment="是否验证")
    token = Column(String(64), nullable=False, unique=True, comment="返回给前端用来鉴权的 token")
    admin = Column(Boolean, nullable=False, default=False, comment="是否为管理员")

    @classmethod
    def register(cls, session, nickname, email, password):
        user = User(
            nickname=nickname,
            email=email,
            password=cls.gen_password(password),
            token=str(uuid.uuid4()).replace("-", ""),
        )
        session.add(user)
        return user

    @classmethod
    def login(cls, session, email, password):
        user = cls.get_by_email(session, email)
        if user and user.check_password(password):
            return user

    @classmethod
    def logout(cls, session, token):
        user = cls.get_by_token(session, token)
        user.password = str(uuid.uuid4()).replace("-", "")

    @classmethod
    def get_by_email(cls, session, email):
        return session.query(cls).filter(
            cls.email == email,
            cls.deleted_at.is_(None),
        ).first()

    @classmethod
    def get_by_token(cls, session, token):
        return session.query(cls).filter(
            cls.token == token,
            cls.deleted_at.is_(None),
        ).first()

    @classmethod
    def get_list(cls, session, offset, limit):
        return session.query(cls).offset(offset).limit(limit).all()

    def reset_token(self, session):
        self.token = str(uuid.uuid4()).replace("-", "")
        session.add(self)

    @staticmethod
    def gen_password(password):
        return bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt()).decode("utf8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf8"), self.password.encode("utf8"))

    def get_base_info(self):
        """
        获取用户基本信息，可在一些实体的 "作者" 部分进行展示
        :return:
        """
        return dict(
            id=self.id,
            nickname=self.nickname,
        )

