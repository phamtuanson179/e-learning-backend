from hashlib import new
import jwt
from app.repositories.ExamRepo import ExamRepo
from app.repositories.ResultRepo import ResultRepo
from app.models.Exam import Exam, ExamCreate
from app.models.Result import Result
from app.models.Exam import  ExamCreate

from app.exceptions.CredentialException import CredentialException
from app.exceptions.RequestException import RequestException
from app.configs.Config import AuthConfig
from app.utils.AuthUtil import AuthUtil
from app.utils.TimeUtil import TimeUtil
from app.services.UserService import UserService

class ExamService:
    
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = ExamRepo()

    def create_exam(self, exam_created: ExamCreate, token):
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        username: str = payload.get("username")
        exam = Exam(name=exam_created.name, 
                    min_point_to_pass=exam_created.min_point_to_pass,
                    duration=exam_created.duration,
                    require_subjects=exam_created.require_subjects,
                    image=exam_created.image,
                    questions=exam_created.questions,
                    created_by=username)
        res =  ExamRepo().create_exam(exam)
        return "Create exam success"

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

    def get_exam_history(self, user_id: str, exam_id: str):
        list_history = ResultRepo().get_exam_history(user_id, exam_id)
        return list_history

    def get_full_exam_ranking(self, exam_id: str):
        list_result = ResultRepo().get_full_exam_ranking(exam_id)
        return list_result

    def get_summary_exam_ranking(self, exam_id: str, token: str):
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["username"])
        list_result = ResultRepo().get_summary_exam_ranking(exam_id, user.user_id)
        return list_result

    def save_result(self, new_result: ExamCreate, token: str):
        exam = ExamRepo().get_exam(new_result.exam_id)
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["username"])

        test_result = Result(user_id=user.user_id, 
                                exam_id=new_result.exam_id, 
                                point=new_result.point, 
                                max_point=len(exam.questions)*10, 
                                is_pass=new_result.is_pass, 
                                duration=new_result.duration,
                                user_name=user.fullname,
                                create_at=TimeUtil.get_timestamp_now())
        res =  ResultRepo().save_result(test_result)
        return "Save result success"

    def save_img(self, new_result: ExamCreate, token: str):
        exam = ExamRepo().get_exam(new_result.exam_id)
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["username"])

        test_result = Result(user_id=user.user_id, 
                                exam_id=new_result.exam_id, 
                                point=new_result.point, 
                                max_point=len(exam.questions)*10, 
                                is_pass=new_result.is_pass, 
                                duration=new_result.duration,
                                user_name=user.fullname,
                                create_at=TimeUtil.get_timestamp_now())
        res =  ResultRepo().save_result(test_result)
        return "Save result success"

    def update_exam(self, exam: Exam):
        self.get_exam(exam.id)
        try:
            self.repo.update_exam(exam)
        except:
            raise RequestException(message="Update fail!")
        return "Success"