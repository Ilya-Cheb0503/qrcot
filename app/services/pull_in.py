from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def filling_up(
    model_fill_up,
    model_sponsor,
    session: AsyncSession,
):

    open_donations_list = await session.execute(select(model_sponsor).where(
        model_sponsor.fully_invested is not True)
    )
    incomplete_donations = open_donations_list.scalars().all()
    for model_sponsor in incomplete_donations:
        if model_fill_up.invested_amount < model_fill_up.full_amount:
            project_requests = (
                model_fill_up.full_amount - model_fill_up.invested_amount)
            donation_balance = (
                model_sponsor.full_amount - model_sponsor.invested_amount)
            if donation_balance <= project_requests:
                model_fill_up.invested_amount += donation_balance
                model_sponsor.invested_amount = model_sponsor.full_amount
                model_sponsor.fully_invested = True
                model_sponsor.close_date = datetime.now()
            else:
                model_fill_up.invested_amount = model_fill_up.full_amount
                model_sponsor.invested_amount += project_requests
            session.add(model_sponsor)

        if model_fill_up.invested_amount == model_fill_up.full_amount:
            model_fill_up.fully_invested = True
            model_fill_up.close_date = datetime.now()
            break

    session.add(model_fill_up)
    await session.commit()
    await session.refresh(model_fill_up)
    return model_fill_up
