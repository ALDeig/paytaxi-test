from enum import Enum

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from paytaxi_test.src.services.db.base import Base


class Status(Enum):
    dismissed = 1
    tmp_not_working = 2
    work = 3


class Category(Enum):
    driver = "driver"
    courier = "courier"


class MEmployee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str]
    last_name: Mapped[str]
    patronymic: Mapped[str]
    status: Mapped[Status] = mapped_column(sa.Enum(Status))
    category: Mapped[Category] = mapped_column(sa.Enum(Category))
    document: Mapped[str] = mapped_column(sa.String, nullable=True)

    phone: Mapped[list["MPhone"]] = relationship()


class MPhone(Base):
    __tablename__ = "phones"

    id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    phone: Mapped[str]
    employee_id: Mapped[int] = mapped_column(
        sa.ForeignKey("employees.id", ondelete="CASCADE")
    )
