

from pydantic import BaseModel

# class Account(BaseModel): 
class AccessToken(BaseModel):
    username: str
    token: str

class ForgotPassword(BaseModel):
    email: str

class ChangePassword(BaseModel):
    curr_password: str
    new_password: str
    confirm_password: str