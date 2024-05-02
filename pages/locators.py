from selenium.webdriver.common.by import By


class LoginPageLocators():
    NEW_USER_SIGN_UP_LABEL = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    NAME_INPUT_LOGIN_PAGE = (By.NAME, "name")
    EMAIL_INPUT_LOGIN_PAGE = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-button"][type="submit"][class="btn btn-default"]')


class MainPageLocators():
    SLIDER_CAROUSEL_MAIN = (By.ID, "slider-carousel")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    LOGGED_NAME = (By.CSS_SELECTOR, "a > i.fa.fa-user + b")
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/delete_account"]')


class SignupPageLocators():
    ENTER_ACCOUNT_INFORMATION_LABEL = (By.XPATH, '//b[text()="Enter Account Information"]')
    GENDER_MR_CHECKBOX = (By.CSS_SELECTOR, "[id='id_gender1']")
    GENDER_MRS_CHECKBOX = (By.CSS_SELECTOR, "[id='id_gender2']")
    PASSWORD_LABEL = (By.ID, "password")
    DAY_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="days"]')
    MONTH_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="months"]')
    YEAR_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="years"]')
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    OFFERS_FROM_PARTNERS_CHECKBOX = (By.ID, "optin")

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '[data-qa="first_name"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '[data-qa="last_name"]')
    COMPANY_INPUT = (By.CSS_SELECTOR, '[data-qa="company"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, '[data-qa="address"]')
    ADDRESS_2_INPUT = (By.CSS_SELECTOR, '[data-qa="address2"]')
    COUNTRY_SELECT = (By.ID, "country")
    STATE_INPUT = (By.CSS_SELECTOR, '[data-qa="state"]')
    CITY_INPUT = (By.CSS_SELECTOR, '[data-qa="city"]')
    ZIPCODE_INPUT = (By.CSS_SELECTOR, '[data-qa="zipcode"]')
    MOBILE_NUMBER_INPUT = (By.CSS_SELECTOR, '[data-qa="mobile_number"]')

    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, '[data-qa="create-account"]')


class AccountCreatedLocators():
    ACCOUNT_CREATED_LABEL = (By.CSS_SELECTOR, '[data-qa="account-created"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '[data-qa="continue-button"]')


class AccountDeleteLocators():
    ACCOUNT_DELETE_LABEL = (By.CSS_SELECTOR, '[data-qa="account-deleted"]')