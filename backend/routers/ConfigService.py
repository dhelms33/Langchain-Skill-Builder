import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables
load_dotenv()

class ConfigService:
    @staticmethod
    def get_openai_api_key():
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(status_code=500, detail="API key not found.")
        return api_key