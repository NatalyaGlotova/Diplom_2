import allure
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@allure.suite('Авторизация пользователя')
class Testlogin:

    @allure.description('При авторизация под пользователем, который есть в системе, происходит успешная авторизация')
    @allure.title('Авторизация под пользователем, который есть в системе')
    def test_login_user(self):
        with allure.step('Отправить запрос на авторизацию с корректными данными'):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('При авторизация под пользователем с некорректным логином/паролем, срабатывает allert')
    @allure.title('Авторизация с некорректным логином/паролем')
    def test_login_user_error(self):
        with allure.step('Отправить запрос на авторизацию с некорректным логином/паролем'):
            response = requests.post(f'{Urls.MAIN_URL}{Handlers.LOGIN}', data=User.data_negative)
        assert response.status_code == 401 and response.json().get('success') == False
        