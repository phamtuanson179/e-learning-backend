from app.utils.auth_util import AuthUtil
from app.utils.question_util import QuestionUtil
from app.utils.subject_util import SubjectUtil
from app.repositories.subject_repo import SubjectRepo, UserRepo
from app.models.Question import Question, QuestionUpdate
from app.models.Answer import Answer
from bson.objectid import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import Body
from app.constants.common import ROLE
from app.repositories.subject_repo import SubjectRepo
import random
from . import *

class QuestionRepo(BaseRepo):
    def __init__(self, collection: str="questions") -> None:
        super().__init__()
        self.subjrepo = SubjectRepo()
        self.collection = self.mydb[collection]
        self.subcollection = self.mydb["subjects"]
    
    def create_question(self, question: Question):
        new_ques = jsonable_encoder(question.__dict__)
        res = self.collection.insert_one(new_ques)
        return res

    def get_all_question(self):
        res = list(self.collection.find({}))
        list1 = [QuestionUtil.format_question(response) for response in res]
        return list1
    
    def get_question_for_user(self, token: str):
        data = AuthUtil.decode_token(token)
        username = data['username']
        user = UserRepo().get_user_by_username(username)

        if not user:
            return None
        else:
            list_question = []
            if user.role == ROLE.ADMIN:
                data = self.collection.find({})
                for question in data:
                    list_question.append(QuestionUtil.format_question(question))
            elif user.role == ROLE.TEACHER:  
                for subject_id in user.list_subjects_id:
                    data = self.collection.find({'subject_id':subject_id})
                    for question in data:
                        list_question.append(QuestionUtil.format_question(question))
            else:
                return None
            if not list_question:
                return None
            else:
                return list_question
    
    def get_by_id(self, id: str):
        res = self.collection.find_one({"_id": ObjectId(id)})
        if res is not None:
            return QuestionUtil.format_question(res)
        else:
            return f'Question id {id} not exist'
    
    def update_question(self, id: str, question: QuestionUpdate):
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
        # subj = self.subcollection.find({"id": id_subject})

        list1 = [QuestionUtil.format_question(response) for response in res]
        return list1

    def get_question_random(self, subject_id: str):
        list_questions = list(self.collection.find({"subject_id": subject_id}))
        subject = SubjectRepo().get_subject_by_id(subject_id)
        amount_question = subject.amount_question

        list_format_questions = []
        for question in list_questions:
            question['answers'] = random.sample(question['answers'], 4)
            # return QuestionUtil.format_question(question)
            list_format_questions.append(QuestionUtil.format_question(question))
        list_random_questions = random.sample(list_format_questions, amount_question)
        return list_random_questions
        # return 200
