
from app.routes.auth_route import oauth2_scheme
from app.services.auth_service import AuthService
from app.services.exam_service import ExamService
from fastapi import APIRouter, Depends
from fastapi.staticfiles import StaticFiles

router = APIRouter(prefix = "/exam")
@router.get("/get-exam-by-id")
async def get_exam(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam(id)
        return res

@router.get("/get-exam-by-subject")
async def get_exams_for_subject(subject: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_exams_for_subject(subject)
        return res
