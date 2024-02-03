from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

MIN_LENGTH_FOR_NAME = 1
MAX_LENGTH_FOR_NAME = 100


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=MIN_LENGTH_FOR_NAME,
        max_length=MAX_LENGTH_FOR_NAME
    )
    description: Optional[str] = Field(None, min_length=MIN_LENGTH_FOR_NAME)
    full_amount: Optional[int] = Field(None,)


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(
        ...,
        min_length=MIN_LENGTH_FOR_NAME,
        max_length=MAX_LENGTH_FOR_NAME
    )
    description: str = Field(..., min_length=MIN_LENGTH_FOR_NAME)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = Field(0)
    fully_invested: bool = Field(False)
    create_date: datetime
    close_date: Optional[datetime] = Field(None)

    class Config:
        orm_mode = True


class CharityProjectCreateResponse(CharityProjectDB):
    close_date: Optional[datetime] = Field(None)


class CharityProjectUpdateResponse(CharityProjectDB):
    close_date: Optional[datetime] = Field(None)


class CharityProjectDelete(CharityProjectDB):
    close_date: Optional[datetime] = Field(None)
