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
    userName = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followings = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    following_id = Column(Integer, ForeignKey('following.id'))


    def serialize(self): # cambiar el objeto python a JSON
        # son los datos q devuelve de la tabla
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "followings": self.followings,
            "follower_id": self.follower_id,
            "following_id": self.following_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagramUML.png')