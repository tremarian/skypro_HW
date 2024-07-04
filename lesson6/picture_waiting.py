from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
driver.implicitly_wait(20)
driver.maximize_window()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
           )

driver.implicitly_wait(20)
driver.find_element(By.CSS_SELECTOR, '.lead')
src = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')

print(src)

driver.quit()
