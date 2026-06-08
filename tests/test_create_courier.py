import pytest
import allure

from api_methods.courier_methods import CourierMethods
from helpers import generate_new_courier_login_password_first_name



class TestCreateCourier:

    @allure.title("Создание курьера")
    @allure.description("Тест проверяет, что можно создать курьера  с корректными данными")
    def test_create_courier(self):
        courier_data = generate_new_courier_login_password_first_name()
        response = CourierMethods.create_courier(courier_data)
        assert response.status_code == 201, f"Ожидаемый статус код 201, но получили {response.status_code}"
        assert response.json()["ok"] is True


    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description("Тест проверяет, что нельзя создать двух курьеров с одинаковым логином")
    def test_cannot_create_duplicate_courier(self):
        courier_data = generate_new_courier_login_password_first_name()
        response1 = CourierMethods.create_courier(courier_data)
        response2 = CourierMethods.create_courier(courier_data)
        response2_body = '{"message": "Этот логин уже используется"}'

        assert response2.status_code == 409, f"Ожидаемый статус код 409, но получили {response2.status_code}" 
        assert response2.json() == response2_body

