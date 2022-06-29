from app.repositories.subject_repo import SubjectRepo
from app.models.Subject import SubjectCreate, UpdateSubjectModel
from app.exceptions.RequestException import RequestException
from fastapi import Body 

class SubjectService:

    def __init__(self):
        self.__name__= "ExamService"
        self.repo = SubjectRepo()

    def create_subject(self, new_subject: SubjectCreate = Body(...)):
        try:
            res =  self.repo.create_subject(new_subject)
            return res
        except:
            raise RequestException(message="Create subject fail!")
        return "Success"
        # return res

    def get_all_subject(self):
        try:
            subjects = self.repo.get_all_subject()
        except:
            raise RequestException(message="Get subjects fail!")
        return subjects

    def get_subject(self, id: str):
        try:
            subject = self.repo.get_subject(id)
        except:
            raise RequestException(message="Get subjects fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        return subject

    def update_subject(self,id:str, subject: UpdateSubjectModel = Body(...)):
        try:
            res = self.repo.update_subject(id, subject)
            return res
        except:
            raise RequestException(message="Update subject fail!")
        return "Success"

    def delete_subject(self, id: str):
        try:
            subject = self.repo.get_subject(id)
        except:
            raise RequestException(message="Fail!")
        if not subject:
            raise RequestException(message="subject does not exist!")
        res = self.repo.delete_subject(id)
        return "Delete success"
