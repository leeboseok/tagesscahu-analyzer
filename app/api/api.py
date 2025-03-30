from fastapi import APIRouter
from app.models.schema import ArticleRequest, ArticleResponse, ArticleResult
from app.services.fetcher import fetch_latest_articles
from app.services.sentiment import analyze_sentiment
from app.services.keywords import extract_keywords

router = APIRouter()

@router.post("/", response_model=ArticleResponse)
def analyze_article(article: ArticleRequest):
    sentiment = analyze_sentiment(article.content)
    keywords = extract_keywords(article.content)
    return ArticleResponse(
        sentiment=sentiment,
        keywords=keywords
    )

@router.get("/latest", response_model=list[ArticleResult])
def analyze_latest_articles():
    articles = fetch_latest_articles(limit=100)
    results = []

    for article in articles:
        sentiment = analyze_sentiment(article["summary"])
        keywords = extract_keywords(article["summary"])
        results.append(ArticleResult(
            title=article["title"],
            summary=article["summary"],
            link=article["link"],
            sentiment=sentiment,
            keywords=keywords
        ))

    return results
