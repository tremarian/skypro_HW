import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from configurations import *

def test_fill_form(chrome_browser):
    chrome_browser.get(url_2)
    chrome_browser.implicitly_wait(50)
    delay = chrome_browser.find_element(By.CSS_SELECTOR, '#delay')
    delay.send_keys('45')

    seven = chrome_browser.find_element(By.CSS_SELECTOR,'.keys span:nth-child(1)')
    plus = chrome_browser.find_element(By.CSS_SELECTOR,'.keys span:nth-child(4)')
    eight = chrome_browser.find_element(By.CSS_SELECTOR,'.keys span:nth-child(2)')
    equal = chrome_browser.find_element(By.CSS_SELECTOR,'.keys span:nth-child(15)')

    seven.click()
    plus.click()
    eight.click()
    equal.click()
    assert chrome_browser.find_element(By.CSS_SELECTOR,'.screen').text() == 15

