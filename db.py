
from sqlalchemy.orm import sessionmaker, declarative_base

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker  

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/what2do"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)  # deleted 2nd arguement because it was for SQLite db

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()





async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        

create_tables()