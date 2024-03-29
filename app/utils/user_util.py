from app.models.User import User
from app.models.Auth import AccessToken

class UserUtil:

    def format_info_user(user)-> User:
        return User(
            id=str(user["_id"]),
            email=user["email"],
            role=user["role"],
            list_subjects_id=user["list_subjects_id"],
            fullname=user["fullname"],
            dob=user["dob"],
            avatar=user["avatar"],
            username=user["username"],
        )

    

    
    def format_user_for_update_me(user):
        if hasattr(user, 'password'):
            delattr(user,'password')
        if hasattr(user, 'token'):
            delattr(user,'token')
        if hasattr(user, 'id'):
            delattr(user,'id')
        if hasattr(user, 'username'):
            delattr(user,'username')
        if hasattr(user, 'role'):
            delattr(user,'role')
        if hasattr(user, 'list_subjects_id'):
            delattr(user,'list_subjects_id')
        return user

    def format_user_for_update(user):
        if hasattr(user, 'password'):
            delattr(user,'password')
        if hasattr(user, 'token'):
            delattr(user,'token')
        if hasattr(user, 'id'):
            delattr(user,'id')
        if hasattr(user, 'username'):
            delattr(user,'username')
        return user
        
    def format_user_for_get(user):
        if hasattr(user, 'password'):
            delattr(user,'password')
        if hasattr(user, 'token'):
            delattr(user,'token')
        return user

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
