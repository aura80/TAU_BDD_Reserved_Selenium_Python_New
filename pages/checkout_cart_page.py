from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckoutCartPage:
    #URL
    URL = "https://www.reserved.com/ro/ro/checkout/cart/"

    #locators
    ACCOUNT_INFO_NAME = (By.CSS_SELECTOR, 'div[data-testid="account-info-logged-true"]')

    def __init__(self, browser):
        self.browser = browser

    def check_current_url(self):
        try:
            assert self.browser.current_url == self.URL
        except:
            print("Url after create account is not ok")

    def check_firstname(self, firstname):
        ACCOUNT_INFO_NAME = (By.CSS_SELECTOR, 'div[data-testid="account-info-logged-true"]')
        assert self.browser.find_element(By.CSS_SELECTOR, 'div[data-testid="account-info-logged-true"]').text == firstname, "Firstname is not ok"
        wait = WebDriverWait(self.browser, 5)
        element = wait.until(EC.element_to_be_clickable(ACCOUNT_INFO_NAME))




