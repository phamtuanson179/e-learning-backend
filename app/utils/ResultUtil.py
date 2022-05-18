from app.models.Result import Result, FullResult

class ResultUtil:

    def format_result(result) -> Result:
        return Result(
            id=str(result["_id"]),
            user_id=result["user_id"],
            exam_id=result["exam_id"],
            point=result["point"],
            max_point=result["max_point"],
            user_name=result["user_name"],
            is_pass=result["is_pass"],
            duration=result["duration"]
        )
    
    def format_full_result(result) -> FullResult:
        return FullResult(
            id=str(result["_id"]),
            user_id=result["user_id"],
            exam_id=result["exam_id"],
            point=result["point"],
            max_point=result["max_point"],
            user_name=result["user_name"],
            is_pass=result["is_pass"],
            duration=result["duration"],
            create_at=result["create_at"]
        )