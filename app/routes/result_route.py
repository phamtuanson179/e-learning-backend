from fastapi import APIRouter, Depends
from app.services.auth_service import AuthService
from app.services.exam_service import ExamService
from app.models.Result import ResultCreate, Result
from app.routes.auth_route import oauth2_scheme
router = APIRouter(prefix = "/result")

@router.post("/save")
async def save_result(result: ResultCreate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().save_result(result)
        return res

@router.get("/get-exam-history")
async def get_exam_history(user_id: str, subject_id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam_history(user_id, subject_id)
        return res

@router.get("/get-full-result-ranking")
async def get_full_exam_ranking(subject_id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_full_result_ranking(subject_id)
        return res

# @router.get("/get-shortcut-exam-ranking")
# async def get_shortcut_exam_ranking(exam_id: str, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         res = ExamService().get_shortcut_exam_ranking(exam_id, token)
#         return res

@router.get("/get-result-for-user")
async def get_result_for_user(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = ExamService().get_result_for_user(token)
        return res