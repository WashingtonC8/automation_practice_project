from .base_page import BasePage
from .locators import AccountDeleteLocators


class AccountDeletePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(AccountDeletePage, self).__init__(*args, **kwargs)

    def should_be_account_deleted_is_visible(self):
        assert self.is_element_present(*AccountDeleteLocators.ACCOUNT_DELETE_LABEL), 'Label "Accont deleted!" is not ' \
                                                                                   'present'
