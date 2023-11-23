from typing import Union

from fastapi import FastAPI,Depends

from models.vallet import Vallet, Currency

from config.database import engine, get_db,Base

from schemas.vallet_schema import CreateRequestVallet,Response,CreateRequestCurrency

from sqlalchemy.orm import Session

# Vallet.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/vallets")
async def get_vallets( db:Session = Depends(get_db)):

    vallets = db.query(Vallet).all()

    return Response(
        code=200,
        message="Success",
        data=vallets
    )
    

@app.post("/currency/add")
async def add_currency(currency: CreateRequestCurrency, db:Session = Depends(get_db)):

    w=Currency(**currency.dict())

    db.add(w)
    db.commit()
    db.refresh(w)

    return Response(
        code=200,
        message="Success",
        data=w
    )
@app.post("/vallets/add")
async def vallets(vallet: CreateRequestVallet, db:Session = Depends(get_db)):

    currency = db.query(Currency).get(vallet.currency_id)

    print(
        'vallet', currency
    )

    if not currency:
        return Response(
            code=404,
            message="Currency not found",
            data=None
        )
    
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