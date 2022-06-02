from fastapi import APIRouter, Depends, Header
import starlette.status
from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.services.ExamService import ExamService
from app.models.Exam import Exam, ExamCreate
from app.exceptions.CredentialException import CredentialException
from app.routes.account_route import oauth2_scheme

router = APIRouter(prefix='/exam')

@router.get("/get_all")
async def get_exam(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam(id)
        return res


@router.get("/get_exams_for_subject")
async def get_exams_for_subject(subject: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exams_for_subject(subject)
        return res

@router.post("/create")
async def create_exam(new_exam: ExamCreate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().create_exam(new_exam, token)
        return res


@router.put("/update")
async def update_exam(info: Exam, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().update_exam(info)
        return res


@router.delete("/delete")
async def delete_exam(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = ExamService().delete_exam(id)
        return res



# @router.get("/get_all_admin")
# async def get_all_admin(token: str = Header(None)):
#     if AuthService().validate_token(token):
#         if not UserService().check_super_admin_permission(token):
#             raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         res = UserService().get_all_admin()
#         return res

# @router.get("/get_all_super_admin")
# async def get_all_super_admin(token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         if not UserService().check_super_admin_permission(token):
#             raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         res = UserService().get_all_super_admin()
#         return res

@router.get("/get_users_in_subject")
async def get_users_in_subject(subject: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        if not UserService().check_admin_permission(token):
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = UserService().get_users_in_subject(subject)
        return res

# @router.put("/admin/update_admin")
# async def update_admin(info: User, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         if (info.role == RoleConfig.ROLE_SUPERADMIN):
#             if not UserService().check_super_admin_permission(token):
#                 raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         elif (info.role == RoleConfig.ROLE_ADMIN):
#             if not UserService().check_admin_permission(token):
#                 raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
#         res = UserService().update_admin(info)
#         return res


