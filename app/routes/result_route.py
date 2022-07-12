from fastapi import APIRouter, Depends
from app.services.auth_service import AuthService
from app.services.exam_service import ExamService
from app.models.Result import ResultCreate, Result
from app.routes.auth_route import oauth2_scheme
router = APIRouter(prefix = "/result")

@router.post("/save-result")
async def save_result(result: Result, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().save_result(result, token)
        return res

@router.get("/get_exam_history")
async def get_exam_history(user_id: str, subject_id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam_history(user_id, subject_id)
        return res

@router.get("/get-full-exam-ranking")
async def get_full_exam_ranking(exam_id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_full_exam_ranking(exam_id)
        return res

@router.get("/get-shortcut-exam-ranking")
async def get_shortcut_exam_ranking(exam_id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_shortcut_exam_ranking(exam_id, token)
        return res