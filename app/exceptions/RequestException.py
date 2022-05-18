from fastapi import HTTPException, status


class RequestException(HTTPException):
    def __init__(
        self,
        message,
        headers={"WWW-Authenticate": "Bearer"},
        status_code=status.HTTP_400_BAD_REQUEST,
    ):
        RequestException.detail = message
        RequestException.headers = headers
        RequestException.status_code = status_code
