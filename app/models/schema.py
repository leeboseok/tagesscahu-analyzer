from pydantic import BaseModel
from typing import List

class ArticleRequest(BaseModel):
    title: str
    content: str

class ArticleResponse(BaseModel):
    sentiment: str
    keywords: List[str]

class ArticleResult(BaseModel):
    title: str
    summary: str
    link: str
    sentiment: str
    keywords: List[str]
