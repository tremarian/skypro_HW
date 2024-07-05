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
seven.click()

plus = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(4)')
plus.click()

eight = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(2)')
eight.click()

equal = driver.find_element(By.CSS_SELECTOR,'.keys span:nth-child(15)')
equal.click()

assert driver.find_element(By.CSS_SELECTOR,'.screen').text() == '15'