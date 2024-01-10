import os
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from shared.factory import WORKER_ID

router = APIRouter()


# Redirect root to docs
@router.get("/", include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@router.get("/ping")
async def ping():
    return {
        "message": "pong",
        "deployment": "dev" if os.environ.get("API_DEBUG", "") == "True" else "prod",
        "host": os.environ.get("HOST", "unknown"),
        "worker_id": WORKER_ID,
    }