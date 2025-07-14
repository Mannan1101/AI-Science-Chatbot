import os
from openai import AsyncOpenAI

# Load environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
gemini_base_url = os.getenv("GEMINI_BASE_URL")
gemini_model_name = os.getenv("GEMINI_MODEL_NAME")

# Create OpenAI client
gemini_client = AsyncOpenAI(api_key=gemini_api_key, base_url=gemini_base_url)
