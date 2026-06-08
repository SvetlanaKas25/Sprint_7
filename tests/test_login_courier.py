import pytest
import allure

from api_methods.courier_methods import CourierMethods
from helpers import random_login_password


class TestLoginCourier:

    @allure.title("Авторизация курьера")
    @allure.description("Тест проверяет, что курьер может авторизоваться  с корректными данными")
    def test_login_courier(self, new_courier):
        data_courier = new_courier
        response = CourierMethods.login_courier(data_courier)
        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert 'id' in response.text 

