from fastapi import FastAPI

from app.api.candidate import router as candidate_router
from app.api.curriculum import router as curriculum_router
from app.api.interview import router as interview_router
from app.api.followup import router as followup_router
from app.api.feedback import router as feedback_router


app = FastAPI(
    title="AI Interview Agent API",
    description="Backend API for the ABTalks AI Interview Agent",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Interview Agent 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "AI Interview Agent Backend"
    }


app.include_router(candidate_router)
app.include_router(curriculum_router)
app.include_router(interview_router)
app.include_router(followup_router)
app.include_router(feedback_router)