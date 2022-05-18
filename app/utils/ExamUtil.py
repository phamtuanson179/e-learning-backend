from app.models.Exam import Exam

class ExamUtil:

    def format_exam(exam) -> Exam:
        return Exam(
            id=exam["id"],
            name=exam["name"],
            min_point_to_pass=exam["min_point_to_pass"],
            duration=exam["duration"],
            created_by=exam["created_by"],
            image=exam["image"],
            require_rooms=exam["require_rooms"],
            questions=exam["questions"]
        )
