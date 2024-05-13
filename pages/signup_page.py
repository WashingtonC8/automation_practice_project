from .base_page import BasePage
from .locators import SignupPageLocators
from selenium.webdriver.support.ui import Select
from .models import AddressInformation
from .models import UserData


class SignupPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SignupPage, self).__init__(*args, **kwargs)

    def should_be_enter_account_information_is_visible(self):
        assert self.is_element_present(*SignupPageLocators.ENTER_ACCOUNT_INFORMATION_LABEL), 'Label "ENTER ACCOUNT' \
                                                                                             ' INFORMATION" ' \
                                                                                             'is not present'

    def fill_details_enter_account_information(self, user_data=UserData):
        self.gender_selection(user_data)
        self.enter_password(user_data)
        self.enter_date_of_birth_select(user_data)

    def gender_selection(self, user_data=UserData):
        if user_data.title == "Mr":
            checkbox_mr = self.browser.find_element(*SignupPageLocators.GENDER_MR_CHECKBOX)
            checkbox_mr.click()
        elif user_data.title == "Mrs":
            checkbox_mrs = self.browser.find_element(*SignupPageLocators.GENDER_MRS_CHECKBOX)
            checkbox_mrs.click()

    def enter_password(self, user_data=UserData):
        input_password = self.browser.find_element(*SignupPageLocators.PASSWORD_LABEL)
        input_password.send_keys(user_data.password)

    def enter_date_of_birth_select(self, user_data=UserData):
        select_day = Select(self.browser.find_element(*SignupPageLocators.DAY_OF_BIRTH_SELECT))
        select_day.select_by_value(str(user_data.day_of_birth))
        select_month = Select(self.browser.find_element(*SignupPageLocators.MONTH_OF_BIRTH_SELECT))
        select_month.select_by_value(str(user_data.month_of_birth))
        select_year = Select(self.browser.find_element(*SignupPageLocators.YEAR_OF_BIRTH_SELECT))
        select_year.select_by_value(str(user_data.year_of_birth))

    def select_newsletter_checkbox(self):
        checkbox_newsletter = self.browser.find_element(*SignupPageLocators.NEWSLETTER_CHECKBOX)
        checkbox_newsletter.click()

    def select_offers_from_partners_checkbox(self):
        checkbox_partners = self.browser.find_element(*SignupPageLocators.OFFERS_FROM_PARTNERS_CHECKBOX)
        checkbox_partners.click()

    def enter_first_name(self, address_information: AddressInformation):
        input_first_name = self.browser.find_element(*SignupPageLocators.FIRST_NAME_INPUT)
        input_first_name.send_keys(address_information.first_name)

    def enter_last_name(self, address_information: AddressInformation):
        input_last_name = self.browser.find_element(*SignupPageLocators.LAST_NAME_INPUT)
        input_last_name.send_keys(address_information.last_name)

    def enter_company(self, address_information: AddressInformation):
        input_company = self.browser.find_element(*SignupPageLocators.COMPANY_INPUT)
        input_company.send_keys(address_information.company)

    def enter_address(self, address_information: AddressInformation):
        input_address = self.browser.find_element(*SignupPageLocators.ADDRESS_INPUT)
        input_address.send_keys(address_information.address)

    def enter_address_2(self, address_information: AddressInformation):
        input_address_2 = self.browser.find_element(*SignupPageLocators.ADDRESS_2_INPUT)
        input_address_2.send_keys(address_information.address_2)

    def enter_country_select(self, address_information: AddressInformation):
        select_country = Select(self.browser.find_element(*SignupPageLocators.COUNTRY_SELECT))
        select_country.select_by_value(address_information.country)

    def enter_state(self, address_information: AddressInformation):
        input_state = self.browser.find_element(*SignupPageLocators.STATE_INPUT)
        input_state.send_keys(address_information.state)

    def enter_city(self, address_information: AddressInformation):
        input_city = self.browser.find_element(*SignupPageLocators.CITY_INPUT)
        input_city.send_keys(address_information.city)

    def enter_zipcode(self, address_information: AddressInformation):
        input_zipcode = self.browser.find_element(*SignupPageLocators.ZIPCODE_INPUT)
        input_zipcode.send_keys(address_information.zipcode)

    def enter_mobile_number(self, address_information: AddressInformation):
        input_mobile_number = self.browser.find_element(*SignupPageLocators.MOBILE_NUMBER_INPUT)
        input_mobile_number.send_keys(address_information.mobile_number)

    def fill_details_enter_address_information(self, address_information: AddressInformation):
        self.enter_first_name(address_information)
        self.enter_last_name(address_information)
        self.enter_company(address_information)
        self.enter_address(address_information)
        self.enter_address_2(address_information)
        self.enter_country_select(address_information)
        self.enter_state(address_information)
        self.enter_city(address_information)
        self.enter_zipcode(address_information)
        self.enter_mobile_number(address_information)

    def click_create_account_button(self):
        button_create_account = self.browser.find_element(*SignupPageLocators.CREATE_ACCOUNT_BUTTON)
        button_create_account.click()
