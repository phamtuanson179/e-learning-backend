import imp
import pymongo
from app.configs.Config import DBConfig
import certifi
class BaseRepo:
    def __init__(self):
        self.myclient = pymongo.MongoClient(DBConfig.DB_URL,tlsCAFile=certifi.where())
        self.mydb = self.myclient[DBConfig.DB_NAME]
        # print("aaaaaaaaaaaaa", self.myclient.server_info())

    #ket noi db o local
    #First step: create new db (db can co du lieu moi tao dc)
        # self.collection = self.mydb["users"]
        # mydict = {"email": "test@gmail.com", "password": "123", "role": 0, "room": "AI", "fullname": "Test User", "position": "Frontend Developer", "date_of_birth": "01-01-1999", "url_avatar": "", "token": ""}
        # mydict1 = {"email": "test1@gmail.com", "password": "123", "role": 0, "room": "AI", "fullname": "Test User 1", "position": "Backend Developer", "date_of_birth": "02-03-2001", "url_avatar": "", "token": ""}
        # x = self.collection.insert_one(mydict)
        # x = self.collection.insert_one(mydict1)

    #print list db
        # print(self.myclient.list_database_names())\
    
    #delete db
        # self.myclient.drop_database("techpro_elearning")
