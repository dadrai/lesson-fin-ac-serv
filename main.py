from typing import Union

from fastapi import FastAPI

from models.vallet import Vallet

from config.database import engine

from schemas.vallet_schema import ValletSchema, Response

Vallet.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    external_vallet = {
        'currency': 'rub',
        'amount': 145.10
    }
    vallet = Vallet(**external_vallet)
    return vallet

@app.post("/vallets")
def vallets(vallet: ValletSchema ):
    return {Vallet}

@app.post("/vallets")
def read_item( q: Union[str, None] = None):
    return { "q": q}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}