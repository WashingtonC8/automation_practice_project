from ui.pages.base_page import BasePage
from ui.page_static import main_page_static
from ui.locators import main_page_locators
from data.models.user_data_model import UserData


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_main_page(self):
        self.should_be_expected_url(main_page_static.MAIN_PAGE_URL)
        self.should_be_expected_title(main_page_static.MAIN_PAGE_TITLE)
        self.should_be_slider_carousel_main_page()

    def should_be_slider_carousel_main_page(self):
        assert self.is_element_present(*main_page_locators.SLIDER_CAROUSEL_MAIN)

    def should_be_expected_name(self, user_data=UserData):
        logged_name_label = self.browser.find_element(*main_page_locators.LOGGED_NAME)
        logged_name = logged_name_label.text
        assert logged_name == user_data.name, "The name of the logged in user does not match the one entered"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*main_page_locators.LOGIN_LINK)
        login_link.click()

    def click_to_delete_account_link(self):
        self.click_element(*main_page_locators.DELETE_ACCOUNT_LINK)

    def click_to_logout_link(self):
        self.click_element(*main_page_locators.LOGOUT_LINK)