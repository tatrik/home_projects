from fastapi import APIRouter

from  src.api.auth import router as auth_router
from src.api.operations import router as operations_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(operations_router)
