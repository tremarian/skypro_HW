from selenium.webdriver.common.by import By
from configurations import *


def test_fill_form(chrome_browser):
    chrome_browser.get(url_1)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="first-name"]'
        ).send_keys(first_name)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="last-name"]'
        ).send_keys(last_name)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="address"]'
        ).send_keys(address)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]'
        ).send_keys(email)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="phone"]'
        ).send_keys(phone)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="city"]'
        ).send_keys(city)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="country"]'
        ).send_keys(country)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="job-position"]'
        ).send_keys(job)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[name="company"]'
        ).send_keys(company)

    chrome_browser.find_element(
        By.CSS_SELECTOR, '[type="submit"]'
        ).click()


    assert  chrome_browser.find_element(
        By.CSS_SELECTOR, '#zip-code'
        ).value_of_css_property("color") == 'rgba(132, 32, 41, 1)'
    field_list = [
        '#first-name',
        '#last-name',
        '#address',
        '#e-mail',
        '#phone',
        '#city',
        '#country',
        '#job-position',
        '#company']
    l = len(field_list)
    for y in range(0,l):
        assert  chrome_browser.find_element(
            By.CSS_SELECTOR, field_list[y]
            ).value_of_css_property("color") == 'rgba(15, 81, 50, 1)'
