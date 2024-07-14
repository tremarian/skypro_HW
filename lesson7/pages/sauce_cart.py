from selenium.webdriver.common.by import By


class Cart:
    def __init__(self, driver):
        self._driver = driver

    def checkout(self):
        self._driver.find_element(By.NAME, 'checkout').click()
