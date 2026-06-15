import random
from faker import Faker
import random
import string


# Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))


# Метод генерирования данных для регистрации нового курьера
def generate_new_courier_login_password_first_name():
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
        }
    
    return payload


# Метод для генерирования несуществующей пары логин-пароль
def random_login_password():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        }
    return payload


faker = Faker()
# Метод генерирования данных для нового заказа
def generate_order_data(color=None):
    data = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "address" : faker.address(),
        "metroStation" : random.randint(1, 20),
        "phone" : faker.phone_number(),
        "rentTime" : random.randint(1, 14),
        "deliveryDate" : faker.date_between(start_date='today', end_date='+5d').isoformat(),
        "comment" : faker.sentence()
        }
        
    if color is not None:
        data["color"] = color

    return data