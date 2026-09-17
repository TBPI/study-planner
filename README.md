# Study Planner

Building the study planner is inspired by [this post from freeCodeCamp](https://www.freecodecamp.org/news/how-to-build-an-ai-study-planner-agent-using-gemini-in-python/) by Tarun Singh.

# Dependencies

We need the following dependencies:

- `flask`: cosntruct local web server
- `google-genai`: Gemini client (new version of the `google-generativeai` module)
- `python-dotenv`: in order to load GEMINI_API_KEY from .env
- `requests`: HTTP helper
- `ddgs`: web search using DuckDuckGo (new version of `duckduckgo_search` module)

# The application

## gemini_client

The file [`gemini_client`](backend/gemini_client.py) manages user input and chat history.

- `perform_web_search()`:
Check whether prompt starts with `search:` or `/search`

- `generate_response()`:

