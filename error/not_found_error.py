from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self, message):
        self.status_code = 404
        self.detail = message
