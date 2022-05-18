from email import message
from fastapi import APIRouter, Header

from app.services.AuthService import AuthService
from app.services.UserService import UserService
from app.models.User import Account, ForgotPassword, ChangePassword
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil
from app.utils import EmailUtil
from app.models.User import Account

router = APIRouter()

@router.post("/login")
async def login(account : Account):
    res = await AuthService().authenticate_user(account.email, account.password)
    return res

@router.post("/forgot-password")
async def forgot_password(request: ForgotPassword):
    res = await AuthService().handle_forgot_password(request.email)
    return "Reset password complete" 

@router.post("/change-password")
async def change_password(request: ChangePassword, token: str = Header(None)):
    res = await AuthService().handle_change_password(request.curr_password, 
                                                    request.new_password, request.confirm_password, token)
    return "Change password complete" 
