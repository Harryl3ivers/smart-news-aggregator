import pytest
from unittest.mock import patch, MagicMock
from fetcher.analyse_article import analyse_article

@patch('fetcher.analyse_article.TextBlob')
def test_analyse_article(mock_textblob):
    mock_blob = MagicMock()
    mock_blob.sentiment.polarity = 0.5
    mock_textblob.return_value = mock_blob


    articles = [
        {"description": "This is a great day!"},]
    analysed = analyse_article(articles)
    assert analysed[0]["sentiment"] == "positive"

@pytest.mark.parametrize("Sentiment, Description", [
    ("positive", "I love sunny days!"),
    ("neutral", "The sky is blue."),
    ("negative", "I hate rainy days.")

])
@patch('fetcher.aggregate_news.fetch_articles')
@patch('fetcher.aggregate_news.fetch_current_news')
def test_sentiment_variety(mock_news_api,mock_current_news,Sentiment,Description):
    fake_news_api_response = [{
        "title": "Sample Article",
        "description": Description,
        "date": "2024-01-01",

    }
    ]
    fake_current_news_response = [{
        "title": "Another Article",
        "description": "Just an average day.",
        "date": "2024-01-02",
    }]
    mock_current_news.return_value = fake_current_news_response
    mock_news_api.return_value = fake_news_api_response
    result = analyse_article(fake_news_api_response + fake_current_news_response)
    assert result[0]["sentiment"] == Sentiment


@pytest.mark.parametrize("Polarity, ExpectedSentiment", [
    (0.5, "positive"),
    (0.11, "positive"),
    (0.1, "neutral"),
    (0.0, "neutral"),
    (-0.1, "neutral"),
    (-0.11, "negative"),
    (-0.5, "negative"),])
@patch('fetcher.analyse_article.TextBlob')
def test_sentiment_boundary_description(mock_textblob, Polarity, ExpectedSentiment):
    mock_blob = MagicMock()
    mock_blob.sentiment.polarity = Polarity
    mock_textblob.return_value = mock_blob
    articles = [{"description": "Test description"}]
    result = analyse_article(articles)
    assert result[0]["sentiment"] == ExpectedSentiment
     
   