from app.models.Result import Result
from app.utils.QuestionUtil import QuestionUtil

class ResultUtil:

    def format_result(result):
        return {
            "id":str(result["_id"]),
            "user_id":result["user_id"],
            "subject_id":result["subject_id"],
            "point":result["point"],
            "max_point":result["max_point"],
            "is_pass":result["is_pass"],
            "time":result['time'],
            "questions":[QuestionUtil.format_question_2(ques) for ques in result['questions']],
            # duration=result["duration"]
        }

    def format_result_2(result):
        return {
            "id":str(result["_id"]),
            "user_id":result["user_id"],
            "subject_id":result["subject_id"],
            "point":result["point"],
            "max_point":result["max_point"],
            "is_pass":result["is_pass"],
            "time":result['time'],
            # "questions":[QuestionUtil.format_question_2(ques) for ques in result['questions']],
            # duration=result["duration"]
        }
    
    
  