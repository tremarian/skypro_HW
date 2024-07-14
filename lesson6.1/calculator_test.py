from selenium.webdriver.common.by import By
from configurations import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_fill_form(chrome_browser):
    chrome_browser.get(url_2)
    delay = chrome_browser.find_element(By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys('45')

    seven = chrome_browser.find_element(
        By.CSS_SELECTOR, '.keys span:nth-child(1)'
        )
    plus = chrome_browser.find_element(
        By.CSS_SELECTOR, '.keys span:nth-child(4)'
        )
    eight = chrome_browser.find_element(
        By.CSS_SELECTOR, '.keys span:nth-child(2)'
        )
    equal = chrome_browser.find_element(
        By.CSS_SELECTOR, '.keys span:nth-child(15)'
        )

    seven.click()
    plus.click()
    eight.click()
    equal.click()

    WebDriverWait(chrome_browser, "48").until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
    assert chrome_browser.find_element(By.CSS_SELECTOR, '.screen').text == '15'


