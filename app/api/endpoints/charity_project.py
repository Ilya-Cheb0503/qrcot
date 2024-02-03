from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_biil_status, check_corrected_values,
                                check_name_duplicate, check_project_exists,
                                check_project_status,
                                check_project_status_for_update)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.models import Donation
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectDelete,
                                         CharityProjectUpdate,
                                         CharityProjectUpdateResponse)
from app.services.pull_in import filling_up

router = APIRouter()


@router.post('/',
             response_model=CharityProjectDB,
             dependencies=[Depends(current_superuser)],
             response_model_exclude_none=True
             )
async def create_new_charity_project(
        charity_project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):

    """Только для суперюзеров."""

    await check_name_duplicate(charity_project.name, session)
    new_project = await charity_project_crud.create(charity_project, session)

    return await filling_up(new_project, Donation, session)


@router.get('/',
            response_model=list[CharityProjectDB],
            response_model_exclude_none=True
            )
async def get_projects_list(
    session: AsyncSession = Depends(get_async_session),
):

    return await charity_project_crud.get_multi(session)


@router.patch('/{project_id}',
              response_model=CharityProjectUpdateResponse,
              dependencies=[Depends(current_superuser)],
              response_model_exclude_unset=True,
              )
async def project_update(
    project_id: int,
    object_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
):

    """Только для суперюзеров."""

    project = await check_project_exists(project_id, session)

    if object_in.name is not None:
        await check_name_duplicate(object_in.name, session)

    if object_in.full_amount is not None:
        await check_corrected_values(
            object_in.full_amount,
            project.invested_amount,
            session
        )

    await check_project_status_for_update(project.fully_invested, session)

    return await charity_project_crud.update(project, object_in, session)


@router.delete('/{project_id}',
               response_model=CharityProjectDelete,
               dependencies=[Depends(current_superuser)]
               )
async def delete_project_by_id(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
):

    """Только для суперюзеров."""

    project = await check_project_exists(project_id, session)

    await check_project_status(project.fully_invested, session)
    await check_biil_status(project.invested_amount, session)

    return await charity_project_crud.remove(project, session)
