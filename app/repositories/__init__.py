import pymongo
from app.configs.Config import DBConfig
class BaseRepo:
    def __init__(self):
        self.myclient = pymongo.MongoClient(DBConfig.DB_URL)
        self.mydb = self.myclient[DBConfig.DB_NAME]
    #ket noi db o local
    # First step: create new db (db can co du lieu moi tao dc)
        # self.collection = self.mydb["users"]
        # mydict = {"email": "test@gmail.com", "password": "123", "role": 2, "subject": "AI", "fullname": "Test User", "date_of_birth": "01-01-1999", "url_avatar": "", "token": "", "username": "admin","subject": "",}
        # x = self.collection.insert_one(mydict)

    #print list db
        # print(self.myclient['e-learning-app'].list_collection_names())\
    
    #delete db
        # self.myclient.drop_database("techpro_elearning")
