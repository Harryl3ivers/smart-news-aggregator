import pytest
from unittest.mock import patch
from fetcher.news_api import fetch_articles

@patch('fetcher.news_api.requests.get')
def test_fetch_articles_success(mock_get):
    fake_response = {
        "articles": [
            {
                "title": "Test Article 1",
                "description": "Description 1",
                "content": "Content 1",
                "publishedAt": "2024-01-01T00:00:00Z"
            },
        ]
    }
    mock_get.return_value.json.return_value = fake_response
    articles = fetch_articles("technology")
    assert len(articles) == 1
    assert articles[0]["title"] == "Test Article 1"