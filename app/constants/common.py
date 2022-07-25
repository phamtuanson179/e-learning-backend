class ROLE: 
    ADMIN = 'ADMIN' 
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'

class DB:
    URL = 'mongodb://localhost:27017'
    NAME = 'e-learning-app-2'

class AUTH:
    SECRET_KEY = 'elearning_techpro'
    ALGORITHM = 'HS256'
    EXPIRE_MINUTES = 540

class GENERATE_EXAM_TYPE:
    RAMDOM = 'RANDOM'
    ORDER = 'ORDER'

class QUESTION_TYPE:
    ONE_CORRECT_ANSWER = 'ONE_CORRECT_ANSWER'
    TRUE_FALSE_ANSWER = 'TRUE_FALSE_ANSWER'
    MANY_CORRECT_ANSWER = 'MANY_CORRECT_ANSWER'


    