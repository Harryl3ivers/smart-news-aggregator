from config.keywords import CATEGORY_KEYWORDS
 

 
 


def categorise_article(article):
    text = (article.get("title", "") + " " + article.get("description", ""))
    for category, keyword in CATEGORY_KEYWORDS.items():
        if any(word in text.lower() for word in keyword):
            return category
    return "General"


 