from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import ping, pdf, conversation

# Initialize FastAPI
app = FastAPI(
    title="GPT PDF API",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Include routers
app.include_router(ping.router)
app.include_router(pdf.router)
app.include_router(conversation.router)
