from pytest_bdd import scenarios, when, then, given, parsers
from pages.search import SearchTests

# Scenarios
scenarios('../features/test_search_page.feature')

@given('open the page')
def open_page(browser):
    negative = SearchTests(browser)
    negative.load_page()

@when(parsers.cfparse('we wrote pijama "{pijama}" in the search field'))
@when('we wrote pijama "<pijama>" in the search field')
def check_email(browser, pijama):
    negative = SearchTests(browser)
    negative.search_pijama_click(pijama)
