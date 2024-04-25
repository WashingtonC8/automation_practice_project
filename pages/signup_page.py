from .base_page import BasePage
from .locators import SignupPageLocators
from selenium.webdriver.support.ui import Select


class SignupPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SignupPage, self).__init__(*args, **kwargs)

    def should_be_enter_account_information_is_visible(self):
        assert self.is_element_present(*SignupPageLocators.ENTER_ACCOUNT_INFORMATION_LABEL), 'Label "ENTER ACCOUNT' \
                                                                                             ' INFORMATION" is not present'

    def fill_details_enter_account_information(self, title, password, day, month, year):
        self.gender_selection(title)
        self.enter_password(password)
        self.enter_date_of_birth(day, month, year)

    def gender_selection(self, title):
        if title == "Mr":
            checkbox_mr = self.browser.find_element(*SignupPageLocators.GENDER_MR_CHECKBOX)
            checkbox_mr.click()
        elif title == "Mrs":
            checkbox_mrs = self.browser.find_element(*SignupPageLocators.GENDER_MRS_CHECKBOX)
            checkbox_mrs.click()

    def enter_password(self, password):
        input_password = self.browser.find_element(*SignupPageLocators.PASSWORD_LABEL)
        input_password.send_keys(password)

    def enter_date_of_birth(self, day, month, year):
        select_day = Select(self.browser.find_element(*SignupPageLocators.DAY_OF_BIRTH_SELECT))
        select_day.select_by_value(str(day))
        select_day = Select(self.browser.find_element(*SignupPageLocators.MONTH_OF_BIRTH_SELECT))
        select_day.select_by_value(str(month))
        select_day = Select(self.browser.find_element(*SignupPageLocators.YEAR_OF_BIRTH_SELECT))
        select_day.select_by_value(str(year))

