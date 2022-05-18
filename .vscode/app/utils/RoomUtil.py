from app.models.Room import Room

class RoomUtil:

    def format_room(room) -> Room:
        return Room(
            name=room["name"],
            alias=room["alias"],
            description=room["description"]
        )

    