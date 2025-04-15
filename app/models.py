from sqlalchemy import Column, Integer, String, ForeignKey, MONEY
from sqlalchemy.orm import relationship
from app.database import Base

class Game(Base):
    __tablename__ = "games"
    
    appid = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB)
    updated_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    
    userid = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    alerts = relationship("Alert", back_populates="user")


class Alert(Base):
    __tablename__ = "alerts"
    
    alertid = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("users.userid"), nullable=False)
    appid = Column(Integer, ForeignKey("games.appid"), nullable=False)
    price = Column(MONEY, nullable=False)

    user = relationship("User", back_populates="alerts")


