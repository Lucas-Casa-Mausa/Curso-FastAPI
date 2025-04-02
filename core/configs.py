from typing import ClassVar
from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base

class Settings(BaseModel):
    AP1_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:postgresdb@localhost:5432/faculdade'
    DBBaseModel: ClassVar[DeclarativeBase] = declarative_base()

    JWT_SECRET: str = 'DjNx2-CGbOB_amKuCCjEQj9Obb2b7ZdN_QXuXg0k98I'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    model_config = SettingsConfigDict(
        case_sensitive=True
    )

settings: Settings = Settings()