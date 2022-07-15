from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from tgbot.services.database.functions.db_requests import DbRequest


class DbSessionMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ['error', 'update']

    def __init__(self, session_pool):
        super().__init__()
        self.session_pool = session_pool

    async def pre_process(self, obj, data, *args):
        session = self.session_pool()
        data['session'] = session
        data['db_requests'] = DbRequest(session)

    async def post_process(self, obj, data, *args):
        session = data.get('session')
        if session:
            await session.close()
