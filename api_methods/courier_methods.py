import requests
import allure

from URLs import URL

class CourierMethods:

    @staticmethod
    @allure.step("Создание нового курьера")
    def create_courier(data_courier):
        return requests.post(url=URL.CREATE_COURIER_ENDPOINT, json=data_courier)
    
    
    @staticmethod
    @allure.step("Удаление курьера по id: {courier_id}")
    def delete_courier_by_id(courier_id):
        return requests.delete(url=f"{URL.CREATE_COURIER_ENDPOINT}/{courier_id}")
    
    
    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(data_courier):
        return requests.post(url=URL.LOGIN_COURIER_ENDPOINT, json=data_courier)