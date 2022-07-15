from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from tgbot.config import Config
from tgbot.services.database.functions.utils import make_connection_starting


async def create_db_session(config: Config):
    engine = create_async_engine(
        make_connection_starting(config),
        future=True
    )
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    return async_session
