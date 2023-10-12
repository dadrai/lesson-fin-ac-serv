from typing import Union

from fastapi import FastAPI

from models.vallet import Vallet

app = FastAPI()


@app.get("/")
def read_root():
    external_vallet = {
        'currency': 'rub',
        'amount': 145.10
    }
    vallet = Vallet(**external_vallet)
    return vallet

@app.get("/items")
def read_item( q: Union[str, None] = None):
    return { "q": q}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}