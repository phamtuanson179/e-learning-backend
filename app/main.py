from fastapi import FastAPI
import sys
sys.path.append('''E:\Work\TechSoft\Elearning''')
from app.routes import account_route, exam_route, result_route, subject_route, user_route
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
app.include_router(exam_route.router)
app.include_router(account_route.router)
app.include_router(result_route.router)
app.include_router(subject_route.router)
app.include_router(user_route.router)

app.mount("/assets/image", StaticFiles(directory="assets/image/"), name="static")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World"}
