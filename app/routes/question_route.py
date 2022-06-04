from fastapi import APIRouter, Depends
from app.routes.auth_route import oauth2_scheme
from app.services.auth_service import AuthService



router = APIRouter(prefix='/question')

@router.get("/get-all")
async def get_all_question(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass
        # res = 
