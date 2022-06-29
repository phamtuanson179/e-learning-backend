from fastapi import APIRouter, Depends
from app.routes.auth_route import oauth2_scheme
from app.services.auth_service import AuthService
from app.models.Question import QuestionCreate
from app.services.question_service import QuestionService



router = APIRouter(prefix='/question')

@router.get("/get-all")
async def get_all_question(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass
        # res = 

@router.post("/create-ques")
async def create_ques(ques: QuestionCreate, token: str = Depends(oauth2_scheme) ):
    if AuthService().validate_token(token):
        res = QuestionService().create_ques(ques)
        return res