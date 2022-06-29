from fastapi import APIRouter, Depends
from app.services.auth_service import AuthService
from app.services.subject_service import SubjectService
from app.models.Subject import  SubjectCreate, UpdateSubjectModel
from app.routes.auth_route import oauth2_scheme
from fastapi import Body

router = APIRouter(prefix='/subject')

@router.get("/get-all")
async def get_all_subject(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().get_all_subject()
        return res

@router.get("/get-subject-by-id/")
async def get_exam_history(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        # print('sTEP1')
        res = SubjectService().get_subject(id)
        return res

@router.post("/create")
async def create_subject(subject: SubjectCreate = Body(...), token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().create_subject(subject)
        return res

@router.put('/update', response_model=SubjectCreate)
async def update_subject(id: str, subject: UpdateSubjectModel = Body(...), token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        print('Test1')
        res = SubjectService().update_subject(id,subject)
        return res

@router.delete("/delete")
async def delete_subject(id: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        res = SubjectService().delete_subject(id)
        return res
