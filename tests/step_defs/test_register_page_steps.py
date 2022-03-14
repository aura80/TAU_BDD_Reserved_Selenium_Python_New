from functools import partial

from pytest_bdd import scenarios, when, then, given, parsers
from pages.register_page import RegisterPage, Length
from pages.checkout_cart_page import CheckOutCartPage_LogOutPage

# Scenarios
scenarios('../features/test_register_page.feature')


# steps
@given('open the register page')
def open_page(browser):
    register_page = RegisterPage(browser)
    register_page.load_page()


@when(parsers.cfparse('the user type email "{email}"'))
def type_email(browser, email):
    register_page = RegisterPage(browser)
    register_page.type_email(email)


@when(parsers.cfparse('the user type firstname "{firstname}"'))
def type_firstname(browser, firstname):
    register_page = RegisterPage(browser)
    register_page.type_firstname(firstname)


@when(parsers.cfparse('the user type lastname "{lastname}"'))
def type_lastname(browser, lastname):
    register_page = RegisterPage(browser)
    register_page.type_lastname(lastname)


@when(parsers.cfparse('the user type password "{password}"'))
def type_password(browser, password):
    register_page = RegisterPage(browser)
    register_page.type_password(password)


@when('the user click Create Account button')
def click_create_account_button(browser):
    register_page = RegisterPage(browser)
    register_page.click_create_account_button()


@then('the user is redirected to checkout')
def check_user_is_redirected_to_checkout(browser):
    checkout_cart_page = CheckOutCartPage_LogOutPage(browser)
    checkout_cart_page.check_current_url()


@then(parsers.cfparse('the user is logged in with {firstname}'))
def check_user_is_logged_in(browser, firstname):
    checkout_cart_page = CheckOutCartPage_LogOutPage(browser)
    checkout_cart_page.check_firstname(firstname)


@then('the user is logged out')
def user_is_redirected_to_checkout(browser):
    checkout_cart_page = CheckOutCartPage_LogOutPage(browser)
    checkout_cart_page.log_out()

EXTRA_TYPES = {'length':int,}

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)

@given('open the register page')
def open_page(browser):
    utile = RegisterPage(browser)
    utile.load_page()


@when(parse_num('the user type email "{email:length}"'))
def length_email(browser):
    pass
    utile = Length(browser)
    utile.get_length_name(15)






