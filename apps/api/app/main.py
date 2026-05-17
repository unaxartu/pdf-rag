from fastapi import FastAPI
from app.api.v1.routes.health import router as health_router

app = FastAPI(title="RAG Document Assistant API")

app.include_router(health_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "API is running"}