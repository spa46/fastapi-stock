from typing import Optional

from fastapi import FastAPI
from routers import stock

app = FastAPI()
app.include_router(stock.router)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
