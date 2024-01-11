from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    comments = relationship('Comment')

class Comment(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_ = Column(Enum('image', 'video'))
    uri = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    follower_id = Column(Integer, ForeignKey('usuario.id'), primary_key=True)
    
render_er(Base, 'diagram.png')