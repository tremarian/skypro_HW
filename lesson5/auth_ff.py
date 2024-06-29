from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
password.send_keys("SuperSecretPassword!")

login = driver.find_element(By.CSS_SELECTOR, 'button')
login.click()

sleep(10)