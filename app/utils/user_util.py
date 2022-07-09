from app.models.User import User
from app.models.Auth import AccessToken

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
            url_avatar=user["url_avatar"]
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
            list_subjects_id=user["list_subjects_id"],
            fullname=user["fullname"],
            dob=user["dob"],
            avatar=user["avatar"],
            token=user["token"],
            username=user["username"]
        )

    