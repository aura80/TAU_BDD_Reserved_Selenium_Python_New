import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchTests:
    # URL
    URL = "https://www.reserved.com/ro/ro/"

    SEARCH_CLICK = (By.CSS_SELECTOR, '.action-btn__SearchWrapper-zbpc1m-4.eNpASB.verB')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.input__InputText-sc-1mxde2b-0.ipFxa.search-box__StyledTextField-sc-19imnj1-0.hzAHJR')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    ALL_PIJAMAS = (By.CSS_SELECTOR, '.infinite-hits__StyledInfiniteHits-tiohae-0.eEWTYo')
    LIST_HAINE_NAME = (By.CSS_SELECTOR, '.infinite-hits__StyledInfiniteHits-tiohae-0.eEWTYo .hit-item__Title-cz15ax-4.bDBiSH')

    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='search-open-button']")
    SEARCH_BAR = (By.CSS_SELECTOR, "input[type='search']")
    SORTING_DROP_DOWN = (By.CSS_SELECTOR, "[data-testid='sorting']")
    SEARCH_RESULTS_ITEMS = (By.CLASS_NAME, "hit-item__Title-cz15ax-4 bDBiSH")
    nr = 0

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def search_pijama_click(self, haine):
        self.browser.find_element(*self.SEARCH_CLICK).click()
        self.browser.find_element(*self.SEARCH_FIELD).send_keys(haine)
        time.sleep(3)

        results = self.browser.find_elements(*self.LIST_HAINE_NAME)
        for result in results:
            print(result.text)
        titles = [result.text for result in results]
        #assert 'Pijama din două piese' in titles, "Pijama not in titles"
        return titles


    def click_search_button(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def search_product(self, searched_item):
        self.browser.find_element(*self.SEARCH_BAR).send_keys(searched_item)
        # nu imi mergea fara enter tot timpul
        self.browser.find_element(*self.SEARCH_BAR).send_keys(Keys.ENTER)
        # aici am pus wait sa astepte sa se incarce pagina cu produse, am pus un wait dupa dropdownul ala ce sorteaza
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SORTING_DROP_DOWN))

    # aici am schimbat sa imi returneze o lista sa o putem folosi mai jos s aluam textul
    def get_results_list(self):
        return self.browser.find_elements(*self.SEARCH_RESULTS_ITEMS)

    def check_results(self, searched_item):
        for i in self.get_results_list():
            assert searched_item.lower() in i.text.loer(), "Result is not ok"
