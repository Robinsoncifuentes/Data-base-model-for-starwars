import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    user_lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)


class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    specie = Column(String(250), nullable=False)



class Planets(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    lenguage = Column(String(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)



class FavoritsCharacters(Base):
    __tablename__ = 'favoritscharacters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))


class FavoritsPlanets(Base):
    __tablename__ = 'favoritsplanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))


class FavoritsStarships(Base):
    __tablename__ = 'favoritsStarships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    starships_id = Column(Integer, ForeignKey('starships.id'))


class FavoritsSpecies(Base):
    __tablename__ = 'favoritsSpecies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    species_id = Column(Integer, ForeignKey('species.id'))

    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')