import pytest
import requests

from data.handlers import Urls, Handlers
from data.user_data import User


@pytest.fixture(scope="function")
def create_user():
    payload = User.create_data_user()
    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(f"{Urls.MAIN_URL}{Handlers.CREATE_USER}", data=payload)
    token = response.json()["accessToken"]
    yield response, payload, login_data, token
    requests.delete(f"{Urls.MAIN_URL}{Handlers.DELETE_USER}", headers={'Authorization': f'{token}'})

@pytest.fixture(scope="function")
def delete_user():
    user_data = {"token": None}
    
    yield user_data
    
    requests.delete(
        f"{Urls.MAIN_URL}{Handlers.DELETE_USER}",
        headers={"Authorization": f"{user_data['token']}"}
    )

@pytest.fixture
def valid_ingredients():
    response = requests.get(f'{Urls.MAIN_URL}/api/ingredients')
    ingredients_data = response.json().get('data', [])
    return {
        'ingredients': [
            ingredients_data[0]['_id'],
            ingredients_data[1]['_id']
        ]
    }    

@pytest.fixture
def invalid_ingredients(valid_ingredients):
    broken_ids = [f"{item_id}g" for item_id in valid_ingredients["ingredients"]]
    return {"ingredients": broken_ids}
