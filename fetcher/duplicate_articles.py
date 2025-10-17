def duplicate_articles(articles):
    duplicate_items = set()
    unique = []
    for article in articles:
        titles = article.get("title", "").lower()
        if titles not in duplicate_items:
            duplicate_items.add(titles)
            unique.append(article)
    
    return unique
         
     