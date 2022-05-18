
from app.utils.RoomUtil import RoomUtil
from app.models.Room import Room
from .__init__ import *


class RoomRepo(BaseRepo):

    def __init__(self, collection: str="rooms") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_all_room(self):
        rooms = list(self.collection.find({}))
        list_rooms = []
        for record in rooms:
            list_rooms.append(RoomUtil.format_room(record))
        return list_rooms

    def get_room(self, alias: str):
        rooms = list(self.collection.find({"alias": alias}))
        count = 0
        for record in rooms:
            count += 1
        if count < 1:
            return None
        else:
            return RoomUtil.format_room(rooms[0])

    def create_room(self, room: Room):
        res = self.collection.insert_one(room.__dict__)
        return res

    def delete_room(self, alias: str):
        res = self.collection.delete_one({"alias": alias})
        return res

    def update_room(self, info: Room):
        query = {"alias": info.alias,}
        value = {"name": info.name,
                "alias": info.alias,
                "description": info.description
                }
        res = self.collection.update_one(query, { "$set": value})
        return res
