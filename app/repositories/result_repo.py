from app.models.Result import Result
from app.utils.auth_util import AuthUtil
from app.utils.result_util import ResultUtil
from app.utils.subject_util import SubjectUtil

from . import *
from fastapi.encoders import jsonable_encoder
from app.repositories.subject_repo import SubjectRepo, UserRepo
from app.constants.common import ROLE
from bson.objectid import ObjectId



class ResultRepo(BaseRepo):

    def __init__(self, collection: str = "results") -> None:
        super().__init__()
        self.collection = self.mydb[collection]
        self.subcollection = self.mydb["users"]
        self.subjcollection = self.mydb["subjects"]

    def get_result_for_user(self, token):
        data = AuthUtil.decode_token(token)
        username = data['username']
        user = UserRepo().get_user_by_username(username)
        
        if not user:
            return None
        else:
            list_result = []
            if user.role == ROLE.ADMIN:
                data = self.collection.find({})
                for result in data:
                    list_result.append(ResultUtil.format_result(result))
            elif user.role == ROLE.TEACHER:  
                for subject_id in user.list_subjects_id:
                    data = self.collection.find({'subject_id':subject_id})
                    for result in data:
                        list_result.append(ResultUtil.format_result(result))
            else:
                return None
            if not list_result:
                return None
            else:
                return list_result

    def get_exam_history(self, user_id, subject_id):
        res = self.collection.find({"user_id": user_id, "subject_id": subject_id})
        list_result = []
        for result in res:
            list_result.append(ResultUtil.format_result(result))
        return list_result

    def get_full_result_ranking(self, subject_id):
        pipeline = [
            {
                "$match": {
                    "subject_id": subject_id,
                }

            },

            {
                "$sort": {
                    "point": -1,
                    "time": 1,
                    "created_at": 1
                }

            },

            {
                "$group": {
                    "_id": "$user_id", 
                    "user_id": { "$first": "$user_id" }, 
                    "subject_id": { "$first": "$subject_id" }, 
                    'point': {"$max": '$point'}, 
                    "time": { "$first": "$time"},
                    "is_pass": { "$first": "$is_pass"}, 
                    "created_at": {"$first": "$created_at"}
                }
            },
            {
                "$sort": {
                    "point": -1,
                    "time": 1,
                    "created_at": 1
                }

            },

        ]
        res = self.collection.aggregate(pipeline)
        # for result in res:
        #     print(ResultUtil.format_result_2(result))
        list_result = []
        for result in res:
            # student_name = self.subcollection.find_one(result['_id'])
            list_result.append(ResultUtil.format_result_2(result))
        return list_result


    # def get_shortcut_exam_ranking(self, exam_id, user_id):
    #     res = self.collection.aggregate([
    #         {"$match": {"subject_id":  exam_id}},
    #         {"$group": {"_id": '$user_id',"user_id": { "$first": "$user_id" }, "subject_id": { "$first": "$subject_id" }, 'point': {"$max": '$point'}, "time": { "$first": "$time"}, "max_point": { "$first": "$max_point"}, "is_pass": { "$first": "$is_pass"}}},
    #         {"$sort": {'point': -1, 'duration': 1}}
    #     ])
    #     list_res = []
    #     index = 0
    #     user_rank = {}
    #     for result in res:
    #         list_res.append(ResultUtil.format_result_2(result))
    #         if(result["_id"] == user_id):
    #             user_rank.update(ResultUtil.format_result_2(result))
    #             user_rank.update({'rank': str(index+1)})
    #         index += 1
    #     list_result = list_res[:3]
    #     list_result.append(user_rank)
    #     return list_result

    def save_result(self, result: Result):
        converted_result = jsonable_encoder(result.__dict__)
        self.collection.insert_one(converted_result)
        return 'Saved Successfully'
