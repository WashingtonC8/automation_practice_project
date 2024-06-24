from ui.pages.main_page import MainPage
from ui.locators import test_cases_page_locators
from ui.page_static import test_cases_page_static


class TestcasesPage(MainPage):
    def __init__(self, *args, **kwargs):
        super(TestcasesPage, self).__init__(*args, **kwargs)

    def should_be_test_cases_title_is_visible(self):
        assert self.is_element_present(*test_cases_page_locators.TEST_CASES_TITLE_LABEL), 'Label "TEST CASES" is not' \
                                                                                          'present'

    def should_be_test_cases_page(self):
        self.should_be_expected_url(test_cases_page_static.PRODUCT_PAGE_URL)
        self.should_be_expected_title(test_cases_page_static.LOGIN_PAGE_TITLE)
        self.should_be_test_cases_title_is_visible()