from ui.pages.base_page import BasePage
from ui.locators import account_delete_page_locators


class AccountDeletePage(BasePage):
    def __init__(self, *args, **kwargs):
        super(AccountDeletePage, self).__init__(*args, **kwargs)

    def should_be_account_deleted_is_visible(self):
        assert self.is_element_present(*account_delete_page_locators.ACCOUNT_DELETE_LABEL), 'Label "Accont deleted!" is not ' \
                                                                                   'present'
