import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
first_name.send_keys('Иван')

last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
last_name.send_keys('Петров')

address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
address.send_keys('Ленина, 55-3')

email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
email.send_keys('test@skypro.com')

phone = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
phone.send_keys('+7985899998787')

city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
city.send_keys('Москва')

country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
country.send_keys('Россия')

job = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
job.send_keys('QA')

company = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
company.send_keys('SkyPro')

button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
button.click()


@pytest.mark.parametrize('input_str, result', [
    ('#first-name', 'rgba(15, 81, 50, 1)'),
    ('#last-name', 'rgba(15, 81, 50, 1)'),
    ('#address', 'rgba(15, 81, 50, 1)'),
    ('#e-mail', 'rgba(15, 81, 50, 1)'),
    ('#phone', 'rgba(15, 81, 50, 1)'),
    ('#city', 'rgba(15, 81, 50, 1)'),
    ('#country', 'rgba(15, 81, 50, 1)'),
    ('#job-position', 'rgba(15, 81, 50, 1)'),
    ('#company', 'rgba(15, 81, 50, 1)'),
    ('#zip-code', 'rgba(132, 32, 41, 1)')
    ])
def test_filling(locator, result):
    field = driver.find_element(By.CSS_SELECTOR, locator)
    assert field.value_of_css_property("color") == result


driver.quit()
