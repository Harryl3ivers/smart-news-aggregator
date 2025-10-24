import pytest
from unittest.mock import patch
from fetcher.aggregate_news import duplicate_articles
from unittest.mock import patch, MagicMock

def test_duplicate_articles():
    fake_articles = [
        {"title": "Breaking News: AI Advances", "description": "AI is transforming industries."},
        {"title": "Breaking News: AI Advances", "description": "AI is transforming industries."},
        {"title": "New Study on Climate Change", "description": "Climate change impacts are worsening."},]
    
    unique_articles = duplicate_articles(fake_articles)
    assert len(unique_articles) == 2, "There should be 2 unique articles after removing duplicates."


def test_duplication_with_similar_titles():
    fake_articles = [
        {"title": "Tech Innovations in 2024", "description": "The latest advancements in technology."},
        {"title": "Tech Innovations in 2024!", "description": "The latest advancements in technology."},
    ]
    unique_articles = duplicate_articles(fake_articles)
    assert len(unique_articles) == 1, "Similar titles should be considered duplicates."
    

   

