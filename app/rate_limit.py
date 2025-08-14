import asyncio
from redis.asyncio import Redis
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis = Redis.from_url(REDIS_URL, decode_responses=True)

RATE_LIMIT = 5  # max requests
RATE_WINDOW = 60  # seconds

async def is_rate_limited(key: str) -> bool:
    """Check if key exceeded rate limit"""
    current = await redis.get(key)
    if current is None:
        await redis.set(key, 1, ex=RATE_WINDOW)
        return False
    elif int(current) >= RATE_LIMIT:
        return True
    else:
        await redis.incr(key)
        return False

async def check_rate_limit(key: str):
    if await is_rate_limited(key):
        from fastapi import HTTPException
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
