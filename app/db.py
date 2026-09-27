import os
import uuid
from collections.abc import AsyncGenerator
from datetime import datetime

from dotenv import load_dotenv

from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

load_dotenv(override=True)

DATABASE_URL = os.getenv("DATABASE_URL")


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "post"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


engine = create_async_engine(DATABASE_URL)

SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session