
from app.utils.subject_util import SubjectUtil
from app.models.Subject import Subject
from bson.objectid import ObjectId
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

    def create_subject(self, subject: Subject):
        res = self.collection.insert_one(subject.__dict__)
        return res

    def delete_subject(self, id: str):
        res = self.collection.delete_one({"_id": ObjectId(id)})
        return res

    def update_subject(self, id:str,subject: Subject):
        # print(id,subject)
        res = self.collection.find_one_and_update({"_id": ObjectId(id)},{"$set": subject.__dict__})
        return res
