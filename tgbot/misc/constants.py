from tgbot.models.users import User


async def user_status():
    user = User()
    if user.role == -1:
        status = 'Заблокирован'
    elif user.role == 0:
        status = 'Неактивен'
    elif user.role == 1:
        status = 'Воркер'
    elif user.role == 777:
        status = 'Разработчик'
    else:
        status = 'Неизвестен'

    return status
