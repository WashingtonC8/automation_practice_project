from selenium.webdriver.common.by import By

NEW_USER_SIGN_UP_LABEL = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
NAME_INPUT_LOGIN_PAGE = (By.NAME, "name")
EMAIL_INPUT_LOGIN_PAGE = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-button"][type="submit"][class="btn btn-default"]')