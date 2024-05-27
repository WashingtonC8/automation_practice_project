from selenium.webdriver.common.by import By

NEW_USER_SIGN_UP_LABEL = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
NAME_INPUT_SIGNUP_FORM = (By.CSS_SELECTOR, '[data-qa="signup-name"]')
EMAIL_INPUT_SIGNUP_FORM = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
SIGN_UP_FORM_BUTTON = (By.CSS_SELECTOR, '[data-qa="signup-button"]')


EMAIL_INPUT_LOGIN_FORM = (By.CSS_SELECTOR, '[data-qa="login-email"]')
PASSWORD_INPUT_LOGIN_FORM = (By.CSS_SELECTOR, '[data-qa="login-password"]')
LOGIN_FORM_BUTTON = (By.CSS_SELECTOR, '[data-qa="login-button"]')
VALIDATION_ERROR_YOUR_EMAIL_OR_PASSWORD_INCORRECT_LOGIN_FORM = (By.CSS_SELECTOR, ".login-form p[style='color: red;']")