from keybert import KeyBERT

kw_model = KeyBERT(model="distilbert-base-german-cased")

def extract_keywords(text: str, top_n=5):
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]
