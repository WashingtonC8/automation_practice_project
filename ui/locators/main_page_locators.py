from selenium.webdriver.common.by import By

SLIDER_CAROUSEL_MAIN = (By.ID, "slider-carousel")
LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Signup / Login')]")
LOGGED_NAME = (By.CSS_SELECTOR, "a > i.fa.fa-user + b")
DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/delete_account"]')
LOGOUT_LINK = (By.XPATH, "//a[contains(text(), 'Logout')]")