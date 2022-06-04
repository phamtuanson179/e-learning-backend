from app.models.subject import Subject

class SubjectUtil:

    def format_subject(subject) -> Subject:
        return Subject(
            id = str(subject["_id"]),
            name=subject["name"],
            alias=subject["alias"],
            description=subject["description"], 
            time=subject['time'],
            amount_question=subject["amount_question"],
            min_correct_question_to_pass=subject["min_correct_question_to_pass"],
            generate_exam_type=subject["generate_exam_type"]
        )

    