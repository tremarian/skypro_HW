from pages.calculator import Calculator
from selenium import webdriver


def test_fill_form():
    browser = webdriver.Chrome()
    calculation = Calculator(browser)
    delay = '45'

    calculation.set_delay(delay)

    calculation.click_seven()
    calculation.click_plus()
    calculation.click_eight()
    calculation.click_equal()

    assert calculation.text_result(delay) == '15'
