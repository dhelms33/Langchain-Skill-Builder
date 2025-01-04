from fastapi import FastAPI, Depends
from langchain.chains import LLMChain
from langchain.llms import OpenAI

def get_chain():
    llm = OpenAI(api_key="your_openai_api_key")
    chain = LLMChain(llm=llm)
    return chain

app = FastAPI()

@app.get("/api/quiz")
def generate_quiz(skill: str, chain: LLMChain = Depends(get_chain)):
    response = chain.run(f"Generate a quiz on {skill}")
    return {"quiz": response}
