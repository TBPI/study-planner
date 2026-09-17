import os
from typing import List, Dict
import google.genai as gai
# needed for the api key
from dotenv import load_dotenv
from ddgs import DDGS

# Read variables from .env file and make them available as environment variables
load_dotenv()

def perform_web_search(query: str, max_results: int = 5) -> List[Dict[str, str]]:
    '''
    Perform a DuckDuckGo web search and return a list of results.

    Each result contains: title, reference, body
    '''
    # Set results an empty list of dictionaries
    results: List[Dict[str, str]] = []
    # Make a Try - Except clause for the web search on DuckDuckGo
    try:
        with DDGS() as ddgs:
            for result in ddgs.text(query, max_results = max_results):
                # result should be a dictionary
                if not isinstance(result, dict):
                    continue
                # result keys typically have the  attributes title, href, body
                title = result.get('title') or '' 
                href = result.get('href') or ''
                body = result.get('body') or ''
                if title and href:
                    results.append({
                        'title': title,
                        'href': href,
                        'body': body,
                    })
        return results
    except Exception as e:
        print(f'DuckDuckGo search resulted in an error: {e}.')
        return results

# Construction of a class that manages the interaction with the Gemini API

class GeminiClient:
    def __init__(self):
        try:
            self.client = gai.Client(api_key = os.getenv('GEMINI_API_KEY'))
            # Use gemini-3.5-flash-lite
            self.chat = self.client.chats.create(model = "gemini-3.5-flash-lite")
        except Exception as e:
            print(f'Error configuring Gemini API: {e}')
            self.chat = None

    def generate_response(self, user_input: str) -> str | None:
        '''
        Generate an AI response with optional web search when prefixed.

        For web search start the message with:
        - "search: <query>"
        - "/search: <query>"
        Otherwise the model responds using chat history.
        '''
        if not self.chat:
            return 'AI service is not configured correctly.'
        try:
            text = user_input or ""
            lower = text.strip().lower()

            # Search trigger
            search_query = None
            if lower.startswith("search:"):
                search_query = text.split(":", 1)[1].strip()
            elif lower.startswith("/search:"):
                search_query = text.split(" ", 1)[1].strip()
            if search_query:
                web_results = perform_web_search(search_query, max_results = 5)
                if not web_results:
                    return 'I could not retrieve web results. Please try again.'

                refs_lines = []
                for idx, item in enumerate(web_results, start = 1):
                    refs_lines.append(f"[{idx}] {item['title']} - {item['href']}\n{item['body']}")
                refs_block = "\n\n".join(refs_lines)

                system_prompt = (
                    "You are an AI research assistant. Use the provided web search results to answer the user query."
                    "Synthesize concisely, cite sources inline like [1], [2] where relevant, and include a brief summary."
                )
                composed = (
                    f"<system>\n{system_prompt}\n</system>\n"
                    f"<user_query>\n{search_query}\n</user_query>\n"
                    f"<web_results>\n{refs_block}\n</web_results>\n"
                )
                response = self.chat.send_message(composed)
                return response.text
            
            response = self.chat.send_message(text)
            return response.text
        except Exception as e:
            print(f'Error generating response: {e}')
            return 'I\'m sorry, there was an error in processing your request.'
