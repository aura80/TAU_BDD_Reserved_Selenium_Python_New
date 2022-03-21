from pytest_bdd import scenarios, when, then, given, parsers
from pages.util import AddCart

# Scenarios
scenarios('../features/test_register_util_scenario.feature')

@given('open the register page')
def open_page(browser):
    util = AddCart(browser)
    util.load_page()

@when('adding sneakers to the cart')
def add_sneakers(browser):
    util = AddCart(browser)
    util.get_sneakers()

@when('finding the next picture')
def find_next(browser):
    util = AddCart(browser)
    util.get_next()

@when('accessing the menu')
def find_next(browser):
    util = AddCart(browser)
    util.get_color()

@then('validating the mail')
def find_next(browser):
    util = AddCart(browser)
    util.validate_mail("aaav9@yahoo.com")


