# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, DateTime, Float, ForeignKey, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class District(Base):
    __tablename__ = 'districts'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".districts_id_seq'::regclass)"))
    value = Column(String, nullable=False)


class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".roles_id_seq'::regclass)"))
    value = Column(String, nullable=False)

    users = relationship('User', secondary='public.user_roles')


class Street(Base):
    __tablename__ = 'streets'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".streets_id_seq'::regclass)"))
    value = Column(CHAR(1), nullable=False)


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".users_id_seq'::regclass)"))
    login = Column(String, nullable=False)
    password_hash = Column(String)
    token_id = Column(BigInteger, server_default=text("nextval('\"public\".users_id_seq'::regclass)"))


class House(Base):
    __tablename__ = 'houses'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".houses_id_seq'::regclass)"))
    number = Column(String, nullable=False)
    street_id = Column(ForeignKey('public.streets.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    district_id = Column(ForeignKey('public.districts.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    min_laying_depth = Column(Float)
    max_laying_depth = Column(Float)

    district = relationship('District')
    street = relationship('Street')


t_user_roles = Table(
    'user_roles', metadata,
    Column('user_id', ForeignKey('public.users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('role_id', ForeignKey('public.roles.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    schema='public'
)


class Tube(Base):
    __tablename__ = 'tubes'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".tubes_id_seq'::regclass)"))
    depth = Column(Float)
    house_id = Column(ForeignKey('public.houses.id', ondelete='CASCADE', onupdate='CASCADE'))

    house = relationship('House')


class TubeSample(Base):
    __tablename__ = 'tube_samples'
    __table_args__ = {'schema': 'public'}

    _id = Column(' id', BigInteger, primary_key=True, server_default=text("nextval('\"public\".tube_samples_id_seq'::regclass)"))
    depth = Column(Float)
    value = Column(Float)
    tube_id = Column(ForeignKey('public.tubes.id', ondelete='CASCADE', onupdate='CASCADE'))
    date = Column(DateTime, nullable=False)

    tube = relationship('Tube')
