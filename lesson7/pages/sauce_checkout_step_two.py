from selenium.webdriver.common.by import By


class CheckoutStepTwo:
    def __init__(self, driver):
        self._driver = driver

    def total(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label'
            )
        text = total.text
        return text
