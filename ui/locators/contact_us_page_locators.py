from selenium.webdriver.common.by import By

GET_IN_TOUCH_LABEL = (By.CSS_SELECTOR, '.col-sm-8 .title.text-center')

NAME_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="name"]')
EMAIL_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="email"]')
SUBJECT_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="subject"]')
MESSAGE_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="message"]')
UPLOAD_FILE_CONTACT_FORM = (By.NAME, 'upload_file')
SUBMIT_BUTTON_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="submit-button"]')
SUCCESS_ALERT_CONTACT_FORM = (By.CLASS_NAME, 'alert-success')