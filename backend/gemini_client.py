import os
from typing import List, Dict
import google.generativeai as genai
# needed for the api key
from dotenv import load_dotenv
from duckduckgo_search import DDGS

# Read variables from .env file and make them available as environment variables
load_dotenv()

def perform_web_search(query: str, max_results: int = 5) -> List[Dict[Str, Str]]:
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
                    result.append({
                        'title': title,
                        'href': href,
                        'body': body,
                    })
        return results
    except Exception as e:
        print(f'DuckDuckGo search resulted in an error: {e}.')
        return results
