from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert")

def analyze_sentiment(text: str) -> str:
    result = sentiment_model(text[:512])[0]  # BERT는 512 토큰 제한
    return result['label']
