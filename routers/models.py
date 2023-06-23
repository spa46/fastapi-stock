from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base


class Index(Base):
    __tablename__ = "stock_index"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(8), unique=True)


class Ticker(Base):
    __tablename__ = "stock_ticker"
    ticker = Column(String(5), primary_key=True, index=True)
    name = Column(String(32))
    sector = Column(String(64))
    industry = Column(String(64))


class IndexTicker(Base):
    __tablename__ = "stock_indexticker"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticker_id = Column(String, ForeignKey("stock_ticker.ticker"))
    index_id = Column(Integer, ForeignKey("stock_index.id"))

    stock_index = relationship("Index")
    stock_ticker = relationship("Ticker")


