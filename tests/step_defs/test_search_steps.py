import time
from pytest_bdd import scenarios, when, then, given, parsers
from pages.search import SearchTests
from pages.register_page import RegisterPage

# Scenarios
scenarios('../features/test_register_search_scenario.feature')

@given('open the page')
def open_page(browser):
    negative = SearchTests(browser)
    negative.load_page()

@when(parsers.cfparse('we wrote haine "{haine}" in the search field'))
@when('we wrote haine "<haine>" in the search field')
def check_email(browser, haine):
    negative = SearchTests(browser)
    negative.search_pijama_click(haine)


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


# steps
@given('open the search page')
def open_page(browser):
    search_page = SearchTests(browser)
    search_page.load_page()


@when(parsers.cfparse('the user types "{searched_item}" in the search bar'))
def search_product(browser, searched_item):
    # dam searched item ca arametru s aputem cauta cu orice valoare vrem noi ca daca nu tot timpul
    # scrie pijama
    search_page = SearchTests(browser)
    search_page.click_search_button()
    search_page.search_product(searched_item)


@then(parsers.cfparse('each result contains "{searched_item}" in name'))
def check_results(browser, searched_item):
    search_page = SearchTests(browser)
    search_page.check_results(searched_item)