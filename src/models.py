import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String(255), nullable=False)
    people_favorites = relationship('People_favorites', backref="user")
    vehicles_favorites = relationship('Vehicles_favorites', backref="user")
    planets_favorites = relationship('Planets_favorites', backref="user")

class People(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)  
    name = Column(String(255), nullable=False)  
    gender = Column(String(255))  
    birth_year = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    hair_color = Column(String(255)) 
    eye_color : Column(String(255)) 

class People_favorites(Base):
    __tablename__ = 'people_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('users.id'))  
    people_id = Column(Integer, ForeignKey('people.id')) 
    people = relationship('People', backref='people_favorite')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)  
    name = Column(String(255), nullable=False) 
    model = Column(String(255), nullable=False)
    length = Column(Integer, nullable=False)
    crew_capacity = Column(Integer, nullable=False)
    vehicle_class  = Column(String(255), nullable=False) 

class Vehicles_favorites(Base):
    __tablename__ =  'vehicle_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('users.id'))
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship('Vehicles', backref='vehicles_favorite')

class Planets(Base):
    __tablename__ =  'planets'
    id = Column(Integer, primary_key=True) 
    name = Column(String(255), nullable=False) 
    climate = Column(String(255), nullable=False) 
    terrain = Column(String(255), nullable=False) 
    population  = Column(Integer, nullable=False)
    gravity  = Column(Integer, nullable=False)
    orbital_period =  Column(Integer, nullable=False)

class Planets_favorites(Base):
    __tablename__ = 'planets_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets', backref='planets_favorite')

## Examples
# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')