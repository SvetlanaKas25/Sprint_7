import pytest

from api_methods.courier_methods import CourierMethods
from helpers import generate_new_courier_login_password_first_name


# Создание нового курьера, получение его id и удаление курьера после теста
@pytest.fixture(scope="function")
def new_courier():
    courier_data = generate_new_courier_login_password_first_name()
    create_response = CourierMethods.create_courier(courier_data)
    login_pass = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
    yield login_pass
    
    response = CourierMethods.login_courier(login_pass)
    courier_id = response.json()["id"]
    CourierMethods.delete_courier_by_id(courier_id)
    
