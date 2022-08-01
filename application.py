import uvicorn
from app.services.user_service import UserService
from app.models.User import UserCreate

if __name__ == "__main__":
    # new_user = UserCreate(username="admin", password="admin", email="admin@example.com",role="ADMIN", fullname="admin", dob=1, list_subjects_id=[], avatar="string", token="string")
    # new_user = UserService().create_user(new_user)


    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)

