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
        self.enter_date_of_birth_select(day, month, year)

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

    def enter_date_of_birth_select(self, day, month, year):
        select_day = Select(self.browser.find_element(*SignupPageLocators.DAY_OF_BIRTH_SELECT))
        select_day.select_by_value(str(day))
        select_day = Select(self.browser.find_element(*SignupPageLocators.MONTH_OF_BIRTH_SELECT))
        select_day.select_by_value(str(month))
        select_day = Select(self.browser.find_element(*SignupPageLocators.YEAR_OF_BIRTH_SELECT))
        select_day.select_by_value(str(year))

    def select_newsletter_checkbox(self):
        checkbox_newsletter = self.browser.find_element(*SignupPageLocators.NEWSLETTER_CHECKBOX)
        checkbox_newsletter.click()

    def select_offers_from_partners_checkbox(self):
        checkbox_partners = self.browser.find_element(*SignupPageLocators.OFFERS_FROM_PARTNERS_CHECKBOX)
        checkbox_partners.click()

    def enter_first_name(self, first_name):
        input_first_name = self.browser.find_element(*SignupPageLocators.FIRST_NAME_INPUT)
        input_first_name.send_keys(first_name)

    def enter_last_name(self, last_name):
        input_last_name = self.browser.find_element(*SignupPageLocators.LAST_NAME_INPUT)
        input_last_name.send_keys(last_name)

    def enter_company(self, company):
        input_company = self.browser.find_element(*SignupPageLocators.COMPANY_INPUT)
        input_company.send_keys(company)

    def enter_address(self, address):
        input_address = self.browser.find_element(*SignupPageLocators.ADDRESS_INPUT)
        input_address.send_keys(address)

    def enter_address_2(self, address_2):
        input_address_2 = self.browser.find_element(*SignupPageLocators.ADDRESS_2_INPUT)
        input_address_2.send_keys(address_2)

    def enter_country_select(self, country):
        select_country = Select(self.browser.find_element(*SignupPageLocators.COUNTRY_SELECT))
        select_country.select_by_value(str(country))

    def enter_state(self, state):
        input_state = self.browser.find_element(*SignupPageLocators.STATE_INPUT)
        input_state.send_keys(state)

    def enter_city(self, city):
        input_city = self.browser.find_element(*SignupPageLocators.CITY_INPUT)
        input_city.send_keys(city)

    def enter_zipcode(self, zipcode):
        input_zipcode = self.browser.find_element(*SignupPageLocators.ZIPCODE_INPUT)
        input_zipcode.send_keys(zipcode)

    def enter_mobile_number(self, mobile_number):
        input_mobile_number = self.browser.find_element(*SignupPageLocators.MOBILE_NUMBER_INPUT)
        input_mobile_number.send_keys(mobile_number)

    def fill_details_enter_address_information(self, first_name, last_name, company, address, address2, country,
                                               state, city, zipcode, mobile_number):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_company(company)
        self.enter_address(address)
        self.enter_address_2(address2)
        self.enter_country_select(country)
        self.enter_state(state)
        self.enter_city(city)
        self.enter_zipcode(zipcode)
        self.enter_mobile_number(mobile_number)

    def click_create_account_button(self):
        button_create_account = self.browser.find_element(*SignupPageLocators.CREATE_ACCOUNT_BUTTON)
        button_create_account.click()