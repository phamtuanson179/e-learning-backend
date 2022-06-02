from fastapi import APIRouter, Depends, Header
from app.services.AuthService import AuthService
from app.services.SubjectService import subjectService
from app.models.Subject import Subject, SubjectCreate
from app.routes.account_route import oauth2_scheme

router = APIRouter(prefix='/subject')

@router.get("/get-all")
async def get_all_subject(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = subjectService().get_all_subject()
        return res

@router.get("/get-subject-by-id")
async def get_exam_history(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = subjectService().get_subject(id)
        return res

@router.post("/create")
async def create_subject(subject: SubjectCreate, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = subjectService().create_subject(subject)
        return res

@router.put("/update")
async def update_subject(subject: Subject, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = subjectService().update_subject(subject)
        return res

@router.delete("/delete")
async def delete_subject(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = subjectService().delete_subject(id)
        return res
