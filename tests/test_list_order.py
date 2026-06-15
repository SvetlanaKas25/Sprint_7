import pytest
import allure

from api_methods.order_methods import OrderMethods


class TestListOrder:
    @allure.title("Получение списка заказов")
    @allure.description("Тест проверяет, что при запросе возвращается список заказов с полем orders")
    def test_get_orders(self):
        response = OrderMethods.get_orders()

        assert response.status_code == 200, f"Ожидаемый статус код 200, но получили {response.status_code}"
        assert "orders" in response.json(), "В ответе отсутствует поле 'orders'"