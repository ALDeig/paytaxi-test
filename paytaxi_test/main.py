from fastapi import FastAPI

from paytaxi_test.src.schemas.employee import (
    SEmployee,
    SEmployeeCityMobil,
    SEmployeeResponse,
)
from paytaxi_test.src.services.employee.employee import save_employee_data
from paytaxi_test.src.services.employee.exceptions import ApiEmployeeNotFound, EmployeeNotFound
from paytaxi_test.src.services.employee.prepare_data import (
    CityMobilEmployeePrepare,
    MobilAppEmployeePrepare,
    OtherEmployeePrepare,
    YandexEmployeePrepare,
)


app = FastAPI(
    title="PayTaxi",
    version="0.1.0",
)


@app.post("/yandex/employee")
async def create_or_update_yandex_employee(employee: SEmployee) -> SEmployeeResponse:
    try:
        return await save_employee_data(employee, YandexEmployeePrepare)
    except EmployeeNotFound:
        raise ApiEmployeeNotFound


@app.post("/city_mobile/employee")
async def create_or_update_city_mobile_employee(
    employee: SEmployeeCityMobil,
) -> SEmployeeResponse:
    try:
        return await save_employee_data(employee, CityMobilEmployeePrepare)
    except EmployeeNotFound:
        raise ApiEmployeeNotFound



@app.post("/mobile/employee")
async def create_or_update_mobile_employee(employee: SEmployee) -> SEmployeeResponse:
    try:
        return await save_employee_data(employee, MobilAppEmployeePrepare)
    except EmployeeNotFound:
        raise ApiEmployeeNotFound


@app.post("/other/employee")
async def create_or_update_ohter_employee(employee: SEmployee) -> SEmployeeResponse:
    try:
        return await save_employee_data(employee, OtherEmployeePrepare)
    except EmployeeNotFound:
        raise ApiEmployeeNotFound
