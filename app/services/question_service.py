from app.repositories import subject_repo


class questionService: 
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = subject_repo()