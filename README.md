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