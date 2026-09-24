from fastapi import FastAPI
from app.config import settings
from app.routers.api import router as api_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Microservice with high-concurrency distributed rate limiting.",
    version="1.0.0"
)

# Register routes
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Service operational. Visit /docs for Swagger specifications."}
