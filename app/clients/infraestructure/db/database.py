from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from decouple import config
from app.common.infraestructure import models

DATABASE_URL = config('DATABASE_URL') 
#"sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    future=True
)

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session