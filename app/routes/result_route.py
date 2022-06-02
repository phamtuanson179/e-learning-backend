from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Depends, Header, File, UploadFile
from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import User
from app.services.ExamService import ExamService
from app.models.User import User
from app.models.Result import Result, ResultCreate
from app.routes.account_route import oauth2_scheme

router = APIRouter(prefix='/result')



# @router.get("/history")
# async def get_exam_history(user_id: str, exam_id: str, token: str = Depends(oauth2_scheme)):
#     if AuthService().validate_token(token):
#         res = ExamService().get_exam_history(user_id, exam_id)
#         return res

# @router.get("/ranking/full")
# async def get_full_exam_ranking(exam_id: str, token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = ExamService().get_full_exam_ranking(exam_id)
#         return res

# @router.get("/ranking/summary")
# async def get_summary_exam_ranking(exam_id: str, token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = ExamService().get_summary_exam_ranking(exam_id, token)
#         return res

@router.post("/save_result")
async def save_result(result: ResultCreate, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().save_result(result, token)
        return res

