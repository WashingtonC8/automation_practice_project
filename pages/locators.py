from selenium.webdriver.common.by import By


class LoginPageLocators():
    NEW_USER_SIGN_UP_LABEL = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
    EMAIL_INPUT_LOGIN_PAGE = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    NAME_INPUT_LOGIN_PAGE = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-name"]')


class MainPageLocators():
    SLIDER_CAROUSEL_MAIN = (By.ID, "slider-carousel")


class BasePageLocators():
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")