from sqlalchemy.orm.exc import FlushError

__author__ = 'ada'

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Binary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Language(Base):
    __tablename__ = "language"
    id = Column(String(2), primary_key=True)
    name = Column(String(255))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(225))
    name = Column(String(225))
    password = Column(Binary)
    password_salt = Column(Binary)
    preferred_language_id = Column(String(2), ForeignKey('language.id'))
    language = relationship(Language)

class Word(Base):
    __tablename__ = "word"
    id = Column(Integer, primary_key=True)
    word = Column(String(225))
    word_rank = Column(Integer)
    starred = Column(Integer)
    language_id = Column(String(2), ForeignKey('language.id'))
    language = relationship(Language)

    def __str__(self):
        return str(self.word)

class Text(Base):
    __tablename__ = "text"
    id = Column(Integer, primary_key=True)
    content = Column(String(10000))
    content_hash = Column(Binary)
    language_id = Column(String(2), ForeignKey('language.id'))
    url_id = Column(Integer)
    language = relationship(Language)


con_string = 'mysql://{}:{}@{}'.format("zeeguu", "sla2012", "localhost/zeeguu")
engine = create_engine(con_string)

# Base.metadata.create_all(engine)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine # bind-uim informatiile metadata din Base la engine
DBSession = sessionmaker(engine) # cream o clasa DBsession

# cream un obiect sesiune de tip clasa DBSession/ deschidem o noua sesiune in baza de date
session = DBSession()
users = session.query(User).all()
for u in users:
    print u.name + ":" + u.name + ":" + u.email

first_user = session.query(User).first()

english_words = session.query(Word).join(Language).filter(Language.name == "English").all()
for en_word in english_words:
    print en_word.word

english_words_rank_1 = session.query(Word).filter(Word.language_id == "en", Word.word_rank == "2").all()
for ranked_en_word in english_words_rank_1:
    print ranked_en_word

#english_words_rank_1.__str__()

if user = session.query(User).filter(User.name == "Anca Lungu").one():
    if user:

all()[0]

user = session.query(User).filter(User.name == "Anca Lungu").all()
    if len(user) == 1:
        print "Anca Lungu's selected language is:" + user.language.id


try:
    user = session.query(User).filter(User.name == "Anca Lungu").one()
    print "Anca Lungu's selected language is:" + user.language.id
except:
    print "userul nu exista..."

"""new_user = User(name="Anca Lungu", email="bare.fordi@gmail.com")
new_language = Language(id="dn", name="Danish")
session.add(new_language)
new_user.language = new_language
session.add(new_user)
session.commit()"""

try:
    new_language = Language(id="dn", name="Danish")
    new_user = User(name="Anca Lungu", email="bare.fordi@gmail.com", language = new_language)
    session.add(new_language)
    session.add(new_user)
    session.commit()
except FlushError:
    print "probabil languageul exista deja"

































































"""from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine

session = DBSession()
users = session.query(User).all()
for u in users:
    print u.name + " - " + u.language.name"""
















