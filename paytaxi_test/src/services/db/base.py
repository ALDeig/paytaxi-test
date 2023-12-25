from sqlalchemy import NullPool
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from paytaxi_test.config import settings


if settings.mode == "TEST":
    DATABASE_URL = settings.test_db_url
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.db_url
    DATABASE_PARAMS = {}


engine = create_async_engine(str(DATABASE_URL), **DATABASE_PARAMS)
session_factory = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass
