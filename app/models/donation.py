from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from app.core.db import Base


class Donation(Base):

    user_id = Column(Integer, ForeignKey(
        'user.id',
        name='donation_user_id'
    )
    )

    comment = Column(String)

    full_amount = Column(Integer)

    invested_amount = Column(Integer, default=0)

    fully_invested = Column(Boolean, default=False)

    create_date = Column(DateTime)

    close_date = Column(DateTime)
