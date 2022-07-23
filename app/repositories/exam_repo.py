from app.configs.Config import ProjectConfig
from app.utils.time_util import TimeUtil
from app.utils.common_util import CommonUtil
from . import *
from app.exceptions.RequestException import RequestException


class ExamRepo(BaseRepo):

    def __init__(self, collection: str="exams") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_exam(self, exam):
        pass

    def delete_exam(self, id: str):
        res = self.collection.delete_one({"id" : id})
        return res

    def get_exam(self, id: str):
        pass

    def get_exams_for_subject(self, subject):
        pass

    def update_exam(self, exam):
        pass