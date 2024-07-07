import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

driver.implicitly_wait(50)

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.send_keys('45')

seven = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(1)')
plus = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(4)')
eight = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(2)')
equal = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(15)')

@pytest.mark.parametrize('first_summand, second_summand, result', [
    (seven, eight, 15)
    ])
def test_sum(first_summand, second_summand, summ, result):
    first_summand.click()
    plus.click
    second_summand.click()
    equal.click()
    summ = driver.find_element(By.CSS_SELECTOR,'.screen').text()
    assert  summ == result

driver.quit()
