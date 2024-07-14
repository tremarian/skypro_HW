from selenium.webdriver.common.by import By


class CheckoutStepOne:
    def __init__(self, driver):
        self._driver = driver

    def set_first_name(self, first_name):
        user_name = self._driver.find_element(By.NAME, 'firstName')
        user_name.click()
        user_name.send_keys(first_name)

    def set_last_name(self, last_name):
        user_last_name = self._driver.find_element(By.NAME, 'lastName')
        user_last_name.click()
        user_last_name.send_keys(last_name)

    def set_postal_code(self, postal_code):
        user_last_name = self._driver.find_element(By.NAME, 'postalCode')
        user_last_name.click()
        user_last_name.send_keys(postal_code)

    def click_continue(self):
        self._driver.find_element(By.NAME, 'continue').click()
