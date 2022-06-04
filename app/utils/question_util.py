from app.models.question import Question
from app.models.subject import Subject

class QuestionUtil:

    def format_question(question) -> Question:
        return Question(
            id = str(question["_id"]),
            type=question["type"],
            title = question["title"],
            subject=question["subject"],
            url_file=question["url_file"],
            answers=question["answers"]
        )

    