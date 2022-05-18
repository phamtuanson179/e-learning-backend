from fastapi import APIRouter, Header
from app.services.AuthService import AuthService
from app.services.RoomService import RoomService
from app.models.Room import Room

router = APIRouter(prefix="/room")

@router.get("/get-all-room")
async def get_all_room(token: str = Header(None)):
    if AuthService().validate_token(token):
        res = RoomService().get_all_room()
        return res

@router.get("/get-room")
async def get_exam_history(alias: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = RoomService().get_room(alias)
        return res

@router.post("/create-room")
async def create_room(room: Room, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = RoomService().create_room(room)
        return res

@router.put("/update-room")
async def update_room(room: Room, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = RoomService().update_room(room)
        return res

@router.delete("/delete-room")
async def delete_room(alias: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = RoomService().delete_room(alias)
        return res
