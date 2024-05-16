from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def should_be_expected_url(self, expected_url):
        assert expected_url in self.browser.current_url, "The wrong URL page is open"

    def should_be_expected_title(self, expected_title):
        assert expected_title == self.browser.title, "The wrong TITLE page is open"

