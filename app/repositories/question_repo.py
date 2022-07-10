from app.utils.QuestionUtil import QuestionUtil
from app.models.Question import Question
from app.models.Answer import Answer
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Body
from . import *

class QuestionRepo(BaseRepo):
    def __init__(self, collection: str="questions") -> None:
        super().__init__()
        self.collection = self.mydb[collection]
    
    def create_question(self, question: Question):
            new_ques = jsonable_encoder(question.__dict__)
            res = self.collection.insert_one(new_ques)

            return res
    
    def get_all_question(self):
        res = list(self.collection.find({}))
        list1 = [QuestionUtil.format_question(response) for response in res]
        return list1
    
    def get_by_id(self, id: str):
        res = self.collection.find_one({"_id": ObjectId(id)})
        if res is not None:
            return QuestionUtil.format_question(res)
        else:
            return f'Question id {id} not exist'
    
    def update_question(self, id: str, question: Question):
        try:
            new_ques = jsonable_encoder(question.__dict__)
            res = self.collection.find_one_and_update({"_id": ObjectId(id)},{"$set": new_ques})
            return res
        except Exception as e:
            print(e)
        
    def delete_question(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res
    
    def get_question_by_subject(self, id_subject: str):
        res = list(self.collection.find({"subject_id": id_subject}))
        list1 = [QuestionUtil.format_question(response) for response in res]
        return list1
