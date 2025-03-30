from fastapi import FastAPI
from app.api import api

app = FastAPI(title="Tagesschau Analyzer API")
app.include_router(api.router, prefix="/analyze", tags=["Analyzer"])
