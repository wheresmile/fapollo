# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, UniqueConstraint, Boolean

from models import Base
from models.base import BaseMixin


class ChecklistReview(Base, BaseMixin):
    """
    检查列表；用户可以确认
    """

    __tablename__ = "checklist_reviews"
    __table_args__ = (
        {'comment': u'给清单的评论'},
    )

    user_id = Column(Integer, index=True, nullable=False, comment="创建此条记录的用户id")
    checklist_id = Column(Integer, index=True, nullable=False, comment="对应的清单id")
    detail = Column(String(512), comment="详情，为空时表示简单打卡")
    star_count = Column(Integer, comment="点赞数目")

    @classmethod
    def add(cls, session, user_id, checklist_id, detail):
        review = ChecklistReview(
            user_id=user_id,
            checklist_id=checklist_id,
            detail=detail,
        )
        session.add(review)

    @classmethod
    def add_star_count(cls, session, review_id, star_delta):
        review = cls.get_by_id(session, review_id)
        if review is not None:
            review.start_count += star_delta

    @classmethod
    def set_star_count(cls, session, review_id, star_count):
        review = cls.get_by_id(session, review_id)
        if review is not None:
            review.start_count = star_count


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
    def toggle_star(cls, session, user_id, review_id):
        star = cls.get_review_star(session, user_id, review_id)
        if star:
            star.on = not star.on
        else:
            star = ChecklistReviewStar(
                user_id=user_id,
                review_id=review_id,
                on=True,
            )
            session.add(star)
        return star

    @classmethod
    def get_review_star(cls, session, user_id, review_id):
        return session.query(cls).filter(
            cls.user_id == user_id,
            cls.review_id == review_id,
        ).first()



