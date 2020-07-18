# -*- coding: utf-8 -*-
import datetime
import contextlib

from sqlalchemy import (
    create_engine,
    Column,
    DateTime,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from apollo.config import config

engine = create_engine(config.SQLALCHEMY_DB_URI, echo=config.SQLALCHEMY_ECHO)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class BaseMixin:
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")

    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now, comment="创建时间")
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.now, onupdate=datetime.datetime.now,
                        comment="更新时间")
    deleted_at = Column(DateTime, nullable=True, index=True, comment="删除时间（软删除）")

    @classmethod
    def get_by_id(cls, session, item_id):
        """session should be SQLAlchemy Session object"""
        return session.query(cls).filter(
            cls.id == item_id,
            cls.deleted_at == None,  # noqa
        ).first()

    @classmethod
    def get_by_id_list(cls, session, item_id_list):
        return session.query(cls).filter(
            cls.id.in_(item_id_list),
            cls.deleted_at == None,  # noqa
        ).all()

    @classmethod
    def delete_by_id(cls, session, item_id):
        item = cls.get_by_id(session, item_id)
        if item is None:
            return
        item.deleted_at = datetime.datetime.now()
        session.commit()


@contextlib.contextmanager
def get_session():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception:
        s.rollback()
        raise
    finally:
        s.close()
