import requests

from dotenv import load_dotenv
import os
 
 

def fetch_articles(topic):
    load_dotenv()
    print("Loaded API key:", os.getenv("NEWS_API_KEY",))
    NEWS_API_KEY = os.getenv("NEWS_API_KEY","").strip()

    if not NEWS_API_KEY:
        raise ValueError("API key not found. Please set the NEWS_API_KEY environment variable.")

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles")

    if "articles" not in data:
        raise ValueError("Error fetching articles. Please check your API key and topic.")
    
    articles = data["articles"]
    first_ten_articles = articles[:10]
    return [
        {
             
            "title": article.get("title", ""),
            "description": article.get("description", ""),
            "content": article.get("content", ""),
            "date": article.get("publishedAt", ""),
        }
        for article in first_ten_articles
    ]
    