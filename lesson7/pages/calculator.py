from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Calculator:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def set_delay(self, time):
        delay = self._driver.find_element(By.ID, 'delay')
        delay.clear()
        delay.send_keys(time)

    def click_seven(self):
        self._driver.find_element(
                By.CSS_SELECTOR, '.keys span:nth-child(1)'
            ).click()

    def click_plus(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.keys span:nth-child(4)'
        ).click()

    def click_eight(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.keys span:nth-child(2)'
        ).click()

    def click_equal(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '.keys span:nth-child(15)'
        ).click()

    def text_result(self, time):
        time = int(time)
        WebDriverWait(self._driver, time+3).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
                )
            )
        text = self._driver.find_element(By.CSS_SELECTOR, '.screen').text
        return text
