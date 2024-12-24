from fastapi import APIRouter

router = APIRouter()

@router.get("/api/quiz")
def get_quiz():
    # Placeholder logic for generating a quiz
    return {"quiz": "This is a placeholder quiz for learning python"}
