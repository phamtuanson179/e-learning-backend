from app.repositories import question_repo
from app.models.Question import QuestionCreate


class QuestionService: 
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = question_repo.QuestionRepo()

    def create_ques(self, new_ques: QuestionCreate):
        res = self.repo.create_question(new_ques)
        return res