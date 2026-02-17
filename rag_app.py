import google.generativeai as genai
import dotenv
dotenv.load_dotenv() 
from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health_check():
    return {"status": "ok"}, 200
import os
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not found in the environment variables. Please create an .env file.")
@app.get("/test-gemini")
def test_gemini():
    try:
        # Configure the Gemini API using the environment variable
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Specify a model and generate content
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = "Explain the importance of clean code in programming."
        
        response = model.generate_content(prompt)
        
        return {"status": "success", "response": response.text}, 200
    except Exception as e:
        return {"error": f"An error occurred: {e}"}, 500