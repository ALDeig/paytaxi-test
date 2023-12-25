import pytest
from httpx import AsyncClient


yandex_data = [
    (
        {
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "status": 1,
            "category": "driver",
            "phone": "9870000000",
        },
        200,
    ),
    (
        {
            "id": 100,
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "status": 1,
            "category": "driver",
            "phone": "9870000000",
        },
        409,
    ),
]


@pytest.mark.parametrize(
    "data,status_code",
    yandex_data,
)
async def test_create_or_update_yandex_employee(
    data: dict, status_code: int, ac: AsyncClient
):
    response = await ac.post(
        "/yandex/employee",
        json=data,
    )

    assert response.status_code == status_code


city_mobil_data = [
    (
        {
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "status": 1,
            "phone": "9870000000",
        },
        200,
    ),
    (
        {
            "id": 100,
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "status": 1,
            "phone": "9870000000",
        },
        409,
    ),
]


@pytest.mark.parametrize("data,status_code", city_mobil_data)
async def test_create_or_update_city_mobile_employee(
    data: dict, status_code: int, ac: AsyncClient
):
    response = await ac.post(
        "/city_mobile/employee",
        json=data,
    )
    if status_code == 200:
        assert response.json()["status"] == 3
    assert response.status_code == status_code


mobile_data = [
    (
        {
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "phone": "9870000000",
        },
        200,
    ),
]


@pytest.mark.parametrize("data,status_code", mobile_data)
async def test_create_or_update_mobile_employee(
    data: dict, status_code: int, ac: AsyncClient
):
    response = await ac.post(
        "/mobile/employee",
        json=data,
    )

    assert response.status_code == status_code


other_data = [
    (
        {
            "name": "Test3",
            "last_name": "Test3Test3",
            "patronymic": "Test3Test3Test3",
            "phone": "9870000000",
        },
        200,
    ),
]


@pytest.mark.parametrize("data,status_code", other_data)
async def test_create_or_update_ohter_employee(
    data: dict, status_code: int, ac: AsyncClient
):
    response = await ac.post(
        "/other/employee",
        json=data,
    )

    assert response.status_code == status_code
