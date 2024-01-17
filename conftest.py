import pytest
import requests
from faker import Faker
from selenium import webdriver

from urls import api_auth_register, stellarburgers

fake = Faker()



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(stellarburgers)

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
    requests.post(api_auth_register, json=new_user)

    login_and_password = {
        "login": email,
        "password": password
    }

    return login_and_password


