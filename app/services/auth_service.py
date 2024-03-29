from re import U
from app.models.Auth import ChangePassword
from app.utils.user_util import UserUtil
import jwt
from datetime import datetime

from app.repositories.user_repo import UserRepo
from app.services.user_service import UserService
from app.exceptions.CredentialException import CredentialException
from app.utils.auth_util import AuthUtil
from app.configs.Config import AuthConfig
import string, random


class AuthService:
    
    def __init__(self):
        self.__name__= "AuthService"
        self.repo = UserRepo()

    async def authenticate_user(self, username: str, password: str):
        try:
            user = self.repo.get_user_by_username(username)
            # print(AuthUtil.pwd_context.hash(password))
            # print(user.password)
            if not AuthUtil.verify_password(password, user.password):
                raise CredentialException(message="UNAUTHORIZED")
        except Exception as e:
            print(e)
            raise CredentialException(message="UNAUTHORIZED")

        access_token = AuthUtil.create_access_token(username)
        res = self.repo.update_token(username, access_token)
        return {"access_token": access_token, "token_type": "bearer"}

    def validate_token(self, token: str):
        try:
            data = AuthUtil.decode_token(token)
            username: str = data["username"]
            exp = data["exp"]
            expire = datetime.fromtimestamp(exp)
            finded_token = self.repo.get_token_by_username(username)
            if not finded_token:
                raise CredentialException(message="Could not validate credentials")
            if token != finded_token.token:
                raise CredentialException(message="Could not validate credentials")
            if expire < datetime.utcnow():
                raise CredentialException(message="Token expired")
        except:
            raise CredentialException(message="Could not validate credentials3")
        return True

    def validate_password(self, password, token: str):
        try:
            data = AuthUtil.decode_token(token)
            email: str = data["email"]
            user = self.repo.get_user_by_email(email)
            if not AuthUtil.verify_password(password, user.password):
                raise CredentialException(message="UNAUTHORIZED")
        except Exception as e:
            print(e)
            raise CredentialException(message="UNAUTHORIZED")
        return True

    def about_me(self,token:str):
        try:
            decoded_token = AuthUtil.decode_token(token)
            username = decoded_token["username"]
            user = self.repo.get_user_by_username(username)
            if not user:
                raise CredentialException(message="Lỗi hệ thống")
            else:
                return UserUtil.format_user_for_get(user)
        except Exception as e:
            raise CredentialException(message="Lỗi hệ thống")

    def change_password(self, token:str, data:ChangePassword):
        try: 
            if data.new_password != data.repeat_new_password:
                raise CredentialException(message="Lỗi hệ thống")
            else:
                decoded_token = AuthUtil.decode_token(token)
                user = UserRepo().get_user_by_username(decoded_token['username'])
                if not AuthUtil.verify_password(data.old_password, user.password):
                    raise CredentialException(message="Lỗi hệ thống")
                else: 
                    new_hash_password = AuthUtil.hash_password(data.new_password)
                    self.repo.update_password(user.username, new_hash_password)
                    access_token = AuthUtil.create_access_token(user.username)
                    self.repo.update_token(user.username, access_token)
                    return {"access_token": access_token, "token_type": "bearer"}

        except Exception as e:
            raise CredentialException(message="Lỗi hệ thống")
    async def handle_forgot_password(self, email: str):
        # check user exist
        res = UserService().get_user(email)
        random_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        
        # reset token and change password then save database
        reset_password = AuthService().change_password(email, random_password)

        # send email
        subject = "QUÊN MẬT KHẨU"
        recipient = [email]
        message = f"""
                Mật khẩu mới của bạn là:
                {random_password}
                """
        await EmailUtil.send_email(subject, recipient, message)
        
        return "Reset password complete" 

    async def handle_change_password(self, curr_pass: str, new_pass: str, confirm_pass: str, token: str):
        if not AuthService().validate_password(curr_pass, token):
            raise CredentialException(message="Current password is wrong")

        # check new password and confirm password
        if new_pass != confirm_pass:
            raise CredentialException(message="New password does not match confirm password")
        
        # reset token and change password then save database
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        email: str = payload.get("email")
        change_password = AuthService().change_password(email, new_pass)

        return "Change password complete" 
