from hashlib import new
import starlette.status
import jwt
from app.repositories.ExamRepo import ExamRepo
from app.repositories.ResultRepo import ResultRepo
from app.models.Exam import Exam, NewExam
from app.models.Result import Result, NewResult, FullResult
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

    def create_exam(self, new_exam: NewExam, token):
        payload = jwt.decode(token, AuthConfig.SECRET_KEY, algorithms=AuthConfig.ALGORITHM)
        email: str = payload.get("email")
        exam = Exam(name=new_exam.name, 
                    min_point_to_pass=new_exam.min_point_to_pass,
                    duration=new_exam.duration,
                    require_rooms=new_exam.require_rooms,
                    image=new_exam.image,
                    questions=new_exam.questions,
                    created_by=email)
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

    def get_exams_for_room(self, room: str):
        list_exams = self.repo.get_exams_for_room(room)
        return list_exams

    def get_exam_history(self, user_id: str, exam_id: str):
        list_history = ResultRepo().get_exam_history(user_id, exam_id)
        return list_history

    def get_full_exam_ranking(self, exam_id: str):
        list_result = ResultRepo().get_full_exam_ranking(exam_id)
        return list_result

    def get_shortcut_exam_ranking(self, exam_id: str, token: str):
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["email"])
        list_result = ResultRepo().get_shortcut_exam_ranking(exam_id, user.user_id)
        return list_result

    def save_result(self, new_result: NewResult, token: str):
        exam = ExamRepo().get_exam(new_result.exam_id)
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["email"])

        test_result = FullResult(user_id=user.user_id, 
                                exam_id=new_result.exam_id, 
                                point=new_result.point, 
                                max_point=len(exam.questions)*10, 
                                is_pass=new_result.is_pass, 
                                duration=new_result.duration,
                                user_name=user.fullname,
                                create_at=TimeUtil.get_timestamp_now())
        res =  ResultRepo().save_result(test_result)
        return "Save result success"

    def save_img(self, new_result: NewResult, token: str):
        exam = ExamRepo().get_exam(new_result.exam_id)
        data = AuthUtil.decode_token(token)
        user = UserService().get_user(data["email"])

        test_result = FullResult(user_id=user.user_id, 
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