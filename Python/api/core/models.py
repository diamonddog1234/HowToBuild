# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from core import get_database_session

Base = declarative_base()
metadata = Base.metadata


class District(Base):
    __tablename__ = 'districts'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".districts_id_seq'::regclass)"))
    value = Column(String, nullable=False)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value
        }


class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".roles_id_seq'::regclass)"))
    value = Column(String, nullable=False)

    users = relationship('User', secondary='public.user_roles')

    @staticmethod
    def get_roles_from_string_array(roles):
        result = []
        for role in roles:
            result.append(get_database_session().query(Role).filter(Role.value == role).first())
        return result

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value
        }


class Street(Base):
    __tablename__ = 'streets'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".streets_id_seq'::regclass)"))
    value = Column(String, nullable=False)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value
        }


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".users_id_seq'::regclass)"))
    login = Column(String, nullable=False)
    password_hash = Column(String)
    token_id = Column(BigInteger, server_default=text("nextval('\"public\".users_id_seq'::regclass)"))
    roles = relationship('Role', secondary='public.user_roles')

    @property
    def role_string_array(self):
        roles = []
        for role in self.roles:
            roles.append(role.value)
        return  roles


    def create_access_token_payload(self):
        return {
            'user_id': self.id,
            'token_id': self.token_id,
        }


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

    tubes = relationship('Tube', backref='house')



    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'street': self.street.value,
            'district': self.district.value,
            'minLayingDepth': self.min_laying_depth,
            'maxLayingDepth': self.max_laying_depth,
            'number': self.number,
        }

    def to_advanced_dictionary(self):
        return {
            'id': self.id,
            'street': self.street.value,
            'district': self.district.value,
            'minLayingDepth': self.min_laying_depth,
            'maxLayingDepth': self.max_laying_depth,
            'number': self.number,
            'tubes': [tube.to_advanced_dictionary() for tube in self.tubes]
        }


class HouseFilterView(Base):
    __tablename__ = 'house_filter_view'
    __table_args__ = {'schema': 'public'}

    houseId = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".houses_id_seq'::regclass)"))
    number = Column(String, nullable=False)
    street = Column(ForeignKey('public.streets.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    district = Column(ForeignKey('public.districts.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    minLayingDepth = Column(Float)
    maxLayingDepth = Column(Float)

    def to_basic_dictionary(self):
        return {
            'id': self.houseId,
            'street': self.street,
            'district': self.district,
            'minLayingDepth': self.minLayingDepth,
            'maxLayingDepth': self.maxLayingDepth,
            'number': self.number,
        }



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
    value = Column(String)
    samples = relationship('TubeSample', backref='tube')


    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'value': self.value,
            'houseId': self.house_id,
        }

    def to_advanced_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'value': self.value,
            'houseId': self.house_id,
            'samples': [sample.to_advanced_dictionary() for sample in self.samples]
        }


class TubeSample(Base):
    __tablename__ = 'tube_samples'
    __table_args__ = {'schema': 'public'}

    id = Column('id', BigInteger, primary_key=True, server_default=text("nextval('\"public\".tube_samples_id_seq'::regclass)"))
    depth = Column(Float)
    value = Column(Float)
    tube_id = Column(ForeignKey('public.tubes.id', ondelete='CASCADE', onupdate='CASCADE'))
    date = Column(DateTime, nullable=False)


    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'date': self.date.strftime('%d-%m-%Y'),
            'value': self.value,
        }

