from fastapi import APIRouter, Header
import starlette.status
from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.services.ExamService import ExamService
from app.models.User import NewUser, User
from app.models.Exam import Exam, NewExam
from app.models.Room import Room
from app.configs.Config import RoleConfig
from app.exceptions.CredentialException import CredentialException

router = APIRouter()

@router.post("/admin/add_exam")
async def create_exam(new_exam: NewExam, token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().create_exam(new_exam, token)
        return res

@router.post("/admin/add_user")
async def create_user(new_user: NewUser, token: str = Header(None)):
    if AuthService().validate_token(token):
        if (new_user.role == RoleConfig.ROLE_SUPERADMIN):
            if not UserService().check_super_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().create_user(new_user)
        return res

@router.delete("/admin/delete_exam")
async def delete_exam(id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().delete_exam(id)
        return res

@router.delete("/admin/delete_user")
async def delete_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().delete_user(email)
        return res

@router.get("/admin/get_all_admin")
async def get_all_admin(token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_super_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().get_all_admin()
        return res

@router.get("/admin/get_all_super_admin")
async def get_all_super_admin(token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_super_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().get_all_super_admin()
        return res

@router.get("/admin/get_users_in_room")
async def get_users_in_room(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().get_users_in_room(room)
        return res

@router.put("/admin/update_admin")
async def update_admin(info: User, token: str = Header(None)):
    if AuthService().validate_token(token):
        if (info.role == RoleConfig.ROLE_SUPERADMIN):
            if not UserService().check_super_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif (info.role == RoleConfig.ROLE_ADMIN):
            if not UserService().check_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().update_admin(info)
        return res

@router.put("/admin/update_exam")
async def update_exam(info: Exam, token: str = Header(None)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().update_exam(info)
        return res
