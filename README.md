# Study Planner

Building the study planner is inspired by [this post from freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-an-ai-study-planner-agent-using-gemini-in-python/) by Tarun Singh.

# Quick Start

Follow these steps to run the study planner locally.

1. Create a Gemini API key in [Google AI Studio](https://aistudio.google.com/).
2. Create a file named `backend/.env` in the project root and add your API key in this format:

   ```
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   ```

   Keep this file private and do not commit it to version control.
3. Install the required dependencies from the project root:

   ```
   pip install flask google-genai python-dotenv requests ddgs
   ```

4. Start the application:

   ```
   python backend/app.py
   ```

5. Open the app in your browser at `http://127.0.0.1:5000`.

> Tip: To use web search with DuckDuckGo, begin your prompt with `search:` or `/search`.

# Dependencies

We need the following dependencies:

- `flask`: construct local web server
- `google-genai`: Gemini client
- `python-dotenv`: in order to load GEMINI_API_KEY from .env
- `requests`: HTTP helper
- `ddgs`: web search using DuckDuckGo

# The application

## gemini_client

The file [`gemini_client`](backend/gemini_client.py) manages user input and chat history.

- `perform_web_search()`:
Check whether prompt starts with `search:` or `/search`

- `generate_response()`:

