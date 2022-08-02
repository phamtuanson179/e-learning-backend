from app.repositories.subject_repo import SubjectRepo
from app.models.Subject import Subject, SubjectCreate
from app.exceptions.RequestException import RequestException
from app.repositories.user_repo import UserRepo
from app.utils.auth_util import AuthUtil
from app.utils.user_util import UserUtil


class SubjectService:

    def __init__(self):
        self.__name__= "ExamService"
        self.repo = SubjectRepo()

    def create_subject(self, new_subject: SubjectCreate):
        try:
            res =  self.repo.create_subject(new_subject)
        except:
            raise RequestException(message="Create subject fail!")
        return "Success"

    def get_all_subject(self):
        try:
            subjects = self.repo.get_all_subject()
        except:
            raise RequestException(message="Get subjects fail!")
        return subjects

    def get_subject_by_id(self, id: str):
        try:
            subject = self.repo.get_subject_by_id(id)
        except:
            raise RequestException(message="Get subjects fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        return subject

    def get_subject_for_user(self, token: str):
        try:
            subject = self.repo.get_subject_for_user(token)
        except Exception as e:
            print(e)
            raise RequestException(message="Get subjects fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        return subject

    def get_subject_for_me(self, token: str):
        try:
            data = AuthUtil.decode_token(token)
            username = data["username"]
            user = UserRepo().get_user_by_username(username)
            list_subjects=[]
            for subject_id in user.list_subjects_id:
                subject = self.repo.get_subject_by_id(subject_id)
                list_subjects.append(subject)      
        except:
            raise RequestException(message="Get subjects fail!")
        if not list_subjects:
            raise RequestException(message="subject does not exist!")
        return list_subjects

    def update_subject(self,id: str, subject: SubjectCreate):
        try:
            self.repo.update_subject(id,subject)
        except:
            raise RequestException(message="Update subject fail!")
        return "Success"

    def delete_subject(self, id: str):
        try:
            subject = self.repo.get_subject_by_id(id)
        except:
            raise RequestException(message="Fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        res = self.repo.delete_subject(id)
        return "Delete success"
