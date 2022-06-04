
from app.constants.type import ROLE
from app.utils.user_util import UserUtil, User
from . import *


class UserRepo(BaseRepo):

    def __init__(self, collection: str="users") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_user(self, user: User):
        res = self.collection.insert_one(user.__dict__)
        return res

    def delete_user(self, email: str):
        res = self.collection.delete_one({"email": email})
        return res

    def get_all_admin(self):
        admins = list(self.collection.find({"role": ROLE.ADMIN}))
        list_admins = []
        for record in admins:
            list_admins.append(UserUtil.format_info_user(record))
        return list_admins

    def get_all_super_admin(self):
        admins = list(self.collection.find({"role": ROLE.SUPER_ADMIN}))
        list_super_admins = []
        for record in admins:
            list_super_admins.append(UserUtil.format_info_user(record))
        return list_super_admins

    def get_info_user(self, username):
        users = list(self.collection.find({"username": username}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_info_user(users[0])

    def get_token_by_username(self, username):
        users = list(self.collection.find({"username": username}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_token(users[0])
        
    def get_user_by_username(self, username):
        users = list(self.collection.find({"username": username}))
        count = 0
        for record in users:
            count += 1
            
        if count < 1:
            return None
        else:
            return (UserUtil.format_user(users[0]) )

    def get_users_in_subject(self, subject):
        users = list(self.collection.find({"subject": subject}))
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

    def update_user(self, info: User):
        query = { "email": info.email}
        value = { "subject": info.subject,
                "fullname": info.fullname,
                "position": info.position,
                "date_of_birth": info.date_of_birth,
                "url_avatar": info.url_avatar
                }
        res = self.collection.update_one(query, { "$set": value})
        return res