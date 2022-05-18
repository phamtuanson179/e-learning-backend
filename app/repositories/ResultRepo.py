from app.models.Result import Result
from app.utils.ResultUtil import ResultUtil
from . import *


class ResultRepo(BaseRepo):

    def __init__(self, collection: str = "results") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_exam_history(self, user_id, exam_id):
        res = self.collection.find({"user_id": user_id, "exam_id": exam_id})
        list_result = []
        for result in res:
            list_result.append(ResultUtil.format_result(result))
        return list_result

    def get_full_exam_ranking(self, exam_id):
        res = self.collection.aggregate([
            {"$match": {"exam_id":  exam_id}},
            {"$group": {"_id": '$user_id',"user_id": { "$first": "$user_id" }, "exam_id": { "$first": "$exam_id" }, 'point': {"$max": '$point'}, "duration": { "$first": "$duration"}, "max_point": { "$first": "$max_point"}, "is_pass": { "$first": "$is_pass"}, "user_name": { "$first": "$user_name"}}},
            {"$sort": {'point': -1, 'duration': 1}}
        ])
        list_result = []
        for result in res:
            list_result.append(ResultUtil.format_result(result))
        return list_result

    def get_shortcut_exam_ranking(self, exam_id, user_id):
        res = self.collection.aggregate([
            {"$match": {"exam_id":  exam_id}},
            {"$group": {"_id": '$user_id',"user_id": { "$first": "$user_id" }, "exam_id": { "$first": "$exam_id" }, 'point': {"$max": '$point'}, "duration": { "$first": "$duration"}, "max_point": { "$first": "$max_point"}, "is_pass": { "$first": "$is_pass"}, "user_name": { "$first": "$user_name"}}},
            {"$sort": {'point': -1, 'duration': 1}}
        ])
        list_res = []
        index = 0
        user_rank = {}
        for result in res:
            list_res.append(ResultUtil.format_result(result))
            if(result["user_id"] == user_id):
                user_rank.update(ResultUtil.format_result(result))
                user_rank.update({"rank": index+1})
            index += 1
        list_result = list_res[:3]
        list_result.append(user_rank)
        return list_result

    def save_result(self, testResult: Result):
        res = self.collection.insert_one(testResult.__dict__)
        return res
