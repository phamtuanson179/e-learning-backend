from app.models.Auth import ChangePassword
from fastapi import APIRouter

from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    res = await AuthService().authenticate_user(form_data.username, form_data.password)
    return res

@router.get("/about-me")
async def about_me(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = AuthService().about_me(token)
        return res

@router.post("/change-password")
async def change_password(data:ChangePassword,token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = AuthService().change_password(token,data)
        return res

# @router.post("/forgot-password")
# async def forgot_password(request: ForgotPassword):
#     res = await AuthService().handle_forgot_password(request.email)
#     return "Reset password complete" 

# @router.post("/change-password")
# async def change_password(request: ChangePassword, token: str = Header(None)):
#     res = await AuthService().handle_change_password(request.curr_password, 
#                                                     request.new_password, request.confirm_password, token)
#     return "Change password complete" 
