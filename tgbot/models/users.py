from sqlalchemy import Column, String, Integer, BigInteger

from tgbot.services.database.functions.db_base import Base


class User(Base):
    __tablename__ = 'users'
    full_name = Column(String(length=80), nullable=False)
    user_id = Column(BigInteger, primary_key=True)
    username = Column(String(length=80), nullable=True)
    role = Column(Integer, default=0)
    balance = Column(Integer, default=0)
    btc_wallet = Column(String(length=40), default=None)
    warns = Column(Integer, default=0)
