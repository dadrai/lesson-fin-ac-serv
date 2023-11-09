from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


# class ValletSchema(BaseModel):
#     id: Optional[int] = None
#     currency: Optional[str] = None
#     amount: Optional[float] = None

#     # class Config:
#     #     orm_mode = True


class CreateRequestVallet(BaseModel):
    currency: Optional[str | None] = None
    amount: Optional[float | None] = None

class Response(GenericModel, Generic[T]):
    code: int = 200
    # status: str
    message: str = 'Success'
    data: Optional[T]