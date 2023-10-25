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
    planet_of_birth = relationship('Characters_Planets', uselist=True, backref="planets")
    favorite = relationship("Favorite", uselist=True, backref="planets")


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(50), nullable=False)
    eye_color = Column(String(20), nullable=False)
    planet_of_birth = relationship('Characters_Planets', uselist=True, backref="characters")
    characters_lightsaber = relationship("Characters_LightSaber", uselist=True, backref="characters")
    favorite = relationship("Favorite", uselist=True, backref="characters")

class Characters_Planets(Base):
    __tablename__ = 'characters_planets'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer(), ForeignKey('characters.id'))
    planets_id = Column(Integer(), ForeignKey('planets.id'))

class LightSaber(Base):
    __tablename__ = 'lightsaber'
    id = Column(Integer, primary_key=True)
    lightsaber_color = Column(String(30), nullable=False)
    character_lightsaber = relationship("Characters_LightSaber", uselist=True, backref="lightsaber")
    favorite = relationship("Favorite", uselist=True, backref="lightsaber")

class Character_LightSaber(Base):
    __tablename__ = 'character_lightsaber'
    id = Column(Integer(), primary_key=True)
    characters_id = Column(Integer(), ForeignKey('characters.id'))
    lightsaber_id = Column(Integer(), ForeignKey('lightsaber.id'))

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    use_id = Column(Integer(), ForeignKey("user.id"))
    planets_id = Column(Integer(), ForeignKey("planets.id"))
    characters_id = Column(Integer(), ForeignKey("characters.id"))
    lightsaber_id = Column(Integer(), ForeignKey("lightsaber.id"))


    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
