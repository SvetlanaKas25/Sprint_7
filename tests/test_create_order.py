import pytest
import allure

from api_methods.order_methods import OrderMethods
from helpers import generate_order_data


class TestCreateOrder:
    @pytest.mark.parametrize("color_data,details", [
    (["BLACK"], "один цвет — BLACK"),
    (["GREY"], "один цвет — GREY"),
    (["BLACK", "GREY"], "оба цвета"),
    ([""], "цвет не указан")
    ])
    @allure.title("Создание заказа с разными вариантами указания цвета")
    @allure.description("Тест проверяет создание заказа с разными вариантами цвета и что тело ответа содержит 'track'.")
    def test_create_order_with_different_colors(self, color_data, details):
        with allure.step(f"Создание заказа: {details}"):
            order_data = generate_order_data(color=color_data)
            response = OrderMethods.create_order(order_data)

        assert response.status_code == 201, f"Ожидаемый статус код 201, но получили {response.status_code}"
        assert "track" in response.json(), "В ответе отсутствует поле 'track'"
        
