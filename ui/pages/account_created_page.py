from ui.pages.base_page import BasePage
from ui.locators import account_created_page_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountCreatedPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(AccountCreatedPage, self).__init__(*args, **kwargs)

    def should_be_account_created_is_visible(self):
        assert self.is_element_present(*account_created_page_locators.ACCOUNT_CREATED_LABEL), 'Label "Accont created!" ' \
                                                                                             'is not present'

    def click_continue_button(self):
        self.click_element(*account_created_page_locators.CONTINUE_BUTTON)