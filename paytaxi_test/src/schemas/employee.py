from pydantic import BaseModel, ConfigDict, field_validator

from paytaxi_test.src.models.employee import Category, Status


class SEmployee(BaseModel):
    id: int | None = None
    name: str
    last_name: str
    patronymic: str
    status: Status | None = None
    category: Category | None = None
    document: str | None = None
    phone: str


class SEmployeeCityMobil(SEmployee):

    @field_validator("status")
    @classmethod
    def status_validate(cls, v: Status) -> Status:
        return Status.work if v == 1 else Status.dismissed


class SEmployeeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    last_name: str
    status: Status
    category: Category
    document: str | None = None
    phone: list[str]
    
    @field_validator("phone", mode="before")
    @classmethod
    def get_phones(cls, phones):
        print(f"Schema = {phones}")
        return [phone.phone for phone in phones]
