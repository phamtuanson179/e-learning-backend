from app.models.Result import Result
from app.utils.result_util import ResultUtil
from . import *
from fastapi.encoders import jsonable_encoder


class ResultRepo(BaseRepo):

    def __init__(self, collection: str = "results") -> None:
        super().__init__()
        self.collection = self.mydb[collection]
        self.subcollection = self.mydb["users"]

    def get_exam_history(self, user_id, subject_id):
        res = self.collection.find({"user_id": user_id, "subject_id": subject_id})
        print(res)
        list_result = []
        for result in res:
            list_result.append(ResultUtil.format_result(result))
        return list_result

    def get_full_exam_ranking(self, subject_id):
        res = self.collection.aggregate([
            {"$match": {"subject_id":  subject_id}},
            {"$group": {"_id": '$user_id',"user_id": { "$first": "$user_id" }, "subject_id": { "$first": "$subject_id" }, 'point': {"$max": '$point'}, "time": { "$first": "$time"}, "max_point": { "$first": "$max_point"}, "is_pass": { "$first": "$is_pass"}}},
            {"$sort": {'point': -1, 'time': 1}}
        ])
        # res = jsonable_encoder(res.__dict__)
        list_result = []
        # print(res.__dict__)
        for result in res:
            # print(res)
            list_result.append(ResultUtil.format_result_2(result))
        return list_result

    def get_shortcut_exam_ranking(self, exam_id, user_id):
        res = self.collection.aggregate([
            {"$match": {"subject_id":  exam_id}},
            {"$group": {"_id": '$user_id',"user_id": { "$first": "$user_id" }, "subject_id": { "$first": "$subject_id" }, 'point': {"$max": '$point'}, "time": { "$first": "$time"}, "max_point": { "$first": "$max_point"}, "is_pass": { "$first": "$is_pass"}}},
            {"$sort": {'point': -1, 'duration': 1}}
        ])
        list_res = []
        index = 0
        user_rank = {}
        for result in res:
            list_res.append(ResultUtil.format_result_2(result))
            if(result["_id"] == user_id):
                user_rank.update(ResultUtil.format_result_2(result))
                user_rank.update({'rank': str(index+1)})
                # print(user_rank)
                # print(user_rank['rank'])
            index += 1
        list_result = list_res[:3]
        list_result.append(user_rank)
        return list_result

    def save_result(self, testResult: Result):
        saveResult = jsonable_encoder(testResult.__dict__)
        res = self.collection.insert_one(saveResult)
        return 'Saved Successfully'
