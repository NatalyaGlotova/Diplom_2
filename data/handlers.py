class Urls:
    MAIN_URL = 'https://stellarburgers.education-services.ru'


class Handlers:
    # Регистрация пользователя
    CREATE_USER = '/api/auth/register'
    # Авторизация пользователя
    LOGIN = '/api/auth/login'
    # Удаление пользователя
    DELETE_USER = '/api/auth/user'
    # Создание заказа 
    MAKE_ORDER = '/api/orders'
#
    headers = {"Content-Type": "application/json"}