from fastapi import APIRouter


from apps.users.routers import router as user_router


router = APIRouter()

router.include_router(user_router, prefix="/users")
