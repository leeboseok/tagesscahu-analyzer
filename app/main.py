from fastapi import FastAPI
from app.api import analyzer

app = FastAPI(title="Tagesschau Analyzer API")

# API 라우터 등록
app.include_router(analyzer.router, prefix="/analyze", tags=["Analyzer"])
