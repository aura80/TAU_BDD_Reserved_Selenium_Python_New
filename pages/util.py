import time
from selenium.webdriver.common.by import By
import re

class AddCart:
    # URL
    #URL = "https://www.reserved.com/ro/ro/new-in/girl?brick=SK_Denim_K&place=kids"
    URL = "https://www.reserved.com/ro/ro/5215g-80x/buty-rekreacyjne-k-2vpn-re"

    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    SNEAKERSI_CLICK = (By.CSS_SELECTOR, 'article[data-sku="5215G-80X"] .sc-jSgvzq.eltUJY.es-product-photo .sc-gKseQn.APvBI')
    ADD_CART = (By.CSS_SELECTOR, '.add-to-cart-text')
    NEXT_CLICK = (By.CSS_SELECTOR, '.control__ControlComponent-sc-1abuwne-0.ffTJtx.control.right-control')
    MENU_CLICK = (By.CSS_SELECTOR, '.hamburger__Button-sc-1m0l526-1.jLcZAh')
    COLOR_CLICK = (By.CSS_SELECTOR, 'button[value="5215G-80X"]')


    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def get_sneakers(self):
        self.browser.find_element(*self.ADD_CART).click()
        time.sleep(2)

    def get_next(self):
        self.browser.find_element(*self.NEXT_CLICK)     #.click()
        time.sleep(2)

    def get_color(self):
        self.browser.find_element(*self.COLOR_CLICK)    #.click()
        time.sleep(2)

    def validate_mail(self, sir_validare):
        sablon = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+.[a-z]{1,3}$"
        if re.match(sablon, sir_validare):
            return True
        return False
