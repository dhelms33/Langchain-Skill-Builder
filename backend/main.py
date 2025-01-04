import os
from fastapi import FastAPI, Depends
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_chain():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set OPENAI_API_KEY in your .env file.")
    
    llm = OpenAI(api_key=api_key)
    chain = LLMChain(model="claude-2")
    return chain

app = FastAPI()

@app.get("/api/quiz")
def generate_quiz(skill: str, chain: LLMChain = Depends(get_chain)):
    response = chain.run(f"Generate a quiz on {skill}")
    return {"quiz": response}

