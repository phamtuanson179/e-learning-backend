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
            answers=result["answers"]
        )
    
    