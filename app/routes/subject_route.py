from fastapi import APIRouter, Depends, Header
from app.services.auth_service import AuthService
from app.services.subject_service import SubjectService
from app.models.Subject import Subject
from app.routes.auth_route import oauth2_scheme

router = APIRouter(prefix="/subject")

@router.get("/get-all")
async def get_all_subject(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().get_all_subject()
        return res

@router.get("/get-by-id")
async def get_exam_history(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().get_subject_by_id(id)
        return res

@router.post("/create")
async def create_subject(subject: Subject, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().create_subject(subject)
        return res

@router.put("/update")
async def update_subject(id: str, subject: Subject, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().update_subject(id,subject)
        return res

@router.delete("/delete")
async def delete_subject(alias: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().delete_subject(alias)
        return res
