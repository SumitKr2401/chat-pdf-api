import os
from fastapi import APIRouter
from .generate_response import router as generate_response_router

router = APIRouter(prefix="/conversation", tags=["Conversation"])

router.include_router(generate_response_router)
