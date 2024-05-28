import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def find_element(self, how, what, timeout=5):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what)),
            message=f"Не удалось найти элемент с локатором ({how}, {what})"
        )

    def click_element(self, how, what, timeout=5):
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((how, what)),
            message=f"Элемент с локатором ({how}, {what}) не кликабелен"
        )
        element.click()

    def pasted_text(self, how, what, text, timeout=5):
        input_name = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what)),
            message=f"Не удалось найти элемент с локатором ({how}, {what})"
        )
        input_name.send_keys(text)

    def should_be_expected_url(self, expected_url):
        assert expected_url in self.browser.current_url, "The wrong URL page is open"

    def should_be_expected_title(self, expected_title):
        assert expected_title == self.browser.title, "The wrong TITLE page is open"


