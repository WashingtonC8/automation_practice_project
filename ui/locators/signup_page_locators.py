from selenium.webdriver.common.by import By

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