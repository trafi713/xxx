from tgbot.config import Config


def make_connection_starting(config: Config, async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{config.db.user}:{config.db.password}@"
        f"{config.db.host}:{config.db.port}/{config.db.database}"
    )

    if async_fallback:
        result += "?async_fallback=True"

    return result
