from fastapi import HTTPException, status


class CredentialException(HTTPException):

	def __init__(self, message, headers={"WWW-Authenticate": "Bearer"}, status_code = status.HTTP_401_UNAUTHORIZED):
		CredentialException.detail = message
		CredentialException.headers = headers
		CredentialException.status_code = status_code
