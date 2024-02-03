from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    comment: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt]


class DonationCreate(DonationBase):
    full_amount: PositiveInt


class DonationDB(DonationCreate):
    id: int
    user_id: Optional[int]
    create_date: datetime

    class Config:
        orm_mode = True


class DonationCreateResponse(DonationDB):
    close_date: Optional[datetime]


class Donations_Super_DB(DonationDB):
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
