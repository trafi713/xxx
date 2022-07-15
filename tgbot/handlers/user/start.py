from aiogram import types, Dispatcher

from tgbot.models.users import User


async def bot_start(message: types.Message, db_requests, session):
    user = await session.get(User, message.from_user.id)
    if not user:
        await db_requests.add_user(full_name=message.from_user.full_name,
                                   username=message.from_user.username,
                                   user_id=message.from_user.id)
        await session.commit()

    text = [f"Привет {message.from_user.full_name}",
            f"Баланс: {user.balance}",
            f"Статус: {user.role}"]

    if user.username != message.from_user.username:
        pass

    if user.full_name != message.from_user.full_name:
        pass

    await message.answer("\n".join(text))


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'], )
