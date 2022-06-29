import pymongo
from app.constants.type import DB
class BaseRepo:
    def __init__(self):
        self.myclient = pymongo.MongoClient(DB.URL)
        self.mydb = self.myclient[DB.NAME]
    #ket noi db o local
    # First step: create new db (db can co du lieu moi tao dc)
        # self.collection = self.mydb["users"]
        # mydict = {"email": "test@gmail.com", "password": "admin", "role": "SUPER_ADMIN", "subject": None, "fullname": "Test User", "dob": "01-01-1999", "url_avatar": "", "token": "", "username": "admin","subject": "",}
        # x = self.collection.insert_one(mydict)

    
    
    
    
    #print list db
        # print(self.myclient['e-learning-app'].list_collection_names())
    
    #delete db
        # self.myclient.drop_database("techpro_elearning")
