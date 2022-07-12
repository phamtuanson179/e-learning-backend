from app.models.User import User
from app.models.Auth import AccessToken

class UserUtil:

    # def format_info_user(user) -> User:
    #     return User(
    #         id=str(user["_id"]),
    #         email=user["email"],
    #         password=user["password"],
    #         role=user["role"],
    #         list_subjects_id=user["list_subjects_id"],
    #         fullname=user["fullname"],
    #         dob=user["dob"],
    #         avatar=user["avatar"],
    #         token=user["token"],
    #         username=user["username"]
    #     )

    def format_token(user) -> AccessToken:
        return AccessToken(
            username=user["username"],
            token=user["token"],
            role = user["role"],
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

    

# class UserCreate(BaseModel):
#     username:str
#     password: str
#     email: str
#     role: str
#     fullname: str
#     dob: str
#     list_subjects_id: Optional[List[str]]
#     avatar: Optional[str] 
#     token: Optional[str] = None

# class User(UserCreate):
#     id: str
