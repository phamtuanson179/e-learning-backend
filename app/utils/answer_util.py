from app.models.Answer import Answer

class AnswerUtil:
    def format_answer(answer) -> Answer:
        return Answer(
            content = answer["content"],
            is_correct = str(answer["is_correct"]),
            url_file = answer["url_file"]

        )
    
