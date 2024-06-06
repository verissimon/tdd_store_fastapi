class BaseException(Exception):
    message: str = "Internal server error"

    def __init__(self, message: str | None = None):
        if message:
            self.message = message


class NotFoundException(BaseException):
    message: str = "Not found"
