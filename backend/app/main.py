from fastapi import FastAPI

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