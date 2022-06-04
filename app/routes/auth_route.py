
from app.services.auth_service import AuthService
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@router.post("/login")
# async def login(account : Account):
#     print (account.email, account.password)
#     res = await AuthService().authenticate_user(account.email, account.password)
#     print (res)
#     return res
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    res = await AuthService().authenticate_user(form_data.username, form_data.password)
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
