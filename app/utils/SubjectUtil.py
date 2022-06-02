from app.models.Subject import Subject

class SubjectUtil:

    def format_subject(subject) -> Subject:
        return Subject(
            id = str(subject["_id"]),
            name=subject["name"],
            alias=subject["alias"],
            description=subject["description"],    
        )

    