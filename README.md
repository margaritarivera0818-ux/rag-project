# RAG Project

This repository contains my Retrieval-Augmented Generation (RAG) project for the GenAI Secure Coding course.

This project will be built incrementally each week.


## Git Commands Used So Far

- git clone  
- git status  
- git add  
- git commit  
- git push


*   **Where environment variables are loaded:** Environment variables are loaded using `dotenv.load_dotenv()`.
*   **How the Gemini API key is read:** The `GEMINI_API_KEY` is read from the environment through the loaded variables.
*   **Where Gemini is configured:** Configuration is currently placeholder, with the `GEMINI_API_KEY` checked for existence and placeholder logic within the `process_query` endpoint.
*   **How the FastAPI app is created:** The FastAPI app is created using `app = FastAPI()`.
*   **What each endpoint does:** The `/health` endpoint checks application status, and the `/query` endpoint processes user queries through RAG logic.
*   **Why the Gemini call is not implemented yet:** The Gemini call is placeholder to focus on the endpoint structure first; the full retrieval and generation logic would be developed next.

**Clarifying the Endpoint's Action**

I've examined the Python code thoroughly. The `/test-gemini` endpoint, defined using `@app.get`, executes the `test_gemini()` function. This function initializes the Gemini API with the `GEMINI_API_KEY`, sets up the 'gemini-2.5-flash' model, and constructs a prompt, "Explain the importance of clean code in programming." Crucially, it then calls `model.generate_content(prompt)` to generate a response. The endpoint returns a JSON response containing the model's text response and a "success" status. The Gemini call resides directly within `test_gemini`, and this endpoint tests the Gemini integration.

**Confirming Gemini Location**

I've zeroed in on the direct answer: the Gemini call resides within the `test_gemini` function, as we established. I wanted to reiterate this, referencing the provided code snippet to ensure we're on the same page before diving deeper into the README update.