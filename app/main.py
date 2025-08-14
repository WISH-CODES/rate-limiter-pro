from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="RateLimiter Pro")

app.include_router(users.router, prefix="/api/v1", tags=["users"])

@app.get("/")
async def root():
    return {"message": "RateLimiter Pro API is running"}
