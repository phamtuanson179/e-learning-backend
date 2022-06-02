
from app.utils.SubjectUtil import SubjectUtil
from app.models.Subject import Subject
from . import *


class subjectRepo(BaseRepo):

    def __init__(self, collection: str="subjects") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_subject(self):
        subjects = list(self.collection.find({}))
        print ('subject', subjects)
        list_subjects = []
        for record in subjects:
            print(record)
            list_subjects.append(SubjectUtil.format_subject(record))
        return list_subjects

    def get_subject(self, alias: str):
        subjects = list(self.collection.find({"alias": alias}))
        count = 0
        for record in subjects:
            count += 1
        if count < 1:
            return None
        else:
            return SubjectUtil.format_subject(subjects[0])

    def create_subject(self, subject: Subject):
        res = self.collection.insert_one(subject.__dict__)
        return res

    def delete_subject(self, alias: str):
        res = self.collection.delete_one({"alias": alias})
        return res

    def update_subject(self, info: Subject):
        query = {"alias": info.alias,}
        value = {"name": info.name,
                "alias": info.alias,
                "description": info.description
                }
        res = self.collection.update_one(query, { "$set": value})
        return res
