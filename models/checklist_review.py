# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import Column, Integer, String, UniqueConstraint, Boolean, Index

from models import Base
from models.base import BaseMixin
from utils import time_utils


class ChecklistReview(Base, BaseMixin):
    """
    检查列表；用户可以确认
    """

    __tablename__ = "checklist_reviews"
    __table_args__ = (
        Index("user_checklist_created", "user_id", "checklist_id", "created_at"),
        {'comment': u'给清单的评论'},
    )

    user_id = Column(Integer, index=True, nullable=False, comment="创建此条记录的用户id")
    checklist_id = Column(Integer, index=True, nullable=False, comment="对应的清单id")
    detail = Column(String(512), comment="详情，为空时表示简单打卡")
    star_count = Column(Integer, default=0, comment="点赞数目")

    @classmethod
    def _get_by_checklist_and_user_between(cls, session, user_id, checklist_id, start_time, end_time):
        """
        获取某个用户在某个时间段对某个 checkitem 的阅评
        :param session:
        :param user_id: 用户id
        :param checklist_id: 指代哪个检查项
        :param start_time: 开始时间
        :param end_time: 结束时间（闭区间）
        :return:
        """
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.checklist_id == checklist_id,
            cls.created_at.between(start_time, end_time),
        ).first()

    @classmethod
    def _get_list_by_user_between(cls, session, user_id, start_time, end_time):
        """
        获取某个用户某个时间段里提交的所有的阅评
        :param session:
        :param user_id:
        :param start_time:
        :param end_time:
        :return:
        """
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.created_at.between(start_time, end_time)
        ).all()

    @classmethod
    def add(cls, session, user_id, checklist_id, detail):
        """
        某用户给某个检查项增加一个阅评；不检查是否已存在，无条件加
        :param session:
        :param user_id:
        :param checklist_id:
        :param detail: 详情
        :return:
        """
        review = ChecklistReview(
            user_id=user_id,
            checklist_id=checklist_id,
            detail=detail,
        )
        session.add(review)
        return review

    @classmethod
    def add_or_update(cls, session, user_id, checklist_id, detail):
        """
        添加前先检查是否已经存在，如果不存在就增加一个阅评，否则更新阅评内容
        :param session:
        :param user_id:
        :param checklist_id: 检查项id
        :param detail: 详情
        :return: 是否新创建；创建的 review
        """
        beginning_of_today, ending_of_today = time_utils.beginning_and_end_of_today()
        review = cls._get_by_checklist_and_user_between(
            session, user_id, checklist_id, beginning_of_today, ending_of_today)
        if review:
            review.detail = detail
            return False, review

        # 如果不存在，创建新的
        return True, cls.add(session, user_id, checklist_id, detail)

    @classmethod
    def get_today_list_of_user(cls, session, user_id):
        """
        获取某个用户今天提交的所有阅
        :param session:
        :param user_id: 用户id
        :return:
        """
        beginning_of_today, ending_of_today = time_utils.beginning_and_end_of_today()
        reviews = cls._get_list_by_user_between(session, user_id, beginning_of_today, ending_of_today)
        return reviews

    @classmethod
    def get_reviews_ref_last_review_id(cls, session, last_review_id, limit=20):
        """
        根据最后一个 last_review_id （开区间）拉取接下来的 limit 个阅评
        :param session:
        :param last_review_id:
        :param limit:
        :return:
        """
        return session.query(cls).filter(
            cls.id < last_review_id,
        ).order_by(cls.id.desc()).limit(limit).all()

    @classmethod
    def add_star_count(cls, session, review_id, star_delta):
        review = cls.get_by_id(session, review_id)
        if review is not None:
            review.star_count += star_delta
        return review

    @classmethod
    def set_star_count(cls, session, review_id, star_count):
        review = cls.get_by_id(session, review_id)
        if review is not None:
            review.star_count = star_count


class ChecklistReviewStar(Base, BaseMixin):
    """
    评价点赞记录
    """
    __tablename__ = "checklist_review_stars"
    __table_args__ = (
        UniqueConstraint('user_id', 'review_id', name='unique_user_review_star'),
        {'comment': u'给清单评论的点赞记录'},
    )

    user_id = Column(Integer, index=True, nullable=False, comment="创建此条记录的用户id")
    review_id = Column(Integer, index=True, nullable=False, comment="点赞的评论 id")
    on = Column(Boolean, default=False, comment="是否点赞（考虑取消点赞的情况）")

    @classmethod
    def add_star(cls, session, user_id, review_id):
        star = cls.get_review_star(session, user_id, review_id)
        if star:
            return False

        star = ChecklistReviewStar(
            user_id=user_id,
            review_id=review_id,
            on=True,
        )
        session.add(star)
        return True

    @classmethod
    def get_review_star(cls, session, user_id, review_id):
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.review_id == review_id,
        ).first()

    @classmethod
    def get_reviews_star_of_user(cls, session, user_id, review_ids):
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.review_id.in_(review_ids),
        ).all()


