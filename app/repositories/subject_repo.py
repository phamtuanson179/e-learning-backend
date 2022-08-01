
from app.utils.subject_util import SubjectUtil
from app.repositories.user_repo import UserRepo
from app.models.Subject import Subject, SubjectCreate, SubjectUpdate
from bson.objectid import ObjectId
from app.constants.common import ROLE
from fastapi.encoders import jsonable_encoder
from . import *


class SubjectRepo(BaseRepo):

    def __init__(self, collection: str="subjects") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_subject(self):
        subjects = list(self.collection.find({}))
        formated_subjects = []
        for subject in subjects:
            formated_subjects.append(SubjectUtil.format_subject(subject))
        return formated_subjects

    def get_subject_by_id(self, id: str):
        subject = self.collection.find_one({"_id": ObjectId(id)})
        if not subject:
            return None
        else:
            return SubjectUtil.format_subject(subject)

    def get_subject_for_user(self, token: str):
        subjects = []
        user = UserRepo.get_user_by_token(self, token)
        if user.role == ROLE.ADMIN:
            subjects = self.get_all_subject()

        elif user.role == ROLE.TEACHER or user.role == ROLE.STUDENT:
            for subject_id in user.list_subjects_id:
                subject = self.collection.find_one({"_id": ObjectId(subject_id)})
                subjects.append(SubjectUtil.format_subject(subject))

        if not subjects:
            return None
        else:
            return subjects

    def create_subject(self, subject: SubjectCreate):
        res = self.collection.insert_one(subject.__dict__)
        return res

    def delete_subject(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res

    def update_subject(self, id:str,subject: SubjectUpdate):
        try:
            new_subj = jsonable_encoder(subject)
            res = self.collection.find_one_and_update({"_id": ObjectId(id)},{"$set": new_subj})
            return res
        except Exception as e:
            print(e)
