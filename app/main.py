from fastapi import FastAPI
from app.routes.auth import auth_router
from app.routes.user import user_router
from app.routes.student import student_router
from app.routes.student_progress import progress_router
from app.routes.result import result_router
from app.routes.exam import exam_router
from app.routes.upload import upload_router
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.utils.db import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")
    create_db_and_tables()
    print("Table created")
    try:
        yield
    finally:
        print("Lifespan context ended")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # allows all methods, adjust as needed
    allow_headers=["*"],  # allows all headers, adjust as needed
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(student_router)
app.include_router(progress_router)
app.include_router(result_router)
app.include_router(exam_router)
app.include_router(upload_router)

@app.get("/")
async def index():
    return {"message": "Welcome to Examinie AI API!"}