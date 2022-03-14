from pytest_bdd import scenarios, when, then, given, parsers
from pages.negative import NegativeTests

# Scenarios
scenarios('../features/test_negative_page.feature')

@given('open the register page')
def open_page(browser):
    negative = NegativeTests(browser)
    negative.load_page()

@when(parsers.cfparse('adding email "{email}"'))
@when('adding email "<email>"')
def check_email(browser, email):
    negative = NegativeTests(browser)
    negative.type_email(email)

@when(parsers.cfparse('adding firstname "{firstname}"'))
@when('adding firstname "<firstname>"')
def check_firstname(browser, firstname):
    negative = NegativeTests(browser)
    negative.type_firstname(firstname)

@when(parsers.cfparse('adding lastname "{lastname}"'))
@when('adding lastname "<lastname>"')
def check_lastname(browser, lastname):
    negative = NegativeTests(browser)
    negative.type_lastname(lastname)

@when(parsers.cfparse('adding password "{password}"'))
@when('adding password "<password>"')
def check_password(browser, password):
    negative = NegativeTests(browser)
    negative.type_password(password)

@when('the user click Create Account button')
def press_create_account(browser):
    negative = NegativeTests(browser)
    negative.click_create_account_button()

@then(parsers.cfparse('"{error}" error message is displayed'))
def check_error_message(browser, error):
    negative = NegativeTests(browser)
    assert error in negative.get_flash_message(), "Flash message is not ok"

