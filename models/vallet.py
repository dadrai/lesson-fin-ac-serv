
#from pydantic import BaseModel
from config.database import Base



from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship




class Vallet(Base):
    __tablename__ = "vallets"

    id = Column(Integer, primary_key=True, index=True)
    #currency = Column(String) // old column without foreign key
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currencies.id"))

    currency = relationship('Currency')



class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    # items = relationship("Item", back_populates="owner")