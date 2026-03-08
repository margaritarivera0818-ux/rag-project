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

Week 6
Multiple API Calls to resuse the first responses

@app.get("/test-gemini-chain")
def test_gemini_chain():
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")

        # 1) First call
        first_prompt = "Explain the importance of clean code in programming."
        first_response = model.generate_content(first_prompt)
        first_text = first_response.text

        # 2) Second call, reusing the first response
        second_prompt = f"Summarize this explanation in one sentence:\n\n{first_text}"
        second_response = model.generate_content(second_prompt)
        second_text = second_response.text

        return {
            "status": "success",
            "first_response": first_text,
            "second_response": second_text,
        }, 200

    except Exception as e:
        return {"error": f"An error occurred: {e}"}, 500

        Week 7
        Why input validation exists
Protect the model and your app: Input validation makes sure the question is non‑empty, not too short, and not absurdly long. This prevents:
Wasted API calls on garbage input (empty strings, accidental whitespace).
Unexpected behavior or errors from the model on malformed input.
Performance issues or higher cost from extremely long prompts.
Improve user experience: Instead of a vague “Internal Server Error”, users get clear, actionable messages like “Question cannot be empty” or “Question is too long”, so they know how to fix it.
Security and safety: In more advanced scenarios, input validation can also filter out obviously dangerous, irrelevant, or disallowed content before it ever reaches the AI.
Why output validation exists
Catch bad or unusable model responses: Models are not guaranteed to always return good text. Output validation checks things like:
Not empty.
Not trivially short or useless.
Roughly the expected shape (e.g., at least some length, sometimes valid JSON, etc.).
Fail fast with clear errors: Instead of returning a broken or nonsense answer to the client, you detect it and return a controlled 500 error like “AI returned an empty response” or “AI response is too short”. That makes debugging and monitoring much easier.
Guardrails for downstream systems: If other parts of your system depend on the AI output (e.g., storing in a database, sending to another service), output validation prevents bad data from flowing further and causing bigger problems later.
Why a second AI model is used to review responses
Quality improvement / “second pair of eyes”: The reviewer model acts like an editor:
If the first answer is unclear, incomplete, or poorly written, the reviewer rewrites or expands it.
If the first answer is already good, the reviewer is instructed to leave it unchanged.
Separation of roles:
Primary model: Focused on answering the user’s question as directly and richly as possible.
Reviewer model: Focused on clarity, completeness, tone, and quality control.
This separation often produces more reliable and polished responses than a single pass.
Defense in depth: If the primary model makes small mistakes, is vague, or misses a key point, the reviewer has a chance to catch and correct it. Over time, this leads to:
More consistent style and structure in answers.
Fewer low‑quality responses reaching the user without extra engineering effort on your side.
In short: input validation keeps bad questions out, output validation keeps bad answers from slipping through, and the second AI model is an automated editor that upgrades or confirms the primary model’s work.