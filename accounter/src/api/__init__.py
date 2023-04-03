from fastapi import APIRouter

from src.api.operations import router as operations_router


router = APIRouter()
router.include_router(operations_router)
