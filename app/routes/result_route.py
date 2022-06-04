from app.models.result import Result, ResultCreate
from app.models.user import User
from app.routes.auth_route import oauth2_scheme
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, File, Header, UploadFile
from fastapi.staticfiles import StaticFiles

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

# @router.post("/save_result")
# async def save_result(result: ResultCreate, token: str = Header(None)):
#     if AuthService().validate_token(token):
#         res = ExamService().save_result(result, token)
#         return res

