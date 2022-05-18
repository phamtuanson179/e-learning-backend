from app.models.User import User, AccessToken

class UserUtil:

    def format_info_user(user) -> User:
        return User(
            user_id= str(user["_id"]),
            email=user["email"],
            role=user["role"],
            room=user["room"],
            fullname=user["fullname"],
            position=user["position"],
            date_of_birth=user["date_of_birth"],
            url_avatar=user["url_avatar"]
        )

    def format_token(user) -> AccessToken:
        return AccessToken(
            email=user["email"],
            token=user["token"]
        )

    def format_user(user) -> User:
        return User(
            email=user["email"],
            password=user["password"],
            role=user["role"],
            room=user["room"],
            fullname=user["fullname"],
            position=user["position"],
            date_of_birth=user["date_of_birth"],
            url_avatar=user["url_avatar"],
            token=user["token"]
        )

    