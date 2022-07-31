
# from time import clock_getres
from pickle import FALSE
from app.constants.common import ROLE
from app.models.User import UserCreate, UserUpdate
from app.utils.auth_util import AuthUtil
from app.utils.user_util import UserUtil, User
from . import *
from app.configs.Config import RoleConfig
from bson.objectid import ObjectId


class UserRepo(BaseRepo):

    def __init__(self, collection: str="users") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_user(self, user: UserCreate):
        res = self.collection.insert_one(user.__dict__)
        return res

    def delete_user(self, user_id: str):
        res = self.collection.delete_one({"_id":ObjectId(user_id)})
        return res

    def get_all_admin(self):
        admins = list(self.collection.find({"role": RoleConfig.ROLE_ADMIN}))
        list_admins = []
        for record in admins:
            list_admins.append(UserUtil.format_user(record))
        return list_admins
    
    def get_all_user(self):
        users = list(self.collection.find({}))
        print(users)
        formated_users = []
        for user in users:
            formated_users.append(UserUtil.format_info_user(user))
        return formated_users

    def get_all_super_admin(self):
        admins = list(self.collection.find({"role": RoleConfig.ROLE_SUPERADMIN}))
        list_super_admins = []
        for record in admins:
            list_super_admins.append(UserUtil.format_info_user(record))
        return list_super_admins
    
    def get_user_by_id(self,id:str):
        user = self.collection.find_one({"_id":ObjectId(id)})
        if not user:
            return None
        return UserUtil.format_info_user(user)
    
    def get_user_by_token(self, token: str):
        user = self.mydb.get_collection("users").find_one({"token": token})
        if not user:
            return None
        return UserUtil.format_info_user(user)

    def get_info_user(self, username):
        users = list(self.collection.find({"username": username}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_user(users[0])

    def get_token_by_username(self, username):
        user = self.collection.find_one({"username": username})
        if not user:
            return None
        else:
            return UserUtil.format_token(user)
        
    def get_user_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if not user:
            return None
        else:
            return UserUtil.format_user(user)

    def get_user_by_username(self, username):
        user = self.collection.find_one({"username": username})
        if not user:
            return None
        else:
            return UserUtil.format_user(user)

    def get_users_in_subject(self, id_subject):
        users = list(self.collection.find({"list_subjects_id": id_subject}))
        list_users = []
        for record in users:
            list_users.append(UserUtil.format_info_user(record))
        return list_users

    def update_admin(self, info: User):
        query = { "email": info.email}
        value = { "subject": info.subject,
                "fullname": info.fullname,
                "role": info.role,
                "position": info.position,
                "date_of_birth": info.date_of_birth,
                "url_avatar": info.url_avatar
                }
        res = self.collection.update_one(query, { "$set": value})
        return res

    def update_token(self, username, token):
        query = { "username": username}
        value = { "token": token}
        res = self.collection.update_one(query, { "$set": value})
        return res

    def update_password(self, email, hash_password):
        query = {"email": email}
        value = {"password": hash_password}
        res = self.collection.update_one(query, {"$set": value})
        return res

    def update_user(self,user_id:str, user: UserUpdate):
        res = self.collection.update_one({"_id":ObjectId(user_id)}, { "$set": UserUtil.format_user_for_update(user).__dict__})
        return res

    def get_user_for_user(self, token: str):
        data = AuthUtil.decode_token(token)
        username = data['username']
        user = UserRepo().get_user_by_username(username)

        if not user:
            return None
        else:
            list_user = [] 
            datas = list(self.collection.find({}))
            # print(datas)
            
            if user.role == ROLE.ADMIN:
                for data in datas:
                    list_user.append(UserUtil.format_user_for_get(UserUtil.format_user(data)))
            elif user.role == ROLE.TEACHER:  
                print (user.list_subjects_id)
                    # print (user['list_subjects_id'])
                for data in datas:
                    flag= False
                    for subject_id in user.list_subjects_id:
                        print(subject_id,data['list_subjects_id'])
                        if(subject_id in data['list_subjects_id']):
                            print('a')
                            flag = True
                            break
                    if flag == True:
                        list_user.append(UserUtil.format_user_for_get(UserUtil.format_user(data)))    
            else:
                return None
            if not list_user:
                return None
            else:
                return list_user