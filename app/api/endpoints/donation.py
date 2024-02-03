from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import (DonationCreate, DonationCreateResponse,
                                  DonationDB, Donations_Super_DB)
from app.services.pull_in import filling_up

router = APIRouter()


@router.post('/',
             response_model=DonationCreateResponse,
             response_model_exclude_none=True,
             response_model_exclude={'user_id'})
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):

    new_donation = await donation_crud.create(donation, session, user)

    return await filling_up(new_donation, CharityProject, session)


@router.get('/',
            response_model=list[Donations_Super_DB],
            dependencies=[Depends(current_superuser)],
            response_model_exclude_none=True
            )
async def get_donations_list(
    session: AsyncSession = Depends(get_async_session),
):

    """Только для суперюзеров."""

    return await donation_crud.get_multi(session)


@router.get('/my',
            response_model=list[DonationDB],
            response_model_exclude={'user_id'},
            )
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Получает список всех донатов принадлежащих текущему пользователю."""

    return await donation_crud.get_by_user(user.id, session)


@router.delete(
    '/donations/{id}',
    tags=['Donations'],
    deprecated=True
)
def delete_donate(id: str):

    """Нельзя удалять донаты, а как же котики?!"""

    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail='Удаление донатов запрещено!'
    )


@router.patch(
    '/donations/{id}',
    tags=['Donations'],
    deprecated=True
)
def update_donate(id: str):

    """Нельзя изменять донаты, ФС котиков на страже порядка!"""

    raise HTTPException(
        status_code=HTTPStatus.METHOD_NOT_ALLOWED,
        detail='изменение донатов запрещено!'
    )
