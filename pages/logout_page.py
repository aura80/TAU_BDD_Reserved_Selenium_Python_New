import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LogOutPage:
    URL = "https://www.reserved.com/ro/ro/checkout/cart/"

    #DATA_FEMEI = (By.CSS_SELECTOR, ".empty__Block-sc-1mx1otu-4.jIECtA ul li:nth-child(1)")
    #WAIT_EXPLICIT = (By.CSS_SELECTOR, ".primary__PrimaryButtonComponent-sc-1pct4vx-0.fYiUIK")

    def __init__(self, browser):
        self.browser = browser

    def log_out(self):
        #WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(*self.DATA_FEMEI)).click()
        DATA_FEMEI = (By.CSS_SELECTOR, ".empty__Block-sc-1mx1otu-4.jIECtA ul li:nth-child(1)")
        wait = WebDriverWait(self.browser, 5)
        element = wait.until(EC.element_to_be_clickable(DATA_FEMEI))
        element.click()


