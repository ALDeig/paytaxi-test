import asyncio
import json 

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from pytest_asyncio import is_async_test
from sqlalchemy import insert

from paytaxi_test.main import app as fastapi_app
from paytaxi_test.config import settings
from paytaxi_test.src.services.db.base import Base, engine, session_factory
from paytaxi_test.src.models.employee import MEmployee, MPhone


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    assert settings.mode == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


    def open_mock_json(model: str):
        with open(f"paytaxi_test/tests/mock_{model}.json", encoding="utf8") as file:
            return json.load(file)

    employees = open_mock_json("employees_2")
    phones = open_mock_json("phones_2")

    async with session_factory() as session:
        add_employee = insert(MEmployee).values(employees)
        add_phone = insert(MPhone).values(phones)

        await session.execute(add_employee)
        await session.execute(add_phone)

        await session.commit()


@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


def pytest_collection_modifyitems(items):
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker)

