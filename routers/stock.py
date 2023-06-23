from fastapi import APIRouter, Response, Query, Depends
from sqlalchemy.orm import Session
from database import get_db

from routers import models, stock_service

# import yfinance as yf
import FinanceDataReader as fdr # https://github.com/financedata-org/FinanceDataReader

from routers import models
import json

router = APIRouter(
    prefix="/stock",
    tags=["stock"]
)

# S&P 500 symbol list
sp500 = fdr.StockListing('S&P500')

Index=['SP500', 'NASDAQ', 'KRX', 'KOSPI', 'KOSDAQ', 'SSE', 'SZSE', 'HKEX', 'TSE', 'HOSE']


@router.get("/list_tickers")
async def list_tickers(index: str = Query('SP500', enum=Index), db: Session = Depends(get_db)):
    # KRX: 코스피, 코스닥, 코넥스 전체
    # OSPI: 코스피
    # KOSDAQ: 코스닥
    # KONEX: 코넥스
    # SSE: 상해 거래소
    # SZSE: 신천 거래소
    # HKEX: 홍콩거래소
    # TSE: 도쿄 증권거래소
    # HOSE: 호치민 증권거래소
    # NYSE: 뉴욕거래소
    # NASDAQ: 나스닥
    # AMEX 아멕스

    df = fdr.StockListing(index)

    return df['Symbol'].to_list()


@router.post("/update_tickers")
async def update_tickers(index: str = Query('SP500', enum=Index), db: Session = Depends(get_db)):
    # KRX: 코스피, 코스닥, 코넥스 전체
    # OSPI: 코스피
    # KOSDAQ: 코스닥
    # KONEX: 코넥스
    # SSE: 상해 거래소
    # SZSE: 신천 거래소
    # HKEX: 홍콩거래소
    # TSE: 도쿄 증권거래소
    # HOSE: 호치민 증권거래소
    # NYSE: 뉴욕거래소
    # NASDAQ: 나스닥
    # AMEX 아멕스

    # new index list
    df = fdr.StockListing(index)
    _fdr_tickers = df['Symbol'].to_list()

    # get db index list
    _index_id = stock_service.get_index_id(db, index)
    _index_id_tickers = stock_service.get_index_tickers_by_index_id(db, _index_id)

    print(f'index: {index},')
    print(f'FinanceDataReader tickers: {len(_fdr_tickers)} found.')
    print(f'tickers in db: {len(_index_id_tickers)} found.',end='\n\n')

    _db_tickers = [r.ticker_id for r in _index_id_tickers]
    new_tickers = list(set(_fdr_tickers) - set(_db_tickers))
    old_tickers = list(set(_db_tickers) - set(_fdr_tickers))

    # add new tickers
    print(f'update tickers: {new_tickers}')
    stock_service.add_tickers_into_index(db, new_tickers, _index_id)

    # delete in index
    print(f'remove tickers: {old_tickers}')
    stock_service.delete_index_tickers_by_tickers(db, old_tickers)

    db.commit()

    return {'add tickers': new_tickers, 'remove tickers': old_tickers}


@router.get("/quarterly_earnings")
def quarterly_earnings(ticker: str):
    # yf.Ticker("MSFT")
    t = yf.Ticker(ticker)
    return {t.quarterly_earnings}


def update_nasdaq():
    pass


def update_etf():
    pass

