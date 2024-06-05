from selenium.webdriver.common.by import By

GET_IN_TOUCH_LABEL = (By.CSS_SELECTOR, '.col-sm-8 .title.text-center')

NAME_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="name"')
EMAIL_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="email"')
SUBJECT_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="email"')
MESSAGE_INPUT_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="email"')
UPLOAD_FILE_CONTACT_FORM = (By.NAME, 'upload_file')
SUBMIT_BUTTON_CONTACT_FORM = (By.CSS_SELECTOR, '[data-qa="submit-button"')