from fastapi import HTTPException, status


class EmployeeNotFound(Exception):
    pass


class ForrbidenMethodError(Exception):
    pass


class ApiError(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class ApiEmployeeNotFound(ApiError):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с таким ID не найден"
