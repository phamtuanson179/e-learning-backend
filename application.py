import uvicorn
from app.services.user_service import UserService

if __name__ == "__main__":
    # new_user = {
    #     "username": "admin",
    #     "password": "admin",
    #     "email": "admin@gmail.com",
    #     "role": "ADMIN",
    #     "fullname": "admin",
    #     "dob": "11/01/2011",
    #     "list_subjects_id": [],
    #     "avatar": 'string',

    # }
    # new_user = UserService().create_user(new_user)


    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)

