import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_name = Column(String(30), unique=True)
    bio = Column(String(120))
    post = relationship('Post')
    comment = relationship('Comments')
    like = relationship('Likes')

class Followers(Base):
    __tablename__= 'followers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    user_name = Column(String(30), unique=True)
    bio = Column(String(120))

class User_Follower(Base):
    __tablename__ = 'user_follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_id_relationship = relationship(User)
    follower_id = Column(Integer, ForeignKey('followers.id'))
    follower_id_relationship = relationship(Followers)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    description = Column(String(150))
    publication_date = Column(Date)
    user = Column(Integer, ForeignKey('user.id'))
    media = relationship('Media')
    comment = relationship('Comments')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    source = Column(String(255))
    post = Column(Integer, ForeignKey('post.id'))

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String(150))
    post = Column(Integer, ForeignKey('post.id'))
    user = Column(Integer, ForeignKey('user.id'))

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    user = Column(Integer, ForeignKey('user.id'))

class Likes_Posts(Base):
    __tablename__ = 'likes_posts'
    id = Column(Integer, primary_key=True)
    like = Column(Integer, ForeignKey('likes.id'))
    like_relationship = relationship(Likes) 
    post = Column(Integer, ForeignKey('post.id'))
    post_relationship = relationship(Post)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
