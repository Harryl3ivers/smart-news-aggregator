from textblob import TextBlob
def analyse_article(articles):
    for a in articles:
        text = a["description"] or ""
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0.1:
            a["sentiment"] = "positive"
        elif polarity < -0.1:
            a["sentiment"] = "negative"
        else:
            a["sentiment"] = "neutral"
    return articles

     