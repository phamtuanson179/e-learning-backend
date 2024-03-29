from app.models.Question import Question
from app.models.Answer import Answer
from app.utils.answer_util import AnswerUtil

class QuestionUtil:
    def format_question(question) -> Question:
        return Question(
            id=str(question['_id']),
            type=str(question['type']),
            title=question['title'],
            subject_id = question['subject_id'],
            url_file = question['url_file'],
            answers = [AnswerUtil.format_answer(answer) for answer in question['answers']]

        )

    def format_question_for_update(question):
        if hasattr(question, 'id'):
            delattr(question,'id')
        return question

