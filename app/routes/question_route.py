from fastapi import APIRouter, Depends
from app.routes.auth_route import oauth2_scheme
from app.services.auth_service import AuthService
from app.models.Question import Question
from app.services.question_service import QuestionService
from fastapi import Body



router = APIRouter(prefix='/question')

@router.get("/get-all")
async def get_all_question(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = QuestionService().get_all_question()
        return res
        # res = 

@router.post("/create-ques")
async def create_ques(ques: Question = Body(...), token: str = Depends(oauth2_scheme) ):
    if AuthService().validate_token(token):
        res = QuestionService().create_ques(ques)
        return res