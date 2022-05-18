from app.repositories.RoomRepo import RoomRepo
from app.models.Room import Room
from app.exceptions.RequestException import RequestException


class RoomService:

    def __init__(self):
        self.__name__= "ExamService"
        self.repo = RoomRepo()

    def create_room(self, new_room: Room):
        try:
            res =  self.repo.create_room(new_room)
        except:
            raise RequestException(message="Create room fail!")
        return "Success"

    def get_all_room(self):
        try:
            rooms = self.repo.get_all_room()
        except:
            raise RequestException(message="Get rooms fail!")
        return rooms

    def get_room(self, alias: str):
        try:
            room = self.repo.get_room(alias)
        except:
            raise RequestException(message="Get rooms fail!")
        if not room:
            raise RequestException(message="Room does not exist!")
        return room

    def update_room(self, room: Room):
        self.get_room(room.alias)
        try:
            self.repo.update_room(room)
        except:
            raise RequestException(message="Update room fail!")
        return "Success"

    def delete_room(self, alias: str):
        try:
            room = self.repo.get_room(alias)
        except:
            raise RequestException(message="Fail!")
        if not room:
            raise RequestException(message="Room does not exist!")
        res = self.repo.delete_room(alias)
        return "Delete success"
