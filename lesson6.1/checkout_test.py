from selenium.webdriver.common.by import By
from configurations import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_checkout(chrome_browser):
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(url_3)
    user_name = chrome_browser.find_element(By.NAME, 'user-name')
    user_name.click()
    user_name.send_keys(login)

    password = chrome_browser.find_element(By.NAME, 'password')
    password.click()
    password.send_keys(user_password)

    chrome_browser.find_element(By.NAME, 'login-button').click()

    goods = [
        'add-to-cart-sauce-labs-backpack',
        'add-to-cart-sauce-labs-bolt-t-shirt',
        'add-to-cart-sauce-labs-onesie']
    l = len(goods)
    for y in range(0,l):
        chrome_browser.find_element(By.NAME, goods[y]).click()
    
    chrome_browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    chrome_browser.find_element(By.NAME, 'checkout').click()
    name = chrome_browser.find_element(By.NAME, 'firstName')
    name.click()
    name.send_keys(f_name)

    surname = chrome_browser.find_element(By.NAME, 'lastName')
    surname.click()
    surname.send_keys(f_name)

    surname = chrome_browser.find_element(By.NAME, 'postalCode')
    surname.click()
    surname.send_keys(postal_code)

    chrome_browser.find_element(By.NAME, 'continue').click()
    total = chrome_browser.find_element(By.CSS_SELECTOR, '.summary_total_label')
    assert total.text == 'Total: $58.29'



