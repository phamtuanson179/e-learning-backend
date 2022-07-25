from hashlib import new
from app.repositories.exam_repo import ExamRepo
from app.repositories.result_repo import ResultRepo
from app.models.Result import Result
from app.exceptions.RequestException import RequestException
from app.utils.auth_util import AuthUtil
from app.utils.time_util import TimeUtil
from app.services.user_service import UserService

class ExamService:
    
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = ExamRepo()

    def create_exam(self, new_exam, token):
        pass

    def delete_exam(self, id: str):
        if self.get_exam(id):
            res = ExamRepo().delete_exam(id)
            return "Delete success"

    def get_exam(self, id: str):
        _u = ExamRepo().get_exam(id)
        if not _u:
            raise RequestException(message= "Exam not exists")
        return _u

    def get_exams_for_subject(self, subject: str):
        list_exams = self.repo.get_exams_for_subject(subject)
        return list_exams

    def get_exam_history(self, user_id: str, subject_id: str):
        list_history = ResultRepo().get_exam_history(user_id, subject_id)
        return list_history

    def get_full_exam_ranking(self, exam_id: str):
        list_result = ResultRepo().get_full_exam_ranking(exam_id)
        return list_result

    def get_shortcut_exam_ranking(self, exam_id: str, token: str):
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["username"])
        list_result = ResultRepo().get_shortcut_exam_ranking(exam_id, user.id)
        return list_result

    def save_result(self, new_result: Result):
        try:
            ResultRepo().save_result(new_result)
            return "Save result success"
        except Exception as e:
            print(e)
            raise RequestException(message="save results fail")
    
    def get_exam_for_user(self, token: str):
        try:
            res = ResultRepo().get_exam_for_user(token)
            return res
        except Exception as e:
            print(e)
            raise RequestException(message="get results fail")

    def update_exam(self, exam):
        pass