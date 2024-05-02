from .base_page import BasePage
from .locators import AccountCreatedLocators


class AccountCreatedPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(AccountCreatedPage, self).__init__(*args, **kwargs)

    def should_be_account_created_is_visible(self):
        assert self.is_element_present(*AccountCreatedLocators.ACCOUNT_CREATED_LABEL), 'Label "Accont created!" is not ' \
                                                                                   'present'

    def click_continue_button(self):
        button_continue = self.browser.find_element(*AccountCreatedLocators.CONTINUE_BUTTON)
        button_continue.click()