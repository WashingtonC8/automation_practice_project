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


class SignupPageLocators():
    ENTER_ACCOUNT_INFORMATION_LABEL = (By.XPATH, '//b[text()="Enter Account Information"]')
    GENDER_MR_CHECKBOX = (By.CSS_SELECTOR, "[id='id_gender1']")
    GENDER_MRS_CHECKBOX = (By.CSS_SELECTOR, "[id='id_gender2']")
    PASSWORD_LABEL = (By.ID, "password")
    DAY_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="days"]')
    MONTH_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="months"]')
    YEAR_OF_BIRTH_SELECT = (By.CSS_SELECTOR, '[data-qa="years"]')
