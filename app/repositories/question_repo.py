from app.repositories import BaseRepo
from app.utils.question_util import QuestionUtil


class QuestionRepo(BaseRepo):
    def __init__(self, collection:str="questions")-> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_question(self):
        questions = list(self.collection.find({}))
        list_questions = []
        for record in questions:
            list_questions.append(QuestionUtil.format_question(record))