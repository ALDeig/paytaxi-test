from fastapi import FastAPI

from paytaxi_test.src.schemas.employee import (
    SEmployee,
    SEmployeeCityMobil,
    SEmployeeResponse,
)
from paytaxi_test.src.services.employee.employee import save_employee_data
from paytaxi_test.src.services.employee.prepare_data import (
    CityMobilEmployeePrepare,
    MobilAppEmployeePrepare,
    OtherEmployeePrepare,
    YandexEmployeePrepare,
)


app = FastAPI()


@app.post("/yandex/employee")
async def create_or_update_yandex_employee(employee: SEmployee) -> SEmployeeResponse:
    return await save_employee_data(employee, YandexEmployeePrepare)


@app.post("/city_mobile/employee")
async def create_or_update_city_mobile_employee(
    employee: SEmployeeCityMobil,
) -> SEmployeeResponse:
    return await save_employee_data(employee, CityMobilEmployeePrepare)


@app.post("/mobile/employee")
async def create_or_update_mobile_employee(employee: SEmployee) -> SEmployeeResponse:
    return await save_employee_data(employee, MobilAppEmployeePrepare)


@app.post("/ohter/employee")
async def create_or_update_ohter_employee(employee: SEmployee) -> SEmployeeResponse:
    return await save_employee_data(employee, OtherEmployeePrepare)
