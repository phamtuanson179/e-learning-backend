from app.repositories.SubjectRepo import subjectRepo
from app.models.Subject import Subject
from app.exceptions.RequestException import RequestException


class subjectService:

    def __init__(self):
        self.__name__= "ExamService"
        self.repo = subjectRepo()

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

    def get_subject(self, alias: str):
        try:
            subject = self.repo.get_subject(alias)
        except:
            raise RequestException(message="Get subjects fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        return subject

    def update_subject(self, subject: Subject):
        self.get_subject(subject.alias)
        try:
            self.repo.update_subject(subject)
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
