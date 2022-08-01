from app.models.Result import Result
from app.utils.question_util import QuestionUtil

class ResultUtil:

    def format_result(result) -> Result:
        return Result(
            id=str(result["_id"]),
            user_id=result["user_id"],
            subject_id=result["subject_id"],
            point=result["point"],
            time=result["time"],
            is_pass=result["is_pass"],
            questions=result["questions"],
            created_at = result["created_at"]
        )
    
    def format_result_2(result):
        return {
            "id": str(result["_id"]),
            "user_id": result["user_id"],
            # "student_name": student_name, 
            "subject_id": result["subject_id"],
            "point": result["point"],
            "time": result["time"],
            "is_pass": result["is_pass"],
            "created_at": result["created_at"]
        }
    
    
    