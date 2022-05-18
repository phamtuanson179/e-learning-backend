from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter, Header, File, UploadFile
from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import User
from app.services.ExamService import ExamService
from app.models.User import User
from app.models.Result import NewResult

router = APIRouter()

@router.get("/get_exam")
async def get_exam(id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam(id)
        return res

@router.get("/get_exam_history")
async def get_exam_history(user_id: str, exam_id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam_history(user_id, exam_id)
        return res

@router.get("/get-full-exam-ranking")
async def get_full_exam_ranking(exam_id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_full_exam_ranking(exam_id)
        return res

@router.get("/get-shortcut-exam-ranking")
async def get_shortcut_exam_ranking(exam_id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_shortcut_exam_ranking(exam_id, token)
        return res

@router.get("/get_exams_for_room")
async def get_exams_for_room(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exams_for_room(room)
        return res

@router.get("/get_user")
async def get_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().get_user(email)
        return res

@router.post("/save_result")
async def save_result(result: NewResult, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().save_result(result, token)
        return res

@router.put("/update_user")
async def update_user(info: User, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().update_user(info, token)
        return res

@router.post("/upload-file/")
async def upload_file(file: UploadFile=File(...), token: str = Header(None)):
    if AuthService().validate_token(token):
        res = await UserService().upload_file(file)
        return res

@router.get("/get-file/")
async def get_file(url_file: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().get_file(url_file)
        return res

@router.put("/update-file/")
async def update_file(url_old_file: str, file: UploadFile=File(...), token: str = Header(None)):
    if AuthService().validate_token(token):
        res = await UserService().update_file(url_old_file, file)
        return res