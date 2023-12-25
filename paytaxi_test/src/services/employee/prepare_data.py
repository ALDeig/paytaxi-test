from abc import ABC
from dataclasses import dataclass

from paytaxi_test.src.models.employee import Category, MEmployee, Status
from paytaxi_test.src.schemas.employee import SEmployee


@dataclass(slots=True, frozen=True)
class EmployeeData:
    name: str
    last_name: str
    patronymic: str
    status: Status
    category: Category
    phone: list[str]
    document: str | None = None


class EmployeeDataPrepare(ABC):
    """Interface for validate employees data"""

    def __init__(self, raw_data: SEmployee) -> None:
        self._raw_data = raw_data

    def prepare_data_for_add(self) -> EmployeeData:
        raise NotImplementedError

    def prepare_data_for_update(self, current_data: MEmployee) -> dict:
        raise NotImplementedError


class YandexEmployeePrepare(EmployeeDataPrepare):
    def prepare_data_for_add(self) -> EmployeeData:
        return EmployeeData(**self._raw_data.model_dump(exclude={"id",}))

    def prepare_data_for_update(self, current_data: MEmployee) -> dict:
        update_data = {}
        if self._raw_data.phone not in current_data.phone:
            update_data["phone"] = self._raw_data.phone
        if current_data.status != self._raw_data.status:
            update_data["status"] = self._raw_data.status
        return update_data


class CityMobilEmployeePrepare(EmployeeDataPrepare):
    def prepare_data_for_add(self) -> EmployeeData:
        return EmployeeData(
            **self._raw_data.model_dump(exclude={"id", "category"}),
            category=Category.driver
        )

    def prepare_data_for_update(self, current_data: MEmployee) -> dict:
        update_data = {}
        if self._raw_data.phone[0] not in current_data.phone:
            update_data["phone"] = self._raw_data.phone[0]
        if current_data.status != self._raw_data.status:
            update_data["status"] = self._raw_data.status
        return update_data


class MobilAppEmployeePrepare(EmployeeDataPrepare):
    def prepare_data_for_add(self) -> EmployeeData:
        return EmployeeData(
            **self._raw_data.model_dump(exclude={"id", "status", "category"}),
            status=Status.work,
            category=Category.driver
        )


class OtherEmployeePrepare(EmployeeDataPrepare):
    def prepare_data_for_add(self) -> EmployeeData:
        return EmployeeData(
            **self._raw_data.model_dump(exclude={"id", "status", "category"}),
            status=Status.work,
            category=Category.courier
        )
