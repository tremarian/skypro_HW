from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/inputs")
input = driver.find_element(By.CSS_SELECTOR, 'input')
input.send_keys("1000")
sleep(1)
input.clear()
input.send_keys("999")

sleep(10)
