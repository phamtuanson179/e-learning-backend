from app.repositories import question_repo
from app.models.Question import Question
from fastapi import Body


class QuestionService: 
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = question_repo.QuestionRepo()

    def create_ques(self, new_ques: Question = Body(...)):
        res = self.repo.create_question(new_ques)
        return res
    
    def get_all_question(self):
        res = self.repo.get_all_question()
        return res