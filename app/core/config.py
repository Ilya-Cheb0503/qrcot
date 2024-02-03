from typing import Optional  # noqa

from pydantic import BaseSettings, EmailStr  # noqa


class Settings(BaseSettings):
    app_title: str = 'Фонд спасения QRKot_иков'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = 'user@mail.ru'
    first_superuser_password: Optional[str] = 'password'

    class Config:
        env_file = '/home/cloudy/cat_charity_fund/.env'


settings = Settings()
