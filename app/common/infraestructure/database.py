from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from decouple import config

DATABASE_URL = config('DATABASE_URL') 
#"sqlite+aiosqlite:///./test.db"

engine = create_async_engine(
    DATABASE_URL, 
    echo=True, 
    future=True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)