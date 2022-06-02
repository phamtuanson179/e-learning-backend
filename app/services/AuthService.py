import jwt
from datetime import datetime

from app.repositories.UserRepo import UserRepo
from app.services.UserService import UserService
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil
from app.configs.Config import AuthConfig
import string, random


class AuthService:
    
    def __init__(self):
        self.__name__= "AuthService"
        self.repo = UserRepo()

    async def authenticate_user(self, username: str, password: str):
        try:
            user = self.repo.get_user_by_username(username)
            if not AuthUtil.verify_password(password, user.password):
                raise Exception(message="UNAUTHORIZED")
            access_token = AuthUtil.create_access_token(username)
            self.repo.update_token(username, access_token)
            return {"access_token": access_token, "token_type": "bearer"}
        except Exception as e:
            raise CredentialException(message="UNAUTHORIZED")


    def validate_token(self, token: str):
        try:
            data = AuthUtil.decode_token(token)
            username: str = data["username"]
            exp = data["exp"]
            expire = datetime.fromtimestamp(exp)
            if not self.repo.get_token_by_username(username):
                raise CredentialException(message="Could not validate credentials")
            if token != self.repo.get_token_by_username(username).token:
                raise CredentialException(message="Could not validate credentials")
            if expire < datetime.utcnow():
                raise CredentialException(message="Token expired")
        except:
            raise CredentialException(message="Could not validate credentials3")
        return True

    def validate_password(self, password, token: str):
        try:
            data = AuthUtil.decode_token(token)
            username: str = data["username"]
            user = self.repo.get_user_by_username(username)
            if not AuthUtil.verify_password(password, user.password):
                raise CredentialException(message="UNAUTHORIZED")
        except Exception as e:
            raise CredentialException(message="UNAUTHORIZED")
        return True

    def change_password(self, username: str, password: str):
        access_token = AuthUtil.create_access_token(username)
        reset_token = self.repo.update_token(username, access_token)
        hash_password = AuthUtil.hash_password(password)
        reset_password = self.repo.update_password(username, hash_password)
        return {"access_token": access_token, "hash_password": password}

    async def handle_forgot_password(self, username: str):
        # check user exist
        res = UserService().get_user(username)
        random_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        
        # reset token and change password then save database
        reset_password = AuthService().change_password(username, random_password)

        # send username
        subject = "QUÊN MẬT KHẨU"
        recipient = [username]
        message = f"""
                Mật khẩu mới của bạn là:
                {random_password}
                """
        await usernameUtil.send_username(subject, recipient, message)
        
        return "Reset password complete" 

    async def handle_change_password(self, curr_pass: str, new_pass: str, confirm_pass: str, token: str):
        if not AuthService().validate_password(curr_pass, token):
            raise CredentialException(message="Current password is wrong")

        # check new password and confirm password
        if new_pass != confirm_pass:
            raise CredentialException(message="New password does not match confirm password")
        
        # reset token and change password then save database
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        username: str = payload.get("username")
        change_password = AuthService().change_password(username, new_pass)

        return "Change password complete" 
