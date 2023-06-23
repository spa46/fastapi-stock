from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db
from main import app

from routers import stock_service

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://home:home1234@127.0.0.1:3306/stock_test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=20, pool_recycle=500, max_overflow=20
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_add_fresh_ticker(db: Session = Depends(override_get_db)):
    stock_service.add_tickers(db, ['AAAA', 'BBBB'])


def test_del_ticker():
    stock_service.delete_tickers_from_index(db, ['BBBB'])


def test_add_ticker_info_index():
    stock_service.add_tickers_into_index(db, ['BBBB'])
