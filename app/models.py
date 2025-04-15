from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB, MONEY

Base = declarative_base()

class Game(Base):
    __tablename__ = "games"

    appid = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)


class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


class Alert(Base):
    __tablename__ = "alerts"

    alertid = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("users.userid", ondelete="CASCADE"))
    appid = Column(Integer, ForeignKey("games.appid", ondelete="CASCADE"))
    price = Column(String, nullable=False)  # Using String instead of Money for better cross-compatibility

    user = relationship("User")
    game = relationship("Game")
