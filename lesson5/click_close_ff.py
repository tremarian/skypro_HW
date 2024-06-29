from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(5)
button = driver.find_element(By.CSS_SELECTOR, '.modal-footer p')
button.click()

sleep(10)