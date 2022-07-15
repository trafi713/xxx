from sqlalchemy import select

from tgbot.models.users import User


class DbRequest:
    def __init__(self, session):
        self.session = session

    async def get_user(self, user_id: int):
        sql = select(User).where(User.user_id == user_id)
        request = await self.session.execute(sql)
        user = request.scalar()
        return user

    async def add_user(self,
                       full_name: str,
                       username: str,
                       user_id: int):
        user = User(full_name=full_name,
                    username=username,
                    user_id=user_id)
        self.session.add(user)
        return user
