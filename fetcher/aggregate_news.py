from fetcher.current_news import fetch_current_news
from fetcher.news_api import fetch_articles
from fetcher.analyse_article import analyse_article
from fetcher.categorise_article import categorise_article
from datetime import datetime, timedelta
from fetcher.duplicate_articles import duplicate_articles
from fetcher.summariser import generate_summary
from datetime import datetime



def validate_article(article):
    required_fields = ["title","description"]
    return all(article.get(i) for i in required_fields)

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
    
    articles = [i for i in articles if validate_article(i)]
    articles = duplicate_articles(articles)
    analysed_articles = analyse_article(articles)
    for article in analysed_articles:
        if "category" not in article:
            article["category"] = categorise_article(article)
    
    for article in analysed_articles:
        date_str = article.get("date")
        try:
            parsed = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            article["parsed_date"] = parsed.date()
        except Exception:
            article["parsed_date"] = datetime.min.date()    
    analysed_articles.sort(key=lambda x: x["parsed_date"],reverse=True) # sort articles by date newsest first

    for article in analysed_articles:
        content = article.get("title") or article.get("description") or article.get("category")
        article["summary"] = generate_summary(content)

 

    return analysed_articles
if __name__ == "__main__":
    topic = input("Enter a topic to fetch news about: ")
    articles = aggregate_news(topic)

    print(f"\n📰 Top {len(articles)} articles for '{topic}'\n")

    for i, article in enumerate(articles, 1):
        title = article['title']
        summary = article['summary']
        sentiment = article['sentiment']
        category = ', '.join(article['category']) if isinstance(article['category'], list) else article['category']
        date = article['parsed_date']

        # print a nice box for each article
        print(f"╭─ {i}. {title} ─{'─'*(80-len(title))}╮")
        print(f"│ 🧠 Summary: {summary}")
        print(f"│ 💬 Sentiment: {sentiment}")
        print(f"│ 🏷️ Category: {category}")
        print(f"│ 📅 Date: {date}")
        print(f"╰{'─'*80}╯\n")