from ui.pages.main_page import MainPage
from ui.pages.test_cases_page import PageTestCases
from ui.page_static import main_page_static


def test_verify_test_cases_page(browser):
    main_page = MainPage(browser, url=main_page_static.MAIN_PAGE_URL)
    main_page.open()
    main_page.should_be_main_page()
    main_page.go_to_test_cases_page()
    test_cases_page = PageTestCases(browser, browser.current_url)
    test_cases_page.should_be_test_cases_page()