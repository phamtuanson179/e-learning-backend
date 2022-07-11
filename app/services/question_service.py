from app.repositories.question_repo import QuestionRepo
from app.models.Question import Question
from app.exceptions.RequestException import RequestException

class QuestionService:
    def __init__(self):
        self.__name__ = 'QuestionService'
        self.repo = QuestionRepo()
    
    def create_question(self, question: Question):
        try: 
            res = self.repo.create_question(question)
        except: 
            raise RequestException(message="Create Question failed")
        return "Success"
        
    def get_all_question(self):
        try: 
            res = self.repo.get_all_question()
            return res
        except: 
            raise RequestException(message="get question failed")
        
    def get_question_by_id(self, id: str):
        try: 
            res = self.repo.get_by_id(id)
            return res
        except: 
            raise RequestException(message="get question failed")
        
    def update_question(self, id: str, question: Question):
        try:
            self.repo.update_question(id,question)
        except:
            raise RequestException(message="Update question fail!")
        return "Success"

    def delete_question(self, id: str):
        try:
            question = self.repo.get_by_id(id)
        except:
            raise RequestException(message="Fail!")
        if not question:
            raise RequestException(message="question does not exist!")
        res = self.repo.delete_question(id)
        return "Delete success"
    
    def get_question_by_id_subject(self, id_subject: str):
        try: 
            res = self.repo.get_question_by_subject(id_subject)
            return res
        except: 
            raise RequestException(message="get question failed")
        
    def get_question_random(self, id_subject: str):
        try: 
            res = self.repo.get_question_random(id_subject)
            return res
        except: 
            raise RequestException(message="get question failed")