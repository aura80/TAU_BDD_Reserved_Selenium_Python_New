from pytest_bdd import scenarios, when, then, given, parsers
from pages.search import SearchTests

# Scenarios
scenarios('../features/test_search_page.feature')

@given('open the page')
def open_page(browser):
    negative = SearchTests(browser)
    negative.load_page()

@when(parsers.cfparse('we wrote haine "{haine}" in the search field'))
@when('we wrote pijama "<haine>" in the search field')
def check_email(browser, haine):
    negative = SearchTests(browser)
    negative.search_pijama_click(haine)
