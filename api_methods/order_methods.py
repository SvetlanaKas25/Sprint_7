import requests
import allure

from URLs import URL

class OrderMethods:

    @staticmethod
    @allure.step("Создание нового заказа")
    def create_order(data_order):
        return requests.post(url=URL.CREATE_ORDER_ENDPOINT, json=data_order)
    
    
    @staticmethod
    @allure.step("Отправляет GET‑запрос на получение списка заказов.")
    def get_orders():
        return requests.get(url=URL.CREATE_ORDER_ENDPOINT)