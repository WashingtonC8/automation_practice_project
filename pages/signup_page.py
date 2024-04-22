from .base_page import BasePage
from .locators import SignupPageLocators


class SignupPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SignupPage, self).__init__(*args, **kwargs)

    def should_be_enter_account_information_is_visible(self):
        assert self.is_element_present(*SignupPageLocators.ENTER_ACCOUNT_INFORMATION_LABEL), 'Label "ENTER ACCOUNT' \
                                                                                             ' INFORMATION" is not present'
