from fastapi import APIRouter, Depends, status , HTTPException
from app.configs.Config import RoleConfig
from app.constants.common import ROLE
from app.exceptions import CredentialException
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.models.User import UserCreate, User
from app.models.User import User
from app.routes.auth_route import oauth2_scheme
import starlette.status

router = APIRouter(prefix="/user")

@router.get("/get-user-by-email")
async def get_user(email: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().get_user(email)
        return res


@router.post("/create")
async def create_user(new_user: UserCreate, token: str = Depends(oauth2_scheme)):
    # print(token)
    print(UserService().is_admin(token))
    if AuthService().validate_token(token):
        if (new_user.role == ROLE.ADMIN):
            if not UserService().is_admin(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif not (UserService().is_admin(token) or  UserService().is_teacher(token)) :
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
            # return 101
    res = UserService().create_user(new_user)
    return res


@router.put("/update")
async def update_user(data: User, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().update_user(data, token)
        return res

@router.put("/update-me")
async def update_user(data: User, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().update_me(data, token)
        return res

@router.delete("/delete")
async def delete_user(email: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().delete_user(email)
        return res