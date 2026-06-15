
class URL:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    
    # Ручка - Создание курьера
    CREATE_COURIER_ENDPOINT = f"{BASE_URL}/api/v1/courier"

    # Ручка - Логин курьера в системе
    LOGIN_COURIER_ENDPOINT = f"{BASE_URL}/api/v1/courier/login"
    
    # Ручка - Создание заказа
    CREATE_ORDER_ENDPOINT = f"{BASE_URL}/api/v1/orders"
    