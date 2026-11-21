import allure
import requests
from data.handlers import Urls, Handlers


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    @allure.description("Проверка успешного создания заказа с валидным токеном и актуальными ингредиентами")
    def test_create_order_with_auth(self, create_user, valid_ingredients):
        access_token = create_user[0].json().get("accessToken")
        headers = {"Authorization": access_token}

        with allure.step("Отправка запроса на создание заказа авторизованным пользователем"):
            response = requests.post(
                f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
                headers=headers,
                json=valid_ingredients
            )

        with allure.step("Проверка статус-кода и тела ответа"):
            assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Создание заказа неавторизованным пользователем")
    @allure.description("Проверка успешного создания заказа без передачи токена авторизации")
    def test_create_order_not_auth(self, valid_ingredients):
        with allure.step("Отправка запроса на создание заказа без авторизации"):
            r = requests.post(
                f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
                json=valid_ingredients
            )
        assert r.status_code == 200 and r.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    @allure.description("Проверка получения ошибки 400 при попытке создать заказ без передачи ингредиентов")
    def test_create_order_without_ingredients(self):
        with allure.step("Отправка запроса на создание заказа без ингредиентов"):
            r = requests.post(
                f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
                json={"ingredients": []}
            )
        assert r.status_code == 400 and r.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с невалидным хешем ингредиента")
    @allure.description("Проверка получения ошибки 500 при передаче некорректного хеша ингредиентов")
    def test_create_order_invalid_hash_ingredient(self, invalid_ingredients):
        with allure.step("Отправка запроса на создание заказа с невалидным хешем ингредиента"):
            r = requests.post(
                f"{Urls.MAIN_URL}{Handlers.MAKE_ORDER}",
                json=invalid_ingredients
            )
        assert r.status_code == 500 and "Internal Server Error" in r.text


