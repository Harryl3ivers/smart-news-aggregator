import pytest
from unittest.mock import patch
from fetcher.aggregate_news import aggregate_news

@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_aggregate_news(mock_news_api,mock_current_news):
    fake_news_api_response = [
        {
            "title": "News AI model in business",
            "description": "AI is transforming industries.",
            "content": "Content 1",
            "date": "2024-01-01T00:00:00Z"
        },
    ]

    fake_current_news_response = [
        {
            "title": "AI model released to help with climate change",
            "description": "Impressive results!",
            "category": "general",
            "date": "2024-01-02T00:00:00Z"
        },
    ]

    mock_news_api.return_value = fake_news_api_response
    mock_current_news.return_value = fake_current_news_response
    result = aggregate_news("AI")
    assert len(result) == 2
    assert all("sentiment" in article for article in result)
