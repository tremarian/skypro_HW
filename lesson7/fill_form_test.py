from pages.data_types import DataTypes
from selenium import webdriver


def test_fill_form():
    browser = webdriver.Chrome()
    data_types = DataTypes(browser)

    data_types.fill_name('Иван')
    data_types.fill_surname('Петров')
    data_types.fill_address('Ленина, 55-3')
    data_types.fill_email('test@skypro.com')
    data_types.fill_phone('+7985899998787')
    data_types.fill_city('Москва')
    data_types.fill_country('Россия')
    data_types.fill_job('QA')
    data_types.fill_company('SkyPro')
    data_types.click_submit()

    assert data_types.field_color('zip-code') == 'rgba(132, 32, 41, 1)'

    pass_field_list = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company']
    l = len(pass_field_list)
    for y in range(0, l):
        assert data_types.field_color(pass_field_list[y]) == 'rgba(15, 81, 50, 1)'
