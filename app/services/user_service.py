from fastapi import UploadFile
import starlette.status
import aiofiles
import os
from app.constants.type import ROLE
from app.repositories.user_repo import UserRepo
from app.models.User import UserCreate, User
from app.exceptions.CredentialException import CredentialException
from app.utils.auth_util import AuthUtil
from app.utils.time_util import TimeUtil
from fastapi.responses import FileResponse

class UserService:
    
    def __init__(self):
        self.__name__= "UserService"
        self.repo = UserRepo()

    def check_admin_permission(self, token: str):
        data = AuthUtil.decode_token(token)
        print('username', data)
        username: str = data["username"]
        user_call_api = self.repo.get_user_by_username(username)
        print ('user_call_api',user_call_api)
        if not user_call_api:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")
        if(user_call_api.role == ROLE.ADMIN or user_call_api.role == ROLE.SUPER_ADMIN):
            print('true')
            return True
        # else:
        #     return False

    def check_super_admin_permission(self, token: str):
        data = AuthUtil.decode_token(token)
        username: str = data["username"]
        user_call_api = self.repo.get_user_by_username(username)
        if not user_call_api:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")
        if(user_call_api.role == ROLE.SUPER_ADMIN):
            return True
        else:
            return False

    def create_user(self, user_created: UserCreate):
        _u = self.repo.get_user_by_username(user_created.username)
        if _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User already exists")
        hash_password = AuthUtil.hash_password(user_created.password)
        user = UserCreate(username=user_created.username, password= hash_password, role=user_created.role, subject=user_created.subject, fullname=user_created.fullname, dob=user_created.dob, url_avatar=user_created.dob, token="", email=user_created.email)
        res = self.repo.create_user(user)
        return "Sucessfully created!"

    def delete_user(self, username: str):
        res = self.repo.delete_user(username)
        if not res:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error")
        return "Sucessfully deleted!"

    def get_all_admin(self):
        list_admins = self.repo.get_all_admin()
        return list_admins

    def get_all_super_admin(self):
        list_super_admins = self.repo.get_all_super_admin()
        return list_super_admins

    def get_user(self, username: str):
        _u = self.repo.get_info_user(username)
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
        username: str = data["username"]
        if(username != info.username):
            if not self.check_admin_permission(token):
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        res = self.repo.update_user(info)
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
