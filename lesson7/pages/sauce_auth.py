from selenium.webdriver.common.by import By


class Auth:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_login(self, login):
        user_name = self._driver.find_element(By.NAME, 'user-name')
        user_name.click()
        user_name.send_keys(login)

    def set_password(self, password):
        user_password = self._driver.find_element(By.NAME, 'password')
        user_password.click()
        user_password.send_keys(password)

    def click_login(self):
        self._driver.find_element(By.NAME, 'login-button').click()
