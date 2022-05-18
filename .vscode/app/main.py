from fastapi import FastAPI
import sys
sys.path.append('''E:\Work\TechSoft\Elearning''')
from app.routes import AuthRoute, UserRoute, AdminRoute, RoomRoute
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.include_router(AdminRoute.router)
app.include_router(AuthRoute.router)
app.include_router(UserRoute.router)
app.include_router(RoomRoute.router)

app.mount("/assets/image", StaticFiles(directory="assets/image/"), name="static")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World"}
