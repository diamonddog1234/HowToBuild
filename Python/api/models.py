# coding: utf-8
from sqlalchemy import BigInteger, Column, ForeignKey, Integer, String, text, orm, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from core import get_database_session

Base = declarative_base()
metadata = Base.metadata


def get_props_for_entity(entity_id, entity_type):
    prop_values = get_database_session().query(PropValue).\
        filter(PropValue.entity_id == entity_id).\
        filter(PropValue.entity_type == entity_type).\
        all()

    result = {}
    for prop_value in prop_values:
        result[prop_value.prop.value] = prop_value.value

    return result


def add_props_to_entity(entity_id, entity_type, props):
    for prop_key, prop_value in props.items():
        p = get_database_session().query(Prop).filter(Prop.value == prop_key).first()
        prop_id = 0
        if not p:
            created_prop = Prop(value=prop_key)
            get_database_session().add(created_prop)
            get_database_session().flush()
            get_database_session().commit()
            prop_id = created_prop.id
        else:
            prop_id = p.id

        pv = get_database_session().query(PropValue).\
            filter(PropValue.entity_id == entity_id).\
            filter(PropValue.entity_type == entity_type).\
            filter(PropValue.prop_id == prop_id).first()
        if not pv:
            created_prop_value = PropValue(prop_id = prop_id, value = prop_value, entity_type=entity_type, entity_id=entity_id)
            get_database_session().add(created_prop_value)
            get_database_session().flush()
            get_database_session().commit()
    pass


def get_answers_from_interpretation_group(group_id):
    answers_in_group = get_database_session().query(AnswersInInterpetationGroup).\
        filter(AnswersInInterpetationGroup.interpetation_group_id == group_id).all()
    result = [{'id':answer_in_group.answer_id, 'value':answer_in_group.value} for answer_in_group in answers_in_group]
    return  result


class Prop(Base):
    __tablename__ = 'props'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".props_id_seq'::regclass)"))
    value = Column(String, nullable=False)

    prop_values = relationship('PropValue', back_populates="prop")

    def __repr__(self):
        return self.value


class Test(Base):
    __tablename__ = 'tests'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".tests_id_seq'::regclass)"))
    value = Column(String, nullable=False)
    description = Column(String)
    interpetation_method_id = Column(BigInteger)
    questions = relationship("Question", back_populates="test")

    @property
    def props(self):
        return get_props_for_entity(entity_type=0, entity_id=self.id)




    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value,
            'description': self.description,
            'questions': [q.to_basic_dictionary() for q in self.questions],
            **self.props
        }


    def __repr__(self):
        return self.value


class PropValue(Base):
    __tablename__ = 'prop_values'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".prop_values_id_seq'::regclass)"))
    entity_type = Column(Integer, nullable=False)
    prop_id = Column(ForeignKey('public.props.id'), nullable=False)
    entity_id = Column(BigInteger, nullable=False)
    value = Column(String)

    prop = relationship('Prop')

    def __repr__(self):
        return self.prop.value


class Question(Base):
    __tablename__ = 'questions'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".questions_id_seq'::regclass)"))
    value = Column(String)
    test_id = Column(ForeignKey('public.tests.id', ondelete='CASCADE'))
    test = relationship('Test')
    answers = relationship('Answer', back_populates="question")

    @property
    def props(self):
        return get_props_for_entity(entity_type=1, entity_id=self.id)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value,
            'answers': [a.to_basic_dictionary() for a in self.answers],
            **self.props
        }

    # @orm.reconstructor
    # def init_on_load(self):
    #     self.props = get_props_for_entity(entity_type=1, entity_id=self.id)

    def __repr__(self):
        return self.value



class Answer(Base):
    __tablename__ = 'answers'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".answers_id_seq'::regclass)"))
    value = Column(String, nullable=False)
    question_id = Column(ForeignKey('public.questions.id'))

    question = relationship('Question')

    @property
    def props(self):
        return get_props_for_entity(entity_type=2, entity_id=self.id)

    def to_basic_dictionary(self):
        return {
            'id': self.id,
            'value': self.value,
            **self.props
        }

    @orm.reconstructor
    def init_on_load(self):
        pass
        # self.props = get_props_for_entity(entity_type=2, entity_id=self.id)
        # for key, value in props.items():
        #     self.__dict__[key] = value

    def __repr__(self):
        return self.value


class InterpretationGroup(Base):
    __tablename__ = 'interpretation_groups'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True,
                server_default=text("nextval('\"public\".interpretation_group_id_seq'::regclass)"))
    thinks = relationship('InterpretationGroupThink', back_populates='interpretation_group')
    test_id = Column(BigInteger,ForeignKey('public.tests, id'), nullable=False)

    relationship('Test')

    value = Column(String)


class InterpretationMethod(Base):
    __tablename__ = 'interpretation_methods'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True,
                server_default=text("nextval('\"public\".interpretation_methods_id_seq'::regclass)"))
    value = Column(String, nullable=False)


class InterpretationGroupThink(Base):
    __tablename__ = 'interpretation_group_thinks'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True)
    interpretation_group_id = Column(ForeignKey('public.interpretation_groups.id'), nullable=False)
    min_interpretation_group_value = Column(Float)
    max_interpretation_group_value = Column(Float)
    value = Column(String)

    interpretation_group = relationship('InterpretationGroup', back_populates='thinks')


class AnswersInInterpetationGroup(Base):
    __tablename__ = 'answers_in_interpetation_groups'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".answers_in_interpetation_groups_id_seq'::regclass)"))
    interpetation_group_id = Column(ForeignKey('public.interpretation_groups.id'), nullable=False)
    answer_id = Column(BigInteger, nullable=False)
    value = Column(Float, nullable=False)

    interpetation_group = relationship('InterpretationGroup')


class UserAnswer(Base):
    __tablename__ = 'user_answers'
    __table_args__ = {'schema': 'public'}

    id = Column(BigInteger, primary_key=True, server_default=text("nextval('\"public\".user_answers_id_seq'::regclass)"))
    user_id = Column(ForeignKey('public.users.id'), nullable=False)
    answer_id = Column(ForeignKey('public.answers.id'), nullable=False)

    answer = relationship('Answer')
    user = relationship('User')


class UserTelegram(Base):
    __tablename__ = 'user_telegrams'
    __table_args__ = {'schema': 'public'}

    user_id = Column(ForeignKey('public.users.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    telegram_id = Column(BigInteger)
