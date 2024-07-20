from selenium.webdriver.common.by import By


class CatalogList:
    def __init__(self, driver):
        self._driver = driver

    def add_to_cart(self, goods):
        count = len(goods)
        for y in range(0, count):
            self._driver.find_element(By.NAME, goods[y]).click()

    def go_to_cart(self):
        self._driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
