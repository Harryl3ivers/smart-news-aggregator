from fetcher.current_news import fetch_current_news
from fetcher.news_api import fetch_articles
from fetcher.analyse_article import analyse_article
from fetcher.categorise_article import categorise_article

def aggregate_news(topic):
    articles = []
    try:
        articles += fetch_articles(topic)
    except Exception as e:
        print(f"Error fetching from News API: {e}")
    
    try:
        articles += fetch_current_news(topic)
    except Exception as e:
        print(f"Error fetching from News API: {e}")
    
    analysed_articles = analyse_article(articles)
    for article in analysed_articles:
        if "category" not in article:
            article["category"] = categorise_article(article)

    return analysed_articles
if __name__ == "__main__":
    topic = input("Enter a topic to fetch news about: ")
    aggregate_news = aggregate_news(topic)
 
    print(f"\n✅ Fetched {len(aggregate_news)} total articles for '{topic}'\n")
    for i, article in enumerate(aggregate_news, 1):
        print(f"{i}. {article['title']} - Sentiment: {article['sentiment']} - Category: {article['category']} -date: {article.get('date')}")