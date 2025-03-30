import feedparser

def fetch_latest_articles(limit=100):
    rss_url = "https://www.tagesschau.de/xml/rss2"
    feed = feedparser.parse(rss_url)
    return [{
        "title": entry.title,
        "link": entry.link,
        "summary": entry.summary
    } for entry in feed.entries[:limit]]
