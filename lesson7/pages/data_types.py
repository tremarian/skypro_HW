from selenium.webdriver.common.by import By


class DataTypes:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def fill_name(self, name):
        self._driver.find_element(By.NAME, 'first-name').send_keys(name)

    def fill_surname(self, surname):
        self._driver.find_element(By.NAME, 'last-name').send_keys(surname)

    def fill_address(self, address):
        self._driver.find_element(By.NAME, 'address').send_keys(address)

    def fill_email(self, email):
        self._driver.find_element(By.NAME, 'e-mail').send_keys(email)

    def fill_phone(self, phone):
        self._driver.find_element(By.NAME, 'phone').send_keys(phone)

    def fill_city(self, city):
        self._driver.find_element(By.NAME, 'city').send_keys(city)

    def fill_country(self, country):
        self._driver.find_element(By.NAME, 'country').send_keys(country)

    def fill_job(self, job):
        self._driver.find_element(By.NAME, 'job-position').send_keys(job)

    def fill_company(self, company):
        self._driver.find_element(By.NAME, 'company').send_keys(company)

    def click_submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[type="submit"]'
        ).click()

    def field_color(self, id):
        field = self._driver.find_element(By.ID, id)
        color = field.value_of_css_property("color")
        return color
