from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class CheckOutCartPage_LogOutPage:
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
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_clickable(self.ACCOUNT_INFO_NAME))
        assert self.browser.find_element(*self.ACCOUNT_INFO_NAME).text == firstname, "Firstname is not ok"

    def log_out(self):
        #WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(*self.DATA_FEMEI)).click()
        DATA_FEMEI = (By.CSS_SELECTOR, ".empty__Block-sc-1mx1otu-4.jIECtA ul li:nth-child(1)")
        wait = WebDriverWait(self.browser, 5)
        element = wait.until(EC.element_to_be_clickable(DATA_FEMEI))
        element.click()



