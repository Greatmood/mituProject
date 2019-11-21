#!/usr/bin/python3
# coding: utf-8

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Article(Base):
    __tablename__ = 'article'

    article_id = Column(Integer, primary_key=True)
    ud_id = Column(ForeignKey('article_to_user.ud_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    a_title = Column(String(10), nullable=False)
    a_image = Column(String(30))
    view_num = Column(Integer)
    a_talk = Column(Integer)
    good_num = Column(Integer)

    ud = relationship('ArticleToUser', primaryjoin='Article.ud_id == ArticleToUser.ud_id', backref='articles')


class ArticleContent(Base):
    __tablename__ = 'article_content'

    ac_id = Column(Integer, primary_key=True)
    article_id = Column(ForeignKey('article.article_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    content = Column(Text, nullable=False)

    article = relationship('Article', primaryjoin='ArticleContent.article_id == Article.article_id', backref='article_contents')


class ArticleToUser(Base):
    __tablename__ = 'article_to_user'

    ud_id = Column(Integer, primary_key=True)


class EndRecommend(Base):
    __tablename__ = 'end_recommend'

    id = Column(Integer, primary_key=True)
    recommend = Column(String(50))


class EndProductRecommend(EndRecommend):
    __tablename__ = 'end_product_recommend'

    id = Column(ForeignKey('end_recommend.id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True)
    ti_id = Column(Integer)
    wed_id = Column(Integer)
    pro_id = Column(Integer)
    add_tell = Column(String(100))


class LevelChange(Base):
    __tablename__ = 'level_change'

    ch_l_id = Column(Integer, primary_key=True)
    ud_id = Column(Integer)
    b_level = Column(Integer)
    a_level = Column(Integer)
    ch_time = Column(DateTime, nullable=False)
    ch_reson = Column(String(40))


class ManagerDetail(Base):
    __tablename__ = 'manager_detail'

    manager_d_id = Column(Integer, primary_key=True)
    manager_id = Column(Integer)
    login = Column(String(20), nullable=False)


class OrderTable(Base):
    __tablename__ = 'order_table'

    order_id = Column(Integer, primary_key=True)
    ud_id = Column(Integer)
    get_time = Column(DateTime)
    pay_time = Column(DateTime)
    last_time = Column(DateTime)
    status = Column(Integer)
    no_need = Column(DateTime)
    return_money_time = Column(DateTime)
    is_talk = Column(Integer)


class ScoreSave(Base):
    __tablename__ = 'score_save'

    score_save_id = Column(Integer, primary_key=True)
    ud_id = Column(Integer)
    num = Column(Integer)
    get_record = Column(String(10))
    get_time = Column(DateTime)
    get_way = Column(String(10))


class SysInfo(Base):
    __tablename__ = 'sys_info'

    sys_info_id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    info = Column(String(20), nullable=False)


class SysInfoDetail(Base):
    __tablename__ = 'sys_info_detail'

    info_detail_id = Column(Integer, primary_key=True)
    sys_info_id = Column(ForeignKey('sys_info.sys_info_id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    title = Column(String(10), nullable=False)
    info = Column(String(20), nullable=False)
    detail = Column(String(50), nullable=False)

    sys_info = relationship('SysInfo', primaryjoin='SysInfoDetail.sys_info_id == SysInfo.sys_info_id', backref='sys_info_details')


class TLDetail(Base):
    __tablename__ = 't_l_detail'

    t_l_id = Column(Integer, primary_key=True)
    ti_id = Column(Integer)
    pro_id = Column(Integer)


class Ticket(Base):
    __tablename__ = 'ticket'

    ticket_id = Column(Integer, primary_key=True)
    ticket_name = Column(String(20), nullable=False)
    ticket_account = Column(Float, nullable=False)
    ticket_desc = Column(String(50))
    is_use = Column(Integer)


class TravelCircle(Base):
    __tablename__ = 'travel_circle'

    id = Column(Integer, primary_key=True)
    ti_id = Column(Integer)
    pro_id = Column(Integer)
    head_picture = Column(String(200))
    nickname = Column(String(20))
    pic_dis = Column(String(200))


class TravelLife(Base):
    __tablename__ = 'travel_life'

    id = Column(Integer, primary_key=True)
    picture = Column(String(200))
    pic_dis = Column(String(50))


class TravelerInfo(Base):
    __tablename__ = 'traveler_info'

    travel_id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('order_table.order_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(String(6), nullable=False)
    gender = Column(Integer, nullable=False)
    id_card = Column(Integer, nullable=False)
    phone_num = Column(Integer, nullable=False)
    date = Column(DateTime)

    order = relationship('OrderTable', primaryjoin='TravelerInfo.order_id == OrderTable.order_id', backref='traveler_infos')


class UserAccount(Base):
    __tablename__ = 'user_account'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(10), nullable=False)
    user_password = Column(String(20), nullable=False)


class UserWallet(Base):
    __tablename__ = 'user_wallet'

    wallet_id = Column(Integer, primary_key=True)
    ud_id = Column(Integer)
    w_acount = Column(Float, nullable=False, server_default=FetchedValue())
    rest_money = Column(Float, nullable=False, server_default=FetchedValue())
    recharge = Column(Float, nullable=False, server_default=FetchedValue())
    is_have = Column(Integer, nullable=False, server_default=FetchedValue())
    is_display = Column(Integer, nullable=False)


class ViewPlace(Base):
    __tablename__ = 'view_place'

    vp_id = Column(Integer, primary_key=True)
    v_p_id = Column(Integer)
    city_name = Column(String(10), nullable=False)
    province_name = Column(String(4), nullable=False)
    district_name = Column(String(4), nullable=False)


class WalletRecord(Base):
    __tablename__ = 'wallet_record'

    record_id = Column(Integer, primary_key=True)
    wallet_id = Column(ForeignKey('user_wallet.wallet_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    corder_id = Column(Integer)

    wallet = relationship('UserWallet', primaryjoin='WalletRecord.wallet_id == UserWallet.wallet_id', backref='wallet_records')


class WedDiscount(Base):
    __tablename__ = 'wed_discount'

    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    ord = Column(String(10))


class ProductRecommend(WedDiscount):
    __tablename__ = 'product_recommend'

    id = Column(ForeignKey('wed_discount.id', ondelete='RESTRICT', onupdate='RESTRICT'), primary_key=True)
    ti_id = Column(Integer)
    wed_id = Column(Integer)
    pro_id = Column(Integer)
    inventory = Column(Integer)
    discount_price = Column(Float)
    limit_cnt = Column(String(10))
