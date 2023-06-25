from sqlalchemy.orm import Session
from routers import models
from routers.models import Ticker, IndexTicker


def get_index_id(db: Session, index: str):
    return db.query(models.Index).filter(models.Index.name == index).first().id


def get_ticker(db: Session, ticker: str):
    return db.query(models.Ticker).filter(models.Ticker.ticker == ticker).first()


def get_tickers(db: Session):
    return db.query(Ticker).all()


def add_tickers_into_index(db: Session, index_df , index_id: int):
    for _, r in index_df.iterrows():
        _ticker = Ticker(ticker=r['Symbol'], name=r['Name'], sector=r['Sector'], industry=r['Industry'])
        if not get_ticker(db, r['Symbol']):
            db.add(_ticker)

        db.add(IndexTicker(ticker_id=_ticker.ticker, index_id=index_id))

def get_index_tickers_by_index_id(db: Session, index_id: int):
    return db.query(models.IndexTicker.ticker_id).filter(models.IndexTicker.index_id == index_id).all()


def delete_index_tickers_by_tickers(db: Session, ticker: list):
    return db.query(models.IndexTicker).filter(models.IndexTicker.ticker_id.in_(ticker)).delete()


