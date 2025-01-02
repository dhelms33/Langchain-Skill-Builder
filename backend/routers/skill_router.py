import random
from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/api/quiz")
def get_quiz(skill: str = Query(..., description="The skill to generate a quiz for")):
    # generates questions
    questions = {
        "python": [
            {"question": "What is the output of `print(2 * 3)`?", "options": ["5", "6", "8"], "answer": "6"},
            {"question": "Which keyword is used to define a function?", "options": ["fun", "define", "def"], "answer": "def"}
        ],
        "spanish": [
            {"question": "What is the Spanish word for 'hello'?", "options": ["Hola", "Bonjour", "Ciao"], "answer": "Hola"},
            {"question": "What does 'gracias' mean?", "options": ["Thank you", "Goodbye", "Please"], "answer": "Thank you"}
        ]
    }

    quiz = questions.get(skill.lower(), [])
    if not quiz:
        return {"error": f"No quiz available for the skill: {skill}"}
    
    random.shuffle(quiz)  # Shuffle the questions
    return {"quiz": quiz[:3]}  # Return the first 3 questions

