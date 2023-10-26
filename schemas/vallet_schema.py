from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class ValletSchema(BaseModel):
    id: Optional[int] = None
    currency: Optional[str] = None
    amount: Optional[float] = None

    # class Config:
    #     orm_mode = True


class RequestVallet(BaseModel):
    parameter: ValletSchema = Field(...)


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]