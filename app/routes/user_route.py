from fastapi import APIRouter, Depends, status , HTTPException
from app.configs.Config import RoleConfig
from app.constants.common import ROLE
from app.exceptions import CredentialException
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.models.User import UserCreate, User, UserUpdate
from app.models.User import User
from app.routes.auth_route import oauth2_scheme
import starlette.status

router = APIRouter(prefix="/user")

@router.get("/get-all")
async def get_user(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().get_all_user()
        return res

@router.get("/get-user-by-email")
async def get_user(email: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().get_user(email)
        return res


@router.post("/create")
async def create_user(new_user: UserCreate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if (new_user.role == ROLE.ADMIN):
            if not UserService().is_admin(token):
                # return None
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif not (UserService().is_admin(token) or  UserService().is_teacher(token)) :
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
            # return 101
    res = UserService().create_user(new_user)
    return res


@router.put("/update")
async def update_user(id:str,data: UserCreate, token: str = Depends(oauth2_scheme)):
    print(data)
    if AuthService().validate_token(token):
        res = UserService().update_user(id,data)
        return res

@router.put("/update-me")
async def update_user(data: UserUpdate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().update_me(token,data)
        return res

@router.delete("/delete")
async def delete_user(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().delete_user(id)
        return res

@router.get('/get-user-for-user')
async def get_user_for_user(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = UserService().get_user_for_user(token)
        return res