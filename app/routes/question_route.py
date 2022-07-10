from fastapi import APIRouter, Depends, Header
from app.services.auth_service import AuthService
from app.services.question_service import QuestionService
from app.models.Question import Question
from app.routes.auth_route import oauth2_scheme

router = APIRouter(prefix="/question")

@router.get("/get-all")
async def get_all_question(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().get_all_question()
        return res 

@router.get("/get-by-id")
async def get_exam_history(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().get_question_by_id(id)
        return res

@router.get("/get_by_id_subject")
async def get_exam_history(id_subject: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().get_question_by_id_subject(id_subject)
        return res

@router.post("/create")
async def create_question(question: Question, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        # print(123)
        res = QuestionService().create_question(question)
        return res


@router.put("/update")
async def update_question(id:str, question: Question, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().update_question(id, question)
        return res

@router.delete("/delete")
async def delete_question(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().delete_question(id)
        return res


