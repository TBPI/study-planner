# Study Planner

Building the study planner is inspired by [this post from freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-an-ai-study-planner-agent-using-gemini-in-python/) by Tarun Singh.

# Quick start

1) Create an API key in [Google AI studio](https://aistudio.google.com/).
2) Create a file `backend/.env` and copy the API key `AP.IKEY.12345` into the file
such that it consists of one line
```
GEMINI_API_KEY=AP.IKEY.12345
```
3) Make sure the dependencies `flask`, `google-genai`, `python-dotenv`, `requests`, `ddgs` are installed.
4) Run `python backend/app.py`
5) You can access the study planner on `http://127.0.0.1:5000`.
*Hint.* If you want to perform a web search using `DuckDuckGo` type `search:` or `/search` in the prompt.

# Dependencies

We need the following dependencies:

- `flask`: cosntruct local web server
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

