from app.repositories.subject_repo import SubjectRepo
from app.models.Subject import Subject
from app.exceptions.RequestException import RequestException


class SubjectService:

    def __init__(self):
        self.__name__= "ExamService"
        self.repo = SubjectRepo()

    def create_subject(self, new_subject: Subject):
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

    def update_subject(self,id: str, subject: Subject):
        try:
            self.repo.update_subject(id,subject)
        except:
            raise RequestException(message="Update subject fail!")
        return "Success"

    def delete_subject(self, alias: str):
        try:
            subject = self.repo.get_subject(alias)
        except:
            raise RequestException(message="Fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        res = self.repo.delete_subject(alias)
        return "Delete success"
