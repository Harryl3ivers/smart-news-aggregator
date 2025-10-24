import re
def duplicate_articles(articles):
    duplicate_items = set()
    unique = []
    try:
          for article in articles:
            titles = article.get("title", "").lower().strip()
            normalised_title = re.sub(r'\W+', '', titles)
            if normalised_title not in duplicate_items:
                duplicate_items.add(normalised_title)
                unique.append(article)
    except Exception as e:
        print(f"Error during duplicate removal: {e}")
    
    return unique
   
         
 