from typing import Union

from fastapi import FastAPI,Depends

from models.vallet import Vallet

from config.database import engine, get_db

from schemas.vallet_schema import CreateRequestVallet,Response

from sqlalchemy.orm import Session

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
async def vallets(vallet: CreateRequestVallet, db:Session = Depends(get_db)):
    w=Vallet(**vallet.dict())

    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}