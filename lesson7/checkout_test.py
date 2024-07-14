from pages.sauce_auth import Auth
from pages.sauce_catalog import CatalogList
from pages.sauce_cart import Cart
from pages.sauce_checkout_step_one import CheckoutStepOne
from pages.sauce_checkout_step_two import CheckoutStepTwo
from selenium import webdriver


def test_fill_form():
    browser = webdriver.Chrome()
    log_in = Auth(browser)

    log_in.set_login('standard_user')
    log_in.set_password('secret_sauce')
    log_in.click_login()

    catalog_list = CatalogList(browser)
    goods = [
        'add-to-cart-sauce-labs-backpack',
        'add-to-cart-sauce-labs-bolt-t-shirt',
        'add-to-cart-sauce-labs-onesie']
    catalog_list.add_to_cart(goods)
    catalog_list.go_to_cart()

    cart = Cart(browser)
    cart.checkout()

    checkout_step_one = CheckoutStepOne(browser)
    checkout_step_one.set_first_name('Полина')
    checkout_step_one.set_last_name('Шаимова')
    checkout_step_one.set_postal_code('450000')
    checkout_step_one.click_continue()

    checkout_step_two = CheckoutStepTwo(browser)
    text = checkout_step_two.total()
    assert text == 'Total: $58.29'
