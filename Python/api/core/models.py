# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Float, ForeignKey, String, Table, text, Integer
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

    lat = Column(Float(53))
    lng = Column(Float(53))
    build_year = Column(Integer)

    district = relationship('District')
    street = relationship('Street')

    tubes = relationship('Tube', cascade="all,delete", backref='house')



    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'street': self.street.value,
            'district': self.district.value,
            'minLayingDepth': self.min_laying_depth,
            'maxLayingDepth': self.max_laying_depth,
            'number': self.number,
            'buildYear': self.build_year,
            'lat': self.lat,
            'lng': self.lng,
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

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".houses_id_seq'::regclass)"))
    number = Column(String, nullable=False)
    street = Column(ForeignKey('public.streets.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    district = Column(ForeignKey('public.districts.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    minLayingDepth = Column(Float)
    maxLayingDepth = Column(Float)

    lat = Column(Float(53))
    lng = Column(Float(53))
    buildYear = Column(Integer)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'street': self.street,
            'district': self.district,
            'minLayingDepth': self.minLayingDepth,
            'maxLayingDepth': self.maxLayingDepth,
            'number': self.number,
            'buildYear': self.buildYear,
            'lat': self.lat,
            'lng': self.lng,
        }



t_user_roles = Table(
    'user_roles', metadata,
    Column('user_id', ForeignKey('public.users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    Column('role_id', ForeignKey('public.roles.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False),
    schema='public'
)

class TubeFilterView(Base):
    __tablename__ = 'tube_filter_view'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".tubes_id_seq'::regclass)"))
    depth = Column(Float)
    houseId = Column(ForeignKey('public.houses.id', ondelete='CASCADE', onupdate='CASCADE'))
    value = Column(String)


    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'value': self.value,
            'houseId': self.houseId,
        }

    def to_advanced_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'value': self.value,
            'houseId': self.houseId,
            'samples': [sample.to_advanced_dictionary() for sample in self.samples]
        }



class Tube(Base):
    __tablename__ = 'tubes'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".tubes_id_seq'::regclass)"))
    depth = Column(Float)
    house_id = Column(BigInteger, ForeignKey('public.houses.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    value = Column(String)
    samples = relationship('TubeSample', cascade="all,delete", backref='tube')

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


class TubeSampleFilterView(Base):
    __tablename__ = 'sample_filter_view'
    __table_args__ = {'schema': 'public'}

    id = Column('id', BigInteger, primary_key=True, server_default=text("nextval('\"public\".tube_samples_id_seq'::regclass)"))
    depth = Column(Float)
    value = Column(Float)
    tubeId = Column(ForeignKey('public.tubes.id', ondelete='CASCADE', onupdate='CASCADE'))
    date = Column(DateTime, nullable=False)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'depth': self.depth,
            'date': self.date.strftime('%d-%m-%Y'),
            'value': self.value,
            'tubeId': self.tubeId,
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



class PivotView(Base):
    __tablename__ = 'pivot_filter_view'
    __table_args__ = {'schema': 'public'}

    houseId = Column(BigInteger, primary_key=True)
    tubeId = Column(BigInteger, primary_key=True)
    sampleId = Column(BigInteger, primary_key=True)
    tube = Column(String)
    date = Column(DateTime, nullable=False)
    depth = Column(Float)
    value = Column(Float)
    quarter = Column(BigInteger)
    month = Column(BigInteger)
    day = Column(BigInteger)
    year = Column(BigInteger)



