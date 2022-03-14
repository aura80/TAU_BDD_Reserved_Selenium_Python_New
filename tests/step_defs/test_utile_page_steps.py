from functools import partial
import time

from pytest_bdd import scenarios, when, then, given, parsers
from pages.register_page import RegisterPage

# Scenarios
scenarios('../features/test_utile_page.feature')

@given('open the register page')
def open_page(browser):
    utile = RegisterPage(browser)
    utile.load_page()

@when('generate random email')
def random_email(browser):
    utile = RegisterPage(browser)
    utile.get_random_mail(5)

@when('generate random firstname lastname password')
def random_name_pass(browser):
    utile = RegisterPage(browser)
    utile.get_random_string(8, 10, 8)
    time.sleep(5)

@when('searching element fuste')
def search_element(browser):
    utile = RegisterPage(browser)
    utile.get_search()

@when('searching element assert')
def search_cautare(browser):
    utile = RegisterPage(browser)
    utile.get_cautare()

@when('searching element pijama')
def search_cautare(browser):
    utile = RegisterPage(browser)
    utile.get_pijama()
    #utile.text_cautare()


