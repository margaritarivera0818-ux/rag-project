import dotenv
dotenv.load_dotenv() 
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health_check():
    return {"status": "ok"}, 200
GEMINI_API_KEY = "AIzaSyDv6lA0YiW804z8nJhGQr7h9jWZb5y_Nk"
if GEMINI_API_KEY is None: 
    raise ValueError("GEMINI_API_KEY is not found in the environment variables. Please create an .env file.")