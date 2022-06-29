from app.repositories import BaseRepo
from app.utils.question_util import QuestionUtil
from app.models.Question import Question
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Body, status

class QuestionRepo(BaseRepo):
    def __init__(self, collection:str="questions")-> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_question(self):
        res = list(self.collection.find({}))
        # print(res)
        list1 = []
        for response in res:
            # print(response)
            # print(SubjectUtil().format_subject(response))
            list1.append(QuestionUtil().format_question(response))
        # list1 = [SubjectUtil().format_subject(response) for response in res]
        # print(list1)
        return list1
    
    #create ques
    def create_question(self, question: Question = Body(...)):
        ques = jsonable_encoder(question)
        new_ques = self.collection.insert_one(ques)
        created_ques = self.collection.find_one({"_id": new_ques.inserted_id})
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_ques)