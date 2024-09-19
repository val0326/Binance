from fastapi import APIRouter


from app.users.routers import router as user_router


router = APIRouter()

router.include_router(user_router, prefix="/users")
