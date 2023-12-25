from paytaxi_test.src.models.employee import MEmployee, MPhone
from paytaxi_test.src.schemas.employee import SEmployee, SEmployeeResponse
from paytaxi_test.src.services.employee.dao import EmployeeDAO
from paytaxi_test.src.services.employee.prepare_data import (
    EmployeeDataPrepare,
)


async def save_employee_data(
    employee: SEmployee, employee_creator: type[EmployeeDataPrepare]
) -> SEmployeeResponse:
    creator = employee_creator(employee)
    if employee.id is None:
        result = await _create_employee(creator)
    else:
        result = await _update_employee(employee.id, creator)
    return SEmployeeResponse.model_validate(result)


async def _create_employee(employee_creator: EmployeeDataPrepare) -> MEmployee:
    data = employee_creator.prepare_data_for_add()
    created_employee = await EmployeeDAO.add(
        MEmployee,
        name=data.name,
        last_name=data.last_name,
        patronymic=data.patronymic,
        status=data.status,
        category=data.category,
        document=data.document,
    )
    await EmployeeDAO.add(MPhone, employee_id=created_employee.id, phone=data.phone[0])
    return await EmployeeDAO.get_employee(MEmployee, id=created_employee.id)


async def _update_employee(
    employee_id: int, employee_creator: EmployeeDataPrepare
) -> MEmployee:
    current_data = await EmployeeDAO.get_employee(MEmployee, id=employee_id)
    data = employee_creator.prepare_data_for_update(current_data)
    if phone := data.get("phone"):
        await EmployeeDAO.add(MPhone, employee_id=employee_id, phone=phone)
    if status := data.get("status"):
        await EmployeeDAO.update_employee(MEmployee, {"status": status}, id=employee_id)
    return await EmployeeDAO.get_employee(MEmployee, id=employee_id)
