from ui.pages.base_page import BasePage
from ui.locators import login_page_locators
from ui.page_static import login_page_static
from data.models.user_data_model import UserData


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def should_be_user_signup_is_visible(self):
        assert self.is_element_present(*login_page_locators.NEW_USER_SIGN_UP_LABEL), 'Label "New User Signup!" is not ' \
                                                                                   'present'

    def should_be_login_page(self):
        self.should_be_expected_url(login_page_static.LOGIN_PAGE_URL)
        self.should_be_expected_title(login_page_static.LOGIN_PAGE_TITLE)
        self.should_be_user_signup_is_visible()

    def enter_name_and_email_to_sign_up_form(self, user_data=UserData):
        input_name = self.browser.find_element(*login_page_locators.NAME_INPUT_LOGIN_PAGE)
        input_name.send_keys(user_data.name)
        input_email = self.browser.find_element(*login_page_locators.EMAIL_INPUT_LOGIN_PAGE)
        input_email.send_keys(user_data.email)

    def click_sign_up_form_button(self):
        button_sign_up = self.browser.find_element(*login_page_locators.SIGN_UP_BUTTON)
        button_sign_up.click()