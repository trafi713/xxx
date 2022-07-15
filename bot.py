import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
from tgbot.handlers.user.start import register_start
from tgbot.services.database.functions.database import create_db_session
from tgbot.middlewares.db import DbSessionMiddleware

logger = logging.getLogger(__name__)


def register_all_middleware(dp, sessionmaker):
    dp.setup_middleware(DbSessionMiddleware(sessionmaker))


def register_all_handlers(dp):
    register_start(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    config = load_config(".env")
    storage = RedisStorage2 if config.misc.use_redis else MemoryStorage()
    bot = Bot(token=config.tg.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    logger.info("connecting database")
    sessionmaker = await create_db_session(config)
    logger.info("database connected")
    await bot.send_message(config.tg.chat_logs, "Bot launched")

    register_all_middleware(dp, sessionmaker)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        logger.error("Bot Stopped")
