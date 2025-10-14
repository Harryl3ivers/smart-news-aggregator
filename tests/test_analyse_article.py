import pytest
from unittest.mock import patch, MagicMock
from fetcher.analyse_article import analyse_article

@patch('fetcher.analyse_article.TextBlob')
def test_analyse_article(mock_textblob):
    mock_blob = MagicMock()
    mock_blob.sentiment.polarity = 0.5
    mock_textblob.return_value = mock_blob
    