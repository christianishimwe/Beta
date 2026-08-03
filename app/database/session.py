from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.config import database_settings


engine = create_async_engine(
    url=database_settings.POSTGRES_URL,
    echo=True
)

async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_session():
    async with async_session() as session:
        yield session
