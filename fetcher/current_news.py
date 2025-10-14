import requests
from dotenv import load_dotenv
import os

def fetch_current_news(topic):
    load_dotenv()
    CURRENTS_NEWS_API_KEY = os.getenv("CURRENTS_NEWS_API_KEY")
    print("Loaded API key:", os.getenv("CURRENTS_NEWS_API_KEY"))

    if not CURRENTS_NEWS_API_KEY:
        raise ValueError("Error fetching articles. Please check your API key and topic.")
    
    url = f"https://api.currentsapi.services/v1/search?keywords={topic}&apiKey={CURRENTS_NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    articles = data["news"]
    first_ten_articles = articles[:10]
    return [
        {
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "category": article.get("category", ""),
            "date": article.get("published", ""),
            
        }
        for article in first_ten_articles
    ]