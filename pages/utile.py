import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.register_page import RegisterPage
import random
import string

class Utils:
    # URL
    URL = "https://www.reserved.com/ro/ro/customer/account/login/#register"

    # locators
    EMAIL_FIELD = (By.ID, "email_id")
    FIRSTNAME_FIELD = (By.ID, "firstname_id")
    LASTNAME_FIELD = (By.ID, "lastname_id")
    PASSWORD_FIELD = (By.ID, "password_id")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'div[version="verB"]')
    SEARCH_BUTTON_TEXT = (By.CSS_SELECTOR, 'div button[data-testid="search-button"]')
    SEARCH_ELEMENT = (By.CSS_SELECTOR, 'input[placeholder="Căutare"]')
    TEXT_COS = (By.CSS_SELECTOR, '.headline__HeadlineComponent-sc-1b12ysc-0.gKokaC')
    TEXT_PIJAMA = (By.CSS_SELECTOR, '.styled__StyledChip-sc-1w6uiwa-0.kDlZCJ.popular-chip:nth-child(4)')

    CAUTARE_TEXT = (By.CSS_SELECTOR, '.action-btn__ActionBtn-zbpc1m-1.fvxYdz')



    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def get_length_name(self, length):
        obiect = RegisterPage
        obiect.type_email()

    def get_random_mail(self, mail_length):
        letters = string.ascii_lowercase + string.digits
        result_str = ''.join(random.choice(letters) for i in range(mail_length))
        e_mail = result_str + '@yahoo.com'
        self.browser.find_element(*self.EMAIL_FIELD).send_keys(e_mail)

    def get_random_string(self, length_firstname, length_lastname, length_password):
        l_firstname = string.ascii_lowercase
        result_firstname = ''.join(random.choice(l_firstname) for i in range(length_firstname))
        self.browser.find_element(*self.FIRSTNAME_FIELD).send_keys(result_firstname)

        l_lastname = string.ascii_lowercase
        result_lastname = ''.join(random.choice(l_lastname) for i in range(length_lastname))
        self.browser.find_element(*self.LASTNAME_FIELD).send_keys(result_lastname)

        l_password = string.ascii_letters + string.digits + string.punctuation
        result_password = ''.join(random.choice(l_password) for i in range(length_password))
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(result_password)

        CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-selen='create-account-submit']")
        wait = WebDriverWait(self.browser, 7)
        element = wait.until((EC.element_to_be_clickable(CREATE_ACCOUNT_BUTTON)))
        element.click()

        time.sleep(2)

    def get_search(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()
        self.browser.find_element(*self.SEARCH_ELEMENT).send_keys('fuste')
        time.sleep(2)

    def get_cautare(self):
        assert self.browser.find_element(*self.TEXT_COS).text == 'Coșul de cumpărături este gol', 'Not search'
        cautare = self.browser.find_element(*self.TEXT_COS).text
        print(cautare)

    def get_pijama(self):
        self.browser.find_element(*self.TEXT_PIJAMA).click()
        time.sleep(2)

    def text_cautare(self):
        assert self.browser.find_element(*self.CAUTARE_TEXT).text == 'Căutare', 'Not search'





