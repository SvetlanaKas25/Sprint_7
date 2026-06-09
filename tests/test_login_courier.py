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
        assert 'id' in response.json() 


    @allure.title("Проверка обязательности поля login")
    @allure.description("Тест проверяет, что для авторизации курьера необходимо передать поле login")
    def test_without_login_returns_error(self, new_courier):
        with allure.step(f"Попытка авторизации курьера с незаполненным полем login"):
            data_courier = new_courier
            login = ""
            password = data_courier["password"]
            body_without_login = {
                "login" : login,
                "password" : password
                }
        response = CourierMethods.login_courier(body_without_login)
        assert response.status_code == 400, f"Ожидаемый статус код 400, но получили {response.status_code}"
        assert "Недостаточно данных для входа" in response.json()["message"]


    @allure.title("Проверка обязательности поля password")
    @allure.description("Тест проверяет, что для авторизации курьера необходимо передать поле password")
    def test_without_password_returns_error(self, new_courier):
        with allure.step(f"Попытка авторизации курьера с незаполненным полем password"):
            data_courier = new_courier
            login = data_courier["login"]
            password = ""
            body_without_password = {
                "login" : login,
                "password" : password
                }
        response = CourierMethods.login_courier(body_without_password)
        assert response.status_code == 400, f"Ожидаемый статус код 400, но получили {response.status_code}"
        assert "Недостаточно данных для входа" in response.json()["message"]



    @allure.title("Авторизация под несуществующим пользователем")
    @allure.description("Тест проверяет, что при попытке авторизоваться под несуществующей парой login-password, запрос возвращает ошибку")
    def test_incorrect_credentials_returns_error(self):
        with allure.step(f"Попытка авторизации курьера с несуществующей парой login-password"):
            data_courier = random_login_password()
        response = CourierMethods.login_courier(data_courier)
        assert response.status_code == 404, f"Ожидаемый статус код 404, но получили {response.status_code}"
        assert "Учетная запись не найдена" in response.json()["message"]


    @pytest.mark.parametrize("key,value", [
        ("login", "wronglogin"),
        ("password", "wrongpassword"),
        ])
    @allure.title("Проверка, система вернёт ошибку, если неправильно указать логин или пароль")
    @allure.description("Тест проверяет, что при вводе неверного логина или пароля из пары login-password зарегистрированного курьера, система вернёт ошибку ")
    def test_incorrect_data_login_courier_returns_error(self, new_courier, key, value):
        courier_data = new_courier.copy()
        courier_data[key] = value

        with allure.step(f"Попытка авторизации курьера с неверным полем: {key}"):
            response = CourierMethods.login_courier(courier_data)
        assert response.status_code == 404, f"Ожидаемый статус код 404, но получили {response.status_code}"
        assert "Учетная запись не найдена" in response.json()["message"]
        