import time

from .base_page import BasePage
from .locators import LoginPageLocators
from pages.variables import Pages
from pages.variables import Titles


class LoginPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(LoginPage, self).__init__(*args, **kwargs)

    def should_be_user_signup_is_visible(self):
        assert self.is_element_present(*LoginPageLocators.NEW_USER_SIGN_UP_LABEL), 'Label "New User Signup!" is not ' \
                                                                                   'present'

    def should_be_login_page(self):
        self.should_be_expected_url(Pages.LOGIN_PAGE_URL)
        self.should_be_expected_title(Titles.LOGIN_PAGE_TITLE)
        self.should_be_user_signup_is_visible()

    def enter_name_and_email_to_sign_up_form(self, name, email):
        input_name = self.browser.find_element(*LoginPageLocators.NAME_INPUT_LOGIN_PAGE)
        input_name.send_keys(name)
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE)
        input_email.send_keys(email)

    def click_sign_up_form_button(self):
        button_sign_up = self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON)
        button_sign_up.click()

    def enter_new_user_signup_form(self, name, email):
        input_name = self.browser.find_element(*LoginPageLocators.NAME_INPUT_LOGIN_PAGE)
        input_name.send_keys(name)
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE)
        input_email.send_keys(email)