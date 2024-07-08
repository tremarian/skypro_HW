from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
    )
driver.implicitly_wait(20)

driver.maximize_window()
driver.get("http://uitestingplayground.com/ajax")

button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
button.click()

text = driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text
print(text)

driver.quit()
