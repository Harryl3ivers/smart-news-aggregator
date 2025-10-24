from fetcher.categorise_article import categorise_article
import pytest
from config.keywords import CATEGORY_KEYWORDS as keywords

def generate_test_article():
    test_cases = []
    for category, topic in keywords.items():
        for i in topic:
            test_cases.append((
                {"title": f"Article about {i}", "description": f"News related to {i}"},
                category
            ))
    return test_cases

@pytest.mark.parametrize("article, expected_category",generate_test_article())
def test_categorise_all_categories(article,expected_category):
    result = categorise_article(article)
    assert result == expected_category, f"Article should be categorised as {expected_category}"
 
   
def test_categorise_article():
    fake_article = {"title": "Tech Innovations in 2024", "description": "The latest advancements in technology."}
    categorised_article = categorise_article(fake_article)
    assert categorised_article== "Technology"