from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")  # async DB URL
SYNC_DATABASE_URL = os.getenv("SYNC_DATABASE_URL")  # sync DB URL for Alembic

# Async engine for FastAPI
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency for routes
async def get_db():
    async with async_session() as session:
        yield session
