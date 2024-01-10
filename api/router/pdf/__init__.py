import os
from fastapi import APIRouter
from .upload import router as upload_pdf_router

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)

router.include_router(upload_pdf_router)