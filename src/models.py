from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    phoneNumber = Column(String(10), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    favorite = relationship("Favorite", uselist=True, backref="user")


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    planet_name = Column(String(80), unique=True)
    favorite = relationship("Favorite", uselist=True, backref="planets")


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(50), nullable=False)
    eye_color = Column(String(20), nullable=False)


class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    use_id = Column(Integer(), ForeignKey("user.id"))
    planets_id = Column(Integer(), ForeignKey("planets.id"))

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
