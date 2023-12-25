import pytest
from paytaxi_test.src.models.employee import MEmployee, Status
from paytaxi_test.src.schemas.employee import SEmployee
from paytaxi_test.src.services.employee.dao import EmployeeDAO
from paytaxi_test.src.services.employee.prepare_data import YandexEmployeePrepare


yandex_data = [
    ({
        "id": None,
        "name": "Denis",
        "last_name": "test",
        "patronymic": "test",
        "phone": "12345123",
        "status": 1,
        "category": "driver",
    }, 1),
    ({
        "id": 1,
        "name": "Тест",
        "last_name": "ТестТест2",
        "patronymic": "ТестТестТест2",
        "phone": "12345123",
        "status": 1,
        "category": "driver",
    }, 1)
]


@pytest.mark.parametrize("data,status", yandex_data)
async def test_yandex_employee_prepare(data: dict, status: int):
    schema = SEmployee.model_validate(data)
    yandex = YandexEmployeePrepare(schema)
    data_to_add = yandex.prepare_data_for_add()
    assert data_to_add.status == Status(status)

    if data["id"] == 1:
        current_data = await EmployeeDAO.get_employee(MEmployee, id=1)
        data_to_update = yandex.prepare_data_for_update(current_data)
        assert data_to_update["phone"] == data["phone"]
