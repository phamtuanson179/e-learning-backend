from fastapi import UploadFile
import starlette.status
import aiofiles
import os
from app.configs.Config import AuthConfig
from app.constants.common import ROLE
from app.repositories.user_repo import UserRepo
from app.repositories.exam_repo import ExamRepo
from app.models.User import UserCreate, User
from app.exceptions.CredentialException import CredentialException
from app.utils.auth_util import AuthUtil
from app.utils.time_util import TimeUtil
from app.configs.Config import RoleConfig
from app.utils.user_util import UserUtil
from fastapi.responses import FileResponse
# from fastapi.encoders import jsonable_encoder


class UserService:
    
    def __init__(self):
        self.__name__= "UserService"
        self.repo = UserRepo()

    def check_admin_permission(self, token: str):
        data = AuthUtil.decode_token(token)
        username: str = data["username"]
        user_call_api = self.repo.get_user_by_username(username)
        print("user_call_api",user_call_api)
        if not user_call_api:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")
        if(user_call_api.role == ROLE.ADMIN):
            return True
        else:
            return False

    def is_admin(self, token: str):
        data = AuthUtil.decode_token(token)
        username: str = data["username"]
        cur_user = self.repo.get_user_by_username(username)
        # print(cur_user)

        if not cur_user:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")
        if(cur_user.role == ROLE.ADMIN):
            return True
        else:
            return False

    def is_teacher(self, token: str):
        data = AuthUtil.decode_token(token)
        username: str = data["username"]
        cur_user = self.repo.get_token_by_username(username)
        print(cur_user)
        if not cur_user:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")
        if(cur_user.role == ROLE.TEACHER):
            return True
        else:
            return False

    def create_user(self, new_user: UserCreate):
        _u = self.repo.get_user_by_username(new_user.username)
        if _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User already exists")
        hash_password = AuthUtil.hash_password(new_user.password)
        new_user.password = hash_password
        # user = User(email=new_user.email, password= hash_password, role=new_user.role, subject=new_user.subject, fullname=new_user.fullname, position=new_user.position, date_of_birth="", url_avatar="", token="")
        # formated_user = UserUtil.format_user(new_user)
        res = self.repo.create_user(new_user)
        return "Sucessfully created!"

    def delete_user(self, email: str):
        res = self.repo.delete_user(email)
        if not res:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error")
        return "Sucessfully deleted!"

    def get_all_admin(self):
        list_admins = self.repo.get_all_admin()
        return list_admins

    def get_all_super_admin(self):
        list_super_admins = self.repo.get_all_super_admin()
        return list_super_admins

    def get_all_user(self):
        users = self.repo.get_all_user()
        return users

    def get_user(self, email: str):
        _u = self.repo.get_info_user(email)
        if not _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User not exists")
        return _u

    def get_users_in_subject(self, subject: str):
        list_users = self.repo.get_users_in_subject(subject)
        return list_users

    def update_admin(self, info: User):
        res = self.repo.update_admin(info)
        return "Update success"

    def update_user(self, info: User, token: str):
        data = AuthUtil.decode_token(token)
        email: str = data["email"]
        if(email != info.email):
            if not self.check_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = self.repo.update_user(info)
        return "Update success"

    def update_me(self, token: str, user: User):
        data = AuthUtil.decode_token(token)
        print(data,user)
        username: str = data["username"]
        if(username != user.username):
            if not self.check_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = self.repo.update_user(user.id,user)
        return "Update success"

    async def upload_file(self, file: UploadFile):
        name = file.filename
        path = "assets/image/" + TimeUtil.get_timestamp_now() + name
        async with aiofiles.open(path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
        return path

    def get_file(self, url: str):
        return FileResponse(url)

    async def update_file(self, url_old_file: str, file: UploadFile):
        name = file.filename
        path = "assets/image/" + TimeUtil.get_timestamp_now() + name
        async with aiofiles.open(path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
        os.remove(url_old_file)
        return path
