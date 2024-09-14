from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.users.routers import router
from config import settings
from database import engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
)

app.include_router(router, prefix=settings.API_PREFIX)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
