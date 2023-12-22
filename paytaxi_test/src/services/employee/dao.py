import sqlalchemy as sa
from sqlalchemy.orm import selectinload

from paytaxi_test.src.models.employee import MEmployee
from paytaxi_test.src.services.db.base import session_factory
from paytaxi_test.src.services.db.dao import BaseDAO
from paytaxi_test.src.services.employee.exceptions import EmployeeNotFound


class EmployeeDAO(BaseDAO):
    @classmethod
    async def get_employee(
        cls, model: type[MEmployee], **filter_by
    ) -> MEmployee:
        query = (
            sa.select(model).options(selectinload(model.phone)).filter_by(**filter_by)
        )
        async with session_factory() as session:
            response = await session.scalar(query)
            if response is None:
                raise EmployeeNotFound
            return response

    @classmethod
    async def update_employee(
        cls, model: type[MEmployee], update_fields: dict, **filter_by
    ) -> None:
        query = sa.update(model).filter_by(**filter_by).values(**update_fields)
        async with session_factory() as session:
            await session.execute(query)
            await session.commit()
