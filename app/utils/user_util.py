from app.models.account import AccessToken
from app.models.user import User

class UserUtil:

    def format_info_user(user) -> User:
        return User(
            user_id= str(user["_id"]),
            email=user["email"],
            role=user["role"],
            subject=user["subject"],
            fullname=user["fullname"],
            position=user["position"],
            date_of_birth=user["date_of_birth"],
            url_avatar=user["url_avatar"],
            username=user["username"]
        )

    def format_token(user) -> AccessToken:
        return AccessToken(
            username=user["username"],
            token=user["token"]
        )

    def format_user(user) -> User:
        return User(
            id=str(user["_id"]),
            email=user["email"],
            password=user["password"],
            role=user["role"],
            subject=user["subject"],
            fullname=user["fullname"],
            dob=user["dob"],
            url_avatar=user["url_avatar"],
            token=user["token"],
            username=user["username"]
        )

    