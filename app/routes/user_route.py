from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Depends, Header, File, UploadFile
import starlette
from app.constants.type import ROLE
from app.exceptions import CredentialException
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.models.User import UserCreate, User
from app.models.User import User
from app.routes.auth_route import oauth2_scheme

router = APIRouter(prefix='/user')



# @router.get("/get")
# async def get_user(username: str, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         res = UserService().get_user(username)
#         return res

# @router.put("/update")
# async def update_user(info: User, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         res = UserService().update_user(info, token)
#         return res

@router.post("/create")
async def create_user(new_user: UserCreate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if (new_user.role == ROLE.SUPER_ADMIN):
            if not UserService().check_super_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().create_user(new_user)
        return res

# @router.get("/get_users_in_subject")
# async def get_users_in_subject(subject: str, token: str = Header(None)):
#     if AuthService().validate_token(token):
#         if not UserService().check_admin_permission(token):
#             raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         res = UserService().get_users_in_subject(subject)
#         return res

# @router.delete("/delete_user")
# async def delete_user(username: str, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         if not UserService().check_admin_permission(token):
#             raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         res = UserService().delete_user(username)
#         return res

# @router.post("/upload-file/")
# async def upload_file(file: UploadFile=File(...), token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = await UserService().upload_file(file)
#         return res

# @router.get("/get-file/")
# async def get_file(url_file: str, token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = UserService().get_file(url_file)
#         return res

# @router.put("/update-file/")
# async def update_file(url_old_file: str, file: UploadFile=File(...), token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = await UserService().update_file(url_old_file, file)
#         return res