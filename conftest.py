import pytest
from selenium import webdriver
import requests
from faker import Faker




fake = Faker()



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site')

    yield driver
    driver.quit()




@pytest.fixture
def register_user(driver):
    email = fake.email()
    password = fake.password()
    name = fake.first_name()

    new_user = {
        "email": email,
        "password": password,
        "name": name
    }
    register_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=new_user)
    if register_response.status_code != 200:
        raise Exception("Регистрация пользователя не удалась")

    login_and_password = {
        "login": email,
        "password": password
    }

    return login_and_password

    # delete_response = requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user",
    #                                   headers={"Authorization": access_token})
    # if delete_response.status_code != 200:
    #     raise Exception("Удаление пользователя не удалось")




# @pytest.fixture
# def user_with_registered_order(driver, register_user):
#     login_credentials = register_user
#
#     login_response = requests.post("https://stellarburgers.nomoreparties.site/api/auth/login", json=login_credentials)
#     if login_response.status_code != 200:
#         raise Exception("Вход пользователя не удался")
#
#     access_token = login_response.json()["accessToken"]
#
#     data = {
#         "ingredients": ["61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa71"]
#     }
#     response = requests.post("https://stellarburgers.nomoreparties.site/api/orders", data=data,
#                              headers={"Authorization": access_token})
#     # order_number = response.json()['number']
#
#     return response






