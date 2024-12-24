from fastapi import FastAPI
from backend.routers import skill_router

app = FastAPI()

# Include routers
app.include_router(skill_router.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Skill Builder API"}
