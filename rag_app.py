import google.generativeai as genai
import dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

dotenv.load_dotenv()

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


def validate_user_input(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if len(text) < 5:
        raise HTTPException(status_code=400, detail="Question is too short")

    if len(text) > 500:
        raise HTTPException(status_code=400, detail="Question is too long")


def validate_model_output(text: str):
    if text is None or text.strip() == "":
        raise HTTPException(status_code=500, detail="AI returned an empty response")

    if len(text) < 10:
        raise HTTPException(status_code=500, detail="AI response is too short")


def review_model_output(original_answer: str):
    review_prompt = f"""
You are reviewing an AI-generated response.

Your job:
- If the response is unclear, incomplete, or poorly written, improve it.
- If the response is already good, return it unchanged.

AI response to review:
{original_answer}
"""

    review_model = genai.GenerativeModel("gemini-2.5-flash")
    review_response = review_model.generate_content(review_prompt)

    return review_response.text

@app.get("/health")
def health_check():
    return {"status": "ok"}, 200

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY is not found in the environment variables. Please create an .env file.")
@app.get("/test-gemini")
def test_gemini():
    try:
        # Configure the Gemini API using the environment variable
        genai.configure(api_key=GEMINI_API_KEY)

        # Specify a model and generate content
        model = genai.GenerativeModel("gemini-2.5-flash")

        # 1) First call
        first_prompt = "Explain what a large language model is in one paragraph."
        first_response = model.generate_content(first_prompt)
        first_text = first_response.text

        # 2) Second call, reusing the first response
        second_prompt = f"Summarize this explanation in one sentence:\n\n{first_text}"
        second_response = model.generate_content(second_prompt)
        second_text = second_response.text

        return {
            "status": "success",
            "response": second_text,
        }, 200

    except Exception as e:
        return {"error": f"An error occurred: {e}"}, 500


@app.post("/query")
def query_ai(request: QueryRequest):
    try:
        validate_user_input(request.question)

        genai.configure(api_key=GEMINI_API_KEY)
        primary_model = genai.GenerativeModel("gemini-2.5-flash")
        primary_response = primary_model.generate_content(request.question)

        raw_answer = primary_response.text

        validate_model_output(raw_answer)

        reviewed_answer = review_model_output(raw_answer)

        return {
            "question": request.question,
            "raw_answer": raw_answer,
            "reviewed_answer": reviewed_answer,
        }
    except HTTPException:
        # Propagate validation and explicit HTTP errors as-is
        raise
    except Exception as e:
        # Surface unexpected errors as a 500 with details
        raise HTTPException(status_code=500, detail=str(e))
        
        
        
        
        
        
        
        
        
        
        
        
        
        