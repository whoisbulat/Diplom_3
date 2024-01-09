from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from urls import stellarburgers



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = stellarburgers

    def find_element(self, locator):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self,locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

