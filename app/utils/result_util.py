from app.models.result import Result

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
            time=result["time"],
            create_at=result["create_at"]

        )
    
  