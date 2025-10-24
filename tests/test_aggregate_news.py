import pytest
from unittest.mock import patch
from fetcher.aggregate_news import aggregate_news

@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_full_pipeline(mock_news_api,mock_current_news):
    fake_news_api_response = [
        {
            "title": "AI revolutionizes healthcare",
            "description": "New AI tools are improving patient care.",
           
            "date": "2024-01-01",
            
        },
        {
           "title": "AI revolutionizes healthcare",
            "description": "New AI tools are improving patient care.",
            
            "date": "2024-01-01",
            
        }
    ]

    fake_current_news_response = [
        {
            "title": "AI model released to help with climate change",
            "description": "Impressive results!",
            "category": "general",
            "date": "2024-01-03",
            
        },
        {
            "title": "New study on AI ethics",
            "description": "Ethical considerations in AI development.",
            "category": "technology",
            "date": "2024-01-04",
            
        }
    ]

    mock_news_api.return_value = fake_news_api_response
    mock_current_news.return_value = fake_current_news_response
    result = aggregate_news("AI")
    assert len(result) == 3 ,"3 unique articles expected after deduplication"
    for article in result:
        assert "title" in article
        assert "description" in article
        assert "category" in article
        assert "summary" in article
        assert "sentiment" in article
        assert "parsed_date" in article
    
    sentiments = [a["sentiment"] for a in result]
    assert all(s in ["positive", "negative", "neutral"] for s in sentiments)
 
     


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

@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_mixed_data(mock_news_api,mock_current_news):
    fake_news_api = [
        {
            "title": "AI in healthcare",
            "description": "AI is improving patient care.",
            "content": "Content 1",
            "date": "2024-01-01T00:00:00Z"

        },
        {
            "title": "No description",
            "description": None,
            "content": "Content 1",
            "date": "2024-01-01T00:00:00Z"

        },
        {
            "title": None,
            "description": "This article has no content.",
            "content": " ",
            "date": "2024-01-01T00:00:00Z"
        }
        ]
    fake_current_news = [
        {
            "title": None,
            "description": "Impressive results!",
            "category": "general",
            "date": "2024-01-02T00:00:00Z"
        },  
        {
            "title": "No content article",
            "description": None,
            "category": " ",
            "date": "2024-01-03T00:00:00Z"
        }
    ]
    mock_news_api.return_value = fake_news_api
    mock_current_news.return_value = fake_current_news
    result = aggregate_news("test")
    assert len(result) == 1, "Only one valid article should be processed"
    assert  result[0]["title"] == "AI in healthcare"
    


@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news') 
def test_pipeline_with_api_failure(mock_news_api,mock_current_news):
    #the first api fails
    mock_news_api.side_effect = Exception("News API failure")
    fake_current_news_response = [
        {
            "title": "AI model released to help with climate change",
            "description": "Impressive results!",
            "category": "general",
            "date": "2024-01-02"
        },
    ]
    mock_current_news.return_value = fake_current_news_response
    result = aggregate_news("AI")
    assert len(result) == 1
    assert result[0]["title"] == "AI model released to help with climate change"
     
   
@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_pipeline_with_both_apis_failure(mock_news_api,mock_current_news):
    mock_news_api.side_effect = Exception("News API failure")
    mock_current_news.side_effect = Exception("Current News API failure")
    result = aggregate_news("AI")
    assert len(result) == 0, "No articles should be returned when both APIs fail"

@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_empty_responses_both_apis(mock_news_api,mock_current_news):
    fake_news_api_response = []
    fake_current_news_response = []
    mock_news_api.return_value = fake_news_api_response
    mock_current_news.return_value = fake_current_news_response
    result = aggregate_news("AI")
    assert len(result) == 0, "No articles should be returned for empty API responses"
     