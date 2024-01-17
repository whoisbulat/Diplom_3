from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from urls import stellarburgers


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = stellarburgers

    def find_element(self, locator):
        return WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self,locator):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def return_element_text(self, locator):
        return self.driver.find_element(*locator).text


    def wait_element_(self, locator, element):
        return WebDriverWait(self.driver, 5).until(EC.none_of(
            EC.text_to_be_present_in_element(locator, element)))

    def wait_element_text_to_be_present(self, locator, text):
        return WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(locator, text))